#!/usr/bin/env bash
set -euo pipefail

# ====== YOUR CLASSROOM SETTINGS ======
ORG="II-2111-2026"
TEMPLATE_REPO="tugas"
STUDENT_PREFIX="tugas-"
UPSTREAM_URL="https://github.com/${ORG}/${TEMPLATE_REPO}.git"
# ====================================

# Where to clone student repos locally
WORKDIR="_sync_repos"
mkdir -p "$WORKDIR"
cd "$WORKDIR"

# Auth check
gh auth status >/dev/null 2>&1 || {
  echo "ERROR: GitHub CLI not authenticated. Run: gh auth login"
  exit 1
}

# Get upstream default branch (main/master)
UPSTREAM_BRANCH="$(gh repo view "${ORG}/${TEMPLATE_REPO}" --json defaultBranchRef --jq '.defaultBranchRef.name')"

# Create a unique branch name for this update
BRANCH_NAME="sync-upstream-$(date +%Y%m%d-%H%M)"
PR_TITLE="Sync course updates ($(date +%Y-%m-%d))"
PR_BODY="Sync instructor updates from ${ORG}/${TEMPLATE_REPO}. Student work in submissions/ is unchanged."

echo "Upstream: ${ORG}/${TEMPLATE_REPO} (${UPSTREAM_BRANCH})"
echo "Branch : ${BRANCH_NAME}"
echo

# List repos in org, filter by prefix
REPOS="$(gh repo list "$ORG" --limit 1000 --json name --jq '.[].name' | grep "^${STUDENT_PREFIX}" || true)"

if [ -z "$REPOS" ]; then
  echo "No student repos found with prefix: ${STUDENT_PREFIX}"
  exit 0
fi

for REPO in $REPOS; do
  FULL="${ORG}/${REPO}"
  echo "=============================="
  echo "Repo: $FULL"

  # Skip the template itself (extra safety)
  if [ "$REPO" = "$TEMPLATE_REPO" ]; then
    echo "Skipping template repo."
    continue
  fi

  # Detect the student's default branch (could be main/master)
  BASE_BRANCH="$(gh repo view "$FULL" --json defaultBranchRef --jq '.defaultBranchRef.name')"
  echo "Base branch: $BASE_BRANCH"

  # Clone if needed
  if [ ! -d "$REPO/.git" ]; then
    gh repo clone "$FULL" "$REPO"
  fi

  cd "$REPO"

  # Ensure remotes
  git remote get-url upstream >/dev/null 2>&1 || git remote add upstream "$UPSTREAM_URL"

  git fetch origin
  git fetch upstream

  # Make sure local base is up to date
  git checkout "$BASE_BRANCH"
  git pull --ff-only origin "$BASE_BRANCH"

  BEFORE="$(git rev-parse HEAD)"

  # Create / reset update branch from current base
  git checkout -B "$BRANCH_NAME"

  # Merge upstream changes
  if ! git merge --no-edit "upstream/${UPSTREAM_BRANCH}"; then
    echo "⚠️ Merge conflict in $FULL"
    echo "   Resolve manually in: $WORKDIR/$REPO"
    echo "   Then push branch and create PR manually (or rerun after fix)."
    cd ..
    continue
  fi

  AFTER="$(git rev-parse HEAD)"

  # If no changes, skip PR
  if [ "$BEFORE" = "$AFTER" ]; then
    echo "No upstream changes to apply. Skipping PR."
    cd ..
    continue
  fi

  # Push branch
  git push -u origin "$BRANCH_NAME" --force-with-lease

  # Create PR if it doesn't already exist
  if ! gh pr view --repo "$FULL" "$BRANCH_NAME" >/dev/null 2>&1; then
    gh pr create --repo "$FULL" \
      --base "$BASE_BRANCH" \
      --head "$BRANCH_NAME" \
      --title "$PR_TITLE" \
      --body "$PR_BODY"
    echo "✅ PR created."
  else
    echo "PR already exists."
  fi

  # OPTIONAL: auto-merge clean PRs (uncomment if you want)
  # gh pr merge --repo "$FULL" "$BRANCH_NAME" --auto --squash || true

  cd ..
done

echo
echo "Done. PRs opened (where changes existed)."

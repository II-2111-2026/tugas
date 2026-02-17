# Local testing helper
# Usage:
#   make test WEEK=w02
#   make test           # defaults to w01

WEEK ?= w01

.PHONY: test
test:
	python -m pip install -r requirements.txt
	pytest -q tests_bank/$(WEEK)/quiz_tests.py

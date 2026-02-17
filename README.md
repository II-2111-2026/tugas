<!-- PACKAGE: INSTRUCTOR SOLUTION (answers.py sudah terisi) -->

# Probability & Statistics — GitHub Classroom (Practice Mode)

This starter repo is built for **Option 3**:
- Instructor updates quizzes/tests freely
- Student work is isolated in `submissions/` so it won't be overwritten

## Golden rule
Students edit **ONLY**:
- `submissions/wXX/answers.py`

Instructors edit/update freely:
- `weeks/wXX/quiz.qmd`
- `tests_bank/wXX/quiz_tests.py`
- `.github/**`, `tools/**`, `requirements.txt`, `ACTIVE_WEEK.txt`

## Week 01 (Practice Mode)
Week 01 is **complete** (quiz + tests), but `submissions/w01/answers.py` starts as **stubs**.
So the first run will fail until students implement the functions.

If you want a separate “demo-green” experience, use the other template that pre-fills a solution.

## How autograding chooses the week
- If a push changes exactly one folder `submissions/wXX/...`, that `wXX` is graded.
- Otherwise, autograding uses `ACTIVE_WEEK.txt` (instructor sets it weekly).

## GitHub Classroom setup (recommended)
Create **one** Classroom assignment for the whole semester from this template repo.

Protect these paths:
- `.github/**`
- `tools/**`
- `weeks/**`
- `tests_bank/**`
- `ACTIVE_WEEK.txt`
- `requirements.txt`

Do NOT protect:
- `submissions/**`


## Jenis soal (T/F, Pilihan Ganda, Numeric)

Setiap minggu ada **12 tugas**:
- **3 soal True/False (T/F)** → jawab dengan `True` (Benar) atau `False` (Salah)
- **4 soal pilihan ganda (MC)** → jawab dengan huruf `"A"`, `"B"`, `"C"`, atau `"D"`
- **5 soal isian bilangan (Numeric)** → jawab dengan `int` / `float` (desimal pakai titik `.`)

Semua jawaban ditulis **satu-satunya** di:
- `submissions/wXX/answers.py`

Autograding akan:
1) Mengimpor `submissions/wXX/answers.py`
2) Memanggil `q01()..q12()`
3) Membandingkan dengan **kunci jawaban** di `tests_bank/wXX/quiz_tests.py`

## Quarto (opsional tapi direkomendasikan)

Di setiap minggu ada:
- `submissions/wXX/laporan.qmd` → laporan ramah dibaca yang mengambil nilai dari `answers.py` (tidak ada “dua versi jawaban”).

Kamu bisa render lokal:
```bash
quarto render submissions/wXX/laporan.qmd
```

Repo ini juga disiapkan supaya GitHub Actions **merender Quarto otomatis** saat kamu `git push`
(dan mengunggah hasilnya sebagai artifact build).

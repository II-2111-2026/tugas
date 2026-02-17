"""Jawaban w11 — SOLUSI (untuk dosen/validasi)
"""

from __future__ import annotations

def q01() -> bool:
    """[T/F] Semakin tinggi tingkat kepercayaan yang diinginkan, semakin lebar interval
kepercayaan yang dihasilkan."""
    return True

def q02() -> bool:
    """[T/F] Interval kepercayaan 95% berarti ada peluang 95% bahwa parameter populasi
berada dalam rentang tersebut untuk satu interval yang sudah dihitung.  - secara
teknis interpretasinya tentang proses sampling)."""
    return False

def q03() -> bool:
    """[T/F] Distribusi t-Student mendekati distribusi Normal saat derajat kebebasan (df) menjadi
sangat besar."""
    return True

def q04() -> str:
    """[MC] Jika kita ingin mempersempit interval kepercayaan tanpa mengubah tingkat
kepercayaan, kita harus:
a) Mengurangi ukuran sampel.
b) Meningkatkan ukuran sampel.
c) Meningkatkan simpangan baku.
d) Tidak melakukan apa-apa."""
    return "B"

def q05() -> str:
    """[MC] Nilai kritis  untuk tingkat kepercayaan 95% adalah:
a) 1,645
b) 1,96
c) 2,58
d) 1,00"""
    return "B"

def q06() -> str:
    """[MC] Derajat kebebasan (df) untuk interval kepercayaan rata-rata satu sampel berukuran $n$ adalah:
a) $n$
b) $1$
c) $n - 1$
d) $n + 1$"""
    return "C"

def q07() -> str:
    """[MC] Estimasi titik terbaik untuk rata-rata populasi $\mu$ adalah:
a) Median sampel.
b) Modus sampel.
c) Rata-rata sampel ($\bar{x}$).
d) Standar deviasi sampel."""
    return "C"

def q08() -> float:
    """[Numeric] Jika = 100, Margin Error = 5, berapakah batas bawah interval kepercayaan?"""
    return 95

def q09() -> float:
    """[Numeric] Untuk sampel = 16 dan simpangan baku sampel = , berapakah nilai
estimasi Standard Error-nya?"""
    return 1

def q10() -> float:
    """[Numeric] Berapakah derajat kebebasan jika ukuran sampel adalah 25?"""
    return 24

def q11() -> float:
    """[Numeric] Jika interval kepercayaan adalah , berapakah nilai estimasi titik rata-ratanya?"""
    return 50

def q12() -> float:
    """[Numeric] Jika margin error adalah 2 dan nilai kritis = , berapakah Standard Error-nya?"""
    return 1

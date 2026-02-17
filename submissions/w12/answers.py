"""Jawaban w12 — SOLUSI (untuk dosen/validasi)
"""

from __future__ import annotations

def q01() -> bool:
    """[T/F] Jika p-value lebih kecil dari tingkat signifikansi , maka kita gagal menolak hipotesis
nol."""
    return False

def q02() -> bool:
    """[T/F] Galat Tipe I adalah kean menolak 0 padahal 0 ."""
    return True

def q03() -> bool:
    """[T/F] Meningkatkan ukuran sampel biasanya akan meningkatkan kekuatan uji (power)."""
    return True

def q04() -> str:
    """[MC] Nilai probabilitas yang menunjukkan kekuatan bukti melawan hipotesis nol disebut:
a) Tingkat kepercayaan.
b) p-value.
c) Statistik uji.
d) Parameter."""
    return "B"

def q05() -> str:
    """[MC] Jika kita menguji 0
= 50 vs 1
50, maka kita melakukan uji:
a) Satu arah (kanan).
b) Satu arah (kiri).
c) Dua arah.
d) Tanpa arah.

Minggu 13: Analisis Regresi Linear dan Korelasi
Minggu ketiga belas memperkenalkan pemodelan prediktif. Mahasiswa belajar mencari
hubungan linear antara variabel, yang merupakan dasar dari algoritma machine learning
modern.
Bank Soal Mingguan
Pertanyaan Konseptual"""
    return "C"

def q06() -> str:
    """[MC] Kondisi di mana kita menolak hipotesis nol padahal sebenarnya salah disebut:
a) Keputusan yang benar (Power).
b) Galat Tipe I.
c) Galat Tipe II.
d) Signifikansi."""
    return "A"

def q07() -> str:
    """[MC] Tingkat signifikansi yang umum digunakan dalam penelitian adalah:
a) 0,5
b) 0,05
c) 0,95
d) 1,0"""
    return "B"

def q08() -> float:
    """[Numeric] Jika statistik uji = , 5 dan nilai kritis = 1, 6 untuk uji dua arah, apakah 0
ditolak? (Tulis 1 untuk Ya, 0 untuk Tidak)"""
    return 1

def q09() -> float:
    """[Numeric] Berapakah nilai  jika tingkat kepercayaan adalah 99%?"""
    return 0.01

def q10() -> float:
    """[Numeric] Dalam uji t dengan sampel = 10, berapakah derajat kebebasannya?"""
    return 9

def q11() -> float:
    """[Numeric] Jika p-value = 0,02 dan  = 0,05, apakah kita menolak 0? (Tulis 1 untuk Ya, 0
untuk Tidak)"""
    return 1

def q12() -> float:
    """[Numeric] Jika statistik = 0, berapakah p-value untuk uji dua arah?"""
    return 1

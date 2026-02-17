"""Jawaban w06 — SOLUSI (untuk dosen/validasi)
"""

from __future__ import annotations

def q01() -> bool:
    """[T/F] Distribusi Binomial digunakan untuk eksperimen dengan jumlah percobaan yang
tidak terbatas."""
    return False

def q02() -> bool:
    """[T/F] Parameter mean dan variansi pada distribusi Poisson memiliki nilai yang sama."""
    return True

def q03() -> bool:
    """[T/F] Distribusi Bernoulli adalah kasus khusus dari distribusi Binomial dengan = 1."""
    return True

def q04() -> str:
    """[MC] Jika 10, 0, , maka nilai harapannya adalah:
a) 2
b) 0,2
c) 8
d) 1,6"""
    return "A"

def q05() -> str:
    """[MC] Distribusi yang paling tepat untuk memodelkan jumlah telepon yang masuk ke call
center dalam satu menit adalah:
a) Binomial.
b) Poisson.
c) Uniform.
d) Normal."""
    return "B"

def q06() -> str:
    """[MC] Pada distribusi Binomial, probabilitas sukses p harus:
a) Berubah tiap percobaan.
b) Tetap konstan tiap percobaan.
c) Selalu 0,5.
d) Berkurang seiring waktu."""
    return "B"

def q07() -> str:
    """[MC] Rumus = = − adalah untuk distribusi:

Minggu 07: Distribusi Probabilitas Kontinu - Normal dan
Eksponensial
Minggu ketujuh memperkenalkan distribusi paling penting dalam statistika: Distribusi Normal
(Gaussian) dan pasangannya untuk waktu tunggu, distribusi Eksponensial.
Bank Soal Mingguan
Pertanyaan Konseptual
Pertanyaan Aplikatif
a) Binomial.
b) Poisson.
c) Geometrik.
d) Eksponensial."""
    return "B"

def q08() -> float:
    """[Numeric] Jika , 0, 5, hitung = ."""
    return 0.375

def q09() -> float:
    """[Numeric] Untuk distribusi Poisson dengan = , berapakah probabilitas = 0? (Gunakan
3 desimal)"""
    return 0.135

def q10() -> float:
    """[Numeric] Hitung variansi dari variabel acak 100, 0, 1."""
    return 9

def q11() -> float:
    """[Numeric] Berapakah nilai maksimum yang mungkin dari variabel acak 10, 0, 5?"""
    return 10

def q12() -> float:
    """[Numeric] Jika rata-rata kedatangan paket adalah 5 per ms, berapakah variansi jumlah
paket per ms?"""
    return 5

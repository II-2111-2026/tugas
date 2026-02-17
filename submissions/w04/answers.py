"""Jawaban w04 — SOLUSI (untuk dosen/validasi)
"""

from __future__ import annotations

def q01() -> bool:
    """[T/F] Jika kejadian  dan  independen, maka = ."""
    return True

def q02() -> bool:
    """[T/F] Probabilitas kondisional  selalu sama dengan ."""
    return False

def q03() -> bool:
    """[T/F] Teorema Bayes memungkinkan kita untuk membalik kondisi probabilitas dari 
menjadi ."""
    return True

def q04() -> str:
    """[MC] Jika = 0, 5, = 0,  dan ,  independen, maka  adalah:
a) 0,9
b) 0,1
c) 0,2
d) 0,5"""
    return "C"

def q05() -> str:
    """[MC] Rumus Bayes menyatakan bahwa  sama dengan:
a) 

Minggu 05: Variabel Acak, Ekspektasi, dan Variansi
Minggu ini menandai transisi dari kejadian diskrit ke variabel numerik. Mahasiswa belajar
memetakan hasil dunia nyata ke dalam fungsi matematika. Konsep nilai harapan
(ekspektasi) diperkenalkan sebagai representasi keuntungan jangka panjang atau rata-rata
beban sistem.
b) 
c) 
d)"""
    return "A"

def q06() -> str:
    """[MC] Kejadian di mana hasil satu eksperimen tidak mempengaruhi hasil eksperimen
lainnya disebut:
a) Saling lepas.
b) Independen.
c) Kondisional.
d) Komplementer."""
    return "B"

def q07() -> str:
    """[MC] Jika sebuah tes medis memiliki sensitivitas tinggi, maka:
a) Banyak hasil false positive.
b) Probabilitas mendeteksi orang sakit sangat tinggi.
c) Probabilitas mendeteksi orang sehat sangat tinggi.
d) Tes tersebut tidak berguna."""
    return "B"

def q08() -> float:
    """[Numeric] Jika = 0,  dan = 0, 5, berapakah ?"""
    return 0.4

def q09() -> float:
    """[Numeric] Probabilitas hujan adalah 0,1. Jika hujan, probabilitas jalan macet adalah 0,8.
Berapa probabilitas (Hujan DAN Macet)?"""
    return 0.08

def q10() -> float:
    """[Numeric] Dalam sebuah populasi, 1% menderita penyakit. Sebuah tes memiliki akurasi
99% (baik untuk yang sakit maupun sehat). Jika seseorang dites positif, berapa
probabilitas dia benar-benar sakit?"""
    return 0.5

def q11() -> float:
    """[Numeric] Jika = 0, , = 0,  dan = 0, , hitung  menggunakan Hukum Probabilitas Total."""
    return 0.49

def q12() -> float:
    """[Numeric] Dari soal nomor 11, hitung  menggunakan Teorema Bayes (Gunakan 3
desimal)."""
    return 0.429

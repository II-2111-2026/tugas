"""Jawaban w01 — SOLUSI (untuk dosen/validasi)
"""

from __future__ import annotations

def q01() -> bool:
    """[T/F] Dalam model probabilistik, output yang sama akan selalu dihasilkan dari input yang
sama terlepas dari variasi acak."""
    return False

def q02() -> bool:
    """[T/F] Ruang sampel dari sebuah eksperimen acak harus mencakup semua hasil yang
mungkin terjadi tanpa tumpang tindih."""
    return True

def q03() -> bool:
    """[T/F] Probabilitas empiris mendekati probabilitas teoretis ketika jumlah percobaan
mendekati tak hingga."""
    return True

def q04() -> str:
    """[MC] Manakah yang merupakan contoh variabel acak dalam sistem STI?
a) Kapasitas total hard disk 1TB.
b) Jumlah core pada prosesor Intel i7.
c) Waktu yang dibutuhkan untuk merespons query database.
d) Jumlah bit dalam satu byte."""
    return "C"

def q05() -> str:
    """[MC] Jika sebuah ruang sampel  terdiri dari 4 kejadian yang memiliki peluang sama,
maka probabilitas satu kejadian adalah:
a) 0,5

Minggu 02: Kerangka Probabilitas dan Operasi Kejadian
Minggu kedua memperdalam struktur matematika melalui teori himpunan. Pemahaman
tentang irisan, gabungan, dan komplemen sangat krusial dalam merancang logika sistem
informasi yang tangguh.
Bank Soal Mingguan
Pertanyaan Konseptual
b) 0,25
c) 0,75
d) 1,0"""
    return "B"

def q06() -> str:
    """[MC] Kejadian yang mustahil terjadi memiliki nilai probabilitas sebesar:
a) 0
b) 1
c) -1
d) 0,5"""
    return "A"

def q07() -> str:
    """[MC] Sekumpulan hasil eksperimen yang merupakan subset dari ruang sampel disebut:
a) Populasi.
b) Parameter.
c) Kejadian (Event).
d) Konstanta."""
    return "C"

def q08() -> float:
    """[Numeric] Berapa jumlah elemen dalam ruang sampel jika kita melempar dua buah
dadu bersisi enam?"""
    return 36

def q09() -> float:
    """[Numeric] Jika probabilitas sebuah link internet mati adalah 0,01, berapa probabilitas
link tersebut hidup?"""
    return 0.99

def q10() -> float:
    """[Numeric] Berapa banyak susunan berbeda yang bisa dibuat dari kata "DATA"?"""
    return 12

def q11() -> float:
    """[Numeric] Jika sebuah server memiliki probabilitas uptime 0,95, berapa probabilitas
server tersebut downtime dalam satu periode?"""
    return 0.05

def q12() -> float:
    """[Numeric] Dalam simulasi 1000 kali login, jika 20 kali gagal, berapa frekuensi relatif
kegagalan tersebut?"""
    return 0.02

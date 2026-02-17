"""Jawaban w03 — SOLUSI (untuk dosen/validasi)
"""

from __future__ import annotations

def q01() -> bool:
    """[T/F] Dalam konfigurasi paralel, sistem akan gagal hanya jika semua komponen gagal."""
    return True

def q02() -> bool:
    """[T/F] Menambahkan komponen secara seri akan meningkatkan reliabilitas keseluruhan
sistem."""
    return False

def q03() -> bool:
    """[T/F] Reliabilitas total sistem seri selalu lebih kecil atau sama dengan reliabilitas
komponen terlemahnya."""
    return True

def q04() -> str:
    """[MC] Sebuah sistem terdiri dari dua komponen dengan reliabilitas 0,9 yang disusun
secara paralel. Reliabilitas sistem adalah:
a) 0,81
b) 0,99
c) 0,90
d) 1,80"""
    return "B"

def q05() -> str:
    """[MC] Jika tiga switch identik dengan reliabilitas 0,8 disusun seri, reliabilitas totalnya
adalah:
a) 0,512
b) 0,8
c) 2,4
d) 0,2"""
    return "A"

def q06() -> str:
    """[MC] Manakah konfigurasi yang paling tahan terhadap kegagalan komponen tunggal?
a) Seri.
b) Paralel.
c) Campuran seri-paralel.
d) Sistem tanpa redundansi."""
    return "B"

def q07() -> str:
    """[MC] Istilah untuk probabilitas sistem berfungsi pada waktu tertentu  adalah:
a) Efisiensi.
b) Reliabilitas.
c) Kapasitas.
d) Latensi."""
    return "B"

def q08() -> float:
    """[Numeric] Hitung reliabilitas sistem seri dari dua komponen dengan reliabilitas 0,95 dan
0,8."""
    return 0.76

def q09() -> float:
    """[Numeric] Jika reliabilitas satu server adalah 0,9, berapa probabilitas dua server
tersebut gagal bersamaan dalam susunan paralel?"""
    return 0.01

def q10() -> float:
    """[Numeric] Sebuah sistem memiliki reliabilitas 0,99. Berapa probabilitas kegagalannya?"""
    return 0.01

def q11() -> float:
    """[Numeric] Tiga lampu disusun paralel dengan reliabilitas masing-masing 0,5. Berapa
reliabilitas total sistem lampu tersebut?"""
    return 0.875

def q12() -> float:
    """[Numeric] Berapa probabilitas sistem seri dengan 10 komponen identik (masing-masing
= 0,99) tetap berfungsi? (Gunakan 3 desimal)"""
    return 0.904

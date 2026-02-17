"""Jawaban w14 — SOLUSI (untuk dosen/validasi)
"""

from __future__ import annotations

def q01() -> bool:
    """[T/F] Pengujian A/B adalah aplikasi nyata dari uji hipotesis dua sampel."""
    return True

def q02() -> bool:
    """[T/F] Metrik "Presisi" mengukur seberapa banyak dari total prediksi positif yang -
 positif."""
    return True

def q03() -> bool:
    """[T/F] Dalam monitoring sistem, kita biasanya mengabaikan outlier karena itu bukan
bagian dari pola normal.  - outlier seringkali menunjukkan anomali atau
kegagalan)."""
    return False

def q04() -> str:
    """[MC] Metrik evaluasi yang tepat untuk dataset dengan kelas yang tidak seimbang
(imbalanced) adalah:

a) Akurasi.
b) F1-Score.
c) Mean.
d) Range."""
    return "B"

def q05() -> str:
    """[MC] Dalam deteksi anomali, data yang berada di luar  biasanya dianggap:
a) Data normal.
b) Outlier atau anomali.
c) Nilai rata-rata.
d) Sampel ideal."""
    return "B"

def q06() -> str:
    """[MC] Pengujian A/B dilakukan untuk:
a) Mengurangi biaya server.
b) Menentukan versi produk mana yang memberikan performa/konversi lebih baik.
c) Menghapus bug secara otomatis.
d) Mengganti peran programmer."""
    return "B"

def q07() -> str:
    """[MC] Jika sebuah sistem memiliki presisi 1,0, berarti:
a) Tidak ada false positive.
b) Tidak ada false negative.
c) Akurasi 100%.
d) Sistem sempurna."""
    return "A"

def q08() -> float:
    """[Numeric] Jika TP = 80 dan FP = 20, berapakah nilai presisinya?"""
    return 0.8

def q09() -> float:
    """[Numeric] Jika akurasi model adalah 0,95 dan ada 1.000 data, berapa banyak prediksi
yang benar?"""
    return 950

def q10() -> float:
    """[Numeric] Hitung F1-score jika Presisi = 0,8 dan Recall = 0,8."""
    return 0.8

def q11() -> float:
    """[Numeric] Berapakah nilai skor-Z untuk data point 110 jika rata-rata 100 dan simpangan
baku 5?"""
    return 2

def q12() -> float:
    """[Numeric] Jika dalam pengujian A/B, p-value yang didapat adalah 0,001, apakah ada
perbedaan signifikan pada = 0, 05? (Tulis 1 untuk Ya, 0 untuk Tidak)"""
    return 1

"""
Program tebak angka sederhana.
Ini SOURCE CODE ASLI yang akan
diambil (checkout) oleh GitHub
Actions, lalu dikemas (packaging)
jadi artifact terdistribusi.
"""
import sys

# Angka rahasia ditanam langsung
# di kode, contoh logika program
# sungguhan (bukan file kosong)
RAHASIA = 7


def main():
    if len(sys.argv) < 2:
        print("Cara pakai: python tebak_angka.py <angka>")
        return

    tebakan = int(sys.argv[1])
    if tebakan == RAHASIA:
        print(f"Benar! Angka rahasianya {RAHASIA}")
    else:
        print("Salah, coba lagi.")


if __name__ == "__main__":
    main()

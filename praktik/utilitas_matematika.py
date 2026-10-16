def luas_persegi_panjang(p, l):
    return p * l

def luas_segitiga(a, t):
    return 0.5 * a * t

def jumlah_n(n):
    if n < 0:
        return "Error: n harus berupa bilangan bulat nonnegatif!"
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def faktorial(n):
    if n < 0:
        return "Error: n harus berupa bilangan bulat nonnegatif!"
    hasil = 1
    for i in range(2, n + 1):
        hasil *= i
    return hasil

def tampilkan_menu():
    print("\n=== UTILITAS MATEMATIKA ===")
    print("1. Luas persegi panjang")
    print("2. Luas segitiga")
    print("3. Jumlah 1 sampai n")
    print("4. Faktorial")
    print("5. Keluar")

# Program utama
def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == '1':
            p = float(input("Masukkan panjang (p): "))
            l = float(input("Masukkan lebar (l): "))
            hasil = luas_persegi_panjang(p, l)
            print(f"Hasil Luas Persegi Panjang: {hasil}")

        elif pilihan == '2':
            a = float(input("Masukkan alas (a): "))
            t = float(input("Masukkan tinggi (t): "))
            hasil = luas_segitiga(a, t)
            print(f"Hasil Luas Segitiga: {hasil}")

        elif pilihan == '3':
            n = int(input("Masukkan nilai n: "))
            hasil = jumlah_n(n)
            print(f"Hasil Jumlah 1 sampai {n}: {hasil}")

        elif pilihan == '4':
            n = int(input("Masukkan nilai n: "))
            hasil = faktorial(n)
            print(f"Hasil Faktorial dari {n}! : {hasil}")

        elif pilihan == '5':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()
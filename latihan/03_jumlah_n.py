def jumlah_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def rumus_n(n):
    return int(n * (n + 1) / 2)

nilai_n = [1, 5, 10, 100]

for n in nilai_n:
    hasil_loop = jumlah_n(n)
    hasil_rumus = rumus_n(n)
    print(f"n = {n} -> Hasil loop: {hasil_loop}, Hasil rumus: {hasil_rumus}")
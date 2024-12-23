import matplotlib.pyplot as plt
from prettytable import PrettyTable

# Data Gizi Harian
kalori = []  # Menyimpan data kalori harian
protein = []  # Menyimpan data protein harian
lemak = []    # Menyimpan data lemak harian

# Fungsi untuk memperbarui grafik
def update_graph():
    plt.figure(figsize=(8, 6))
    plt.plot(range(1, len(kalori) + 1), kalori, label='Kalori (kcal)', marker='o', linestyle='-')
    plt.plot(range(1, len(protein) + 1), protein, label='Protein (g)', marker='o', linestyle='-')
    plt.plot(range(1, len(lemak) + 1), lemak, label='Lemak (g)', marker='o', linestyle='-')
    plt.title('Optimasi Pemilihan Gizi Harian')
    plt.xlabel('Hari ke')
    plt.ylabel('Jumlah Gizi')
    plt.legend()
    plt.grid(True)
    plt.show()

# Fungsi untuk mencetak tabel data gizi
def print_execution_table():
    table = PrettyTable()
    table.field_names = ["Hari", "Kalori (kcal)", "Protein (g)", "Lemak (g)"]
    for i in range(len(kalori)):
        table.add_row([i + 1, kalori[i], protein[i], lemak[i]])
    print(table)

# Program utama
hari = 1  # Mulai dari hari ke-1
while True:
    try:
        print(f"\nMasukkan data gizi untuk Hari ke-{hari}:")

        # Input data gizi harian
        kalori_harian = int(input("  Kalori (kcal): "))
        protein_harian = int(input("  Protein (g): "))
        lemak_harian = int(input("  Lemak (g): "))

        if kalori_harian < 0 or protein_harian < 0 or lemak_harian < 0:
            print("Masukkan nilai gizi yang positif!")
            continue

        # Menyimpan data gizi
        kalori.append(kalori_harian)
        protein.append(protein_harian)
        lemak.append(lemak_harian)

        # Cetak tabel data gizi
        print_execution_table()

        # Perbarui grafik
        update_graph()

        # Tanyakan apakah lanjutkan
        lanjut = input("\nApakah Anda ingin melanjutkan ke hari berikutnya? (y/n): ").strip().lower()
        if lanjut != 'y':
            print("Program selesai. Terima kasih!")
            break

        # Naikkan hari
        hari += 1

    except ValueError:
        print("Masukkan nilai yang valid!")

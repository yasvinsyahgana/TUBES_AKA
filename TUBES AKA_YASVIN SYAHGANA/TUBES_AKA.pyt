import time
import matplotlib.pyplot as plt
from prettytable import PrettyTable

# Contoh data gizi (kalori, protein, karbohidrat, lemak dalam gram)
makanan = [
    {"nama": "Ayam", "kalori": 165, "protein": 31, "karbohidrat": 0, "lemak": 4},
    {"nama": "Nasi", "kalori": 130, "protein": 2, "karbohidrat": 28, "lemak": 0},
    {"nama": "Telur", "kalori": 68, "protein": 6, "karbohidrat": 0, "lemak": 5},
    {"nama": "Susu", "kalori": 42, "protein": 3, "karbohidrat": 5, "lemak": 1},
]

def gizi_recursive(target, idx):
    if target <= 0 or idx == len(makanan):
        return []
    
    with_current = gizi_recursive(target - makanan[idx]['kalori'], idx + 1) + [makanan[idx]]
    without_current = gizi_recursive(target, idx + 1)

    total_calories_with = sum(item['kalori'] for item in with_current)
    total_calories_without = sum(item['kalori'] for item in without_current)

    return with_current if total_calories_with >= total_calories_without else without_current

def gizi_iterative(target):
    dp = [[] for _ in range(target + 1)]

    for food in makanan:
        for cal in range(target, food['kalori'] - 1, -1):
            new_combination = dp[cal - food['kalori']] + [food]
            if sum(item['kalori'] for item in new_combination) > sum(item['kalori'] for item in dp[cal]):
                dp[cal] = new_combination

    return dp[target]

# Grafik untuk menyimpan data
target_values = []
recursive_times = []
iterative_times = []

# Fungsi untuk memperbarui grafik
def update_graph():
    plt.figure(figsize=(8, 6))
    plt.plot(target_values, recursive_times, label='Recursive', marker='o', linestyle='-')
    plt.plot(target_values, iterative_times, label='Iterative', marker='o', linestyle='-')
    plt.title('Performance Comparison: Recursive vs Iterative')
    plt.xlabel('Target Calories')
    plt.ylabel('Execution Time (seconds)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Fungsi untuk mencetak tabel waktu eksekusi
def print_execution_table():
    table = PrettyTable()
    table.field_names = ["Target Calories", "Recursive Time (s)", "Iterative Time (s)"]
    min_len = min(len(target_values), len(recursive_times), len(iterative_times))
    for i in range(min_len):
        table.add_row([target_values[i], recursive_times[i], iterative_times[i]])
    print(table)

# Program utama
while True:
    try:
        target = int(input("Masukkan target kalori (atau ketik -1 untuk keluar): "))
        if target == -1:
            print("Program selesai. Terima kasih!")
            break
        if target < 0:
            print("Masukkan nilai target yang positif!")
            continue

        target_values.append(target)

        # Ukur waktu eksekusi algoritma rekursif
        start_time = time.time()
        gizi_recursive(target, 0)
        recursive_times.append(time.time() - start_time)

        # Ukur waktu eksekusi algoritma iteratif
        start_time = time.time()
        gizi_iterative(target)
        iterative_times.append(time.time() - start_time)

        # Cetak tabel waktu eksekusi
        print_execution_table()

        # Perbarui grafik
        update_graph()

    except ValueError:
        print("Masukkan nilai target yang valid!")

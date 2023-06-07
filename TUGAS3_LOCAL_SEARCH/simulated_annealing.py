import random
import math

# fungsi untuk menghitung jumlah queen yang saling menyerang pada papan catur
def calculate_conflicts(state):
    conflicts = 0
    for i in range(len(state)):
        for j in range(i + 1, len(state)):
            if state[i] == state[j] or abs(state[i] - state[j]) == j - i:
                conflicts += 1
    return conflicts

# fungsi untuk menghasilkan kemungkinan solusi baru dengan mengganti 
# posisi dua queen
def generate_neighbor(state):
    new_state = state.copy()
    i, j = random.sample(range(len(state)), 2)
    new_state[i], new_state[j] = new_state[j], new_state[i]
    return new_state

# fungsi untuk menentukan apakah solusi baru diterima atau tidak
def accept_solution(current_conflicts, new_conflicts, temperature):
    if new_conflicts < current_conflicts:
        return True
    delta = new_conflicts - current_conflicts
    probability = math.exp(-delta / temperature)
    return random.random() < probability

# inisialisasi posisi awal queen secara acak
start_state = [1, 3, 0, 6, 4, 7, 5, 2]
current_state = start_state

# konfigurasi parameter algoritma simulated annealing
initial_temperature = 1000
temperature_factor = 0.95
iterations_per_temperature = 100

# iterasi algoritma simulated annealing
temperature = initial_temperature
current_conflicts = calculate_conflicts(current_state)
while current_conflicts > 0 and temperature > 0.1:
    for i in range(iterations_per_temperature):
        new_state = generate_neighbor(current_state)
        new_conflicts = calculate_conflicts(new_state)
        if accept_solution(current_conflicts, new_conflicts, temperature):
            current_state = new_state
            current_conflicts = new_conflicts
    temperature *= temperature_factor

# output hasil solusi yang ditemukan
if current_conflicts == 0:
    print("posisi awal:", start_state)
    print("Solusi ditemukan:", current_state)
else:
    print("posisi awal:", start_state)
    print("Tidak ada solusi yang ditemukan.")

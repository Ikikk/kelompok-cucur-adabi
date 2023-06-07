import random

# Inisialisasi papan catur dan posisi awal queen
board_size = 8
current_state = start_state = [1, 3, 0, 6, 4, 7, 5, 2]

# Definisi fungsi untuk menghitung jumlah konflik pada papan catur
def count_conflicts(state):
    conflicts = 0
    for i in range(len(state)):
        for j in range(i+1, len(state)):
            if state[i] == state[j] or abs(state[i]-state[j]) == j-i:
                conflicts += 1
    return conflicts

# Definisi fungsi untuk mencari posisi queen yang dapat dipindahkan untuk meminimalkan konflik
def find_best_move(state):
    best_move = None
    min_conflicts = board_size
    for i in range(len(state)):
        for j in range(board_size):
            if j != state[i]:
                new_state = state.copy()
                new_state[i] = j
                new_conflicts = count_conflicts(new_state)
                if new_conflicts < min_conflicts:
                    best_move = (i, j)
                    min_conflicts = new_conflicts
    return best_move

# Definisi fungsi utama untuk menyelesaikan 8 queen tidak 
# saling menyerang dengan hill climbing
def hill_climbing(state):
    while True:
        best_move = find_best_move(state)
        if best_move is None:
            break
        i, j = best_move
        state[i] = j
        if count_conflicts(state) == 0:
            return state
    return None

# Menyelesaikan 8 queen tidak saling menyerang dengan hill climbing 
# dan mencetak hasilnya
print("Posisi awal:", start_state)
solution = hill_climbing(current_state)
if solution is not None:
    print("Solusi ditemukan:", solution)
else:
    print("Tidak ada solusi yang ditemukan.")

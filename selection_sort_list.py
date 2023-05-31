def selection_sort_list(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Daftar angka Andi
andi_value = [9, 5, 3, 8, 2]

# Menggunakan Selection Sort untuk mengurutkan daftar angka
selection_sort_list(andi_value)

# Menampilkan hasil
print("Hasil pengurutan angka Andi:", andi_value)

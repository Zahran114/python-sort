def bubble_sort_exam(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Daftar nilai Hannah
hannah_value = [78, 65, 90, 82, 70]

# Menggunakan Bubble Sort untuk mengurutkan daftar nilai
bubble_sort_exam(hannah_value)

# Menampilkan hasil
print("Hasil pengurutan nilai Hannah:", hannah_value)

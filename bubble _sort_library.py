def bubble_sort_book(sort_book):
    n = len(sort_book)
    for i in range(n):
        
        swapped = False
        for j in range(0, n-i-1):
            if sort_book[j]["Jumlah Halaman"] > sort_book[j+1]["Jumlah Halaman"]:
                
                sort_book[j], sort_book[j+1] = sort_book[j+1], sort_book[j]
                swapped = True
        
        if not swapped:
            break
    return sort_book


sort_book = [
    {"No.": 1, "Judul Buku": "Harry Potter and the Sorcerer's Stone", "Penulis": "J.K. Rowling", "Jumlah Halaman": 320},
    {"No.": 2, "Judul Buku": "To Kill a Mockingbird", "Penulis": "Harper Lee", "Jumlah Halaman": 281},
    {"No.": 3, "Judul Buku": "The Great Gatsby", "Penulis": "F. Scott Fitzgerald", "Jumlah Halaman": 180},
    {"No.": 4, "Judul Buku": "Pride and Prejudice", "Penulis": "Jane Austen", "Jumlah Halaman": 432},
    {"No.": 5, "Judul Buku": "1984", "Penulis": "George Orwell", "Jumlah Halaman": 328}
]


sorted_book_list = bubble_sort_book(sort_book)

# Menampilkan hasil pengurutan
print("Hasil pengurutan daftar buku berdasarkan jumlah halaman secara ascending:")
for book in sorted_book_list:
    print("No.:", book["No."])
    print("Judul Buku:", book["Judul Buku"])
    print("Penulis:", book["Penulis"])
    print("Jumlah Halaman:", book["Jumlah Halaman"])
    print()
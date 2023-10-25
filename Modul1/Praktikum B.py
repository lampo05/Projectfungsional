class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True
class User:
    def __init__(self, username):
        self.username = username
        self.borrowed_books = []
class Admin:
    def __init__(self, username):
        self.username = username
        self.available_books = []

# Inisialisasi buku yang tersedia
book1 = Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling")
book2 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book3 = Book("To Kill a Mockingbird", "Harper Lee")

# Inisialisasi akun admin dan user
admin = Admin("admin")
user1 = User("user1")
user2 = User("user2")

# Menambahkan buku ke daftar buku yang tersedia
admin.available_books.extend([book1, book2, book3])


# Fungsi untuk peminjaman buku oleh user
def borrow_book(user, book_title):
    for book in admin.available_books:
        if book.title == book_title and book.is_available:
            user.borrowed_books.append(book)
            book.is_available = False
            print(f"{user.username} telah meminjam buku: {book.title}")
            return
    print("Buku tidak tersedia atau sudah dipinjam.")


# Fungsi untuk pengembalian buku oleh user
def return_book(user, book_title):
    for book in user.borrowed_books:
        if book.title == book_title:
            user.borrowed_books.remove(book)
            book.is_available = True
            print(f"{user.username} telah mengembalikan buku: {book.title}")
            return
    print("Anda tidak meminjam buku ini.")


# Simulasi interaksi admin dan user
while True:
    print("\nPilihan:")
    print("1. Admin")
    print("2. User")
    print("3. Pengembalian")
    print("4. Keluar")
    choice = input("Pilih tipe akun (1/2/3/4): ")

    if choice == "1":
        admin_username = input("Masukkan username admin: ")
        if admin_username == admin.username:
            book_title = input("Masukkan judul buku yang akan ditambahkan: ")
            book_author = input("Masukkan nama penulis buku: ")
            new_book = Book(book_title, book_author)
            admin.available_books.append(new_book)
            print(f"Buku '{new_book.title}' berhasil ditambahkan ke daftar buku yang tersedia.")
        else:
            print("Username admin salah.")

    elif choice == "2":
        user_username = input("Masukkan username user: ")
        if user_username == user1.username:
            book_title = input("Masukkan judul buku yang ingin dipinjam: ")
            borrow_book(user1, book_title)
        elif user_username == user2.username:
            book_title = input("Masukkan judul buku yang ingin dipinjam: ")
            borrow_book(user2, book_title)
        else:
            print("Username user salah.")

    elif choice == "3":
        user_username = input("Masukkan username user : ")
        if user_username == user1.username:
            book_title = input("Masukkan judul buku yang ingin di kembalikan : ")
            return_book(user1, book_title)
        elif user_username == user2.username:
            book_title = input("Masukkan judul buku yang ingin di kembalikan : ")
            return_book(user2, book_title)
        else:
            print("Username user salah.")

    elif choice == "4":
        break

    else:
        print("Pilihan tidak valid. Silakan masukkan angka 1, 2,3, atau 4.")

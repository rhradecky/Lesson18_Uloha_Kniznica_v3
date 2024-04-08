class Book:
    def __init__(self, id, title, author_id, genre_id, isbn, publication_year, copies):
        self.id = id
        self.title = title
        self.author_id = author_id
        self.genre_id = genre_id
        self.isbn = isbn
        self.publication_year = publication_year
        self.copies = copies

    @classmethod
    def from_db(cls, value):
        return cls(value[0], value[1], value[2])

    @staticmethod
    def vloz_do_db(cursor, author_id, genre_id):
        print("Vlozte nazov knihy ")
        title = input()
        print("Vlozte ISBN: ")
        isbn = input()
        cursor.execute("INSERT INTO books (title, author_id, genre_id, isbn) VALUES (%s, %s, %s, %s)", (title, author_id, genre_id, isbn))

    @staticmethod
    def hladaj_v_db(cursor):
        print("Vyhladavanie knih podla ")
        print("1. Nazov")
        print("2. Autor")
        print("3. zaner")
        choice = input("#> ")

        if choice == "1":
            title = input("Zadaj Nazov:")
            cursor.execute("SELECT title FROM books")
            knihy = cursor.fetchone()
            for kniha in knihy:
                if kniha == title:
                    print("Kniha pod nazvom ", title, "najdena")
                else:
                    print("Kniha pod nazvom ", title, "sa nenachadza v DB")

        if choice == "2":
            author_id = input("Zadaj Autora:")
            cursor.execute("SELECT author_id FROM books")
            knihy = cursor.fetchone()
            for kniha in knihy:
                if kniha == author_id:
                    print("Kniha od autora ", author_id, "najdena")
                else:
                    print("Kniha od autora ", author_id, "sa nenachadza v DB")

        if choice == "3":
            genre_id = input("Zadaj hladany zaner: ")
            cursor.execute("SELECT genre_id FROM books")
            knihy = cursor.fetchone()
            for kniha in knihy:
                if kniha == genre_id:
                    print("Knihy podla zanru ", genre_id, "najdena")
                else:
                    print("Knihy podla zanru ", genre_id, "sa nenachadza v DB")



    def zobraz_knihy(cursor):
        print("-- Zoznam knih --")
        cursor.execute("SELECT * FROM books")
        books = cursor.fetchall()
        for book in books:
            print(f"ID: {book[0]}, Name: {book[1]}")






    def vymaz_z_db(cursor):
        print()
        book_id = int(input("Zadaj ID knihy, ktory chcete vymazat: "))
        cursor.execute("DELETE FROM books WHERE book_id = %s;", (book_id,))
        print()
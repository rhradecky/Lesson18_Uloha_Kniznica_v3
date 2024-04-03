import psycopg2
from author import Author
from book import Book
from genre import Genre
from members import Members


conn = psycopg2.connect(
    dbname='b4l1o2iguxktujhgmzv1',
    user='uhkelmgkhpkwcyjdl3qd',
    password='ZIuTMMFceJbOGxBmDJGxtBRfTrRVSs',
    host='b4l1o2iguxktujhgmzv1-postgresql.services.clever-cloud.com',
    port=50013
)

cursor = conn.cursor()

def vypis_menu():
    print("1. Pridat autora")
    print("2. Pridat zaner")
    print("3. Pridat knihu")
    print("4. Hladaj knihu")
    print("5. Pridat uzivatela")


def aplikacia():
    while True:
        vypis_menu()
        choice = input("Vasa moznost: ")
        if choice == "1":
            Author.vloz_do_db(cursor)
            conn.commit()
        elif choice == "2":
            Genre.vloz_do_db(cursor)
            conn.commit()
        elif choice == "3":
            Author.zobraz_autorov(cursor)
            authorID = input("ID Authora: ")
            Genre.zobraz_zanre(cursor)
            genreID = input("ID zanru: ")
            Book.vloz_do_db(cursor, authorID, genreID)
            conn.commit()

        if choice == "4":
            Search.hladaj_v_db(cursor)
            conn.commit()




        elif choice == "5":
            Members.vloz_do_db(cursor)
            Members.zobraz_uzivatelov(cursor)
            conn.commit()

        else:
            print("Neplatny vstup")

aplikacia()
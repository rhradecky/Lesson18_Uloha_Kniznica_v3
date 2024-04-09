import psycopg2
from author import Author
from book import Book
from genre import Genre
from members import Members


conn = psycopg2.connect(
    dbname='bdipmw29ejuoeccxynb1',
    user='upkjsca8ynbl11b0ikgz',
    password='f1nKXzsR6eivAWjmQDT6i6W0E7b2vG',
    host='bdipmw29ejuoeccxynb1-postgresql.services.clever-cloud.com',
    port='50013'
    port=50013
)

cursor = conn.cursor()

def vypis_menu():
    print()
    print("1. Pridat autora")
    print("2. Pridat zaner")
    print("3. Pridat knihu")
    print("4. Vymazat knihu")
    print("5. Hladaj knihu")
    print("6. Pridat uzivatela")
    print("7. Vymazat uzivatela")




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

        elif choice == "4":
            Book.zobraz_knihy(cursor)
            Book.vymaz_z_db(cursor)
            Book.zobraz_knihy(cursor)
            conn.commit()



        if choice == "5":
            print()
            Book.zobraz_knihy(cursor)
            Book.hladaj_v_db(cursor)
            conn.commit()




        elif choice == "6":
            Members.vloz_do_db(cursor)
            Members.zobraz_uzivatelov(cursor)
            conn.commit()
        elif choice == "7":
            Members.zobraz_uzivatelov(cursor)
            Members.vymaz_z_db(cursor)
            Members.zobraz_uzivatelov(cursor)
            conn.commit()
        else:
            print("Neplatny vstup")

aplikacia()
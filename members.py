class Members:
    def __init__(self, members_id, first_name, last_name,email):
        self.id = members_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email


    @classmethod
    def from_db(cls, value):
        return cls(value[0], value[1], value[2])

    @staticmethod
    def vloz_do_db(cursor):
        print("Vlozte meno: ")
        first_name = input()
        print("Vlozte priezvisko: ")
        last_name = input()
        print("Vlozte email: ")
        email = input()
        cursor.execute("INSERT INTO members (first_name, last_name, email) VALUES (%s, %s, %s)", (first_name, last_name, email))


    def vymaz_z_db(cursor):
        print("Zadaj ID uzivatela, ktoreho chcete vymazat: ")
        member_id = int(input())
        cursor.execute("DELETE FROM members WHERE member_id = %s;", (member_id,))
        print()






    def zobraz_uzivatelov(cursor):
        print("-- Zoznam autorov --")
        cursor.execute('SELECT * FROM members')
        uzivatelia = cursor.fetchall()
        for uzivatel in uzivatelia:
            print(f"ID: {uzivatel[0]}, Meno: {uzivatel[1]}, Priezvisko: {uzivatel[2]}, Email: {uzivatel[3]}")

        def __str__(self):
            return f"---MEMBER---\nID Autora: {self.first_name}\nMeno: {self.last_name}"



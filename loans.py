class Loans:
    def __init__(self, loan_id, book_id, member_id, ):
        self.loan_id = loan_id
        self.book_id = book_id
        self.member_id = member_id
        self.loan_date = loan_date
        self.due_date = due_date

    def zobraz_vypozicky(cursor):
        print("-- Zoznam vypoziciek --")
        #cursor.execute("SELECT book_id, member_id, loan_date, due_date FROM loans")
        cursor.execute("SELECT books.title, loans.loan_date, loans.due_date FROM loans INNER JOIN books ON books.book_id = loans.book_id")

        loans = cursor.fetchall()
        for loan in loans:
            print(f"Nazov knihy:: {loan[0]},            Datum Pozicky:  {loan[1]},           Pozicane do: {loan[2]}")



    def vloz_do_db(cursor, book_id, member_id):
        cursor.execute("INSERT INTO loans (book_id, member_id) VALUES (%s, %s)",(book_id, member_id))
        print("Kniha  s ID: ",book_id," bola vypozicana")

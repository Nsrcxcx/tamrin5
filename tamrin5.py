
import sqlite3

cnt = sqlite3.connect('expense.db')
c = cnt.cursor()


def create_table():
    c.execute(
        '''CREATE TABLE IF NOT EXISTS expenses (id INTEGER PRIMARY KEY, date TEXT, amount REAL)''')
    cnt.commit()


def add_cost(date, amount):
    c.execute("INSERT INTO expenses (date, amount) VALUES (?, ?)", (date, amount))
    cnt.commit()


def show_costs():
    c.execute("SELECT * FROM expenses")
    result = c.fetchall()
    print(result)


def delete_cost(expense_id):
    c.execute("DELETE FROM expenses WHERE id=?", (expense_id,))
    cnt.commit()


create_table()
while True:
    print("1.add cost")
    print("2.show costs")
    print("3.delete cost")
    print("4.exit")

    option = int(input("choose an option : "))

    if option == 1:
        date = input("enter the date of deposit : ")
        amount = float(input("enter amount of money :"))
        add_cost(date, amount)
        print("succesfully added")
    elif option == 2:
        show_costs()
    elif option == 3:
        expense_id = int(input("enter id of deposit :"))
        delete_cost(expense_id)
        print("succesfully deleted")
    elif option == 4:
        break
    else:
        print("wrong option, try again :")

cnt.close()

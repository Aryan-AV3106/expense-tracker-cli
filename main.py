import sqlite3
from datetime import datetime

class ExpenseTracker:
    def __init__(self):
        self.conn = sqlite3.connect("expenses.db")
        self.cur = self.conn.cursor()
        self._create_table()
        

    def _create_table(self):
        self.cur.execute(""" CREATE TABLE IF NOT EXISTS expenses(
                         Id INTEGER PRIMARY KEY AUTOINCREMENT,
                         Amount REAL,
                         Category TEXT,
                         Note TEXT,
                         Timestamp TEXT)
                         """)
    
    def add_expense(self):
        try : 
            print("")
            amount = float(input("Please enter the amount : "))
        except :
            print("Please enter an integer or a float number \n \n")
            return
        
        category = input("Please enter the category : ")
        note = input("Please enter a note(optional) : ")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        self.cur.execute("INSERT INTO expenses (Amount, Category, Note, Timestamp) VALUES (?,?,?,?)",(amount,category,note,timestamp))
        self.conn.commit()
        
        print()
        print("Values successfully added into the table\n\n")
        print()

    def view_expense(self):
        self.cur.execute("SELECT * FROM expenses")
        rows = self.cur.fetchall()
        if not rows: 
            print("No expenses found\n\n")
            return
            
        for row in rows:
            Timestamp = row[4]
            Amount= row[1]
            Category = row[2]
            Note = row[3]
            print(f"Time : {Timestamp} | Amount : {Amount} | Category : {Category} | Note : {Note}")
        print()
        

    def calculate_total(self):
        self.cur.execute("SELECT SUM(Amount) FROM expenses")
        total = self.cur.fetchone()
        if total[0] is None:
            print("Total spent: $0.00\n\n")
            return
        print(f"Total spent: ₹{total[0]:.2f}\n")
        print()

    def reset(self):
        self.cur.execute("DROP TABLE IF EXISTS expenses")
        print("Database resetted successfully\n\n")

    def run(self):
        while True:
            print("")
            print("Hello User, please select a choice from the menu")
            print("")

            print("1). Add an expense")
            print("2). View expenses")
            print("3). view the total expenses")
            print("4). Reset the database")
            print("5). Exit")
            print("")

            try:
                choice = int(input("Please enter Your choice : "))             # checking for valid input 
            except:
                print("Incorrect choice!!! Please enter an integer")
                print("")
                continue
            
            if choice == 1 : self.add_expense()
            elif choice == 2 : self.view_expense()
            elif choice == 3 : self.calculate_total()
            elif choice == 4 : self.reset()
            elif choice == 5 : 
                print("Goodbye,\nThank you")
                self.cur.close()
                self.conn.close()
                break
            else: 
                print("Invalid choice !!!") 
                continue

if __name__ == "__main__":
    expenses = ExpenseTracker()
    expenses.run()


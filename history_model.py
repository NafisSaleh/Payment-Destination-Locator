import sqlite3

class history_model:
    
    record_ID = None

    # def get_ID(self, user_ID):
    #     history_model.record_ID = user_ID

class transaction_history(history_model):

    def __init__(self):
        self.conn = sqlite3.connect("transactions.db")
        self.csr = self.conn.cursor()
        self.csr.execute("SELECT name FROM sqlite_master WHERE type = 'table' AND name = 'transactions'")
        self.box = self.csr.fetchall()
        self.conn.commit()
        if(len(self.box) >= 1):
            pass
        else:
            self.csr.execute("""CREATE TABLE transactions (
                user_ID text,
                bill_type text,
                method text,
                amount int,
                date text)""")
            self.conn.commit()

    def get_ID(self, user_ID):
        history_model.record_ID = user_ID

    def save_transaction(self, bill_type, method, amount, date):
        if history_model.record_ID != None:
            self.csr.execute("INSERT INTO transactions VALUES (?, ?, ?, ?, ?)", (history_model.record_ID, bill_type, method, amount, date))
            self.conn.commit()

    def show_transactions(self):
        if history_model.record_ID != None:
            self.csr.execute("SELECT * FROM transactions WHERE user_ID = ?", (history_model.record_ID,))
            box = self.csr.fetchall()
            for item in box:
                print(item)

    #Test method:
    def delete_all(self):
        self.csr.execute("DELETE FROM transactions")
        self.conn.commit()

import sqlite3

# conn = sqlite3.connect("user.db")
# csr = conn.cursor()

class user_model:

    def __init__(self):
        self.conn = sqlite3.connect("user.db")
        self.csr = self.conn.cursor()
        # self.csr.execute("""CREATE TABLE user (
        #     first_name text,
        #     last_name text, 
        #     user_ID text, 
        #     password text, 
        #     logged_in int)""")
        # self.conn.commit()

    def create_table(self):
        self.csr.execute("SELECT name FROM sqlite_master WHERE type = 'table' AND name = 'user'")
        box = self.csr.fetchall()
        self.conn.commit()
        if(len(box)>=1):
            pass
        else:
            self.csr.execute("""CREATE TABLE user (
                first_name text,
                last_name text, 
                user_ID text, 
                password text, 
                logged_in int)""")
            self.conn.commit()    

    def duplicate_checker(self, user_ID):
        self.csr.execute("SELECT * FROM user WHERE user_ID = ?", (user_ID,))
        box = self.csr.fetchall()
        self.conn.commit()
        if len(box)>=1:
            return False
        return True

    def new_user(self, firstName, lastName, user_ID, password):
        if self.duplicate_checker(user_ID):
            self.csr.execute("INSERT INTO user VALUES (?, ?, ?, ?, ?) ", (firstName, lastName, user_ID, password, 1))
            self.conn.commit()

    def login(self, user_ID, password):
        self.csr.execute("SELECT * FROM user WHERE user_ID = ? AND password = ?", (user_ID, password))    
        #box = self.csr.fetchone()
        box = self.csr.fetchall()
        self.conn.commit()
        #print(box)
        #print(len(box))
        # if type(box) == None:
        #     return False 
        if len(box) >= 1:
            #self.csr.execute("INSERT INTO user VALUES ")
            self.csr.execute("UPDATE user SET logged_in = 1 WHERE user_ID = ? AND password = ?", (user_ID, password))
            self.conn.commit()
            return True   
        return False    

    def logout(self):
        self.csr.execute("UPDATE user SET logged_in=0")
        self.conn.commit()

    def logged_in_user(self):
        self.csr.execute("SELECT user_ID FROM user WHERE logged_in = 1")
        box = self.csr.fetchone()
        self.conn.commit()
        for item in box:
            return item

    #tester method:
    def show_users(self):
        self.csr.execute("SELECT * FROM user")
        box = self.csr.fetchall()
        self.conn.commit()
        return box

    #test method:
    def delete_all(self):
        self.csr.execute("DELETE FROM user")
        self.conn.commit()    




#import sqlite3

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
                amount text,
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
            self.csr.execute("SELECT bill_type, method, amount, date FROM transactions WHERE user_ID = ?", (history_model.record_ID,))
            box = self.csr.fetchall()
            res_box = []
            for item in box:
                res_box.append(list(item))
            print("model test:")
            for item in res_box:
                print(item)
            print(res_box)    
            return res_box

    #Test method:
    def delete_all(self):
        self.csr.execute("DELETE FROM transactions")
        self.conn.commit()

    #Test method:
    def show_all(self):
        self.csr.execute("SELECT * FROM transactions")
        box = self.csr.fetchall()
        print(box)


class preferred_banks(history_model):

    def __init__(self):
        self.conn = sqlite3.connect("banks.db")
        self.csr = self.conn.cursor()
        self.csr.execute("SELECT name FROM sqlite_master WHERE type = 'table' AND name = 'banks'")
        self.box = self.csr.fetchall()
        self.conn.commit()
        if(len(self.box) >= 1):
            pass
        else:
            self.csr.execute("""CREATE TABLE banks (
                user_ID text,
                bank_name text,
                branch text,
                address text,
                contact text)""")
            self.conn.commit()

    def get_ID(self, user_ID):
        history_model.record_ID = user_ID

    def save_preference(self, bank_info):
        if history_model.record_ID != None:
            self.csr.execute("INSERT INTO banks VALUES (?, ?, ?, ?, ?)", (history_model.record_ID, bank_info[0], bank_info[1], bank_info[2], bank_info[3]))
            self.conn.commit()

    def show_banks(self):
        if history_model.record_ID != None:
            self.csr.execute("SELECT bank_name, branch, address, contact FROM banks WHERE user_ID = ?", (history_model.record_ID,))
            box = self.csr.fetchall()
            res_box = []
            for item in box:
                item_list = list(item)
                res_box.append(item_list)
            print("model test:")
            for item in res_box:
                print(item)
            print(res_box)
            return res_box

    def delete_all(self):
        self.csr.execute("DELETE FROM banks")
        self.conn.commit()
                
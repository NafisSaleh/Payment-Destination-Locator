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
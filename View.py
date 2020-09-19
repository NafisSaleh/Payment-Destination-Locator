import tkinter as tk
import Control
from tkinter import ttk
from tkinter.ttk import Notebook,Entry

f = open("demo.txt", mode = "w")
f.write("")
f.close()

f2 = open("search.txt", mode = "w")
f2.write("")
f2.close()

user_name = ""
bank_obj = Control.bank_controller()
preferred_obj = Control.preffered_banks(user_name)
historyobj = Control.transaction_history(user_name)
p = Control.registered_user()

LARGE_FONT = {"Verdana", 12, "bold"}
MEDIUM_FONT = {"Verdana", 9, "bold"}

class main_frame(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        
        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)

        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {}

        for F in (home_page, register, user_account, pay_bill, nearby_banks, wrong_location, history, nearby_banks_for_wrong, search_bank):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")

        self.show_frame(home_page)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class home_page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label_homepage = ttk.Label(self, text = "Home Page", font = LARGE_FONT)
        label_homepage.grid(row = 0, column = 0, columnspan = 2, padx = (200,0), pady = (20,20))

        def login_user():            
            user_name = entry_user_name.get()
            password = entry_password.get()
            boo = p.login(user_name, password)
            if boo :
                historyobj.update_uName(user_name)
                entry_user_name.delete(0, 'end')
                entry_password.delete(0, 'end')
                controller.show_frame(user_account)
            else :
                label_incorrect = tk.Label(self, text = "Incorrect Username or Password", fg = "red")
                label_incorrect.grid(row = 3, column = 1) 
                label_incorrect.after(2500, label_incorrect.destroy)


        label_user_name = ttk.Label(self, text = "Username", width = 20, anchor = "e")
        label_user_name.grid(row= 1, column = 0, padx = (120,10), pady = (0,10))

        entry_user_name = ttk.Entry(self, width = 20)
        entry_user_name.grid(row= 1, column = 1, pady = (0,10))


        label_password = ttk.Label(self, text = "Password", width = 20, anchor = "e")
        label_password.grid(row= 2, column = 0, padx = (120,10))

        entry_password = ttk.Entry(self, width = 20)
        entry_password.grid(row= 2, column = 1)

        label_register = ttk.Label(self, text = "Don't have an account?", width = 22)
        label_register.grid(row= 5, column = 0, columnspan = 2, padx = (110,0), pady = (20,0 ))

        button_login = ttk.Button(self, text = "Login", command = login_user)        
        button_login.grid(row = 4, column = 0, columnspan = 2, padx = (150,0), pady = (20,0))

        button_register = ttk.Button(self, text = "Register", command = lambda: controller.show_frame(register))
        button_register.grid(row = 5, column = 1, padx = (70,0),pady = (20,0))


class register(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        label_register = ttk.Label(self, text = "Register", font = LARGE_FONT)
        label_register.grid(row = 0, column = 0, columnspan = 2, padx = (200,0), pady = (20,20))
      
        def register_user():    
            input_first_name = entry_first_name.get()
            input_last_name = entry_last_name.get()
            input_user_name = entry_user_name.get()
            input_password = entry_password.get()

            boo = p.not_duplicate(input_user_name)

            if boo :
                p.add_user(input_first_name, input_last_name, input_user_name, input_password)
                entry_first_name.delete(0, 'end')
                entry_last_name.delete(0, 'end')
                entry_user_name.delete(0, 'end')
                entry_password.delete(0, 'end')          
                controller.show_frame(user_account)

            else :
                entry_user_name.delete(0, 'end')                
                label1 = tk.Label(self, text = "Username already taken \n   Try another one", fg = "red")
                label1.grid(row= 14, column = 1) 
                label1.after(2500, label1.destroy)
                
        def backToHome():
            entry_first_name.delete(0, 'end')
            entry_last_name.delete(0, 'end')
            entry_user_name.delete(0, 'end')
            entry_password.delete(0, 'end')
            controller.show_frame(home_page)

        label_first_name = ttk.Label(self, text = "First name", width = 20, anchor = "e")
        label_first_name.grid(row= 10, column = 0, padx = (150,10), pady = (0,10))
        
        entry_first_name = ttk.Entry(self, width = 20)
        entry_first_name.grid(row = 10, column = 1, pady = (0,10))

        label_last_name = ttk.Label(self, text = "Last name", width = 20, anchor = "e")
        label_last_name.grid(row= 11, column = 0, padx = (150,10), pady = (0,10))

        entry_last_name = ttk.Entry(self, width = 20)
        entry_last_name.grid(row= 11, column = 1, pady = (0,10))

        label_user_name = ttk.Label(self, text = "Choose a username", width = 20, anchor = "e")
        label_user_name.grid(row= 12, column = 0, padx = (150,10), pady = (0,10))

        entry_user_name = ttk.Entry(self, width = 20)
        entry_user_name.grid(row= 12, column = 1, pady = (0,10))

        label_password = ttk.Label(self, text = "Choose a password", width = 20, anchor = "e")
        label_password.grid(row= 13, column = 0, padx = (150,10), pady = (0,10))

        entry_password = ttk.Entry(self, width = 20)
        entry_password.grid(row= 13, column = 1, pady = (0,10))

        button_submit = ttk.Button(self, text = "Submit", command = register_user)        
        button_submit.grid(row = 15, column = 0, columnspan = 2, padx = (200,0), pady = (10,0))

        button_home = ttk.Button(self, text = " Back to Home", command = backToHome)        
        button_home.grid(row = 16, column = 0, pady = 30, columnspan = 2, padx = (200,0))

      
class user_account(tk.Frame):
    bank_name =""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
                
        def logout():
            p.logout()
            user_account.bank_name.set("                 Choose Bank")
            controller.show_frame(home_page)

        def popupmsg():
            popup = tk.Tk()
            
            def redirect_wrong_location():
                popup.destroy()
                controller.show_frame(wrong_location)
            
            def redirect():
                popup.destroy()                
                controller.show_frame(nearby_banks)
                
            popup.wm_title("Attention!")

            label_loc_det = ttk.Label(popup, text = "Location Detected", font = MEDIUM_FONT)
            label_loc_det.pack(pady = 20)

            label_location = ttk.Label(popup, text = p.get_location())
            label_location.pack(pady = (0,0))

            button_confirm = ttk.Button(popup, text = "Confirm", command = redirect)
            button_confirm.pack(side = "left", padx = (150,0))

            button_wrong_loc = ttk.Button(popup, text = "Wrong Location?", command = redirect_wrong_location)
            button_wrong_loc.pack(side = "right", padx = (0,150))

            popup.geometry("500x150")
            popup.mainloop()
            
        def show_banks():
            f2 = open("search.txt", mode = "w")
            f2.write(user_account.bank_name.get())
            f2.close()
            controller.show_frame(search_bank)

        label_user_account = ttk.Label(self, text = "User Account", font = LARGE_FONT)
        label_user_account.grid(row = 0, column = 0, columnspan = 2, padx = (150,0), pady = (20,50))

        label_nearby_bank = ttk.Label(self, text = "See Nearby Banks")
        label_nearby_bank.grid(row = 0, column = 0, padx = (150,0), pady = (70,10))

        button_nearby = ttk.Button(self, text = "Proceed", command = popupmsg)
        button_nearby.grid(row = 0, column = 1, pady = (70,10))
        
        label_search_bank = ttk.Label(self, text = "Search bank", anchor = "e")
        label_search_bank.grid(row= 1, column = 0, padx = (150,0))

        user_account.bank_name = tk.StringVar()
        
        bank_chosen = ttk.Combobox(self, width = 27, textvariable = user_account.bank_name, state = "readonly")

        bank_chosen['values'] = ('Dutch-Bangla Bank',
                                'One Bank',
                                'Islami Bank',
                                'Dhaka Bank',
                                'Prime Bank',
                                'Brac Bank',
                                'Bank Asia')

        bank_chosen.grid(row = 1, column =1)
        bank_obj.AddBankToDataFrame("Dutch-Bangla Bank","https://www.banksbd.org/dbbl/branches/dhaka.html")
        bank_obj.AddBankToDataFrame("One Bank","https://www.banksbd.org/obl/branches/dhaka.html")
        bank_obj.AddBankToDataFrame("Islami Bank","https://www.banksbd.org/ibbl/branches/dhaka.html")
        bank_obj.AddBankToDataFrame("Dhaka Bank","https://www.banksbd.org/dhbl/branches/dhaka.html")
        bank_obj.AddBankToDataFrame("Prime Bank","https://www.banksbd.org/prbl/branches/dhaka.html")
        bank_obj.AddBankToDataFrame("Brac Bank","https://www.banksbd.org/brac/branches/dhaka.html")
        bank_obj.AddBankToDataFrame("Bank Asia","https://www.banksbd.org/balb/branches/dhaka.html")

        user_account.bank_name.set("                 Choose Bank")

        button_select = ttk.Button(self, text = "Select", command = show_banks)        
        button_select.grid(row = 1, column = 2)

        label_pay = ttk.Label(self, text = "Pay Bill", anchor = "e")
        label_pay.grid(row = 2, column = 0, padx = (150,0),  pady = (10,10))
        
        button_pay = ttk.Button(self, text = "Proceed", command = lambda: controller.show_frame(pay_bill))
        button_pay.grid(row = 2, column = 1,  pady = (10,10))
        
        label_history = ttk.Label(self, text = "View history")
        label_history.grid(row = 3, column = 0, padx = (150,0))
        
        button_history = ttk.Button(self, text = "Proceed", command = lambda: controller.show_frame(history))
        button_history.grid(row = 3, column = 1)

        button_logout = ttk.Button(self, text = "Log Out", command = logout)        
        button_logout.grid(row = 4, column = 0, pady = 30, columnspan = 3, padx = (100,0))


class pay_bill(tk.Frame):
    
    n = ""
    i = ""
    e1 = ""
    e2 = ""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def goBack():
            pay_bill.n.set("               Choose Bill")
            pay_bill.i.set("            Choose Method")
            pay_bill.e1.delete(0, 'end')
            pay_bill.e2.delete(0, 'end')
            controller.show_frame(user_account)

        def popupmsg():
            popup = tk.Tk()
            historyobj.add_transaction(pay_bill.n.get(), pay_bill.e1.get(), pay_bill.e2.get(), pay_bill.i.get() )   

            def redirect():
                popup.destroy()                
                controller.show_frame(pay_bill)

            popup.wm_title("Attention!")
            label0 = ttk.Label(popup, text = "Payment Successful!!", font = MEDIUM_FONT)
            label0.pack(pady = 20)

            label1 = ttk.Label(popup, text = "     Bill Type      -     " + pay_bill.n.get(), width = 60, anchor = "center")
            label1.pack(pady = (0,10))
  
            label2 = ttk.Label(popup, text = "   Amount         -      " + pay_bill.e1.get(), width = 60, anchor = "center")
            label2.pack(pady = (0,10))

            label3 = ttk.Label(popup, text = " Payment Date     -     " + pay_bill.e2.get(), width = 60, anchor = "center")
            label3.pack(pady = (0,10))

            label4 = ttk.Label(popup, text = "Payment Method    -    " + pay_bill.i.get(), width = 60, anchor = "center")
            label4.pack(pady = (0,10))

            button1 = ttk.Button(popup, text = "Okay", command = redirect)        
            button1.pack()

            popup.geometry("400x300")
            popup.mainloop()
        
        
        label0 = ttk.Label(self, text = "Bill Payment", font = LARGE_FONT)
        label0.grid(row = 0, column = 0, columnspan = 2, padx = (150,0), pady = (20,50))

        label1 = ttk.Label(self, text = "Bill Type", anchor = "e")
        label1.grid(row= 1, column = 0, padx = (150,0), pady = (0,10))

        pay_bill.n = tk.StringVar()
        
        billchosen = ttk.Combobox(self, width = 27, textvariable = pay_bill.n, state = "readonly")
        billchosen['values'] = ('Electricity',
                                'Gas',
                                'Telephone')

        pay_bill.n.set("               Choose Bill")
        billchosen.grid(row = 1, column = 1, pady = (0,10))

        label2= ttk.Label(self, text = "Amount", width = 20, anchor = "e")
        label2.grid(row= 2, column = 0, padx = (70,0), pady = (0,10))

        pay_bill.e1 = ttk.Entry(self, width = 20)
        pay_bill.e1.grid(row= 2, column = 1, pady = (0,10))

        label3 = ttk.Label(self, text = "Payment Date", width = 20, anchor = "e")
        label3.grid(row= 3, column = 0, padx = (70,0), pady = (0,10))

        pay_bill.e2 = ttk.Entry(self, width = 20)
        pay_bill.e2.grid(row= 3, column = 1, pady = (0,10))

        label4 = ttk.Label(self, text = "Payment Method", width = 20)
        label4.grid(row= 4, column = 0, padx = (150,0), pady = (0,10))

        pay_bill.i = tk.StringVar()
        
        billchosen = ttk.Combobox(self, width = 27, textvariable = pay_bill.i, state = "readonly")

        billchosen['values'] = ('Bkash',
                                'Rocket',
                                'Nagad')
 
        pay_bill.i.set("            Choose Method")
        billchosen.grid(row = 4, column = 1, pady = (0,10))

        button_confirmpay = ttk.Button(self, text = "Confirm Payment", command = popupmsg)
        button_confirmpay.grid(row = 5, column = 1, columnspan = 2, pady = 20)
        
        button_back = ttk.Button(self, text = "Back", command = goBack)  
        button_back.grid(row = 6, column = 1, columnspan = 2, pady = 10)


class nearby_banks(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)    

        loc_String = p.get_location()
        loc_list = loc_String.split(", ")
        location_list=[]
        for loc in loc_list:
            box = loc.split(" ")
            for item in box:
                location_list.append(item) 

        print(location_list)
            
        tree_view = ttk.Treeview(self, height = "20")
        tree_view['columns'] = ("a", "b", "c", "d")
        
        tree_view.column("#0", width = 0, stretch = "no")
        tree_view.column("a", anchor = "center", width = 100)
        tree_view.column("b", anchor = "w", width = 150)
        tree_view.column("c", anchor = "w", width = 400)
        tree_view.column("d", anchor = "w", width = 240)

        tree_view.heading("#0", text = "", anchor = "w")
        tree_view.heading("a", text = "BANK NAME", anchor = "center")
        tree_view.heading("b", text = "BRANCH", anchor = "w")
        tree_view.heading("c", text = "ADDRESS", anchor = "center")
        tree_view.heading("d", text = "CONTACT", anchor = "w")
            
        tree_view.pack(pady = 20, expand = 1)
        tree_view.place(x = 0, y = 0)
        scroll_bar = ttk.Scrollbar(self, orient = "vertical", command= tree_view.yview)
        scroll_bar.pack(side = "right", fill = "y")
        tree_view.configure(yscrollcommand = scroll_bar.set)

        bank_list = bank_obj.see_nearby_banks(location_list)
        
        count = 1
        for record in bank_list:
            tree_view.insert(parent = '', index= 'end', iid = count, text = "", values = (record[0], record[1], record[2], record[3]))
            count = count + 1

        button1 = ttk.Button(self, text = "Back", command = lambda: controller.show_frame(user_account))
        button1.pack(side = "bottom", pady = (0,120))


class wrong_location(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        def select():            
            selected = my_listbox.get("anchor")
            f = open("demo.txt", mode = "w")
            f.write(selected)
            f.close()
            p.wronglc = selected
            controller.show_frame(nearby_banks_for_wrong)
            
        label1 = ttk.Label(self, text = "Select Location", font = MEDIUM_FONT)
        label1.pack(pady = (30,0))
        
        my_frame =tk.Frame(self)
        my_frame.pack(pady = (10,0))

        my_scrollbar = tk.Scrollbar(my_frame, orient = "vertical")        
        my_scrollbar.pack(side = "right", fill = "y")

        my_listbox = tk.Listbox(my_frame, width = 40, yscrollcommand = my_scrollbar.set)
        my_listbox.pack ()     
        my_list = bank_obj.get_branch_list()
        
        for item in my_list:
            my_listbox.insert("end", item)

        my_scrollbar.config(command = my_listbox.yview)  

        my_label = ttk.Label(self, text = "")
        
        button1 = ttk.Button(self, text = "Select", command = select)        
        button1.pack(pady = (5, 20))

        button2 = ttk.Button(self, text = "Cancel", command = lambda: controller.show_frame(user_account))        
        button2.pack()        


class history(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        frame1 = tk.Frame(self)
        frame1.pack(side = "top", fill = "both", expand = True)

        tablayout = Notebook(frame1)
        
        tab1 = tk.Frame(tablayout, height = 300)
        tab1.pack(fil = "both")

        tree_view = ttk.Treeview(tab1, height = "20")
        tree_view['columns'] = ("a", "b", "c", "d")
        
        tree_view.column("#0", width = 0, stretch = "no")
        tree_view.column("a", anchor = "center", width = 150)
        tree_view.column("b", anchor = "center", width = 150)
        tree_view.column("c", anchor = "center", width = 150)
        tree_view.column("d", anchor = "center", width = 150)

        tree_view.heading("#0", text = "", anchor = "w")
        tree_view.heading("a", text = "BILL TYPE", anchor = "center")
        tree_view.heading("b", text = "PAYMENT METHOD", anchor = "center")
        tree_view.heading("c", text = "AMOUNT", anchor = "center")
        tree_view.heading("d", text = "DATE", anchor = "center")
            
        tree_view.pack(pady = 20, expand = 1)
        tree_view.place(x = 0, y = 0)

        tablayout.add(tab1, text = "Transaction history")

        tab2 = tk.Frame(tablayout, height = 300)
        tab2.pack(fil = "both")
        
        tablayout.add(tab2, text = "Preferred Banks")
        tablayout.pack(fill = "both")

        def reload_transaction():
            translist = historyobj.check_transactions()            
            count1 = 1

            for record in translist:
                tree_view.insert(parent = '', index= 'end', iid = count1, text = "", values = (record[0], record[1], record[2], record[3]))
                count1 = count1 + 1

        def reload_preferred():
            preferred_list = preferred_obj.check_preferences()
            count2 = 1
            for record in preferred_list:
                tree_view_preferred.insert(parent = '', index= 'end', iid = count2, text = "", values = (record[0], record[1], record[2], record[3]))
                count2 = count2 + 1 

        def goBack():

            for i in tree_view.get_children():
                tree_view.delete(i)
            
            for i in tree_view_preferred.get_children():
                tree_view_preferred.delete(i)

            controller.show_frame(user_account)

        tree_view_preferred = ttk.Treeview(tab2, height = "20")
        tree_view_preferred['columns'] = ("a", "b", "c", "d")
        
        tree_view_preferred.column("#0", width = 0, stretch = "no")
        tree_view_preferred.column("a", anchor = "center", width = 100)
        tree_view_preferred.column("b", anchor = "w", width = 150)
        tree_view_preferred.column("c", anchor = "w", width = 400)
        tree_view_preferred.column("d", anchor = "w", width = 240)

        tree_view_preferred.heading("#0", text = "", anchor = "w")
        tree_view_preferred.heading("a", text = "BANK NAME", anchor = "center")
        tree_view_preferred.heading("b", text = "BRANCH", anchor = "w")
        tree_view_preferred.heading("c", text = "ADDRESS", anchor = "center")
        tree_view_preferred.heading("d", text = "CONTACT", anchor = "w")
            
        tree_view_preferred.pack(pady = 20, expand = 1)
        tree_view_preferred.place(x = 0, y = 0)
                    
        button1 = ttk.Button(self, text = "Back", command = goBack)        
        button1.pack(side = "bottom", pady = (0,60))

        button2 = ttk.Button(self, text = "Reload Transactions", command = reload_transaction)
        button2.pack(side = "left", padx = (170,0), pady = (100,30))

        button3 = ttk.Button(self, text = "   Reload Banks     ", command = reload_preferred)
        button3.pack(side = "right",padx = (0,180), pady = (100,30))

    
class nearby_banks_for_wrong(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def reloadpage():            
            f =  open("demo.txt", mode = "r")
            var1 = f.read()
            f.close()
            df_list_final = bank_obj.see_nearby_banks_wrong(var1)
            
            
            count = 1
            for record in df_list_final:
                tree_view.insert(parent = '', index= 'end', iid = count, text = "", values = (record[0], record[1], record[2], record[3]))
                count = count + 1

            
        def goBack():
            f =  open("demo.txt", mode = "r")
            var1 = f.read()
            f.close()
            df_list_final = bank_obj.see_nearby_banks_wrong(var1)
           
            for i in tree_view.get_children():
                tree_view.delete(i)

            controller.show_frame(user_account)

        tree_view = ttk.Treeview(self, height = "20")
        tree_view['columns'] = ("a", "b", "c", "d")
        
        tree_view.column("#0", width = 0, stretch = "no")
        tree_view.column("a", anchor = "center", width = 100)
        tree_view.column("b", anchor = "w", width = 150)
        tree_view.column("c", anchor = "w", width = 400)
        tree_view.column("d", anchor = "w", width = 240)

        tree_view.heading("#0", text = "", anchor = "w")
        tree_view.heading("a", text = "BANK NAME", anchor = "center")
        tree_view.heading("b", text = "BRANCH", anchor = "w")
        tree_view.heading("c", text = "ADDRESS", anchor = "center")
        tree_view.heading("d", text = "CONTACT", anchor = "w")
            
        tree_view.pack(pady = 20, expand = 1)
        tree_view.place(x = 0, y = 0)
        scroll_bar = ttk.Scrollbar(self, orient = "vertical", command= tree_view.yview)
        scroll_bar.pack(side = "right", fill = "y")
        tree_view.configure(yscrollcommand = scroll_bar.set)

       

        button2 = ttk.Button(self, text = "Back", command = goBack)                                
        button2.pack(side = "bottom", pady = (0,80))

        button1 = ttk.Button(self, text = "Reload", command = reloadpage)        
        button1.pack(side = "bottom", pady = (0,30))


class search_bank(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        def reloadpage():            
            f2 =  open("search.txt", mode = "r")
            var2 = f2.read()
            f2.close()
            search_bank_list = bank_obj.search_bank(var2)
            count = 1
            for record in search_bank_list:
                tree_view.insert(parent = '', index= 'end', iid = count, text = "", values = (record[0], record[1], record[2], record[3]))
                count = count + 1

            
        def goBack():
            f2 =  open("search.txt", mode = "r")
            var2 = f2.read()
            f2.close()
            search_bank_list = bank_obj.search_bank(var2)

            for i in tree_view.get_children():
                tree_view.delete(i)

            controller.show_frame(user_account)
        
        def selectvalue():
            chosen_bank = tree_view.focus()
            test = tree_view.item(chosen_bank)
            preferred_obj.save_preference(test["values"])
        

        tree_view = ttk.Treeview(self, height = "20")
        tree_view['columns'] = ("a", "b", "c", "d")
        
        tree_view.column("#0", width = 0, stretch = "no")
        tree_view.column("a", anchor = "center", width = 100)
        tree_view.column("b", anchor = "w", width = 150)
        tree_view.column("c", anchor = "w", width = 400)
        tree_view.column("d", anchor = "w", width = 240)

        tree_view.heading("#0", text = "", anchor = "w")
        tree_view.heading("a", text = "BANK NAME", anchor = "center")
        tree_view.heading("b", text = "BRANCH", anchor = "w")
        tree_view.heading("c", text = "ADDRESS", anchor = "center")
        tree_view.heading("d", text = "CONTACT", anchor = "w")
            
        tree_view.pack(pady = 20, expand = 1)
        tree_view.place(x = 0, y = 0)
        scroll_bar = ttk.Scrollbar(self, orient = "vertical", command= tree_view.yview)
        scroll_bar.pack(side = "right", fill = "y")
        tree_view.configure(yscrollcommand = scroll_bar.set)
                
        button1 = ttk.Button(self, text = "Back", command = goBack)
        button1.pack(side = "right", padx = (0,180), pady = (450,0))

        button2 = ttk.Button(self, text = "Bookmark", command = selectvalue)         
        button2.pack(side = "left", padx = (180,0), pady = (450,0))

        button3 = ttk.Button(self, text = "Reload", command = reloadpage)                      
        button3.pack(side = "bottom", pady = (0,120))

app = main_frame()
app.title("main_frame") 
app.geometry("600x600")
app.mainloop()




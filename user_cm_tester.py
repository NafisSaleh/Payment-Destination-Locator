# import sys
# print(sys.path)
import user_controller
import user_model
import bill_controller
import history_controller
import bank_controller

user = user_controller.registered_user()
user.add_user("Tariqul", "Alam", "TA71", "abc321")
print("****USER ADDED****")
print("\n")
print("****CONTENTS OF USER DATABASE IN A LIST****")
user.show_users()
print("\n")   
user.logout()
print("****LOGGED OUT****")
print("\n")
print("****CONTENTS OF USER DATABASE IN A LIST AFTER LOGGING OUT****")
user.show_users()
print("\n")
if user.login("TA71", "abc321"):
    print("****LOGGED IN SUCCESSFULLY!****")
print("****CONTENTS OF USER DATABASE IN A LIST AFTER LOGGING IN****")    
user.show_users()
print("\n")
user.logout()
if user.login("bb23","jhbui"):
    pass
else:
    print("Wrong user ID or password")
    print("****LOG IN FAILED!****")
print("\n")    

print("****CONTENTS OF USER DATABASE IN A LIST****")    
user.show_users()
print("\n")
print("****CLEARING THE TABLE****")
user.delete_all()
print("\n")
print("****CONTENTS OF USER DATABASE AFTER DELETION:****")
user.show_users()
print("\n")

user.add_user("Tariqul", "Alam", "TA71", "abc321")
print("****USER ADDED****")
print("\n")

print("****FINDING USER LOCATION****")
location = user_controller.user_controller.get_location()
print("****LOCATION DETECTED****")
print(location)
print("\n")

#user.login("TA71", "abc321")
print("****CONTENTS OF USER DATABASE IN A LIST****")
user.show_users()
print("\n")
print("****FINDING USER ID OF USER CURRENTLY LOGGED IN****")
logged_in_uID = user.logged_in_user()
print("\n")
#print(type(logged_in_uID))
print("****USER ID OF USER CURRENTLY LOGGED IN****")
print(logged_in_uID)
print("\n")
history = history_controller.history_controller(logged_in_uID)
user_history = history_controller.transaction_history()
user_history.delete_all()
bill = bill_controller.bill_controller()
print("****BILL PAYMENT SYSTEM****")
bill.pay(user_history)
print("\n")
print("****TRANSACTION HISTORY OF LOGGED IN USER IN A LIST:****")
user_history.check_transactions()
print("\n")

bank = bank_controller.bank_controller()
print("****ADDING ISLAMI BANK TO THE DATAFRAME****")
bank.AddBankToDataFrame("Islamic Bank","https://www.banksbd.org/ibbl/branches/dhaka.html")
print("****ISLAMI BANK ADDED SUCCESSFULLY****")
print("\n")
print("****ADDING BRAC BANK TO THE DATAFRAME****")
bank.AddBankToDataFrame("Brac Bank","https://www.banksbd.org/brac/branches/dhaka.html")
print("****BRAC BANK ADDED SUCCESSFULLY****")
print("\n")

print("****SEARCHING THE DATAFRAME FOR NEARBY BANKS BY A LOCATION****")
bank.SearchDataFrameByLocation("Banasree")
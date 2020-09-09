import user_controller

class bill_controller:

    user_ID = None

    def __init__(self):
        if user_controller.user_controller.user_ID != None:
            bill_controller.user_ID = user_controller.user_controller.user_ID

    def pay(self, transaction_history_object):
        bill_type = input("Bill type: ")
        amount = input("Amount: ")
        date = input("Date(dd/mm/yy) of Payment: ")
        method = None
        print("Select payment method:")
        print("1: Bkash")
        print("2: Rocket")
        print("3: Nagad")
        checker = input("Enter method here: ")
        if checker == "1":
            print("Selected payment method: Bkash")
            method = "Bkash"
        elif checker == "2":
            print("Selected payment method: Rocket")
            method = "Rocket"
        elif checker == "3":
            print("Selected payment method: Nagad")
            method = "Nagad"
        else:
            print("Invalid input!")
            method = "Not specified"
        transaction_history_object.add_transaction(bill_type, method, amount, date)
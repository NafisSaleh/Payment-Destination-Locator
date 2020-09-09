import history_model

class history_controller:

    user_ID = None

    def __init__(self, uID):
        history_controller.user_ID = uID

class transaction_history(history_controller):

    def __init__(self):
        self.model = history_model.transaction_history()
        self.model.get_ID(history_controller.user_ID)

    def add_transaction(self, bill_type, method, amount, date):
        self.model.save_transaction(bill_type, method, amount, date)

    def check_transactions(self):
        self.model.show_transactions()

    def delete_all(self):
        self.model.delete_all()    
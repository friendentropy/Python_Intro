class Mpesa:
    def __init__(self, account_balance, phone_number):
        self.account_balance = account_balance
        self.phone_number = phone_number

    def send_money(self, amount, receipient):
        if self.account_balance >= amount:
            self.account_balance -= amount
            print(f"{amount} KES sent to {receipient} successfully")
        else:
            print("insufficient Amount to Send Money")


class PersonalMpesa(Mpesa):
    def __init__(self, account_balance, phone_number, idno):
        super().__init__(account_balance, phone_number)
        self.idno = idno

    def buyairtime(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            print(f"{amount} KES airtime bought successfully")
        else:
            print("insufficient Amount to Buy Airtime")


class BusinessMpesa(Mpesa):
    def __init__(self, account_balance, phone_number, business_id):
        super().__init__(account_balance, phone_number)
        self.business_id = business_id

    def receive_payment(self, amount):
        self.account_balance += amount
        print(f"{amount} KES received from a customer")


personal = PersonalMpesa(2000, 723465782, 40514756)
personal.send_money(300, 746738331)
personal.buyairtime(150)
business = BusinessMpesa(4500, 7843465782, 40514756)
business.receive_payment(6700)
business.send_money(2300, 746738331)

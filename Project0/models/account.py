
class BankAccount:

    # client is an integer so we can choose based on id from the client database
    def __init__(self, client=0, bank_id=0, amount=0):
        self.client = client
        self.bank_id = bank_id
        self.amount = amount

    def json(self):
        return {
            "client": self.client,
            "bankId": self.bank_id,
            "amount": self.amount
        }

    @staticmethod
    def json_parse(json):
        acc = BankAccount()
        acc.client = json["client"]
        acc.bank_id = json["bankId"]
        acc.amount = json["amount"]
        return acc

    def __repr__(self):
        return str(self.json())

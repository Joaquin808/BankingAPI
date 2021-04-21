from models.client import Client
from models.account import BankAccount


class TempDB:

    accounts = {
        1: BankAccount(client=1, bank_id=1, amount=1500),
        2: BankAccount(client=1, bank_id=2, amount=1000),
        3: BankAccount(client=3, bank_id=3, amount=500)
    }

    clients = {
        1: Client(client_id=1, name="Joaquin", accounts=[accounts[2].json(), accounts[1].json()], active=True),
        2: Client(client_id=2, name="Mia", accounts=accounts[2].json(), active=True),
        3: Client(client_id=3, name="Gabriel", accounts=accounts[3].json(), active=True),
    }


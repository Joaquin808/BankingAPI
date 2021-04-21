from abstract_dao.account_dao import AccountDAO
from util.temp_db import TempDB as db


class AccountDAOImplemented(AccountDAO):

    def create_account(self, account):
        db.accounts[int(account.bank_id)] = account
        db.clients[int(account.client)].accounts.append(account)
        return db.accounts[account.bank_id]

    def get_account(self, client_id, bank_id):
        # return db.clients[client_id].accounts[bank_id]

        for account in db.accounts.values():
            if account.bank_id == bank_id:
                acc = account

                return acc if acc else None

    def get_all_accounts_for_client(self, client_id):
        return [account.__dict__ for account in db.accounts.values() if account.client == client_id]

    def update_account(self, update):
        db.accounts.update({update.bank_id: update})

    def delete_account(self, client_id, bank_id):
        del db.accounts[bank_id]

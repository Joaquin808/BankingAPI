from daos.account_dao_impl import AccountDAOImpl


class AccountService:
    account_dao = AccountDAOImpl()

    @classmethod
    def create_account(cls, account):
        return cls.account_dao.create_account(account)

    @classmethod
    def get_account(cls, client_id, bank_id):
        return cls.account_dao.get_account(client_id, bank_id)

    @classmethod
    def get_all_accounts(cls, client_id):
        return cls.account_dao.get_all_accounts_for_client(client_id)

    @classmethod
    def update_account(cls, update):
        return cls.account_dao.update_account(update)

    @classmethod
    def delete_account(cls, client_id, bank_id):
        return cls.account_dao.delete_account(client_id, bank_id)

    @classmethod
    def account_deposit(cls, client_id, bank_id, deposit):
        account = cls.account_dao.get_account(client_id, bank_id)
        account.amount += deposit
        return cls.update_account(account)

    @classmethod
    def account_withdraw(cls, client_id, bank_id, withdraw):
        account = cls.account_dao.get_account(client_id, bank_id)
        account.amount -= withdraw
        return cls.update_account(account)

    @classmethod
    def get_accounts_between_values(cls, client_id, amount_1, amount_2):
        return cls.account_dao.get_account_with_values(client_id, amount_1, amount_2)

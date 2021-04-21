from abc import ABC, abstractmethod


class AccountDAO(ABC):

    @abstractmethod
    def create_account(self, account):
        pass

    @abstractmethod
    def get_account(self, client_id, bank_id):
        pass

    @abstractmethod
    def get_all_accounts_for_client(self, client_id):
        pass

    @abstractmethod
    def update_account(self, update):
        pass

    @abstractmethod
    def delete_account(self, client_id, bank_id):
        pass


from abstract_dao.account_dao import AccountDAO
from exceptions.resource_not_found import ResourceNotFound
from models.account import BankAccount
from util.db_connection import connection
import logger


class AccountDAOImpl(AccountDAO):

    def create_account(self, account):
        sql = "INSERT INTO accounts VALUES(%s, %s, %s) RETURNING *"
        cursor = connection.cursor()
        cursor.execute(sql, (account.client, account.bank_id, account.amount))
        record = cursor.fetchone()
        connection.commit()

    def get_account(self, client_id, bank_id):
        sql = "SELECT * FROM clients WHERE client_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [client_id])
        record = cursor.fetchone()
        if record:
            pass
        else:
            logger.log_error(f"ResourceNotFound error while retrieving account from {client_id}")
            raise ResourceNotFound(f"Client with id of {client_id} does not exist")

        sql = "SELECT * FROM accounts WHERE bank_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [bank_id])
        record = cursor.fetchone()
        if record:
            return BankAccount(int(record[0]), int(record[1]), int(record[2]))
        else:
            logger.log_error(f"ResourceNotFound error while retrieving account {bank_id}")
            raise ResourceNotFound(f"Account with id of {bank_id} was not found")

    def get_all_accounts_for_client(self, client_id):
        sql = "SELECT * FROM accounts WHERE client = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [client_id])
        records = cursor.fetchall()
        account_list = []
        for record in records:
            account = BankAccount(int(record[0]), int(record[1]), int(record[2]))
            account_list.append(account.json())

        return account_list

    def update_account(self, update):
        sql = "UPDATE accounts SET client=%s, amount=%s WHERE bank_id=%s RETURNING *"
        cursor = connection.cursor()
        cursor.execute(sql, (update.client, update.amount, update.bank_id))
        connection.commit()
        record = cursor.fetchone()
        if record:
            return record
        else:
            logger.log_error(f"ResourceNotFound error while updating account {update.bank_id} for client {update.client}")
            ResourceNotFound(f"Account with id of {update.bank_id} could not be updated")

    def delete_account(self, client_id, bank_id):
        sql = "DELETE FROM accounts WHERE bank_id = %s RETURNING *"
        cursor = connection.cursor()
        cursor.execute(sql, [bank_id])
        record = cursor.fetchone()
        if record:
            connection.commit()
        else:
            logger.log_error(f"ResourceNotFound error while deleting {bank_id}")
            raise ResourceNotFound(f"Account with id of {bank_id} could not be found")

    def get_account_with_values(self, client_id, amount_1, amount_2):
        sql = "SELECT * FROM accounts WHERE amount < %s and amount > %s and client = %s"
        cursor = connection.cursor()
        cursor.execute(sql, (amount_1, amount_2, client_id))
        connection.commit()
        accounts = cursor.fetchall()

        account_list = []
        for account in accounts:
            account = BankAccount(int(account[0]), int(account[1]), int(account[2]))
            account_list.append(account.json())

        return account_list

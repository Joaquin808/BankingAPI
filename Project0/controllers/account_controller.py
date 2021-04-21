from flask import jsonify, request

from exceptions.resource_not_found import ResourceNotFound
from models.account import BankAccount
from services.account_service import AccountService
from services.client_service import ClientService


def route(app):
    @app.route("/clients/<client_id>/accounts", methods=["GET"])
    def get_all_accounts_for_client(client_id):
        try:
            ClientService.get_client(client_id)
        except ResourceNotFound as r:
            return r.message, 400

        if len(request.args) > 0:
            try:
                amountLessThan = request.args["amountLessThan"]
                amountGreaterThan = request.args["amountGreaterThan"]
                return jsonify(AccountService.get_accounts_between_values(int(client_id), int(amountLessThan), int(amountGreaterThan))), 200
            except TypeError:
                return f"Incorrect parameters, please use amountGreaterThan or amountLessThan", 400
            except KeyError:
                return f"Incorrect parameters, please use amountGreaterThan or amountLessThan", 400
            except ValueError:
                return f"Incorrect parameter values input, please input numbers only", 400
            except ResourceNotFound as r:
                return r.message, 400
        else:
            return jsonify(AccountService.get_all_accounts(int(client_id))), 200

    @app.route("/clients/<client_id>/accounts/<bank_id>", methods=["GET"])
    def get_account_for_client_by_bank_id(client_id, bank_id):
        try:
            return jsonify(AccountService.get_account(int(client_id), int(bank_id))), 200
        except ResourceNotFound as r:
            return r.message, 404
        except ValueError:
            if isinstance(client_id, int):
                return f"{bank_id} " + "was not a valid input, please input a number", 404
            elif isinstance(bank_id, int):
                return f"{client_id} " + "was not a valid input, please input a number", 404
            else:
                return f"{client_id} and {bank_id} are not valid inputs, please input a number", 404

    @app.route("/clients/<client_id>/accounts", methods=["POST"])
    def post_account_for_client(client_id):
        account = BankAccount.json_parse(request.json)
        account = AccountService.create_account(account)
        return f"Account for client with id of {client_id} was successfully created", 201

    @app.route("/clients/<client_id>/accounts/<bank_id>", methods=["PUT"])
    def put_account_for_client(client_id, bank_id):
        account = BankAccount.json_parse(request.json)
        account.bank_id = int(bank_id)
        AccountService.update_account(account)
        return jsonify(account.json()), 200

    @app.route("/clients/<client_id>/accounts/<bank_id>", methods=["DELETE"])
    def delete_accounts_for_client(client_id, bank_id):
        try:
            AccountService.delete_account(int(client_id), int(bank_id))
            return "", 204
        except ValueError:
            return "Incorrect value input, please only input numbers", 400
        except ResourceNotFound as r:
            return r.message, 400

    @app.route("/clients/<client_id>/accounts/<bank_id>", methods=["PATCH"])
    def patch_account_deposit_withdraw(client_id, bank_id):
        for key in request.json:
            if key == "deposit":
                AccountService.account_deposit(int(client_id), int(bank_id), request.json[key])
                return f"You deposited {request.json[key]} to this account", 200
            if key == "withdraw":
                AccountService.account_withdraw(client_id, bank_id, request.json[key])
                return f"You withdrew {request.json[key]} from this account", 200

    @app.route("/clients/<client_id>/accounts/<bank_id1>/transfer/<bank_id2>", methods=["PATCH"])
    def patch_account_transfer(client_id, bank_id1, bank_id2):
        try:
            amount = request.json["amount"]
            account1 = AccountService.get_account(int(client_id), int(bank_id1))
            account2 = AccountService.get_account(int(client_id), int(bank_id2))

            account1.amount -= amount
            AccountService.update_account(account1)
            account2.amount += amount
            AccountService.update_account(account2)
            return "Transfer complete", 201
        except ResourceNotFound as r:
            return r.message, 404
        except ValueError:
            return "Incorrect input value, please only input numbers", 400

    @app.route("/clients/<client_id>/accounts?amountLessThan=<amount_1>&amountGreaterThan=<amount_2>", methods=["GET"])
    def get_accounts_between_values(client_id, amount_1, amount_2):
        print("running method")
        return jsonify(AccountService.get_accounts_between_values(int(client_id), int(amount_1), int(amount_2)))

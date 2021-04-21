from flask import jsonify, request

from exceptions.resource_not_found import ResourceNotFound
from models.client import Client
from services.client_service import ClientService

import logger


def route(app):

    @app.route("/clients", methods=["GET"])
    def get_all_clients():
        return jsonify(ClientService.all_clients()), 200

    @app.route("/clients/<client_id>", methods=["GET"])
    def get_client(client_id):
        try:
            client = ClientService.get_client(int(client_id))
            return jsonify(client), 200
        except ResourceNotFound as r:
            return r.message, 404
        except ValueError:
            logger.log_error("ValueError was thrown when trying to retrieve a client")
            return f"Please enter a number, {client_id} is not a valid input", 404

    @app.route("/clients", methods=["POST"])
    def post_client():
        client = Client.json_parse(request.json)
        client = ClientService.create_client(client)
        return f"Client with id of {request.json['clientId']} created successfully", 201

    @app.route("/clients/<client_id>", methods=["PUT"])
    def put_client(client_id):
        try:
            client = Client.json_parse(request.json)
            client.client_id = int(client_id)
            ClientService.update_client(client)
            return jsonify(client.json()), 200
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/clients/<client_id>", methods=["DELETE"])
    def delete_client(client_id):
        try:
            ClientService.delete_client(int(client_id))
            return "", 204
        except ResourceNotFound as r:
            return r.message, 404


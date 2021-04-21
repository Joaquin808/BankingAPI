from abstract_dao.client_dao import ClientDAO
from util.temp_db import TempDB as db


class ClientDOAImplemented(ClientDAO):

    def create_client(self, client):
        db.clients[int(client.client_id)] = client

    def get_client(self, client_id):
        return db.clients[int(client_id)]

    def update_client(self, new_client):
        db.clients.update({new_client.id, new_client})

    def all_clients(self):
        return [client.__dict__ for client in db.clients.values()]

    def delete_client(self, client_id):
        del db.clients[int(client_id)]

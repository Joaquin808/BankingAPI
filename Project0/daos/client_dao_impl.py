from abstract_dao.client_dao import ClientDAO
from exceptions.resource_not_found import ResourceNotFound
from models.client import Client
from util.db_connection import connection
import logger


class ClientDAOImpl(ClientDAO):

    def create_client(self, client):
        sql = "INSERT INTO clients VALUES(%s, %s, %s) RETURNING *"
        cursor = connection.cursor()
        cursor.execute(sql, (client.client_id, client.name, client.active))
        record = cursor.fetchone()
        connection.commit()

    def get_client(self, client_id):
        sql = "SELECT * FROM clients WHERE client_id = %s"

        cursor = connection.cursor()
        cursor.execute(sql, [client_id])

        record = cursor.fetchone()
        if record:
            return Client(int(record[0]), record[1], record[2]).json()
        else:
            logger.log_error(f"ResourceNotFound error while retrieving {client_id}")
            raise ResourceNotFound(f"Client with id of {client_id} could not be found")

    def update_client(self, new_client):
        sql = "UPDATE clients SET name=%s, active=%s WHERE client_id = %s RETURNING *"
        # client = self.get_client(new_client.client_id)
        cursor = connection.cursor()
        cursor.execute(sql, (new_client.name, new_client.active, new_client.client_id))
        connection.commit()
        client = cursor.fetchone()
        if client:
            return cursor.fetchone()
        else:
            logger.log_error(f"ResourceNotFound error while updating {new_client.client_id}")
            raise ResourceNotFound(f"Client with the id of {new_client.client_id} does not exist")

    def all_clients(self):
        sql = "SELECT * FROM clients"
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        client_list = []

        for record in records:
            client = Client(int(record[0]), record[1], record[2])
            client_list.append(client.json())

        return client_list

    def delete_client(self, client_id):
        sql = "DELETE FROM clients WHERE client_id = %s RETURNING *"
        cursor = connection.cursor()
        cursor.execute(sql, [client_id])
        record = cursor.fetchone()
        if record:
            connection.commit()
        else:
            logger.log_error(f"ResourceNotFound error while deleting {client_id}")
            raise ResourceNotFound(f"Client with id of {client_id} could not be found")

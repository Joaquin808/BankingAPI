from daos.client_dao_impl import ClientDAOImpl


class ClientService:

    client_dao = ClientDAOImpl()

    @classmethod
    def create_client(cls, client):
        return cls.client_dao.create_client(client)

    @classmethod
    def get_client(cls, client_id):
        return cls.client_dao.get_client(int(client_id))

    @classmethod
    def all_clients(cls):
        return cls.client_dao.all_clients()

    @classmethod
    def update_client(cls, new_client):
        return cls.client_dao.update_client(new_client)

    @classmethod
    def delete_client(cls, client_id):
        return cls.client_dao.delete_client(int(client_id))

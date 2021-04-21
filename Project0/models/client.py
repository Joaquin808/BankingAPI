
class Client:

    def __init__(self, client_id=0, name="", active=True):
        self.client_id = client_id
        self.name = name
        self.active = active

    def json(self):
        return{
            "clientId": self.client_id,
            "name": self.name,
            "active": self.active
        }

    @staticmethod
    def json_parse(json):
        client = Client()
        client.client_id = json["clientId"] if "clientId" in json else 0
        client.name = json["name"] if "name" in json else "null"
        client.active = json["active"] if "active" in json else False
        return client

    def __repr__(self):
        return str(self.json())


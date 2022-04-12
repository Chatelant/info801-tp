class Client:
    def __init__(self, name, cdc):
        self.name = name
        self.cdc = cdc

    def __str__(self):
        print("Client : " + self.name + "CahierDesCharges" + self.cdc)

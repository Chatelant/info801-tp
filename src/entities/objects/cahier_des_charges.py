class CahierDesCharges:
    def __init__(self, cost, time, quantity, version):
        self.cost = cost
        self.time = time
        self.quantity = quantity
        self.version = version

    def __str__(self):
        return f"CahierDesCharges : \n    version : {self.version}\n    cost : {self.cost}\n    time : {self.time}\n    quantity : {self.quantity}\n"
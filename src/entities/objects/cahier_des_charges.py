class CahierDesCharges:
    def __init__(self, requirements, cost, time, quantity, version):
        self.requirements = requirements
        self.cost = cost
        self.time = time
        self.quantity = quantity
        self.version = version

    def __str__(self):
        return f"CahierDesCharges : V{self.version} cost={self.cost} time={self.time} quantity={self.quantity} requirements={self.requirements}"
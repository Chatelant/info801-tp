class Produit:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return f"Produit : {self.name} ~ Quantitée : {self.quantity}"

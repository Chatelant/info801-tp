class Produit:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        print(f"Produit : name={self.name}")
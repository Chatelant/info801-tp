"""
class Client:
    def __init__(self, name, cdc):
        self.name = name
        self.cdc = cdc

    def __str__(self):
        print("Client : " + self.name + "CahierDesCharges" + self.cdc)

    def run(self):
        pass
"""


def Client(self, client_MO_Q, log):
    # Demande de produit
    log.put("Client : " + self.name + " demande un produit")
    client_MO_Q.put("demande_produit")

    offre_acceptee = False
    while not offre_acceptee:
        # Reception des contre offres (elle arrivent toutes en même temps dans un array)
        contre_offre = client_MO_Q.get()
        if demanderClientFront(contre_offre):
            # Acceptation de l'offre
            log.put("Le client accepte l'offre :" + contre_offre)
            client_MO_Q.put("accepte_offre")
            offre_acceptee = True
        else:
            # Refus des offres
            log.put("Le client a refusé l'offre :" + contre_offre)
            client_MO_Q.put("refuse_offre")

    # Reception du produit
    produit = client_MO_Q.get()
    log.put("Le client a recu le produit :" + produit)


def demanderClientFront(contre_offre):
    return True

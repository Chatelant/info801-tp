from src.entities.objects.action_enum import Action
from src.entities.objects.cahier_des_charges import CahierDesCharges


class Client:
    def __init__(self):
        self.produit_fini = False

    def client(self, client_MO_Q, log):
        # Demande de produit.py
        log.put(["CL", "Le client demande un produit.py", 1])
        client_MO_Q.put({
            Action.DEMANDE_PRODUIT: CahierDesCharges("requirements",
                                                     "cost",
                                                     "time",
                                                     "quantity",
                                                     "version")
        })

        offre_acceptee = False

        while not offre_acceptee:
            # Format de contre_offre : {Action.CONTRE_OFFRE: CahierDesCharges}
            contre_offre = client_MO_Q.get()
            log.put(["CL", "Contre offre : " + str(contre_offre), 2])
            try:
                contre_offre = contre_offre[Action.CONTRE_OFFRE]
                if self.demanderClientFront(contre_offre):
                    log.put(["CL", "Le client accepte l'offre : " + str(contre_offre), 1])
                    offre_acceptee = True
                    client_MO_Q.put({
                        Action.ACCEPTE_OFFRE: contre_offre
                    })
                else:
                    log.put(["CL", "Le client a refusé l'offre : " + str(contre_offre), 1])
                    client_MO_Q.put({
                        Action.REFUSE_OFFRE: contre_offre
                    })
            except KeyError:
                pass

        # Reception du produit.py
        produit = client_MO_Q.get()[Action.PRODUIT]
        log.put(["CL", "Le client a recu le produit.py :" + str(produit), 2])
        self.produit_fini = True

    def demanderClientFront(self, contre_offre):
        return True

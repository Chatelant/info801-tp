from time import sleep

from src.entities.objects.action_enum import Action
from src.entities.objects.cahier_des_charges import CahierDesCharges
from src.config import *

class Client:
    def __init__(self):
        self.produit_fini = False

    def client(self, client_MO_Q, log, dialogUser, dialogDisplay):
        sleep(2)
        # Demande de produit.py
        sleep(SLEEP_TIME)
        log.put(["CL", "Demande un super produit", 1])
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
            sleep(SLEEP_TIME)
            log.put(["CL", "Reçoit une contre offre", 2])
            try:
                contre_offre = contre_offre[Action.CONTRE_OFFRE]
                if self.demanderClientFront(contre_offre, dialogUser, dialogDisplay):
                    # log.put(["CL", "Le client accepte l'offre : " + str(contre_offre), 1])
                    sleep(SLEEP_TIME)
                    log.put(["CL", "Accepte l'offre envoyée", 1])
                    offre_acceptee = True
                    client_MO_Q.put({
                        Action.ACCEPTE_OFFRE: contre_offre
                    })
                else:
                    # log.put(["CL", "Le client a refusé l'offre : " + str(contre_offre), 1])
                    sleep(SLEEP_TIME)
                    log.put(["CL", "Refuse l'offre envoyée", 1])
                    client_MO_Q.put({
                        Action.REFUSE_OFFRE: contre_offre
                    })
            except KeyError:
                pass

        # Reception du produit.py
        produit = client_MO_Q.get()
        # log.put(["CL", "Le client a recu le produit.py :" + str(produit), 2])
        sleep(SLEEP_TIME)
        log.put(["CL", "Reçoit le super produit fini !", 2])
        self.produit_fini = True

    def demanderClientFront(self, contre_offre, dialogUser, dialogDisplay):
        dialogDisplay.put(f"Le fabricant vous propose la contre offre suivante (o/n) : \n {str(contre_offre)}")
        return dialogUser.get() == "o"

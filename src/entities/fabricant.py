import os
import random
import time
from src.entities.objects.action_enum import Action
from src.entities.objects.cahier_des_charges import CahierDesCharges
from src.entities.objects.produit import Produit
from src.config import *


def Fabricant(i, MOD_fabricant_Q, log):
    # Recuperation du cdc
    while True:
        message = MOD_fabricant_Q.get()
        # Un autre fabricant s'occupe du cahier des charges
        if Action.OFFRE_KO in message:
            time.sleep(SLEEP_TIME)
            log.put(["FAB", i, "Offre refusée, message reçu", 1])
            time.sleep(SLEEP_TIME)
            log.put(["FAB", i, "", 1])
            break
        # Ce fabricant s'occupe du cahier des charges (donc de faire le produit)
        elif Action.OFFRE_OK in message:
            time.sleep(SLEEP_TIME)
            log.put(["FAB", i, "Demande de produit reçu", 1])
            time.sleep(SLEEP_TIME)
            log.put(["FAB", i, "Produit en cours de fabrication", 1])
            time.sleep(SLEEP_TIME)
            log.put(["FAB", i, "Envoie du produit fini", 4])
            MOD_fabricant_Q.put({
                Action.PRODUIT: Produit(f"Brosse à dent", message[Action.OFFRE_OK].quantity)
            })

        # Offre toujours en négociation
        else:
            time.sleep(SLEEP_TIME)
            log.put(["FAB", i, f"Reçoit le cahier des charges", 1])
            time.sleep(SLEEP_TIME)
            log.put(["FAB", i, "Etudie le cahier des charges " + str(i), 2])
            time.sleep(SLEEP_TIME)
            log.put(["FAB", i, "Rédige la contre offre " + str(i), 3])
            time.sleep(SLEEP_TIME)
            log.put(["FAB", i, f"Envoie une contre offre", 4])
            MOD_fabricant_Q.put({
                Action.CONTRE_OFFRE: CahierDesCharges(
                    message[Action.APPEL_OFFRE].cost - (
                            (message[Action.APPEL_OFFRE].cost / 100) * random.randrange(1, 5, 1)),
                    message[Action.APPEL_OFFRE].time + (
                            (message[Action.APPEL_OFFRE].time / 100) * random.randrange(1, 5, 1)),
                    message[Action.APPEL_OFFRE].quantity,
                    message[Action.APPEL_OFFRE].version + 1
                )
            })
        time.sleep(2)

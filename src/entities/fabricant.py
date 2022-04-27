import os
import time
from src.entities.objects.action_enum import Action
from src.entities.objects.cahier_des_charges import CahierDesCharges
from src.entities.objects.produit import Produit


def Fabricant(i, MOD_fabricant_Q, log):
    id = os.getpid()
    # log.put(["FAB", i, f"Fabricant {id} : start", 1])

    # Recuperation du cdc
    # cahier_des_charges = MOD_fabricant_Q.get()[Action.APPEL_OFFRE]
    while True:
        message = MOD_fabricant_Q.get()
        # log.put(["FAB", i, f"Fabricant {id} : message reçu", 1])

        # Un autre fabricant s'occupe du cahier des charges
        if Action.OFFRE_KO in message:
            log.put(["FAB", i, "Offre refusée, message reçu", 1])
            log.put(["FAB", i, "", 1])
            break
        # Ce fabricant s'occupe du cahier des charges (donc de faire le produit)
        elif Action.OFFRE_OK in message:
            log.put(["FAB", i, "Demande de produit reçu", 1])
            log.put(["FAB", i, "Produit en cours de fabrication", 1])
            log.put(["FAB", i, "Envoie du produit fini", 4])
            MOD_fabricant_Q.put({
                Action.PRODUIT: Produit(f"Fabricant {id} : Super produit")
            })

        # Offre toujours en négociation
        else:
            log.put(["FAB", i, f"Reçoit le cahier des charges", 1])
            log.put(["FAB", i, "Etudie le cahier des charges", 2])
            log.put(["FAB", i, "Rédige la contre offre", 3])
            log.put(["FAB", i, f"Envoie une contre offre", 4])
            MOD_fabricant_Q.put({
                Action.CONTRE_OFFRE: CahierDesCharges("Nouveaurequirements",
                                                      "Nouveaucost",
                                                      "Nouveautime",
                                                      "Nouveauquantity",
                                                      "Nouveauversion")
            })

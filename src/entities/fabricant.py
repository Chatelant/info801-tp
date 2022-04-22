import time
from random import random
from src.entities.objects.action_enum import Action
from src.entities.objects.cahier_des_charges import CahierDesCharges
from src.entities.objects.produit import Produit


def Fabricant(MOD_fabricant_Q, log):
    log.put("Fabricant start")
    # Recuperation du cdc
    # cahier_des_charges = MOD_fabricant_Q.get()[Action.APPEL_OFFRE]

    while True:
        message = MOD_fabricant_Q.get()
        log.put("Le fabricant a reçu message")


        # Un autre fabricant s'occupe du cahier des charges
        if Action.OFFRE_KO in message:
            log.put("Fabricant KO")

            break
        # Ce fabricant s'occupe du cahier des charges (donc de faire le produit)
        elif Action.OFFRE_OK in message:
            log.put("Fabricant OK")
            time.sleep(random.randint(5, 7))
            MOD_fabricant_Q.put({
                Action.PRODUIT: Produit("Super produit")
            })

        # Offre toujours en négociation
        else:
            log.put("Fabricant envoie une contre offre")
            MOD_fabricant_Q.put({
                Action.CONTRE_OFFRE: CahierDesCharges("Nouveaurequirements",
                                                      "Nouveaucost",
                                                      "Nouveautime",
                                                      "Nouveauquantity",
                                                      "Nouveauversion")
            })

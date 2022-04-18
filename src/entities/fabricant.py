import time
from random import random
from src.entities.objects.action_enum import Action
from src.entities.objects.cahier_des_charges import CahierDesCharges
from src.entities.objects.produit import Produit


def Fabricant(MOD_fabricant_Q, log):
    log.put("Fabricant start")
    # Recuperation du cdc
    cahier_des_charges = MOD_fabricant_Q.get()[Action.APPEL_OFFRE]
    log.put("Le fabricant a reçu le cahier des charges : " + str(cahier_des_charges))
    # time.sleep(random.randint(5, 7))

    # Envoie d'une contre offre
    MOD_fabricant_Q.put({
        Action.CONTRE_OFFRE: CahierDesCharges("Nouveaurequirements",
                                              "Nouveaucost",
                                              "Nouveautime",
                                              "Nouveauquantity",
                                              "Nouveauversion")
    })

    while True:
        time.sleep(1)
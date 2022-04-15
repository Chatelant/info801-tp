import time
from random import random
from src.entities.objects.action_enum import Action
from src.entities.objects.cahier_des_charges import CahierDesCharges
from src.entities.objects.produit import Produit



def Fabricant(MOD_fabricant_Q, log):
    cahier_des_charges = MOD_fabricant_Q.get()[Action.APPEL_OFFRE]
    log.put("Le fabricant a reçu le cahier des charges : " + str(cahier_des_charges))
    time.sleep(random.randint(5, 10))
    MOD_fabricant_Q.put({
        Action.CONTRE_OFFRE: CahierDesCharges("Nouveaurequirements",
                                              "Nouveaucost",
                                              "Nouveautime",
                                              "Nouveauquantity",
                                              "Nouveauversion")
    })
    while True:
        reponse_client = MOD_fabricant_Q.get()
        if (Action.APPEL_OFFRE in reponse_client):
            #Modification du cahier des charges
            MOD_fabricant_Q.put({
                Action.CONTRE_OFFRE: CahierDesCharges("Nouveaurequirements",
                                                      "Nouveaucost",
                                                      "Nouveautime",
                                                      "Nouveauquantity",
                                                      "Nouveauversion")
            })
        elif (Action.OFFRE_OK in reponse_client):
            #Le fabricant est définitivement écarté du processus
            break
        elif (Action.OFFRE_KO in reponse_client):
            #Le fabricant est missioné pour réaliser le produit.py
            time.sleep(5)
            MOD_fabricant_Q.put({
                Action.PRODUIT: Produit("Super produit")
            })
            break


import time
from multiprocessing import Queue, Process

from src.config import *


from src.entities.fabricant import Fabricant
from src.entities.objects.action_enum import Action
from src.entities.objects.produit import Produit


def maitre_oeuvre(client_MO_Q, log):
    # En attente d'un cahier des charges client
    cdc = client_MO_Q.get()[Action.DEMANDE_PRODUIT]
    log.put(["MO", "Maitre d'oeuvre a reçu le cdc du client", 1])

    Queues_MO_Fabricant = [Queue() for i in range(NB_FABRICANT)]
    Fabricants = [Process(target=Fabricant, args=(Queues_MO_Fabricant[i], log)) for i in range(NB_FABRICANT)]
    for fabricant in Fabricants:
        fabricant.start()

    # Attendre le lancement des fabricants
    time.sleep(1)

    log.put(["MO", "MO envoie appel d'offre au fab", 3])
    for queue in Queues_MO_Fabricant:
        queue.put({
            Action.APPEL_OFFRE: cdc
        })

    # On se met en attente de la réponse des fabricants
    contre_offres = []
    log.put(["MO", "MO attends les contres offres", 4])
    for queue in Queues_MO_Fabricant:
        contre_offre = queue.get()[Action.CONTRE_OFFRE]
        contre_offres.append(contre_offre)

    log.put(["MO", "MO a toutes les contres offres : " + str(contre_offres), 4])

    for contre_offre in contre_offres:
        log.put(["MO", "MO a envoyé la contre offre au client", 2])
        client_MO_Q.put({Action.CONTRE_OFFRE: contre_offre})
        reponse_client = client_MO_Q.get()
        if Action.ACCEPTE_OFFRE in reponse_client:
            log.put(["MO", "Le client a accepté l'offre du fabricant", 1])
            time.sleep(1)
            # TODO : demande de fabrication au fabricant
            log.put(["MO", "Maitre d'oeuvre envoie le produit fini au client", 2])
            client_MO_Q.put({Action.PRODUIT: Produit("Nom du produit")})
            break
        elif Action.REFUSE_OFFRE in reponse_client:
            log.put(["MO", "Le client a refusé l'offre du fabricant", 1])


    while True:
        time.sleep(1)
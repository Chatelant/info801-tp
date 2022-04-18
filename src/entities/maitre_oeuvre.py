from multiprocessing import Queue, Process

from fabricant import Fabricant
from src.entities.objects.action_enum import Action
from src.entities.objects.produit import Produit

NB_FABRICANT = 3


def maitre_oeuvre(client_MO_Q, log):
    # En attente d'un cahier des charges client
    log.put("Maitre d'oeuvre attends le cahier des charges")
    cdc = client_MO_Q.get()[Action.DEMANDE_PRODUIT]

    # On envoie au client une contre offre
    log.put("Maitre d'oeuvre a reçu le cdc du client")
    client_MO_Q.put({Action.CONTRE_OFFRE: cdc})
    log.put("Maitre d'oeuvre a envoyé la contre offre")

    if Action.ACCEPTE_OFFRE in client_MO_Q.get():
        # Envoie au client du produit fini (correspond à la fin de chaine)
        log.put("Maitre d'oeuvre envoie le produit fini au client")
        client_MO_Q.put({Action.PRODUIT: Produit("Nom du produit")})



import time
from multiprocessing import Queue, Process

from src.config import *

from src.entities.fabricant import Fabricant
from src.entities.objects.action_enum import Action
from src.entities.objects.produit import Produit


def maitre_oeuvre(client_MO_Q, log):
    log.put("Init du fabricant")
    Queues_MO_Fabricant = [Queue() for i in range(NB_FABRICANT)]
    Fabricants = [Process(target=Fabricant, args=(Queues_MO_Fabricant[i], log)) for i in range(NB_FABRICANT)]
    for fabricant in Fabricants:
        fabricant.start()
    # Attendre le lancement des fabricants
    time.sleep(1)

    # En attente d'un cahier des charges client
    log.put("Maitre d'oeuvre attends le cahier des charges")
    cdc = client_MO_Q.get()[Action.DEMANDE_PRODUIT]
    log.put("Maitre d'oeuvre a reçu le cdc du client")

    index_fabricant_retenu = None
    while index_fabricant_retenu is None:
        log.put("MO envoie appel d'offre au fab")
        for queue in Queues_MO_Fabricant:
            queue.put({
                Action.APPEL_OFFRE: cdc
            })

        # On se met en attente de la réponse des fabricants
        contre_offres = []
        log.put("MO attends les contres offres")
        for queue in Queues_MO_Fabricant:
            contre_offre = queue.get()[Action.CONTRE_OFFRE]
            contre_offres.append(contre_offre)

        log.put("MO a toutes les contres offres : " + str(contre_offres))

        responses_client = []
        for index, contre_offre in enumerate(contre_offres):
            log.put("MO a envoyé la contre offre au client")
            client_MO_Q.put({Action.CONTRE_OFFRE: contre_offre})
            reponse = client_MO_Q.get()
            if (Action.ACCEPTE_OFFRE in reponse):
                index_fabricant_retenu = index  # TODO is this true ?
            responses_client.append(reponse)

        if index_fabricant_retenu is not None:
            for i in range(NB_FABRICANT):
                if i == index_fabricant_retenu:
                    log.put(f"Le client a accepté l'offre du fabricant {i}")
                    Queues_MO_Fabricant[i].put({
                        Action.OFFRE_OK: True
                    })
                    produit = Queues_MO_Fabricant[index].get()

                    log.put("Maitre d'oeuvre envoie le produit fini au client")
                    client_MO_Q.put({
                        Action.PRODUIT: produit
                    })
                else:
                    Queues_MO_Fabricant[i].put({
                        Action.OFFRE_KO: True
                    })
                    log.put(f"Le client a refusé l'offre du fabricant {i}")

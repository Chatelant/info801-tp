import time
from multiprocessing import Queue, Process

from src.config import *

from src.entities.fabricant import Fabricant
from src.entities.objects.action_enum import Action


def maitre_oeuvre(client_MO_Q, log):
    Queues_MO_Fabricant = [Queue() for i in range(NB_FABRICANT)]
    Fabricants = [Process(target=Fabricant, args=(i, Queues_MO_Fabricant[i], log)) for i in range(NB_FABRICANT)]
    for fabricant in Fabricants:
        fabricant.start()
    # Attendre le lancement des fabricants
    time.sleep(1)

    # En attente d'un cahier des charges client
    log.put(["MO", "Attends un cahier des charges", 1])
    cdc = client_MO_Q.get()[Action.DEMANDE_PRODUIT]
    log.put(["MO", "Reçoit le cahier des charges du client", 1])

    index_fabricant_retenu = -1
    while index_fabricant_retenu == -1:
        log.put(["MO", "Envoi des appels d'offre aux fabricants", 3])
        for queue in Queues_MO_Fabricant:
            queue.put({
                Action.APPEL_OFFRE: cdc
            })

        # On se met en attente de la réponse des fabricants
        contre_offres = []
        log.put(["MO", "Attends les contres offres...", 4])
        for queue in Queues_MO_Fabricant:
            contre_offre = queue.get()[Action.CONTRE_OFFRE]
            contre_offres.append(contre_offre)

        # log.put(["MO", "MO a toutes les contres offres : " + str(contre_offres), 4])
        log.put(["MO", "A reçu toutes les contres offres", 4])

        for index, contre_offre in enumerate(contre_offres):
            log.put(["MO", "Envoie une contre offre au client", 2])
            client_MO_Q.put({Action.CONTRE_OFFRE: contre_offre})
            reponse = client_MO_Q.get()
            if Action.ACCEPTE_OFFRE in reponse:
                index_fabricant_retenu = index  # TODO is this true ?
                # log.put(["MO", "Index fab retenu : " + str(index_fabricant_retenu), 3])
                break

        # log.put("Index avant cond = " + str(index_fabricant_retenu))
        if index_fabricant_retenu != -1:
            for i in range(NB_FABRICANT):
                # TODO : probleme :
                if i == index_fabricant_retenu:
                    log.put(["MO", f"Le client a accepté l'offre du fabricant {i}", 1])
                else:
                    Queues_MO_Fabricant[i].put({
                        Action.OFFRE_KO: True
                    })
                    log.put(["MO", f"Le client a refusé l'offre du fabricant {i}", 1])
                    log.put(["MO", f"Offre du fabricant {i} refusée", 3])

            log.put(["MO", f"Demande au fabricant {index_fabricant_retenu} le produit fini", 3])
            Queues_MO_Fabricant[index_fabricant_retenu].put({
                Action.OFFRE_OK: True
            })
            produit = Queues_MO_Fabricant[index_fabricant_retenu].get()
            log.put(["MO", "Reçoit le produit fini", 4])

            log.put(["MO", "Envoi le super produit fini au client", 2])
            client_MO_Q.put({
                Action.PRODUIT: produit
            })
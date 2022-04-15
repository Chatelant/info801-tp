from multiprocessing import Queue, Process
from src.entities.objects.action_enum import Action
from src.entities.objects.cahier_des_charges import CahierDesCharges

from fabricant import Fabricant

NB_FABRICANT = 3

def maitre_oeuvre(client_MO_Q, log):
    cahier_des_charges = client_MO_Q.get()[Action.DEMANDE_PRODUIT]
    log.put("Le maitre d'oeuvre a recu la demande du client : " + str(cahier_des_charges))

    #Initialisation des fabricants
    MOD_fabricant_Q = [Queue() for i in range(NB_FABRICANT)]
    Fabricants = [Process(target=Fabricant, args=(MOD_fabricant_Q[i], log)) for i in range(NB_FABRICANT)]
    for fabricant in Fabricants:
        fabricant.start()

    #L'index (dans les tableaux ci-dessus) du fabricant qui a remporté l'appel d'offre
    fabricant_choisi_index = None

    while fabricant_choisi_index is None:
        contre_offres = []

        # envoie sur toutes les queues des fabricants le cahier des charges
        for queue in MOD_fabricant_Q:
            queue.put({
                Action.APPEL_OFFRE: cahier_des_charges
            })

        # reception de la contre-offre des fabricants
        for queue in MOD_fabricant_Q:
            contre_offres.append(queue.get()[Action.CONTRE_OFFRE])

        # Soummission de toutes les contre-offres au client
        for index_fabricant, contre_offre in enumerate(contre_offres):
            # une fois que toutes les contre-offres sont recues, on les envoie au client
            client_MO_Q.put({
                Action.CONTRE_OFFRE: contre_offre
            })
            # le client répond s'il accepte ou non
            reponse_client = client_MO_Q.get()
            if Action.ACCEPTE_OFFRE in reponse_client:
                fabricant_choisi_index = index_fabricant
                log.put("Le client a accepte l'offre du fabricant " + str(index_fabricant))
                break

        # Si le client a accepté au moins une offre, on envoie une réponse aux fabricants
        if(fabricant_choisi_index is not None):
            for index_fabricant in range(NB_FABRICANT):
                if(index_fabricant == fabricant_choisi_index):
                    MOD_fabricant_Q[index_fabricant].put({
                        Action.OFFRE_OK: contre_offre
                    })
                else:
                    MOD_fabricant_Q[index_fabricant].put({
                        Action.OFFRE_KO: contre_offre
                    })
        # s'il n'en accepte pas, modification du CDC et on recommence
        else:
            log.put("Le client n'a pas accepte l'offre, on recommence en changeant le cahier des charges")
            # ==========
            # Modification du CDC à faire
            # ==========

    produit = Fabricants[fabricant_choisi_index].get()
    log.put("Le fabricant " + str(fabricant_choisi_index) + " a produit.py le produit.py : " + str(produit))
    client_MO_Q.put({
        Action.PRODUIT: produit
    })

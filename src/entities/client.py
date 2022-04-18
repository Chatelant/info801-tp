from src.entities.objects.action_enum import Action
from src.entities.objects.cahier_des_charges import CahierDesCharges


def client(client_MO_Q, log):
    # Demande de produit.py
    log.put("Le client demande un produit.py")
    client_MO_Q.put({
        Action.DEMANDE_PRODUIT: CahierDesCharges("requirements",
                                                 "cost",
                                                 "time",
                                                 "quantity",
                                                 "version")
    })

    offre_acceptee = False

    while not offre_acceptee:
        # Format de contre_offre : {Action.CONTRE_OFFRE: CahierDesCharges}
        contre_offre = client_MO_Q.get()
        log.put("Contre offre : " + str(contre_offre))
        try:
            contre_offre = contre_offre[Action.CONTRE_OFFRE]
            if demanderClientFront(contre_offre):
                log.put("Le client accepte l'offre : " + str(contre_offre))
                offre_acceptee = True
                client_MO_Q.put({
                    Action.ACCEPTE_OFFRE: contre_offre
                })
            else:
                log.put("Le client a refusé l'offre : " + str(contre_offre))
                client_MO_Q.put({
                    Action.REFUSE_OFFRE: contre_offre
                })
        except KeyError:
            log.put("Client tjrs en attente")

    # Reception du produit.py
    produit = client_MO_Q.get()[Action.PRODUIT]
    log.put("Le client a recu le produit.py :" + str(produit))


def demanderClientFront(contre_offre):
    return True
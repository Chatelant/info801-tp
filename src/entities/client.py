from src.entities.objects.action_enum import Action
from src.entities.objects.cahier_des_charges import CahierDesCharges

def Client(client_MO_Q, log):
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
        #Format de contre_offre : {Action.CONTRE_OFFRE: CahierDesCharges}
        contre_offre = client_MO_Q.get()
        if demanderClientFront(contre_offre):
            log.put("Le client accepte l'offre : " + contre_offre)
            offre_acceptee = True
            client_MO_Q.put({
                Action.ACCEPTE_OFFRE: contre_offre
            })
        else:
            log.put("Le client a refusé l'offre : " + contre_offre)
            client_MO_Q.put({
                Action.REFUSE_OFFRE: contre_offre
            })

    # Reception du produit.py
    produit = client_MO_Q.get()[Action.PRODUIT]
    log.put("Le client a recu le produit.py :" + produit)


def demanderClientFront(contre_offre):
    return True

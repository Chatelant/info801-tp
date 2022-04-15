from enum import Enum


class Action(Enum):
    DEMANDE_PRODUIT = "demande_produit",
    APPEL_OFFRE = "appel_offre",
    ETUDE_APPEL_OFFRE = "etude_appel_offre",
    ETUDE_CDC = "etude_cdc",
    CONTRE_OFFRE = "contre_offre",
    CONTRE_AVIS = "contre_avis",
    CONTRE_OFFRE_BE = "contre_offre_be",
    ACCEPTE_OFFRE = "accepte_offre",
    OFFRE_OK = "offre_ok",
    REFUSE_OFFRE = "refuse_offre",
    OFFRE_KO = "offre_ko",
    PRODUIT = "produit.py",

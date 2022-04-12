import time
import dearpygui.dearpygui as dpg

height = 100

# TODO: ajouter plus de lignes si besoin pour l'affichage
def update(nb, value):
    dpg.set_value("fo_line_" + str(nb), value)
    time.sleep(2)


def setup(i):
    h = (i * height) + 100 # défini la position de départ de la fenêtre "fabricant"
    with dpg.node(label="Fournisseur " + str(i), pos=[700, h], ):
        with dpg.node_attribute(tag="fo_node1_" + str(i)):
            pass
        with dpg.node_attribute(tag="fo_node2_" + str(i), shape=dpg.mvNode_PinShape_Circle):
            dpg.add_text(tag="fo_line1_" + str(i), default_value="")
            dpg.add_text(tag="fo_line2_" + str(i), default_value="")
            dpg.add_text(tag="fo_line3_" + str(i), default_value="")


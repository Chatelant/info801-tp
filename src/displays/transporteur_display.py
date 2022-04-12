import time
import dearpygui.dearpygui as dpg

width = 100

# TODO: ajouter plus de lignes si besoin pour l'affichage
def update(nb, value):
    dpg.set_value("fo_line_" + str(nb), value)
    time.sleep(2)


def setup(i):
    w = (i * width) + 100 # défini la position de départ de la fenêtre "fabricant"
    with dpg.node(label="Transporteur " + str(i), pos=[w, 500], ):
        with dpg.node_attribute(tag="tr_node1_" + str(i)):
            pass
        with dpg.node_attribute(tag="tr_node2_" + str(i), shape=dpg.mvNode_PinShape_Circle):
            dpg.add_text(tag="tr_line1_" + str(i), default_value="")
            dpg.add_text(tag="tr_line2_" + str(i), default_value="")
            dpg.add_text(tag="tr_line3_" + str(i), default_value="")


import time
import dearpygui.dearpygui as dpg

width = 700
height = 200

# TODO: ajouter plus de lignes si besoin pour l'affichage
def update(nb, value):
    dpg.set_value("fa_line_" + str(nb), value)
    time.sleep(2)


def setup(i):
    w = width
    h = (i * height) + 40 # défini la position de départ de la fenêtre "fabricant"
    with dpg.node(label="Fabricant " + str(i), pos=[w, h], ):
        with dpg.node_attribute(tag="fa_node1_" + str(i)):
            dpg.add_text(tag="fa_line1_" + str(i), default_value="FABRICANT")
            dpg.add_text(tag="fa_space1_" + str(i), default_value="")
            dpg.add_text(tag="fa_line3_" + str(i), default_value="BUREAU D'ETUDE", bullet=True)
            dpg.add_text(tag="fa_line4_" + str(i), default_value="")
            dpg.add_text(tag="fa_line5_" + str(i), default_value="ATELIER DE PROTOTYPAGE", bullet=True)
            dpg.add_text(tag="fa_line6_" + str(i), default_value="")
        with dpg.node_attribute(tag="fa_node2_" + str(i), shape=dpg.mvNode_PinShape_Circle):
            pass


import time
import dearpygui.dearpygui as dpg

width = 700
height = 200

class FabDisplay:
    def __init__(self):
        self.nb = -1

    def setup(self, i):
        w = width
        h = (i * height) + 40 # défini la position de départ de la fenêtre "fabricant"
        self.nb = i
        with dpg.node(label="Fabricant " + str(self.nb), pos=[w, h], ):
            with dpg.node_attribute(tag="fa_node1_" + str(self.nb)):
                dpg.add_text(tag="fa_title1_" + str(self.nb), default_value="FABRICANT")
                dpg.add_text(tag="fa_line1_" + str(self.nb), default_value="")
                dpg.add_text(tag="fa_line4_" + str(self.nb), default_value="")
                dpg.add_text(tag="fa_space1_" + str(self.nb), default_value="")
                dpg.add_text(tag="fa_title2_" + str(self.nb), default_value="BUREAU D'ETUDE", bullet=True)
                dpg.add_text(tag="fa_line2_" + str(self.nb), default_value="")
                dpg.add_text(tag="fa_title3_" + str(self.nb), default_value="ATELIER DE PROTOTYPAGE", bullet=True)
                dpg.add_text(tag="fa_line3_" + str(self.nb), default_value="")
            with dpg.node_attribute(tag="fa_node2_" + str(self.nb), shape=dpg.mvNode_PinShape_Circle):
                pass

    def update(self, val, nb):
        dpg.set_value("fa_line" + str(nb) + "_" + str(self.nb), val)
        time.sleep(2)
        if nb == 1:
            dpg.set_value("fa_line2_" + str(self.nb), "Etudie le cahier des charges")
            time.sleep(2)
            dpg.set_value("fa_line3_" + str(self.nb), "Rédige la contre offre")
            time.sleep(2)
        else:
            dpg.set_value("fa_line1_" + str(self.nb), "")
            dpg.set_value("fa_line2_" + str(self.nb), "")
            dpg.set_value("fa_line3_" + str(self.nb), "")
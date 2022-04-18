import time
import dearpygui.dearpygui as dpg


# TODO: ajouter plus de lignes si besoin pour l'affichage
def update(tag, value):
    dpg.set_value(tag, value)
    time.sleep(2)


def setup():
    with dpg.node(label="Maitre d'Oeuvre", pos=[400, 250]):
        with dpg.node_attribute(tag="mo_node1"):
            dpg.add_text(tag="mo_line1", default_value="CANAL 1")
            dpg.add_text(tag="mo_space1", default_value="")
        with dpg.node_attribute(tag="mo_node2", shape=dpg.mvNode_PinShape_Circle):
            dpg.add_text(tag="mo_line2", default_value="")
        with dpg.node_attribute(tag="mo_node3", attribute_type=dpg.mvNode_Attr_Output,
                                shape=dpg.mvNode_PinShape_Circle):
            dpg.add_text(tag="mo_line3", default_value="CANAL 2")
            dpg.add_text(tag="mo_space3", default_value="")
        with dpg.node_attribute(tag="mo_node4", attribute_type=dpg.mvNode_Attr_Output):
            dpg.add_text(tag="mo_space4", default_value="")

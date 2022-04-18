import time
import dearpygui.dearpygui as dpg


# TODO: ajouter plus de lignes si besoin pour l'affichage
def update(tag, value):
    dpg.set_value(tag, value)
    time.sleep(2)


def setup():
    with dpg.node(label="Client", pos=[200, 250]):
        with dpg.node_attribute(tag="cl_node1", attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_Circle):
            dpg.add_text(tag="cl_line1", default_value="CLIENT")
        with dpg.node_attribute(tag="cl_node2", attribute_type=dpg.mvNode_Attr_Output):
            dpg.add_text(tag="cl_line2", default_value="")
            dpg.add_text(tag="cl_space2", default_value="")
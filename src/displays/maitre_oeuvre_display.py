import time
import dearpygui.dearpygui as dpg

class MODisplay:
    def __init__(self):
        pass

    def setup(self):
        with dpg.node(label="Maitre d'Oeuvre", pos=[400, 250]):
            with dpg.node_attribute(tag="mo_node1"):
                dpg.add_text(tag="mo_title1", default_value="CANAL 1")
                dpg.add_text(tag="mo_line1", default_value="")
                dpg.add_text(tag="mo_space1", default_value="")
            with dpg.node_attribute(tag="mo_node2", shape=dpg.mvNode_PinShape_Circle):
                dpg.add_text(tag="mo_line2", default_value="")
            with dpg.node_attribute(tag="mo_node3", attribute_type=dpg.mvNode_Attr_Output,
                                    shape=dpg.mvNode_PinShape_Circle):
                dpg.add_text(tag="mo_title2", default_value="CANAL 2")
                dpg.add_text(tag="mo_line3", default_value="")
                dpg.add_text(tag="mo_space3", default_value="")
            with dpg.node_attribute(tag="mo_node4", attribute_type=dpg.mvNode_Attr_Output):
                dpg.add_text(tag="mo_line4", default_value="")
                dpg.add_text(tag="mo_space4", default_value="")

    def update(self, val, tag_nb):
        for i in range(4):
            if i + 1 == tag_nb:
                 dpg.set_value("mo_line" + str(tag_nb), val)
            else:
                dpg.set_value("mo_line" + str(i+1), "")
        time.sleep(2)
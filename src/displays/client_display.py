import time
import dearpygui.dearpygui as dpg


class ClientDisplay:
    def __init__(self):
        pass

    def setup(self):
        with dpg.node(label="Client", pos=[200, 250]):
            with dpg.node_attribute(tag="cl_node1", attribute_type=dpg.mvNode_Attr_Output,
                                    shape=dpg.mvNode_PinShape_Circle):
                dpg.add_text(tag="cl_title1", default_value="CANAL 1")
                dpg.add_text(tag="cl_line1", default_value="")
            with dpg.node_attribute(tag="cl_node2", attribute_type=dpg.mvNode_Attr_Output):
                dpg.add_text(tag="cl_line2", default_value="")
                dpg.add_text(tag="cl_space2", default_value="")

    def update(self, val, tag_nb):
        if tag_nb == 1:
            dpg.set_value("cl_line1", val)
            dpg.set_value("cl_line2", "")
        elif tag_nb == 2:
            dpg.set_value("cl_line1", "")
            dpg.set_value("cl_line2", val)
        time.sleep(2)

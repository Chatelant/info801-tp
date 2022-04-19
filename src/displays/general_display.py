import client_display
import maitre_oeuvre_display
import fabricant_display

import dearpygui.dearpygui as dpg

from src.config import NB_FABRICANT


def on_load_maquette():
    if not dpg.get_item_alias("maquette"):
        with dpg.window(label="Maquette", tag="maquette"):
            with dpg.node_editor(tag="editor"):
                client_display.setup()
                maitre_oeuvre_display.setup()
                for i in range(NB_FABRICANT):
                    fabricant_display.setup(i)

            # Connecte le client et le maitre d'oeuvre
            dpg.add_node_link("cl_node1", "mo_node1", parent="editor")
            dpg.add_node_link("cl_node2", "mo_node2", parent="editor")

            # Connecte le maitre d'oeuvre et les fabricants
            for i in range(NB_FABRICANT):
                dpg.add_node_link("mo_node3", "fa_node1_" + str(i), parent="editor")
                dpg.add_node_link("mo_node4", "fa_node2_" + str(i), parent="editor")

        dpg.set_primary_window("maquette", True)


def on_start():
    print("TODO")
    # client_display.update("cl_line1", "AHHHHHHHHHHH")
    # client_display.update("cl_line2", "AHHHHHHHHHHH")
    # client_display.update("cl_line3", "AHHHHHHHHHHH")
    # maitre_oeuvre_display.update("mo_line1", "???")


def init_display():
    dpg.create_context()
    with dpg.window(label="Application", width=150):
        # dpg.add_button(label="Maquette Fabricant", callback=on_load_maquette)
        dpg.add_button(label="Simulation", callback=on_start)

    on_load_maquette()

    dpg.create_viewport(title='Supply Chain Management', width=1280, height=720)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()


init_display()
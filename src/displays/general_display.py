import client_display
import maitre_oeuvre_display
import fabricant_display
import fournisseur_display
import transporteur_display

import dearpygui.dearpygui as dpg


def on_load_maquette1():
    if dpg.get_item_alias("maquette2"): dpg.delete_item("maquette2")

    if not dpg.get_item_alias("maquette1"):
        with dpg.window(label="Maquette", tag="maquette1"):
            with dpg.node_editor(tag="editor"):
                client_display.setup()
                maitre_oeuvre_display.setup()
                for i in range(3):
                    fabricant_display.setup(i)

            # Connecte le client et le maitre d'oeuvre
            dpg.add_node_link("cl_node1", "mo_node1", parent="editor")
            dpg.add_node_link("cl_node2", "mo_node2", parent="editor")

            # Connecte le maitre d'oeuvre et les fabricants
            for i in range(3):
                dpg.add_node_link("mo_node3", "fa_node1_" + str(i), parent="editor")
                dpg.add_node_link("mo_node4", "fa_node2_" + str(i), parent="editor")

        dpg.set_primary_window("maquette1", True)


def on_load_maquette2():
    if dpg.get_item_alias("maquette1"): dpg.delete_item("maquette1")

    if not dpg.get_item_alias("maquette2"):
        with dpg.window(label="Maquette", tag="maquette2"):
            with dpg.node_editor(tag="editor"):
                client_display.setup()
                maitre_oeuvre_display.setup()
                for i in range(4):
                    fournisseur_display.setup(i)
                for i in range(2):
                    transporteur_display.setup(i)

            # Connecte le client et le maitre d'oeuvre
            dpg.add_node_link("cl_node1", "mo_node1", parent="editor")
            dpg.add_node_link("cl_node2", "mo_node2", parent="editor")

            # TODO : update pour que le maitre d'oeuvre aient 2 nodes en plus (2 connectés au fournisseurs, 2 au transporteurs
            # Connecte le maitre d'oeuvre et les fournisseurs
            for i in range(4):
                dpg.add_node_link("mo_node3", "fo_node1_" + str(i), parent="editor")
                dpg.add_node_link("mo_node4", "fo_node2_" + str(i), parent="editor")

            # Connecte le maitre d'oeuvre et les transporteurs
            for i in range(2):
                dpg.add_node_link("mo_node3", "tr_node1_" + str(i), parent="editor")
                dpg.add_node_link("mo_node4", "tr_node2_" + str(i), parent="editor")

        dpg.set_primary_window("maquette2", True)


def on_start():
    client_display.update("cl_line1", "AHHHHHHHHHHH")
    client_display.update("cl_line2", "AHHHHHHHHHHH")
    client_display.update("cl_line3", "AHHHHHHHHHHH")
    maitre_oeuvre_display.update("mo_line1", "???")


def init_display():
    dpg.create_context()
    with dpg.window(label="Application"):
        dpg.add_button(label="Maquette Fabricant", callback=on_load_maquette1)
        dpg.add_button(label="Maquette Fournisseur et Transporteur", callback=on_load_maquette2)
        dpg.add_button(label="Simulation", callback=on_start)

    dpg.create_viewport(title='Supply Chain Management', width=1280, height=720)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()


init_display()
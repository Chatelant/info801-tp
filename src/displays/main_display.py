from src.displays.client_display import ClientDisplay
from src.displays.maitre_oeuvre_display import MODisplay
from src.displays.fabricant_display import FabDisplay

import dearpygui.dearpygui as dpg

from src.config import NB_FABRICANT

from multiprocessing import Process, Queue

from src.entities.client import Client
from src.entities.maitre_oeuvre import maitre_oeuvre


class Display:
    def __init__(self):
        self.cl_display = ClientDisplay()
        self.mo_display = MODisplay()
        self.fab_display = [FabDisplay(), FabDisplay(), FabDisplay()]
        self.on_init()

    def on_load_maquette(self):
        if not dpg.get_item_alias("maquette"):
            with dpg.window(label="Maquette", tag="maquette"):
                with dpg.node_editor(tag="editor"):
                    self.cl_display.setup()
                    self.mo_display.setup()
                    for i in range(NB_FABRICANT):
                        self.fab_display[i].setup(i)

                # Connecte le client et le maitre d'oeuvre
                dpg.add_node_link("cl_node1", "mo_node1", parent="editor")
                dpg.add_node_link("cl_node2", "mo_node2", parent="editor")

                # Connecte le maitre d'oeuvre et les fabricants
                for i in range(NB_FABRICANT):
                    dpg.add_node_link("mo_node3", "fa_node1_" + str(i), parent="editor")
                    dpg.add_node_link("mo_node4", "fa_node2_" + str(i), parent="editor")

            dpg.set_primary_window("maquette", True)

    def on_start(self):
        client_MO_Q = Queue()
        debug = Queue()

        client = Client()

        CL = Process(target=client.client, args=(client_MO_Q, debug,))
        MO = Process(target=maitre_oeuvre, args=(client_MO_Q, debug,))

        CL.start()
        MO.start()

        while not client.produit_fini:
            message = debug.get()
            if message[0] == "CL":
                self.cl_display.update(message[1], message[2])
            elif message[0] == "MO":
                self.mo_display.update(message[1], message[2])
            elif message[0] == "FAB":
                self.fab_display[message[1]].update(message[2], message[3])

        print("FIN")

    def on_init(self):
        dpg.create_context()
        with dpg.window(label="Application", width=150):
            # dpg.add_button(label="Maquette Fabricant", callback=on_load_maquette)
            dpg.add_button(label="Simulation", callback=self.on_start)

        self.on_load_maquette()

        dpg.create_viewport(title='Supply Chain Management', width=1280, height=720)
        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()

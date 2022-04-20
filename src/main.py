from time import sleep, perf_counter, time
from multiprocessing import Process, Lock, Pipe, Queue

from src.entities import objects

from src.displays.main_display import Display
from src.entities.client import Client
from src.entities.maitre_oeuvre import maitre_oeuvre


# TODO : trier les objets de entities/objects
# TODO : rédiger les entities (class + methodes)
# TODO : rédiger les displays (1 affichage tkinter / page)
# TODO : rédiger les controllers (passerelles ?)


# def task():
#     print('Starting a task...')
#     sleep(1)
#     print('done')



    # Synchronisations de deux process
    # lockMaitre.aquire()
    # try:
    #     print("Envoie cdc au maitre")
    # finally:
    #     lockMaitre.release()

if __name__ == '__main__':

    display = Display()

    client_MO_Q = Queue()
    debug = Queue()

    client = Client()

    CL = Process(target=client, args=(client_MO_Q, debug, display))
    MO = Process(target=maitre_oeuvre, args=(client_MO_Q, debug,))

    CL.start()
    MO.start()

    # lance l'affichage
    # Display(3)

    while True:
        print(debug.get())

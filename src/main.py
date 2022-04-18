from time import sleep, perf_counter, time
from multiprocessing import Process, Lock, Pipe, Queue

from src.entities import objects

from src.entities.client import client
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

    client_MO_Q = Queue()
    debug = Queue()

    client = Process(target=client, args=(client_MO_Q, debug,))
    MO = Process(target=maitre_oeuvre, args=(client_MO_Q, debug,))

    MO.start()
    client.start()

    while True:
        print(debug.get())

    client(client_MO_Q, debug).join()
    MO(client_MO_Q, debug).join()


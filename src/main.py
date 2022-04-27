from multiprocessing import Process, Queue

from src.displays.main_display import Display
from src.entities.client import Client
from src.entities.maitre_oeuvre import maitre_oeuvre

if __name__ == '__main__':

    display = Display()

    # client_MO_Q = Queue()
    # debug = Queue()
    #
    # client = Client()
    #
    # CL = Process(target=client, args=(client_MO_Q, debug, display))
    # MO = Process(target=maitre_oeuvre, args=(client_MO_Q, debug,))
    #
    # CL.start()
    # MO.start()
    #
    # while True:
    #     print(debug.get())

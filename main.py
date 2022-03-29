from time import sleep, perf_counter, time
from multiprocessing import Process, Lock, Pipe


class CahierDesCharges:
    def __init__(self, requirements, cost, time, quantity):
        self.requirements = requirements
        self.cost = cost
        self.time = time
        self.quantity = quantity


def task():
    print('Starting a task...')
    sleep(1)
    print('done')


def client(conn):
    # Création du cahier des charges
    print("Client : Elaboration du cahier des charges")
    cdc = CahierDesCharges(["Du pain", "Des sandwich"], 10000, 5, 20)
    print("Envoie sur le pipe")
    conn.send(cdc)
    conn.close()

    # Synchronisations de deux process
    # lockMaitre.aquire()
    # try:
    #     print("Envoie cdc au maitre")
    # finally:
    #     lockMaitre.release()


def maitreOeuvre(l_Client):
    print("Maitre d'Oeuvre : ")


if __name__ == '__main__':
    # Locks

    # Pipes
    client_conn, maitre_conn = Pipe()

    # Threads
    p = Process(target=client, args=(client_conn,))
    p.start()

    print(maitre_conn.recv().requirements)

    p.join()

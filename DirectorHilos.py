import threading
import time

class DirectorHilos:
    def __init__(self):
        self.hilos = []

    def añadirHilo(self, hilo):
        self.hilos.append(hilo)

    def start(self):
        for hilo in self.hilos:
            hilo.start()

    def join(self):
        for hilo in self.hilos:
            hilo.join()

    def stop(self):
        for hilo in self.hilos:
            hilo.stop() 
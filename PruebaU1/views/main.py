import sys
import os
import psutil
sys.path.append('../')
from time import time

from controls.clienteDaoControl import ClienteDaoControl

clienteDC = ClienteDaoControl()
try:
    Inicio = time()

    clienteDC._cliente._nombre = "Christian"
    clienteDC._cliente._apellido = "Cabrera"
    clienteDC._cliente._edad = 18
    clienteDC._cliente._email = "juan@unl.edu.ec"
    clienteDC.save

    #Se calcula el tiempo de ejecución del programa
    FIN = time()
    Total = FIN - Inicio
    print(f"El tiempo de ejecución del programa es: {Total} segundos")

    # Calcula la memoria utilizada
    process = psutil.Process(os.getpid())
    memory_usage = process.memory_info().rss / 1024 ** 2
    print(f"La memoria utilizada por el programa es: {memory_usage} MB")


except Exception as error:
    print(error.args)
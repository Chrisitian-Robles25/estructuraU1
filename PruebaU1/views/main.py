import sys
import os
import psutil
sys.path.append('../')
from time import time

from controls.clienteDaoControl import ClienteDaoControl
from controls.TDA.queuqe.queque import Queque
from controls.DAO.quequeDaoAdapter import QuequeDaoAdapter

clienteDC = ClienteDaoControl()
try:

    clienteDC._cliente._nombre = "Christian"
    clienteDC._cliente._apellido = "Cabrera"
    clienteDC._cliente._edad = 18
    clienteDC._cliente._email = "juan@unl.edu.ec"
    clienteDC.save
   
    clienteDC._cliente._nombre = "Juan"
    clienteDC._cliente._apellido = "Perez"
    clienteDC._cliente._edad = 20
    clienteDC._cliente._email = "perez@unl.edu.ec"
    clienteDC.save
    
except Exception as error:
    print(error.args)


     #Inicio = time()

     #Se calcula el tiempo de ejecución del programa
    """ FIN = time()
    Total = FIN - Inicio
    print(f"El tiempo de ejecución del programa es: {Total} segundos") """

     # Calcula la memoria utilizada
    """ process = psutil.Process(os.getpid())
    memory_usage = process.memory_info().rss / 1024 ** 2
    print(f"La memoria utilizada por el programa es: {memory_usage} MB")
 """
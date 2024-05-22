from typing import TypeVar, Generic, Type
from controls.TDA.queuqe.queque import Queque

import json
import os

T = TypeVar("T")
class QuequeDaoAdapter(Generic[T]):
    atype: T
    def __init__(self, atype: T): 
        self.atype = atype
        self.lista = Queque(5)
        self.file = atype.__name__.lower() + ".json"
        self.URL = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + "/data/"
    
    def _list(self) -> T:
        self.lista.print
        if os.path.isfile(self.URL + self.file):
            f = open(self.URL + self.file, "r")
            datos = json.load(f)
            self.lista.clear
            for data in datos:
                a = self.atype.deserializar(data)
                self.lista.queque(a)
            f.close()
        return self.lista

    def _transform_(self):
        aux = "["
        for i in range(0, self.lista._queque._lenght):
            if i < self.lista._queque._lenght - 1:
                aux += str(json.dumps(self.lista._queque.get(i).serializar)) + ","
            else:
                aux += str(json.dumps(self.lista._queque.get(i).serializar)) 
        aux += "]"
        return aux
    
    @property
    def to_dict(self):
        aux = []
        self._list()
        for i in range(0, self.lista._queque._lenght):
            aux.append(self.lista._queque.get(i)._id)
        return aux

    def _save(self, data: T) -> T:
        self._list()
        self.lista.queque(data)
        f = open(self.URL + self.file, "w")
        print("Nombre del archivo: "+self.file)
        f.write(self._transform_())
        f.close()

    def _merge(self, data: T, pos) -> T:
        self._list()
        self.lista._queque.edit(data, pos)
        f = open(self.URL + self.file, "w")
        print("Nombre del archivo: "+self.file)
        f.write(self._transform_())
        f.close()
    
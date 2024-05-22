from typing import TypeVar, Generic, Type
from controls.TDA.array.arrayList import ArrayList
import json
import os

T = TypeVar("T")

class ArrayDaoAdapter(Generic[T]):
    atype: Type[T]
    
    def __init__(self, atype: Type[T]): 
        self.atype = atype
        self.lista = ArrayList()  # Usamos ArrayList en lugar de LinkedList
        self.file = atype.__name__.lower() + ".json"
        self.URL = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "/data/") #antes "data"

    def _list(self) -> ArrayList:  # Modificamos el tipo de retorno a ArrayList
        if os.path.isfile(os.path.join(self.URL, self.file)):  # Utilizamos os.path.join para manejar rutas de archivos de manera más segura
            with open(os.path.join(self.URL, self.file), "r") as f:
                datos = json.load(f)
                self.lista = ArrayList()  # Reiniciamos la lista
                for data in datos:
                    a = self.atype.deserializar(data)
                    self.lista.__addLast__(a)
        return self.lista

    def _transform_(self) -> str:
        aux = "["
        for i in range(0, len(self.lista.data)):
            if i < len(self.lista.data) - 1:
                aux += str(json.dumps(self.lista.data[i].serializar)) + ","
            else:
                aux += str(json.dumps(self.lista.data[i].serializar))
        aux += "]"
        return aux

    def to_dict(self) -> list:
        self._list()
        aux = []
        for i in range(0, len(self.lista.data)):
            aux.append(self.lista.data[i].serializar)
        return aux

    def _save(self, data: T) -> None:
        self._list()
        self.lista.__addLast__(data)
        with open(os.path.join(self.URL, self.file), "w") as a:
            a.write(self._transform_())
            a.close()

    def _merge(self, data: T, pos: int) -> None:
        self._list()
        self.lista.data[pos] = data
        with open(os.path.join(self.URL, self.file), "w") as a:
            a.write(self._transform_())
            a.close()

    def _delete(self, pos: int) -> None:
        self._list()
        self.lista.data.pop(pos)
        with open(os.path.join(self.URL, self.file), "w") as a:
            a.write(self._transform_())
            a.close()

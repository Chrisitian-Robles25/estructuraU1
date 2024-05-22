
from controls.exception.arrayPositionException import ArrayPositionException
from controls.exception.linkedEmpty import LinkedEmpty
from controls.TDA.linked.linkedList import LinkedList

class StackOperation:
    def __init__(self, tope):
        self.__class = LinkedList()
        self.__tope = tope

    @property
    def _class(self):
        return self.__class

    @_class.setter
    def _class(self, value):
        self.__class = value


    @property
    def verifyTop(self):
        return self.__class._length < self.__tope
    
    
    def push(self, data):
        if self.verifyTop:
            self._class.add(data,0)
        else:
            raise LinkedEmpty("Stack is Full")
        
    @property
    def pop(self):
        if self.__class.isEmpty:
            raise LinkedEmpty("List is Empty")
        else:
            self._class.detele(0)
            
    @property
    def _clear(self):
        self._class.clear

from controls.TDA.linked.linkedList import LinkedList 
from controls.exception.linkedEmpty import LinkedEmpty

class QuequeOperation(LinkedList):
    def __init__(self, top):
        super().__init__()
        self.__top = top

    @property
    def get_top(self):
        return self.__top

    def set_top(self, value):
        self.__top = value

    @property
    def verifyTop(self):
        return self._lenght < self.__top

    def queque(self, data):
        if self.verifyTop:
            self.add(data, self._lenght)
        else:
            raise LinkedEmpty("Stack is full")

    @property
    def dequeque(self):
        if self.isEmpty:
            raise LinkedEmpty("Stack empty")
        else:
            return self.delete(0)
        
    @property
    def _clear(self):
        return self.clear
        
  
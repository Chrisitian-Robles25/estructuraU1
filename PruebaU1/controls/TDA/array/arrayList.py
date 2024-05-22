import sys
from controls.exception.arrayPositionException import ArrayPositionException
from controls.exception.linkedEmpty import LinkedEmpty

class ArrayList:
    def __init__(self):
        self.data = [] 

    def __addFirst__(self, element):
        self.data.insert(0, element)

    def __addLast__(self, element):
        self.data.append(element)

    def add(self, index, element):
        if index < 0 or index > len(self.data):
            raise ArrayPositionException("Index out of bounds")
        self.data.insert(index, element)

    def edit(self, index, element):
        if index < 0 or index >= len(self.data):
            raise ArrayPositionException("Index out of bounds")
        self.data[index] = element

    def delete(self, index):
        if len(self.data) == 0:
            raise LinkedEmpty("Array is empty")
        if index < 0 or index >= len(self.data):
            raise ArrayPositionException("Index out of bounds")
        self.data.pop(index)

    def get(self, element):
        try:
            return self.data.index(element)
        except ValueError:
            return -1
    
    def __str__(self):
        return str(self.data)

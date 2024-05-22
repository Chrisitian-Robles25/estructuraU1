from controls.DAO.daoAdapter import DaoAdapter
from controls.DAO.arrayDaoAdapter import ArrayDaoAdapter
from models.cliente import Cliente

class ClienteDaoControl(DaoAdapter):
    def __init__(self):
        super().__init__(Cliente)
        self.__cliente = None

    @property
    def _cliente(self):
        if self.__cliente is None:
            self.__cliente = Cliente()
        return self.__cliente
    
    @_cliente.setter
    def _cliente(self, value):
        self.__cliente = value
    
    @property
    def _lista(self):
        return self._list()
    
    """ @property
    def save(self):
        self._cliente.id = len(self._lista.data) + 1 
        self._save(self._cliente) """

    @property
    def save(self):
        self._cliente._id = self._lista._lenght + 1  # Ajustamos el id automáticamente
        self._save(self._cliente)

    def merge(self, pos):
        self._merge(self._cliente, pos)
    
    def delete(self, pos):
        self._delete(pos)
class Cliente:
    def __init__(self):
        self.__id = 0
        self.__nombre = ''
        self.__apellido = ''
        self.__edad = 0
        self.__email = ''

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value


    @property
    def _nombre(self):
        return self.__nombre

    @_nombre.setter
    def _nombre(self, value):
        self.__nombre = value

    @property
    def _apellido(self):
        return self.__apellido

    @_apellido.setter
    def _apellido(self, value):
        self.__apellido = value

    @property
    def _edad(self):
        return self.__edad

    @_edad.setter
    def _edad(self, value):
        self.__edad = value

    @property
    def _email(self):
        return self.__email

    @_email.setter
    def _email(self, value):
        self.__email = value

    @property
    def serializar(self):
        return {
            'id': self.__id,
            'nombre': self._nombre,
            'apellido': self._apellido,
            'edad': self._edad,
            'email': self._email
        }
    
    def deserializar(data):
        cliente = Cliente()
        cliente._id = data['id']
        cliente._nombre = data['nombre']
        cliente._apellido = data['apellido']
        cliente._edad = data['edad']
        cliente._email = data['email']
        return cliente
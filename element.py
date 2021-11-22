class Element(object):
    """
    Elemento da linked list
    """

    def __init__(self, data: dict, key: str = None):
        self.key: str = key
        self.data: dict = data
        self.next: Element = None

    def __str__(self):
        """
        representação em str da instância do objeto
        :return: dict
        """
        return f"Key: {self.key}, Values: {self.data}"
    
    def __getitem__(self, index: int):
        """
        Facilita o acesso aos dados da classe 
        """
        if index == 0:
            return self.key

        if index == 2:        
            return self.data
        
        if index == 3:
            return self.next
    
    def __setitem__(self, index: int, value):
        """
        Facilita o override dos dados da classe 
        """
        if index == 0:
            self.key = value

        if index == 2:        
            self.data = value
        
        if index == 3:
            self.next = value

    def __repr__(self):
        """
        dado da instância da classe
        :return: dict
        """
        return self.__str__()

    def __next__(self):
        yield self.next

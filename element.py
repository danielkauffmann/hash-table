class Element(object):
    """
    Elemento da Hash Table
    """

    def __init__(self, data: dict):
        self.data: dict = data

    def __str__(self):
        """
        representação em str da instância do objeto
        :return: dict
        """
        values = [f" {k}: {v}, \n" for k, v in self.data.items()]

        return '{\n' \
               f"{''.join(values)}" \
               '}\n'

    def __repr__(self):
        """
        dado da instância da classe
        :return: dict
        """
        return self.__str__()

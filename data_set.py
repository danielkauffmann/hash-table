from pandas import DataFrame, read_csv, Index
from numpy import ndarray


class DataSet:
    def __init__(self):
        self.data: DataFrame = read_csv('data.csv')

    def columns(self) -> Index:
        """
        retorna uma lista com as colunas do DataFrame
        :return: DataFrame.Index
        """
        return self.data.columns

    def values(self) -> ndarray:
        """
        retorna um numpy array com os dados do DataFrame
        :return: ndarray
        """
        return self.data.values

    def __len__(self) -> int:
        """
        retorna a quantidade de elementos
        :return: int
        """
        return len(self.data)

    def __str__(self) -> str:
        """
        representação em str da instância da classe
        :return: str
        """
        return 'DataSet from "data.csv" file'

    def __repr__(self) -> str:
        """
        representação da instância da classe
        :return: str
        """
        return 'DataSet from "data.csv" file'


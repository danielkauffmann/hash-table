from hash_table import HashTable
from data_set import DataSet
from element import Element


def load_data(table: HashTable, data: DataSet) -> None:
    """
    carrega os dados na Hash Table
    :param table: HashTable
    :param data: DataSet
    :return None
    """
    for row in data.values():
        table[row[0]] = Element({k: v for k, v in zip(data.columns()[1:], row[1:])})


def main():
    # Inicializa a Hash Table
    hash_table = HashTable()

    # Inicializa os dados
    data_set = DataSet()

    # Carrega os dados na Hash Table
    load_data(hash_table, data_set)

    # Mostra o relatório da Hash Table
    hash_table.report()


if __name__ == '__main__':
    main()

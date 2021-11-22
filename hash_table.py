from __future__ import annotations

from element import Element
from linked_list import LinkedList


class HashTable(object):
    """
    Implementação de uma Hash Table em Python puro
    """

    def __init__(self, size: int = 1000):
        """
        utiliza uma lista para armazenar, cada elemento é uma lista,
        onde é utilizado para resolver conflitos de hash
        :param size: int
        :return None
        """
        self.storage = [LinkedList() for _ in range(size)]
        self.size: int = size
        self.length: int = 0

        self.collisions: int = 0

    def hash(self, key: str) -> int:
        """
        dado uma chave e indice, verifica possíveis colisões e
        retorna o índice correto
        :param key: str
        :return int
        """
        return hash(key) % self.size

    def __setitem__(self, key: str, value: Element) -> None:
        """
        adicionar chave e valor, no caso de conflitos, adiciona a
        sub lista
        :param key: str
        :param value: Element
        :return None
        """
        storage_idx = self.hash(key)

        for ele in self.storage[storage_idx]:
            # Se já existir, irá substituir
            if key == ele[0]:
                ele[1] = value
                break

            # Caso o contrário, é uma colisão
            self.collisions += 1

        else:
            self.storage[storage_idx].add(value)
            self.length += 1

    def __getitem__(self, key: str) -> dict:
        """
        busca pela chave, no caso de não encontrado, retorna um erro
        :param key: str
        :raise: KeyError
        :return: Element
        """
        storage_idx = self.hash(key)

        for i in range(len(self.storage[storage_idx])):
            if self.storage[storage_idx][i].key == key:
                return self.storage[storage_idx][i].data

        raise KeyError(f'Key {key} doesn\'t exist')

    def __delitem__(self, key: str) -> None:
        """
        remove chave e valor na hash table do objeto
        :raise KeyError
        :param key: str
        :return: None
        """
        storage_idx = self.hash(key)

        for sub_lst in self.storage[storage_idx]:
            if key == sub_lst[0]:
                self.storage[storage_idx].remove(sub_lst)
                self.length -= 1

                return

        raise KeyError(f'Key {key} dont exist')

    def __contains__(self, key: str) -> bool:
        """
        verifica se a chave existe na hash table do objeto
        :param key: str
        :return: boolean
        """
        storage_idx = self.hash(key)

        for item in self.storage[storage_idx]:
            if item[0] == key:
                return True

        return False

    def __len__(self) -> int:
        """
        :return: int
        """
        return self.length

    def __iterate_kv(self) -> iter:
        """
        retorna um iterator
        :return: iter
        """
        for sub_lst in self.storage:
            if not sub_lst:
                continue
            for item in sub_lst:
                yield item

    def __iter__(self) -> list:
        """
        retorna um iterator
        :return: list
        """
        for key_var in self.__iterate_kv():
            yield key_var[0]

    def keys(self) -> list:
        """
        retorna todas as chaves em uma lista
        :return: list
        """
        return self.__iter__()

    def values(self) -> list:
        """
        retorna todos os valores em uma lista
        :return: list
        """
        for key_var in self.__iterate_kv():
            yield key_var[1]

    def items(self) -> iter:
        """
        retorna todas as chaves:valores em uma lista
        :return: iter
        """
        return self.__iterate_kv()

    def get(self, key: str) -> dict | None:
        """
        retorna o valor dado uma chave
        :param key: str
        :return: Element | None
        """
        try:
            return self.__getitem__(key)
        except KeyError:
            return None

    def __str__(self) -> str:
        """
        representação em str da Hash Table
        :return: string
        """
        res = "[\t"

        for ele in self.storage:
            for key_value in ele:
                res += f"{key_value} |\t"

        return res + " ]"

    def __repr__(self) -> str:
        """
        representação em str da instância da classe
        :return: string
        """
        return self.__str__()

    def report(self) -> None:
        """"
        Calcula e mostra o relatório da Hash Table
        :return None
        """
        max_collisions = 0
        max_collisions_hash = 0

        for ele in self.storage:
            if len(ele) > max_collisions:
                max_collisions = len(ele)
                max_collisions_hash = self.storage.index(ele)

        print(f'Relatório da Hash Table\n'
              f'Colisões: {self.collisions}\n'
              f'Colisões por qtd de dados: {(self.collisions / len(self)) * 100}%\n'
              f'Espaço ocioso: {(self.size - len(self)) / 100}%\n'
              f'Qtd de dados: {len(self)}\n'
              f'Espaço livre: {self.size - len(self)}\n'
              f'Maior hash com colisões: Hash({max_collisions_hash}), Colisões({max_collisions})\n')

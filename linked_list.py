from collections import Sequence
from element import Element


class LinkedList(Sequence):
    """
    Implementação de uma LinkedList em Python
    """

    def __init__(self):
        self.head = None
        self.length = 0

    def __len__(self):
        return self.length

    def __repr__(self) -> str:
        """
        Representação da linked list
        :return: str
        """
        node = self.head
        nodes = []

        while node is not None:
            nodes.append(node.key)
            node = node.next

        nodes.append("None")

        return " -> ".join(nodes)

    def __iter__(self) -> list:
        """
        retorna um iterator
        :return: list
        """
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __getitem__(self, index: int) -> Element:
        """
        Acessa um Element na linked list com o index desejado 
        """
        if index > self.length:
            raise IndexError(f'Index {index} out of range')

        node = self.head
        counter = 0

        if index == -1:
            for iter_node in self:
                node = iter_node
            return node

        while counter != index:
            node = node.next
            counter += 1

        return node

    def keys(self) -> list[str]:
        """
        Retorna as chaves que estão na linked list
        """
        return [item.key for item in self]

    def add(self, value: Element) -> None:
        """
        Adiciona um Element no inicio da lista
        """
        value.next = self.head
        self.head = value
        self.length += 1

    def remove(self, key: str) -> None:
        """
        Remove o elemento com a key passada 
        """
        if self.head is None:
            raise ValueError("Linked list is empty")

        if self.head.key == key:
            self.head = self.head.next
            self.length -= 1
            return

        previous_node = self.head
        for node in self:
            if node.key == key:
                previous_node.next = node.next
                self.length -= 1
                return
            previous_node = node

        raise ValueError("Not Found")

    def __contains__(self, key: str) -> bool:
        """
        Verifica se a linked list possui um Element com a key desejada 
        """
        return key in self.keys

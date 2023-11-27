from abc import (
    ABC,
    abstractmethod,
)
from typing import Protocol, TypeVar, Any
from contextlib import suppress


class ObserverProtocol(Protocol):
    def update(self, subject: "Subject"):
        pass


Observer = TypeVar("Observer", bound=ObserverProtocol)


class Subject:
    def __init__(self) -> None:
        self._data: int | None = None
        self._observers: list[Observer] = []

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        with suppress(ValueError):
            self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)

    @property
    def data(self) -> int:
        return self.data

    @data.setter
    @abstractmethod
    def data(self, value: Any) -> None:
        pass


class Data(Subject):
    @property
    def data(self) -> int:
        return self._data

    @data.setter
    def data(self, value: int) -> None:
        self._data = value
        self.notify()


class DecRepresentation:
    def update(self, subject: "Subject") -> None:
        print(f'The decimal representation is {subject.data:}')


class HexRepresentation:
    def update(self, subject: "Subject") -> None:
        print(f'The hexadecimal representation is {hex(subject.data)}')


class OctRepresentation:
    def update(self, subject: "Subject") -> None:
        print(f'The octal representation is {oct(subject.data)}')


class BinRepresentation:
    def update(self, subject: "Subject") -> None:
        print(f'The binary representation is {bin(subject.data)}')


if __name__ == '__main__':
    dec_representation = DecRepresentation()
    hex_representation = HexRepresentation()
    oct_representation = OctRepresentation()
    bin_representation = BinRepresentation()
    data1 = Data()
    data1.attach(dec_representation)
    data1.attach(hex_representation)
    data1.attach(oct_representation)
    data2 = Data()
    data2.attach(dec_representation)
    data2.attach(hex_representation)
    data2.attach(bin_representation)
    data1.data = 100
    print('================================')
    data2.data = 1024
    print('================================')
    data1.detach(dec_representation)
    data2.detach(dec_representation)
    data1.data = 1234
    print('================================')
    data2.data = 512
    print('================================')





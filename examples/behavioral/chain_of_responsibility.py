import json
from abc import (
    ABC,
    abstractmethod,
)
from typing import (
    Any,
    Optional,
)
from uuid import uuid4


class Handler(ABC):
    def __init__(self, successor: Optional["Handler"] = None):
        self.successor = successor

    @abstractmethod
    def save_data(self, data: Any) -> bool:
        pass

    def handler(self, data: Any) -> bool:
        if self.save_data(data):
            return True
        return self.successor.handler(data)


class TxtFileHandler(Handler):
    FILENAME = 'data.txt'

    def save_data(self, data: Any) -> bool:
        try:
            with open(TxtFileHandler.FILENAME, 'a') as file:
                file.write(str(data))
                print(f'the data has been written to {TxtFileHandler.FILENAME}')
                return True
        except OSError:
            return False


class JsonFileHandler(Handler):
    FILENAME = f'data-{uuid4()}.json'

    def save_data(self, data: Any) -> bool:
        filename = f'data-{uuid4()}.json'
        try:
            with open(filename, 'w') as file:
                json.dump(data, file)
                print(f'the data has been written to {filename}')
                return True
        except (OSError, TypeError):
            return False



if __name__ == '__main__':
    data_handler = JsonFileHandler(
        successor=TxtFileHandler()
    )
    print(f'Handling correct JSON data:')
    data_handler.handler([1, 2, 3])
    print(f'Handling incorrect JSON data:')
    data_handler.handler({'field': Handler})



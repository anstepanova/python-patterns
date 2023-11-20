from abc import (
    ABC,
    abstractmethod,
)


class Image:
    @abstractmethod
    def display(self) -> None:
        raise NotImplementedError()


class RealImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self._width = None
        self._height = None

    def load_image(self) -> None:
        print(f'The real {self.filename} image was loaded')
        self._width = 15
        self._height = 10

    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height

    def display(self) -> None:
        print(f'The real {self.filename} was displayed.')


class ProxyImage(Image):
    images = {
        'photo-1': (10, 15),
        'photo-2': (5, 10),
    }

    def __init__(self, filename):
        self.filename = filename
        self.real_image = None

    def load_image(self) -> None:
        if self.real_image is None:
            self.real_image = RealImage(filename=self.filename)
        self.real_image.load_image()

    @property
    def width(self) -> int | None:
        return self.images.get(self.filename, (None, None))[0]

    @property
    def height(self) -> int | None:
        return self.images.get(self.filename, (None, None))[1]


if __name__ == '__main__':
    proxy_image = ProxyImage(filename='photo-1')
    print(proxy_image.width)
    print(proxy_image.height)
    proxy_image.load_image()


from abc import (
    ABC,
    abstractmethod,
)


class Content(ABC):
    def __init__(self, content):
        self._content = content

    @abstractmethod
    def render(self):
        pass


class TextTag(Content):

    def render(self):
        return self._content


class TextDecorator(Content, ABC):
    pass


class BoldDecorator(TextDecorator):
    def render(self):
        return f'<b>{self._content.render()}<\\b>'


class ItalicDecorator(TextDecorator):
    def render(self):
        return f'<i>{self._content.render()}<\\i>'


class QuoteDecorator(TextDecorator):
    def render(self):
        return f'<q>{self._content.render()}<\\q>'


if __name__ == '__main__':
    text_tag = TextTag('Hello world!')
    print(text_tag.render())
    print(BoldDecorator(ItalicDecorator(QuoteDecorator(text_tag))).render())






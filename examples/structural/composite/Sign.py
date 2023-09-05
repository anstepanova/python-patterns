from abc import abstractmethod


class Sign:
    @abstractmethod
    def draw(self):
        raise NotImplementedError


class Line(Sign):
    line_char = '*'

    def __init__(self, length: int):
        self.length = length

    def draw(self):
        print(''.join([self.line_char] * self.length))


class Content(Sign):
    def __init__(self, text: str):
        self.text = text

    def draw(self):
        print(self.text)


class CompositeSign(Sign):
    def __init__(self):
        self.child_elements = []

    def add_element(self, element: Sign):
        self.child_elements.append(element)

    def draw(self):
        for child_element in self.child_elements:
            child_element.draw()


if __name__ == '__main__':

    simple_upper_line = Line(length=4)
    simple_text = Content(text='test')
    simple_bottom_line = Line(length=4)
    composite_sign = CompositeSign()
    composite_sign.add_element(simple_upper_line)
    composite_sign.add_element(simple_text)
    composite_sign.add_element(simple_bottom_line)
    composite_sign.draw()

    print('\n')

    external_upper_line = Line(length=15)
    external_text = Content(text='External text')
    inner_upper_line = Line(length=10)
    inner_text = Content(text='Inner text')
    inner_bottom_line = Line(length=10)
    external_bottom_line = Line(length=15)

    external_composite_sign = CompositeSign()
    external_composite_sign.add_element(external_upper_line)
    external_composite_sign.add_element(external_text)
    inner_composite_sign = CompositeSign()
    inner_composite_sign.add_element(inner_upper_line)
    inner_composite_sign.add_element(inner_text)
    inner_composite_sign.add_element(inner_bottom_line)
    external_composite_sign.add_element(inner_composite_sign)
    external_composite_sign.add_element(external_bottom_line)

    external_composite_sign.draw()


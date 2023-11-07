# object adapter

import  xmltodict


class Shop1Purchase:
    def get_details(self):
        return """
        <response>
            <price>500</price>
            <name>pizza</name>
        </response>
        """


class TargetPurchase:
    def get_details(self) -> dict:
        return {'price': 100, 'name': 'coffe'}


class Adaptor(TargetPurchase):
    def __init__(self, adaptee):
        self.__adaptee = adaptee

    def get_details(self):
        xml_data = self.__adaptee.get_details()
        return xmltodict.parse(xml_data).get('response')


if __name__ == '__main__':
    adaptor = Adaptor(Shop1Purchase())
    print(adaptor.get_details())




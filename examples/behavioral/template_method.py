from abc import (
    ABC,
    abstractmethod,
)
from typing import Any


class User:
    def __init__(self, name: str, distance_from_warehouse: int):
        self.name = name
        self.distance_from_warehouse = distance_from_warehouse


class Order:
    def __init__(
            self,
            item_prices: list[int],
            user: User,
    ):
        self.item_prices = item_prices
        self.user = user
        self.total_item_price = None
        self.delivery_price = None


    @property
    def total_price(self):
        return self.delivery_price + self.total_item_price

    def _notify_user_about_order(self):
        print(f'Hi, {self.user.name}!\n'
              f'The total price of all items is {self.total_item_price}\n'
              f'Delivery price is {self.delivery_price}\n'
              f'The total price is {self.total_price}\n'
              f'Order type is {self.__class__}'
              )

    def _calculate_price_of_all_items(self):
        return sum(self.item_prices)

    def _calculate_cost_of_delivery(self):
        return self.user.distance_from_warehouse

    def make_order(self):
        self.delivery_price = self._calculate_price_of_all_items()
        self.total_item_price = self._calculate_cost_of_delivery()
        self._notify_user_about_order()


class BlackFridayOrder(Order):
    items_discount = 0.5
    delivery_price = 0

    def _calculate_price_of_all_items(self):
        return super()._calculate_price_of_all_items() * (1 - BlackFridayOrder.items_discount)

    def _calculate_cost_of_delivery(self):
        return BlackFridayOrder.delivery_price


class WinterOrder(Order):
    items_discount = 0.6
    delivery_discount = 0.9

    def _calculate_price_of_all_items(self):
        return super()._calculate_price_of_all_items() * (1 - WinterOrder.items_discount)

    def _calculate_cost_of_delivery(self):
        return super()._calculate_cost_of_delivery() * (1 - WinterOrder.delivery_discount)


if __name__ == '__main__':
    user1 = User(name='user-1', distance_from_warehouse=100)
    user2 = User(name='user-2', distance_from_warehouse=500)
    winter_order_for_user_1 = WinterOrder(user=user1, item_prices=[100, 200, 150])
    winter_order_for_user_1.make_order()
    print('=============================================')
    black_friday_for_user_1 = BlackFridayOrder(user=user1, item_prices=[100, 200, 150])
    black_friday_for_user_1.make_order()
    print('=============================================')
    winter_order_for_user_2 = WinterOrder(user=user2, item_prices=[100, 200, 150])
    winter_order_for_user_2.make_order()
    print('=============================================')
    black_friday_for_user_2 = BlackFridayOrder(user=user2, item_prices=[100, 200, 150])
    black_friday_for_user_2.make_order()
    print('=============================================')

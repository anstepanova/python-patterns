from abc import (
    ABC,
    abstractmethod,
)


class DiscountStrategy(ABC):

    @abstractmethod
    def apply_discount_and_get_price_with_discount(self, purchase_items: list[float]) -> float:
        pass


class ThreeForTwoDiscountStrategy(DiscountStrategy):
    def apply_discount_and_get_price_with_discount(self, purchase_items: list[float]) -> float:
        sorted_purchase_items = sorted(purchase_items)
        free_purchase_items_count = len(purchase_items) // 3
        return sum(purchase_items) - sum(sorted_purchase_items[:free_purchase_items_count])


class PercentDiscountStrategy(DiscountStrategy):
    def apply_discount_and_get_price_with_discount(self, purchase_items: list[float]) -> float:
        return round(sum(purchase_items) * 0.8, 2)


class Purchase:
    def __init__(self, discount_strategy: DiscountStrategy, purchase_items: list[float]):
        self.discount_strategy = discount_strategy
        self.purchase_items = purchase_items

    def get_price_with_discount(self):
        return self.discount_strategy.apply_discount_and_get_price_with_discount(self.purchase_items)


if __name__ == '__main__':
    purchase_items = [1, 2, 3, 4, 5, 6, 7]
    three_for_two_purchase = Purchase(discount_strategy=ThreeForTwoDiscountStrategy(), purchase_items=purchase_items)
    print(three_for_two_purchase.get_price_with_discount())

    percent_discount_purchase = Purchase(discount_strategy=PercentDiscountStrategy(), purchase_items=purchase_items)
    print(percent_discount_purchase.get_price_with_discount())




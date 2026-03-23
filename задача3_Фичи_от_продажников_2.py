print()
'''
Я сдаюсь на задаче фичи от продажников 2 :( Кому не трудно - 
киньте в меня решением для разбора, ну или может помогите 
понять что не так - 
'''
from dataclasses import dataclass, field
from typing import List


@dataclass(order=True)
class Product:
    name: str
    price: float = field(repr=False)


@dataclass
class Promo:
    code: str
    discount: int
    products: List[Product] = None  # Список товаров, на которые действует промокод

    def applies_to_product(self, product_name):
        return self.products is None or any(
            product.name == product_name for product in self.products
        )


ACTIVE_PROMO = [
    Promo('new', 20, [Product('Ручка', 10.0)]),  # Создаем объект товара 'Ручка'
    Promo('all_goods', 30),
]


@dataclass
class Cart:
    producted: List[Product] = field(default_factory=list)
    discount: int = None
    applied_promo: int = None

    def add_product(self, prod, quantity=1):
        for _ in range(quantity):
            self.producted.append(prod)

    def get_total(self):
        total_price = sum(product.price for product in self.producted)

        if self.discount:
            total_price *= 1 - self.discount / 100  # Применение скидки
        elif self.applied_promo is not None:
            if self.applied_promo == -1:  # Промокод для всей корзины
                total_price *= 1 - ACTIVE_PROMO[self.applied_promo].discount / 100
            else:  # Применение промокода к конкретному товару
                total_price -= (
                    self.producted[self.applied_promo].price
                    * ACTIVE_PROMO[self.applied_promo].discount
                    / 100
                )

        return total_price

    def apply_discount(self, value):
        if not isinstance(value, int) or value < 1 or value > 100:
            raise ValueError('Неправильное значение скидки')
        self.discount = value

    def apply_promo(self, code):
        global ACTIVE_PROMO
        for index, promo in enumerate(ACTIVE_PROMO):
            if promo.code == code:
                self.applied_promo = index
                print(f"Промокод '{code}' успешно применен")
                break
        else:
            print(f"Промокода '{code}' не существует")


from dataclasses import dataclass
from projects.project3.Drink import Drink

@dataclass
class OrderItem:
    drink: Drink
    customization: str = ''

    def get_display_name(self) -> str:
        base = f"{self.drink.name} ({self.drink.size})"
        return f"{base} - Custom: {self.customization}" if self.customization else base

    def price(self) -> float:
        return self.drink.price


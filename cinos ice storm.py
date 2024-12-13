from typing import List, Dict, Optional, Union

class Drink:
    """Class to represent a drink with a single base and multiple flavors."""

    _VALID_BASES = ['water', 'sbrite', 'pokeacola', 'Mr. Salt', 'hill fog', 'leaf wine']
    _VALID_FLAVORS = ['lemon', 'cherry', 'strawberry', 'mint', 'blueberry', 'lime']

    def __init__(self) -> None:
        """Initialize a drink with no base and no flavors."""
        self._base: Optional[str] = None
        self._flavors: set[str] = set()

    @classmethod
    def get_valid_bases(cls) -> List[str]:
        return cls._VALID_BASES

    @classmethod
    def get_valid_flavors(cls) -> List[str]:
        return cls._VALID_FLAVORS

    def get_base(self) -> Optional[str]:
        return self._base

    def get_flavors(self) -> List[str]:
        return sorted(self._flavors)  # Ensure consistent order

    def get_num_flavors(self) -> int:
        return len(self._flavors)

    def add_base(self, base: str) -> None:
        if self._base is not None:
            raise ValueError("A base has already been added.")
        if base not in self._VALID_BASES:
            raise ValueError(f"Invalid base: {base}. Valid options: {self._VALID_BASES}")
        self._base = base

    def add_flavor(self, flavor: str) -> None:
        if flavor not in self._VALID_FLAVORS:
            raise ValueError(f"Invalid flavor: {flavor}. Valid options: {self._VALID_FLAVORS}")
        if flavor in self._flavors:
            raise ValueError(f"Flavor '{flavor}' has already been added.")
        self._flavors.add(flavor)

    def set_flavors(self, flavors: List[str]) -> None:
        unique_flavors = set(flavors)
        if not unique_flavors.issubset(self._VALID_FLAVORS):
            invalid_flavors = unique_flavors - set(self._VALID_FLAVORS)
            raise ValueError(f"Invalid flavors: {invalid_flavors}. Valid options: {self._VALID_FLAVORS}")
        self._flavors = unique_flavors


class Food:
    """Class to represent a food item with optional toppings."""

    _VALID_FOOD_ITEMS: Dict[str, float] = {
        'Hotdog': 2.30,
        'Corndog': 2.00,
        'Ice Cream': 3.00,
        'Onion Rings': 1.75,
        'French Fries': 1.50,
        'Tater Tots': 1.70,
        'Nacho Chips': 1.90
    }
    _VALID_TOPPINGS: Dict[str, float] = {
        'Cherry': 0.00,
        'Whipped Cream': 0.00,
        'Caramel Sauce': 0.50,
        'Chocolate Sauce': 0.50,
        'Nacho Cheese': 0.30,
        'Chili': 0.60,
        'Bacon Bits': 0.30,
        'Ketchup': 0.00,
        'Mustard': 0.00
    }

    def __init__(self, food_item: str) -> None:
        if food_item not in self._VALID_FOOD_ITEMS:
            raise ValueError(f"Invalid food item: {food_item}. Valid options: {list(self._VALID_FOOD_ITEMS.keys())}")
        self._food_item: str = food_item
        self._base_price: float = self._VALID_FOOD_ITEMS[food_item]
        self._toppings: Dict[str, float] = {}

    @classmethod
    def get_valid_food_items(cls) -> Dict[str, float]:
        return cls._VALID_FOOD_ITEMS

    @classmethod
    def get_valid_toppings(cls) -> Dict[str, float]:
        return cls._VALID_TOPPINGS

    def get_food_type(self) -> str:
        return self._food_item

    def get_price(self) -> float:
        return self._base_price + sum(self._toppings.values())

    def add_topping(self, topping: str) -> None:
        if topping not in self._VALID_TOPPINGS:
            raise ValueError(f"Invalid topping: {topping}. Valid options: {list(self._VALID_TOPPINGS.keys())}")
        if topping in self._toppings:
            raise ValueError(f"Topping '{topping}' has already been added.")
        self._toppings[topping] = self._VALID_TOPPINGS[topping]

    def get_toppings(self) -> List[str]:
        return sorted(self._toppings.keys())

    def generate_receipt(self) -> str:
        lines = [f"{self._food_item}"]
        lines.append(f"- Base Price: ${self._base_price:.2f}")
        for topping, cost in sorted(self._toppings.items()):
            lines.append(f"- {topping}: ${cost:.2f}")
        lines.append(f"Total: ${self.get_price():.2f}")
        return "\n".join(lines)


class Order:
    """Class to manage a collection of food and drink items."""

    def __init__(self) -> None:
        self._items: List[Union[Drink, Food]] = []

    def get_items(self) -> List[Union[Drink, Food]]:
        return self._items

    def get_num_items(self) -> int:
        return len(self._items)

    def get_total(self) -> float:
        total = 0.0
        for item in self._items:
            if isinstance(item, Drink):
                total += 5.00  # Fixed price per drink
            elif isinstance(item, Food):
                total += item.get_price()
        return total

    def get_receipt(self) -> str:
        if not self._items:
            return "Order is empty. Add some items!"

        receipt_lines = ["--- Order Receipt ---"]
        for idx, item in enumerate(self._items, 1):
            if isinstance(item, Drink):
                receipt_lines.append(
                    f"{idx}. Drink - Base: {item.get_base() or 'None'}, Flavors: {', '.join(item.get_flavors()) or 'None'}"
                )
            elif isinstance(item, Food):
                receipt_lines.append(f"{idx}. {item.generate_receipt()}")
        receipt_lines.append(f"Total Items: {self.get_num_items()}")
        receipt_lines.append(f"Total Cost: ${self.get_total():.2f}")
        return "\n".join(receipt_lines)

    def add_item(self, item: Union[Drink, Food]) -> None:
        if not isinstance(item, (Drink, Food)):
            raise TypeError("Invalid item. Only Drink or Food objects are allowed.")
        self._items.append(item)

    def remove_item(self, index: int) -> None:
        if index < 0 or index >= len(self._items):
            raise IndexError("Invalid index. No item removed.")
        self._items.pop(index)


class IceStorm:
    """Class to represent the Ice Storm menu item with flavors and mix-ins/toppings."""

    _VALID_FLAVORS = {
        'Mint Chocolate Chip': 4.00,
        'Chocolate': 3.00,
        'Vanilla Bean': 3.00,
        'Banana': 3.50,
        'Butter Pecan': 3.50,
        'S\'more': 4.00,
    }
    _VALID_TOPPINGS = {
        'Cherry': 0.00,
        'Whipped Cream': 0.00,
        'Caramel Sauce': 0.50,
        'Chocolate Sauce': 0.50,
        'Storios': 1.00,
        'Dig Dogs': 1.00,
        'T&T\'s': 1.00,
        'Cookie Dough': 1.00,
        'Pecans': 0.50
    }

    def __init__(self, flavor: str) -> None:
        if flavor not in self._VALID_FLAVORS:
            raise ValueError(f"Invalid Ice Storm flavor: {flavor}. Valid options: {list(self._VALID_FLAVORS.keys())}")
        self._flavor: str = flavor
        self._base_price: float = self._VALID_FLAVORS[flavor]
        self._toppings: Dict[str, float] = {}

    @classmethod
    def get_flavors(cls) -> List[str]:
        """Return a list of valid Ice Storm flavors."""
        return list(cls._VALID_FLAVORS.keys())

    def get_flavor(self) -> str:
        """Return the current flavor of the Ice Storm."""
        return self._flavor

    def get_base(self) -> str:
        """Alias for get_flavor."""
        return self.get_flavor()

    def get_toppings(self) -> List[str]:
        """Return a sorted list of added toppings."""
        return sorted(self._toppings.keys())

    def add_topping(self, topping: str) -> None:
        """Add a topping to the Ice Storm."""
        if topping not in self._VALID_TOPPINGS:
            raise ValueError(f"Invalid topping: {topping}. Valid options: {list(self._VALID_TOPPINGS.keys())}")
        if topping in self._toppings:
            raise ValueError(f"Topping '{topping}' has already been added.")
        self._toppings[topping] = self._VALID_TOPPINGS[topping]

    def get_total(self) -> float:
        """Calculate and return the total cost of the Ice Storm."""
        return self._base_price + sum(self._toppings.values())

    def get_num_flavors(self) -> int:
        """Return the number of flavors in the Ice Storm (always 1)."""
        return 1

    def __str__(self) -> str:
        """Return a string representation of the Ice Storm."""
        lines = [f"Ice Storm - {self._flavor}"]
        lines.append(f"- Base Price: ${self._base_price:.2f}")
        for topping, cost in sorted(self._toppings.items()):
            lines.append(f"- {topping}: ${cost:.2f}")
        lines.append(f"Total: ${self.get_total():.2f}")
        return "\n".join(lines)


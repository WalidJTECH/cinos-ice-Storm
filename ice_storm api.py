from typing import Dict

class IceStorm:
    """Class to represent an Ice Storm."""
    _VALID_FLAVORS = {
        'Mint Chocolate Chip': 4.0,
        'Chocolate': 3.0
    }

    def __init__(self, flavor: str):
        if flavor not in self._VALID_FLAVORS:
            raise ValueError("Invalid flavor.")
        self._flavor = flavor
        self._toppings = {}

    def add_topping(self, topping: str, cost: float):
        self._toppings[topping] = cost

    def get_total(self):
        return self._VALID_FLAVORS[self._flavor] + sum(self._toppings.values())
import unittest
from api.ice_storm import IceStorm

class TestIceStorm(unittest.TestCase):
    def setUp(self):
        self.ice_storm = IceStorm('Mint Chocolate Chip')

    def test_add_topping(self):
        self.ice_storm.add_topping('Cherry', 0.5)
        self.assertAlmostEqual(self.ice_storm.get_total(), 4.5)

    def test_invalid_flavor(self):
        with self.assertRaises(ValueError):
            IceStorm('Invalid')

if __name__ == '__main__':
    unittest.main()
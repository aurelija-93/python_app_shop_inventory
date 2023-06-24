import unittest
from models.supplier import Supplier
from models.product import Product

class TestProduct(unittest.TestCase):
    def setUp(self):
        self.supplier = Supplier(
            "Scribbulus", "0200 3333", "muggles@scribbulus.co.uk"
            )
        self.product = Product(
            "Colour-Change Ink",
            "Once used, the charm lasts for one month.",
            5, 15, 25, self.supplier
            )

    def test_product_has_name(self):
        self.assertEqual("Colour-Change Ink", self.product.name)

    def test_product_has_description(self):
        self.assertEqual("Once used, the charm lasts for one month.", self.product.description)

    def test_product_has_stock(self):
        self.assertEqual(5, self.product.stock)

    def test_product_has_purchase_price(self):
        self.assertEqual(15, self.product.purchase_price)

    def test_product_has_selling_price(self):
        self.assertEqual(25, self.product.selling_price)

    def test_product_has_margin(self):
        self.assertEqual(67, self.product.margin)

    def test_product_has_supplier(self):
        self.assertEqual(self.supplier, self.product.supplier)

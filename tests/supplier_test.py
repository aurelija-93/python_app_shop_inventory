import unittest
from models.supplier import Supplier

class TestSupplier(unittest.TestCase):
    def setUp(self):
        self.supplier = Supplier("Scribbulus", "0200 3333", "muggles@scribbulus.co.uk")

    def test_supplier_has_name(self):
        self.assertEqual("Scribbulus", self.supplier.name)

    def test_supplier_has_phone(self):
        self.assertEqual("0200 3333", self.supplier.phone)

    def test_supplier_has_email(self):
        self.assertEqual("muggles@scribbulus.co.uk", self.supplier.email)
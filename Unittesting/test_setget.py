import unittest
import model.product

class Test_product(unittest.TestCase):
    def setUp(self):
        self.n = model.product.Product_info()

    def test_set_productid(self):
        self.n.set_productid(2)
        self.assertEqual(2, self.n.get_productid())


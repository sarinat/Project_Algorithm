import unittest
import model.product

class Test_product(unittest.TestCase):
    def setUp(self):
        self.n = model.product.Product_info()

    def test_set_productid(self):
        self.n.set_productid(2)
        self.assertEqual(2, self.n.get_productid())
        self.assertRaises(TypeError, self.n.get_productid, "SS")
    #==========Test Passed============================

    def test_set_name(self):
        self.n.set_name("rod")
        self.assertEqual("rod",self.n.get_name())
    #==========Test Passed============================

    def test_set_price(self):
        self.n.set_price(100)
        self.assertEqual(100, self.n.get_price())
    # ==========Test Passed============================

    def test_set_qnt(self):
        self.n.set_quantity(120)
        self.assertEqual(120, self.n.get_quantity())
    # ===========Test Passed============================

    def test_set_man(self):
        self.n.set_manufacturer("Ram Company")
        self.assertEqual("Ram Company", self.n.get_manufacturer())
    # ===========Test Passed============================

    def test_set_contact(self):
        self.n.set_contact(981283782)
        self.assertEqual(981283782, self.n.get_contact())
    # ===========Test Passed============================

    def tearDown(self):
        print('teardown method')
        del self.n


if __name__=='__main__':
    unittest.main()












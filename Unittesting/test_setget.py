import unittest
import model.product

class Test_product(unittest.TestCase):
    def setUp(self):
        self.n = model.product.Product_info()
    #===============testing setter and getter method of product_info table=====

    def test_set_productid(self):
        self.n.set_productid(2)
        self.assertEqual(2, self.n.get_productid())
        self.assertRaises(TypeError, self.n.get_productid, "SS")
    #==========test Passed============================

    def test_set_name(self):
        self.n.set_name("rod")
        self.assertEqual("rod",self.n.get_name())
    #==========test Passed============================

    def test_set_price(self):
        self.n.set_price(100)
        self.assertEqual(100, self.n.get_price())
    # ==========test Passed============================

    def test_set_qnt(self):
        self.n.set_quantity(120)
        self.assertEqual(120, self.n.get_quantity())
    # ===========test Passed============================

    def test_set_man(self):
        self.n.set_manufacturer("Ram Company")
        self.assertEqual("Ram Company", self.n.get_manufacturer())
    # ===========test Passed============================

    def test_set_contact(self):
        self.n.set_contact(981283782)
        self.assertEqual(981283782, self.n.get_contact())
    # ===========test Passed============================

    def tearDown(self):
        print('teardown method')
        del self.n


if __name__=='__main__':
    unittest.main()












import unittest
import Backend.connectiondb


class Test_connection(unittest.TestCase):

    def setUp(self):
        self.db = Backend.connectiondb.DBconnect()

    def test_login_authorization(self):
        query = "Select * from user where Username=%s and Password=%s"
        values = ("sarina", "123")
        expected_result=[(1,'sarina', '123', 'ktm', 'Female')]
        actual_result=self.db.select(query, values)
        self.assertEqual(expected_result,actual_result)
    #============test Passed======================

    def test_add_info(self):
        query = "INSERT INTO product_info (productid,name,price,quantity,manufacturer,contact) VALUES (10, 'nkt', '12','10', 'ram llt', '0139935')"
        actual= self.db.iud(query)
        self.assertIsNot(False, actual)
    # ============test Passed======================

    def test_update(self):
        qry = "UPDATE product_info SET name=%s WHERE productid = %s"
        values=("ok",10)
        sarina=self.db.iud(qry,values)
        qry2= "Select * from product_info where productid=10"
        sarina= self.db.fetch_info(qry2)
        self.assertIsNotNone(sarina)
    # ============test Passed======================

    def test_delete_info(self):
        qry = "DELETE FROM product_info WHERE productid=%s"
        values= (10,)
        ss=self.db.iud(qry,values)
        self.assertIsNone(ss)
    # ============test Passed======================

    def tearDown(self):
        print('teardown method')
        del self.db


if __name__=='__main__':
    unittest.main()


















import unittest
from Frontend import *
import Backend.connectiondb


class Test_connection(unittest.TestCase):
    def setUp(self):
        self.db = Backend.connectiondb.DBconnect()

    #======Test 1 =========
    # def test_select(self):
    #     query = "Select * from product_info"
    #     rows = self.db.select(query,)
    #     self.assertIsNotNone(rows)

    #def test_add(self):







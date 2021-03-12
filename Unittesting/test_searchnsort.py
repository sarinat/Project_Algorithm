import unittest
import Backend.connectiondb
import model.searchnsort

class Test_searcnsort(unittest.TestCase):
    def setUp(self):
        '''  set up the method for testing'''
        self.db = Backend.connectiondb.DBconnect()
        self.search = model.searchnsort.My_searching()
        self.sort = model.searchnsort.My_sorting()

    def test_searching(self):
    #Testing the searching value
        query = "select * from product_info"
        abc = self.db.fetch_info(query)
        print(abc)
        bcd = self.search.linear_search('steel', abc)
        print(bcd)
        self.assertEqual(1, bcd)
    # ==========test Passed============================

    def test_sorting(self):
    #Testing the sorting of database fetch value
        query = "select * from product_info"
        abc = (self.db.fetch_info(query))
        bcd = self.sort.insertion_sort(abc, 0)
        print(bcd)
        self.assertEqual(
            [(1, 'rod', '12000', '10000', 'ram lmt', '0134435'),
             (2, 'steel', '1000', '122', 'abc company', '01281237'),
             (3, 'nails', '1111', '120', 'dk wares', '01238923'),
             (4, 'shovel', '1002', '122', ' st wares', '01928848')],bcd)

    # ==========test Passed============================

    def tearDown(self):
        print('teardown method')
        del self.search
        del self.sort
        del self.db


if __name__=='__main__':
    unittest.main()
import unittest
from itertools import islice

from pygments.lexers import configs


class MyTestCase(unittest.TestCase):
    def test_something(self):
        list = [0,1,2,3,4,5]
        for l in islice(list, 0, None):
            print(l)




if __name__ == '__main__':
    unittest.main()

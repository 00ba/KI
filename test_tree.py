'''
Created on Sep 4, 2016

@author: oobasatoshi
'''
from tree import *
import unittest


class Test(unittest.TestCase):


    def test_tree(self):

        self.assertEquals(ki1.view, {'left': 'ki2', 'right': 'ki3', 'name': 'one', 'number': '1'})


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_tree']
    unittest.main()
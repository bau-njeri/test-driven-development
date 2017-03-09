def add(n,m):
    return n+m

def sub (n,m):
    return n-m

def mult(n,m):
    return n*m

def div (n,m):
    return n/m

import unittest

class MyTest (unittest.TestCase):
    def test_add(self):
        self.assertEqual( add(5,5), 10 )
        self.assertEqual( add(15,5), 20 )
        self.assertEqual( add(1,5), 6 )
        
    def test_sub(self):
        self.assertEqual( sub(5,5), 0 )
        self.assertEqual( sub(25,5), 20 )
        self.assertEqual( sub(20,5), 15 )

    def test_mult(self):
        self.assertEqual( mult(5,5), 25 )
        self.assertEqual( mult(7,10), 70 )

    def test_div(self):
        self.assertEqual( div(54,9), 6 )
        self.assertEqual( div(21,7), 3 )
        
unittest.main(verbosity=2)

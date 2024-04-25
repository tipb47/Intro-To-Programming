import a1
import unittest

class MyTests(unittest.TestCase):

    def test_c(self):
        self.assertAlmostEqual(a1.c(2,5),20.94,2)
    def test_f(self):    
        self.assertAlmostEqual(a1.f(10),75,2)
    def test_P(self):    
        self.assertAlmostEqual(a1.P(3),54.02,2)  
    def test_cost(self):    
        self.assertAlmostEqual(a1.cost(70),1.17,2)    
    def test_D(self):    
        self.assertAlmostEqual(a1.D(4,500),104.17,2)   

if __name__=="__main__":
    unittest.main()

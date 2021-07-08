import unittest
from math_dojo_clase import MathDojo


class Test_MathDojo(unittest.TestCase):

    def setUp(self):
        self.md = MathDojo()
        print("Estamos preparando la escena")
        self.num1=1
        self.num2=1
        self.num3=1

    def test01(self):
        print("Se estan comprobando las sumas")
        self.assertEqual(self.md.add(self.num1,self.num2).result, 2)
    
    def test02(self):
        print("Se estan comprobando las restas")
        self.assertEqual(self.md.subtract(self.num1,self.num2).result, 0)
    
    def test03(self):
        print("Se estan comprobando las funciones")
        self.assertEqual(self.md.avg(self.num1,self.num2), 1.0)

    def tearDown(self):
        print("Destruyendo la Data")
        

if __name__ == '__main__':
    unittest.main()

import unittest
from NumeroArmstrong import numero_armstrong

class TestNumeroArmstrong(unittest.TestCase):

    def test_armstrong_numbers(self):
        """Probar con números que son de Armstrong."""
        self.assertTrue(numero_armstrong(153))
        self.assertTrue(numero_armstrong(9474))
        self.assertTrue(numero_armstrong(0))  # El 0 también es un número de Armstrong
        self.assertTrue(numero_armstrong(370))
        self.assertTrue(numero_armstrong(407))

    def test_non_armstrong_numbers(self):
        """Probar con números que no son de Armstrong."""
        self.assertFalse(numero_armstrong(123))
        self.assertFalse(numero_armstrong(456))
        self.assertFalse(numero_armstrong(10))

    def test_single_digit_numbers(self):
        """Probar con números de un solo dígito """
        for i in range(10):
            self.assertTrue(numero_armstrong(i))

    def test_large_numbers(self):
        """Probar con números grandes que no son de Armstrong."""
        self.assertFalse(numero_armstrong(9475))
        self.assertFalse(numero_armstrong(123456))
    
    def test_edge_case_zero(self):
        """Probar el caso límite de 0."""
        self.assertTrue(numero_armstrong(0))


if __name__ == "__main__":
    unittest.main()

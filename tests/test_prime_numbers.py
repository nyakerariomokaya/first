from unittest import TestCase
from first.prime_numbers import is_prime
class TestPrimeNumbers(unittest.TestCase):
    
    def mock_raw_input(n):
         return 
         is_prime.raw_input = mock_raw_input

    def test_n_is_negative(self):
     	 
     	 Assert.IsTrue((n == -1), "invalid")

    def test_error(self):
     	  raise RuntimeError('Test error!')

    def test_is_num_zero(self):
     	 result = is_prime(num==0)
     	 with self.assertRaises(ZeroDivisionError, msg ="zero cant divide")
     	 is_prime(0)

    def test_for_non_numeric_inputs(self):
         with self.assertRaises(ValueError, msg ="only put numeric input")
     	 is_prime(100)

    def test_for_float_inputs(self):
         with self.assertRaises(ValueError, msg ="only put numeric input")
     	 is_prime(100)

    def test_if_input_is_empty(self):
     	 Assert.IsTrue((n ==0), "invalid")

    def test_each_item_is_prime(self):

     	 Assert.IsTrue((num != False), "invalid")





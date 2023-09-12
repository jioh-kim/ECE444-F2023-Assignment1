#Full credit to chatgpt

from utils import utils
import unittest

class TestUtils(unittest.TestCase):
    
    teststring = 'abc'
    testfloat = 11.03
    testinteger = 1103
    
    def setUp(self):
        self.utils_instance = Utils()

    def test_reverse_integer(self):
        reversed_int = self.utils_instance.reverse(self.testinteger)
        self.assertEqual(reversed_int, 3011)
        
    def test_reverse_string(self):
        reversed_string = self.utils_instance.reverse(self.teststring)
        self.assertEqual(reversed_string, 'cba')
        
    def test_reverse_float(self):
        reversed_float = self.utils_instance.reverse(self.testfloat)
        self.assertEqual(reversed_float, 30.11)
        
    def test_formatter(self):
        formatted_integer = self.utils_instance.formatter(self.testinteger)
        self.assertEqual(formatted_integer, ('0b10001000111', '0o2107'))
        
        formatted_string = self.utils_instance.formatter(self.teststring)
        self.assertEqual(formatted_string, ('0b1100010', '0o142'))
        
        formatted_float = self.utils_instance.formatter(self.testfloat)
        self.assertEqual(formatted_float, ('0b11.00000010100011110101110000101001010010110001111', '0o13.0434635226535544625763'))

if __name__ == '__main__':
    unittest.main()

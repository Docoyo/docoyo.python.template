'''
  Test submodule functionality
'''
import unittest
from my_package.my_subpackage.my_functionality import complex_function


class TestMySubPackage(unittest.TestCase):
  '''
    Fixture
  '''

  def test_complex_function(self):
    '''
      Tests the main method while mocking the submodule
    '''
    in_out = 42
    value = complex_function(in_out)
    self.assertEqual(value, in_out)

if __name__ == '__main__':
  unittest.main()

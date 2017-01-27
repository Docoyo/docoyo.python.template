'''
  Test module functionality
'''
import unittest
from unittest.mock import MagicMock
import sys

mock_submodule = MagicMock()  # pylint: disable=C0103
sys.modules['my_package.my_subpackage.my_functionality'] = mock_submodule
from my_package.my_module import special_functionality  # pylint: disable=C0413


class TestMyModule(unittest.TestCase):
  '''
    Fixture
  '''

  def test_main_method(self):
    '''
      Tests the main method while mocking the submodule
    '''
    mock_submodule.complex_function.return_value = {}
    value = special_functionality()
    self.assertDictEqual(value, {"WELL": "...GOODBYE!"})


if __name__ == '__main__':
  unittest.main()

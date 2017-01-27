'''
Implements storage of beacon properties messages
'''
import logging

_logger = logging.getLogger('msgdbhook')  # pylint: disable=C0103

def complex_function(argument):
  '''
    Stores a beacon properties message.
  '''
  _logger.info("Submodule called with " + str(argument))
  return argument

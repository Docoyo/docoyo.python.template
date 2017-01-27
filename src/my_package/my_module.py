'''
  Describe this wonderful functionality
'''
import logging
from logging.handlers import RotatingFileHandler
import json
import argparse
import sys
from itertools import compress
from .my_subpackage.my_functionality import complex_function

_REQUIRED_CONFIG = ['logsize-bytes', 'num-log-bakups', 'logpath']

_logger = logging.getLogger('msgdbhook')  # pylint: disable=C0103


def parse_arguments():
  '''
    Parses the arguments and initializes the logfile.
  '''
  parser = argparse.ArgumentParser(
      description='Message to be shown as commandline information',
      formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  parser.add_argument(
      '--configfile',
      required=True,
      type=str,
      nargs='+',
      help='One or more configfiles read in order')
  parser.add_argument(
      '--verbose',
      '-v',
      required=False,
      default=False,
      action='store_true',
      help='Print informations to console')
  args = parser.parse_args()

  config = {}
  for filename in args.configfile:
    with open(filename) as file:
      config_single = json.load(file)
      config.update(config_single)

  are_attr_missing = [not x in config for x in _REQUIRED_CONFIG]
  if any(are_attr_missing):
    print(
        "The following arguments are missing:" +
        ' '.join(compress(_REQUIRED_CONFIG, are_attr_missing)),
        file=sys.stderr)
    sys.exit(-1)

  _logger.setLevel(logging.DEBUG)
  fh = RotatingFileHandler(
      config['logpath'],
      maxBytes=config['logsize-bytes'],
      backupCount=config['num-log-bakups'])

  fh.setLevel(logging.INFO)
  formatter = logging.Formatter(
      '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
  fh.setFormatter(formatter)
  _logger.addHandler(fh)

  if args.verbose:
    out_console = logging.StreamHandler(sys.stdout)
    out_console.setFormatter(logging.Formatter('%(asctime)s %(message)s'))
    out_console.setLevel(logging.DEBUG)
    _logger.addHandler(out_console)

  _logger.info("Loaded configuration")

  return config

def special_functionality():
  '''
    My special functionality
  '''
  sm_return = complex_function({"HELLO": "WORLD!"})
  sm_return['WELL'] = "...GOODBYE!"
  return sm_return


def main():
  '''
    Main method that:
      parses the arguments,
      runs special functionality.
  '''
  config = parse_arguments()
  _logger.info("Read config: " + str(config))
  special_functionality()


if __name__ == "__main__":
  main()

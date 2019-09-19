from dotenv import load_dotenv
load_dotenv()

import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
import unittest
from ringcentral_engage_digital import RestClient

RINGCENTRAL_ENGAGE_SERVER_URL='xx'
RINGCENTRAL_ENGAGE_API_TOKEN='xxx'

try:
  RINGCENTRAL_ENGAGE_SERVER_URL = os.environ['RINGCENTRAL_ENGAGE_SERVER_URL']
  RINGCENTRAL_ENGAGE_API_TOKEN = os.environ['RINGCENTRAL_ENGAGE_API_TOKEN']
except:
  pass

class TestBot(unittest.TestCase):

  def test_basic_bot(self):
    print('running bot basic test')
    rc = RestClient(
      RINGCENTRAL_ENGAGE_API_TOKEN,
      RINGCENTRAL_ENGAGE_SERVER_URL
    )
    r = rc.get('/1.0/roles')
    self.assertEqual(len(r.json()['records']) > 0, True)

if __name__ == '__main__':
    unittest.main()
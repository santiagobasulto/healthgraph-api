import unittest

import mock
from betamax import Betamax

import requests

from ..resources import User
from ..sessionmgr import Session

from data import USER_BASE


with Betamax.configure() as config:
    config.cassette_library_dir = 'tests/fixtures/cassettes'


class DummyTestCase(unittest.TestCase):
    # def test_santiago(self):
    #     access_token = '0386da64a54b4262bd48cbfc9ffcdd2c'
    #     with mock.patch('resources.User._get_resource_data') as usr_mock_data:
    #         usr_mock_data.return_value = USER_BASE
    #         user = User(session=Session(access_token))
    #         assert str(user.get('userID')) == "10935031"
    #         print str(user.get('userID'))

    def setUp(self):
        self.session = requests.Session()

    def test_santiago(self):
        access_token = '0386da64a54b4262bd48cbfc9ffcdd2c'
        with Betamax(self.session).use_cassette('user'):
            user = User(session=Session(access_token))
            self.assertEqual(str(user.get('userID')), "10935031")


drews = "4c85ea05875f4ac4a4a4df002e56a196"

#test_santiago()

if __name__ == '__main__':
    unittest.main()
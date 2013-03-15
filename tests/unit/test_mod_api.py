# -*- coding: utf-8 *-*
import sys
import os
import mock
if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest
import coverage

sys.path.insert(0, "../../")

from space.modules import api


class TestApi(unittest.TestCase):

    def setUp(self):
        self.sw = mock.Mock()

    @mock.patch('space.lib.api.getApiCallList')
    def test_api_list(self, api_list):
        answer = {
            'things':
            {
                'it': {
                    'name': 't',
                    'parameters': ['blah']
                }
            }
        }
        api_list.return_value = answer
        result = api.list(self.sw, [])
        self.assertEquals(
            result,
            True,
            result
        )

    @mock.patch('space.lib.api.getApiCallList')
    def test_api_list_none(self, api_list):
        # test no answer
        api_list.return_value = None
        result = api.list(self.sw, [])
        self.assertEquals(
            result,
            False,
            result
        )  

# -*- coding: utf-8 *-*
from space.modules import systems
from space.main import swSession
from space.main import main

import sys
if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest
import sys
import os
import mock


class TestSystems(unittest.TestCase):

    @mock.patch('space.main.swSession')
    def test_listsystems(self, sw_mock):
        sw_call = sw_mock.return_value = mock.Mock()
        sw_call.call.return_value = [{'hostname':'blah.com', 'id': 'who'}]

        sys.argv = [
            'space',
            '--username=test',
            '--host=test',
            '--password=test',
            'systems',
            'list',
            '--group', 'test_group']
        result = main()

        self.assertIsInstance(result, list, result)

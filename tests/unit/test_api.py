# -*- coding: utf-8 *-*
from space.modules import api
from space.main import swSession
from space.main import main

import sys
if sys.version_info < (2, 8):
    import unittest2 as unittest
    from io import BytesIO as strio
else:
    import unittest
    from io import StringIO as strio
import sys
import os
import mock


class TestApi(unittest.TestCase):

    def setUp(self):
        self.output = strio()
        self.saved_stdout = sys.stdout
        sys.stdout = self.output

    def tearDown(self):
        self.output.close()
        sys.stdout = self.saved_stdout

    @mock.patch('space.main.swSession')
    def test_list_api(self, sw_mock):
        sw_call = sw_mock.return_value = mock.Mock()
        sw_call.call.return_value = {'call':{'call': {'name':'item', 'parameters': 'param'}}}

        sys.argv = [
            'space',
            '--username=test',
            '--host=test',
            '--password=test',
            'api',
            'list']
        main()        
        result = self.output.getvalue()

        self.assertRegexpMatches(result, "call.item\(param\)\\n", result)

    @mock.patch('space.main.swSession')
    def test_list_api_no_return(self, sw_mock):
        sw_call = sw_mock.return_value = mock.Mock()
        sw_call.call.return_value = None

        sys.argv = [
            'space',
            '--username=test',
            '--host=test',
            '--password=test',
            'api',
            'list']
        main()        
        result = self.output.getvalue()

        self.assertRegexpMatches(result, "No calls in api. Most likely lies", result)

    @mock.patch('space.main.swSession')
    def test_list_api_in_namespace(self, sw_mock):
        sw_call = sw_mock.return_value = mock.Mock()
        sw_call.call.return_value = 'Results. All sorts.'

        sys.argv = [
            'space',
            '--username=test',
            '--host=test',
            '--password=test',
            'api',
            'list_in_namespace',
            '--namespace', 'api',
        ]
        main()        
        result = self.output.getvalue()

        self.assertRegexpMatches(result, "Results. All sorts.", result)

    @mock.patch('space.main.swSession')
    def test_list_api_in_namespace_fail(self, sw_mock):
        sw_call = sw_mock.return_value = mock.Mock()
        sw_call.call.side_effect = Exception

        sys.argv = [
            'space',
            '--username=test',
            '--host=test',
            '--password=test',
            'api',
            'list_in_namespace',
            '--namespace', 'api',
        ]
        with self.assertRaises(Exception):
            main()

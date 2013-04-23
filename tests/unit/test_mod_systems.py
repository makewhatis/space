# -*- coding: utf-8 *-*
import sys
import os
import mock
if sys.version_info < (2, 8):
    import unittest2 as unittest
    from io import BytesIO as strio
else:
    import unittest
    from io import StringIO as strio

import coverage

sys.path.insert(0, "../../")

from space.main import swSession
from space.main import main
from space.modules import system


class TestModSystems(unittest.TestCase):

    def setUp(self):
        self.output = strio()
        self.saved_stdout = sys.stdout
        sys.stdout = self.output

    def tearDown(self):
        self.output.close()
        sys.stdout = self.saved_stdout

    @mock.patch('space.modules.system._get_channels')
    @mock.patch('space.modules.system._get_system')
    def test_channel_children(self, get_system, get_channels):
        sw = mock.Mock()
        # test 0 args
        args = []
        result = system.child_channels(sw, args)
        self.assertEqual(result, False, result)

        # set server return args
        get_system.return_value = [{'id': 'test'}]
        get_channels.return_value = [{'name':'test'}]

        # test legit server arg
        args = [
            '--server', 'test.com'
        ]
        result = system.child_channels(sw, args)
        self.assertEqual(result, True, result)

        # test empty result
        get_system.return_value = []
        result = system.child_channels(sw, args)
        self.assertEqual(result, False, result)

    @mock.patch('space.main.swSession')
    def test_list_child_channels_sid(self, sw_mock):
        sw_call = sw_mock.return_value = mock.Mock()
        sw_call.call.return_value = [{'name':'a channel'}]
        sys.argv = [
            'space',
            '--username=test',
            '--host=test',
            '--password=test',
            'system',
            'child_channels',
            '--sid', '1']
        main()
        result = self.output.getvalue()

        self.assertRegexpMatches(result, 'a channel', result)

    @mock.patch('space.main.swSession')
    def test_list_child_channels_servername_exception(self, sw_mock):
        sw_call = sw_mock.return_value = mock.Mock()
        # giving bunk keys
        sw_call.call.return_value = [{'names':'a channel', 'ids': '1'}]
        sys.argv = [
            'space',
            '--username=test',
            '--host=test',
            '--password=test',
            'system',
            'child_channels',
            '--server', 'test.com']
        main()
        result = self.output.getvalue()
        self.assertRegexpMatches(result, 'Exception', result)

    @mock.patch('space.main.swSession')
    def test_listsystems(self, sw_mock):
        sw_call = sw_mock.return_value = mock.Mock()
        sw_call.call.return_value = [{'hostname':'blah.com', 'id': 'who'}]

        sys.argv = [
            'space',
            '--username=test',
            '--host=test',
            '--password=test',
            'system',
            'list',
            '--group', 'test_group']
        main()
        result = self.output.getvalue()

        self.assertRegexpMatches(result, 'blah.com who', result)

    @mock.patch('space.main.swSession')
    def test_listsystems_group_exception(self, sw_mock):
        sw_call = sw_mock.return_value = mock.Mock()
        sw_call.call.side_effect = Exception

        sys.argv = [
            'space',
            '--username=test',
            '--host=test',
            '--password=test',
            'system',
            'list',
            '--group', 'test_group']
        main()
        result = self.output.getvalue()
        self.assertRegexpMatches(result, 'Error listing systems', result)

    @mock.patch('space.main.swSession')
    def test_listsystems_empty_groups(self, sw_mock):
        sw_call = sw_mock.return_value = mock.Mock()
        sw_call.call.return_value = []

        sys.argv = [
            'space',
            '--username=test',
            '--host=test',
            '--password=test',
            'system',
            'list',
            '--group', 'test_group']
        main()
        result = self.output.getvalue()
        self.assertRegexpMatches(result, 'No servers in group', result)

    @mock.patch('space.main.swSession')
    def test_listsystems_all(self, sw_mock):
        sw_call = sw_mock.return_value = mock.Mock()
        sw_call.call.return_value = [{'name':'blah.com', 'id': 'who'}]

        sys.argv = [
            'space',
            '--username=test',
            '--host=test',
            '--password=test',
            'system',
            'list'
        ]
        main()
        result = self.output.getvalue()
        # test for value return on the above dict
        self.assertRegexpMatches(result, 'blah.com who', result)

    @mock.patch('space.main.swSession')
    def test_listsystems_all_exception(self, sw_mock):
        sw_call = sw_mock.return_value = mock.Mock()
        sw_call.call.side_effect = Exception

        sys.argv = [
            'space',
            '--username=test',
            '--host=test',
            '--password=test',
            'system',
            'list'
        ]
        main()
        result = self.output.getvalue()
        self.assertRegexpMatches(result, 'Error listing all systems', result)

    @mock.patch('space.main.swSession')
    def test_get_channels(self, sw_mock):
        sw_call = sw_mock.return_value = mock.Mock()
        sw_call.call.return_value = ['channels']

        result = system._get_channels(sw_call, 1)
        self.assertEqual(['channels'], result)

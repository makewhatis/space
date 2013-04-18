# -*- coding: utf-8 *-*
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


class TestActivationkey(unittest.TestCase):

    def setUp(self):
        self.output = strio()
        self.saved_stdout = sys.stdout
        sys.stdout = self.output

    def tearDown(self):
        self.output.close()
        sys.stdout = self.saved_stdout

    @mock.patch('space.main.swSession')
    def test_add_child_channels(self, sw_mock):
        sw_call = sw_mock.return_value = mock.Mock()
        sw_call.call.return_value = True

        sys.argv = [
            'space',
            '--username=test',
            '--host=test',
            '--password=test',
            'activationkey',
            'add_child_channels',
            '--keyname', 'test_key',
            '--channels', 'blah', 'blah1',
        ]
        main()
        result = self.output.getvalue()
        self.assertRegexpMatches(
            result, "\[\'blah\', \'blah1\'\] added to test_key\\n", result)

    @mock.patch('space.main.swSession')
    def test_create(self, sw_mock):
        sw_call = sw_mock.return_value = mock.Mock()
        sw_call.call.return_value = ['test_key']

        sys.argv = [
            'space',
            '--username=test',
            '--host=test',
            '--password=test',
            'activationkey',
            'create',
            '--keyname', 'test_key',
            '--basechannel', 'blah',
            '--monitoring_entitled',
            '--provisioning_entitled',
            '--virtualization_host',
            '--virtualization_host_platform',
            '--universal_default',
        ]
        main()
        result = self.output.getvalue()
        self.assertRegexpMatches(
            result, "test_key created", result)

    @mock.patch('space.main.swSession')
    def test_create_fail(self, sw_mock):
        sw_call = sw_mock.return_value = mock.Mock()
        sw_call.call.side_effect = Exception
        sys.argv = [
            'space',
            '--username=test',
            '--host=test',
            '--password=test',
            'activationkey',
            'create',
            '--keyname', 'test_key',
            '--basechannel', 'blah',
            '--monitoring_entitled',
            '--provisioning_entitled',
            '--virtualization_host',
            '--virtualization_host_platform',
            '--universal_default',
        ]
        with self.assertRaises(Exception):
            main()

    @mock.patch('space.main.swSession')
    def test_add_group(self, sw_mock):
        sw_call = sw_mock.return_value = mock.MagicMock()
        sw_call.call.side_effect = [{'id': '1'}, 1]
        sys.argv = [
            'space',
            '--username=test',
            '--host=test',
            '--password=test',
            'activationkey',
            'add_group',
            '--keyname', 'test_key',
            '--groups', 'blah',
        ]
        main()
        result = self.output.getvalue()
        self.assertEquals(result, 'blah has been added to test_key\n', result)

    @mock.patch('space.main.swSession')
    def test_add_group_fail_getDetails(self, sw_mock):
        sw_call = sw_mock.return_value = mock.MagicMock()
        sw_call.call.side_effect = [{'id': '1'}, Exception]
        sys.argv = [
            'space',
            '--username=test',
            '--host=test',
            '--password=test',
            'activationkey',
            'add_group',
            '--keyname', 'test_key',
            '--groups', 'blah',
        ]
        main()
        result = self.output.getvalue()
        self.assertRegexpMatches(result, 'Adding key to group failed', result)

    @mock.patch('space.main.swSession')
    def test_add_group_fail_addServerGroups(self, sw_mock):
        sw_call = sw_mock.return_value = mock.MagicMock()
        sw_call.call.side_effect = [Exception, "FAILED", {'id': '1'}]
        sys.argv = [
            'space',
            '--username=test',
            '--host=test',
            '--password=test',
            'activationkey',
            'add_group',
            '--keyname', 'test_key',
            '--groups', 'blah',
        ]
        main()
        result = self.output.getvalue()
        self.assertRegexpMatches(result, 'FAILED', result)

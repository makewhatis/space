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


class TestChannel(unittest.TestCase):

    def setUp(self):
        self.output = strio()
        self.saved_stdout = sys.stdout
        sys.stdout = self.output

    def tearDown(self):
        self.output.close()
        sys.stdout = self.saved_stdout

    @mock.patch('space.main.swSession')
    def test_listchannels_popcount(self, sw_mock):
        sw_call = sw_mock.return_value = mock.Mock()

        popular_result = [
            {
                'name': 'fedora-16-x86_64-updates',
                'arch_name': 'x86_64',
                'label': 'fedora-16-x86_64-updates',
                'systems': 0,
                'provider_name': 'Spacewalk Default Organization',
                'packages': 10452,
                'id': 109
            },
        ]        
        sw_call.call.return_value = popular_result

        sys.argv = [
            'space',
            '--username=test',
            '--host=test',
            '--password=test',
            'channel',
            'list', 'popular',
            '--popcount=2',
            '--format=raw'
        ]
        main()
        result = self.output.getvalue()
        self.assertRegexpMatches(result, "^{\'name\': \'fedora-16-x86_64-updates\'*", result)

    @mock.patch('space.main.swSession')
    def test_listchannels_popcount_no_arg(self, sw_mock):
        sw_call = sw_mock.return_value = mock.Mock()

        popular_result = [
            {
                'name': 'fedora-16-x86_64-updates',
                'arch_name': 'x86_64',
                'label': 'fedora-16-x86_64-updates',
                'systems': 0,
                'provider_name': 'Spacewalk Default Organization',
                'packages': 10452,
                'id': 109
            },
        ]        
        sw_call.call.return_value = popular_result

        sys.argv = [
            'space',
            '--username=test',
            '--host=test',
            '--password=test',
            'channel',
            'list', 'popular',
            '--format=raw'
        ]
        main()
        result = self.output.getvalue()
        self.assertRegexpMatches(result, "Popular requires popcount arg.*", result)

    @mock.patch('space.main.swSession')
    def test_listchannels_all(self, sw_mock):
        sw_call = sw_mock.return_value = mock.Mock()

        all_result = [
            {
                'name': 'fedora-12-x86_64-updates',
                'arch_name': 'x86_64',
                'label': 'fedora-16-x86_64-updates',
                'systems': 0,
                'provider_name': 'Spacewalk Default Organization',
                'packages': 10452,
                'id': 109
            },
        ]
        sw_call.call.return_value = all_result
        
        # test pretty output
        sys.argv = [
            'space',
            '--username=test',
            '--host=test',
            '--password=test',
            'channel',
            'list', 'all',
            '--format=raw'
        ]
        main()        
        result = self.output.getvalue()
        self.assertRegexpMatches(result, "^{\'name\': \'fedora-12-x86_64-updates\',.*", result)


    @mock.patch('space.main.swSession')
    def test_listchannels_software_pretty(self, sw_mock):
        sw_call = sw_mock.return_value = mock.Mock()
        software_result = [
            {
                'parent_label': '',
                'label': 'centos-5-x86_64-base',
                'arch': 'x86_64', 'end_of_life': '',
                'name': 'centos-5-x86_64-base'
            },
        ]
        sw_call.call.return_value = software_result
        sys.argv = [
            'space',
            '--username=test',
            '--host=test',
            '--password=test',
            'channel',
            'list',
            'software',
            '--format=pretty']
        main()        
        result = self.output.getvalue()
        self.assertRegexpMatches(result, "^| centos-5-x86_64-base | centos-5-x86_64-base |.*", result)

    @mock.patch('space.main.swSession')
    def test_listchannels_software_raw(self, sw_mock):
        sw_call = sw_mock.return_value = mock.Mock()
        all_result = [
            {
                'name': 'fedora-12-x86_64-updates',
                'arch_name': 'x86_64',
                'label': 'fedora-16-x86_64-updates',
                'systems': 0,
                'provider_name': 'Spacewalk Default Organization',
                'packages': 10452,
                'id': 109
            },
        ]
        sw_call.call.return_value = all_result
        sys.argv = [
            'space',
            '--username=test',
            '--host=test',
            '--password=test',
            'channel',
            'list',
            'user',
            '--format=pretty']
        main()        
        result = self.output.getvalue()
        self.assertRegexpMatches(result, "^| centos-5-x86_64-base | centos-5-x86_64-base |.*", result)        

    @mock.patch('space.main.swSession')
    def test_listchannels_software_json(self, sw_mock):
        sw_call = sw_mock.return_value = mock.Mock()
        all_result = [
            {
                'name': 'fedora-12-x86_64-updates',
                'arch_name': 'x86_64',
                'label': 'fedora-16-x86_64-updates',
                'systems': 0,
                'provider_name': 'Spacewalk Default Organization',
                'packages': 10452,
                'id': 109
            },
        ]
        sw_call.call.return_value = all_result
        sys.argv = [
            'space',
            '--username=test',
            '--host=test',
            '--password=test',
            'channel',
            'list',
            'user',
            '--format=json']
        main()        
        result = self.output.getvalue()
        self.assertRegexpMatches(result, "^{\"channels\": \[{\"name\": \"fedora-12-x86_64-updates\".*", result) 

    @mock.patch('space.main.swSession')
    def test_listchannels_empty(self, sw_mock):
        sw_call = sw_mock.return_value = mock.Mock()
        all_result = []
        sw_call.call.return_value = all_result
        sys.argv = [
            'space',
            '--username=test',
            '--host=test',
            '--password=test',
            'channel',
            'list',
            'user',
            '--format=json']
        main()        
        result = self.output.getvalue()
        self.assertRegexpMatches(result, "Empty result set.", result) 
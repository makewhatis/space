# -*- coding: utf-8 *-*
from space.modules import packages
from space.main import swSession
from space.main import main

import mock

import unittest
import sys
if sys.version_info < (2, 8):
    import unittest2 as unittest
    from io import BytesIO as strio
else:
    import unittest
    from io import StringIO as strio
import os


class TestPackages(unittest.TestCase):

    def setUp(self):
        self.output = strio()
        self.saved_stdout = sys.stdout
        sys.stdout = self.output

    def tearDown(self):
        self.output.close()
        sys.stdout = self.saved_stdout

    @mock.patch('space.main.swSession')
    @mock.patch('space.modules.packages.urllib.urlretrieve')
    def test_getpackage(self, url_lib, sw_mock):
        sw_call = sw_mock.return_value = mock.Mock()
        sw_call.call.return_value = "test/bigmoney.blah.rpm"

        url_lib.return_value = [True]

        sys.argv = [
            'space',
            '--username=test',
            '--config=test',
            '--host=test',
            '--password=test',
            'packages',
            'getpackage',
            '-p',
            '1'
        ]
        main()
        result = self.output.getvalue()
        self.assertRegexpMatches(result, 'True', result)

    @mock.patch('space.main.swSession')
    def test_copy_pid(self, sw_mock):
        sw_call = sw_mock.return_value = mock.Mock()
        sw_call.call.return_value = 1

        sys.argv = [
            'space',
            '--username=test',
            '--config=test',
            '--host=test',
            '--password=test',
            'packages',
            'copy',
            '-p', '1',
            '-c', 'blah'
        ]
        main()
        result = self.output.getvalue()
        self.assertRegexpMatches(result, 'Copied package id: \[ blah \]  INTO \[ blah \] successfully!\\n', result)

    @mock.patch('space.main.swSession')
    def test_copy_nvr_bad_package_nvr(self, sw_mock):
        sw_call = sw_mock.return_value = mock.Mock()
        sw_call.call.return_value = []

        sys.argv = [
            'space',
            '--username=test',
            '--config=test',
            '--host=test',
            '--password=test',
            'packages',
            'copy',
            '--nvr', 'devhelp.i386',
            '-c', 'blah'
        ]
        main()
        result = self.output.getvalue()
        self.assertRegexpMatches(result, 'Could not parse Name-Version-Relase', result)


    @mock.patch('space.main.swSession')
    def test_copy_nvr_empty_result(self, sw_mock):
        sw_call = sw_mock.return_value = mock.Mock()
        sw_call.call.return_value = []

        sys.argv = [
            'space',
            '--username=test',
            '--config=test',
            '--host=test',
            '--password=test',
            'packages',
            'copy',
            '--nvr', 'devhelp-0.12-22.el5_8.i386',
            '-c', 'blah'
        ]
        main()
        result = self.output.getvalue()
        self.assertRegexpMatches(result, 'Returned empty list.', result)
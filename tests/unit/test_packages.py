# -*- coding: utf-8 *-*
from space.modules import packages
from space.main import swSession
from space.main import main

import mock

import unittest
import sys
import os


class TestPackages(unittest.TestCase):

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
        result = main()
        self.assertEqual(result, True, result)



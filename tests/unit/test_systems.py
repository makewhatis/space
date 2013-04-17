# -*- coding: utf-8 *-*
from space.modules import systems
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


class TestSystems(unittest.TestCase):

    def setUp(self):
        self.output = strio()
        self.saved_stdout = sys.stdout
        sys.stdout = self.output

    def tearDown(self):
        self.output.close()
        sys.stdout = self.saved_stdout

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
        main()        
        result = self.output.getvalue()

        self.assertRegexpMatches(result, 'blah.com who', result)


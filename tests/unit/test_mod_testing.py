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

from space.modules import systems


class TestModSystems(unittest.TestCase):

    def setUp(self):
        self.sw = mock.Mock()

    @mock.patch('space.modules.systems._get_channels')
    @mock.patch('space.modules.systems._get_system')
    def test_channel_children(self, get_system, get_channels):
        # test 0 args
        args = []
        result = systems.child_channels(self.sw, args)
        self.assertEqual(result, False, result)

        # set server return args
        get_system.return_value = [{'id': 'test'}]
        get_channels.return_value = [{'name':'test'}]
        
        # test legit server arg
        args = [
            '--server', 'test.com'
        ]
        result = systems.child_channels(self.sw, args)
        self.assertEqual(result, True, result)

        # test empty result
        get_system.return_value = []
        result = systems.child_channels(self.sw, args)
        self.assertEqual(result, False, result)        

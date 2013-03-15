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

    @mock.patch('space.lib.system.listSubscribedChildChannels')
    @mock.patch('space.lib.system.searchByName')
    def test_channel_children(self, searchby, subscribed):
        searchby.return_value = [{'id': 000000000}]
        subscribed.return_value = [{'name': 'test_child_channel'}]
        args = [
            '--server', 'test.com'
        ]
        result = systems.child_channels(self.sw, args)
        self.assertEqual(
            result,
            [{'name': 'test_child_channel'}],
            "Bad test result: %s" % result
        )

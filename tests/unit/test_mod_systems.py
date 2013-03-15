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
        args = [
            '--sid', '1'
        ]
        result = systems.child_channels(self.sw, args)
        self.assertEqual(
            result,
            [{'name': 'test_child_channel'}],
            "Bad test result: %s" % result
        )

        # test no args
        args = []
        result = systems.child_channels(self.sw, args)
        self.assertEqual(
            result,
            False,
            result
        )

    @mock.patch('space.lib.system.listSubscribedChildChannels')
    @mock.patch('space.lib.system.searchByName')
    def test_channel_children_multires(self, searchby, subscribed):
        searchby.return_value = [
            {'id': '000000001'},
            {'name': '000000002'}
        ]
        subscribed.return_value = [{'name': 'test_child_channel'}]
        args = [
            '--server', 'test.com'
        ]
        result = systems.child_channels(self.sw, args)
        self.assertEqual(
            result,
            False,
            "Should be False, not: %s" % result
        )

    @mock.patch('space.lib.system.listSystems')
    @mock.patch('space.lib.systemgroup.listSystems')
    def test_list_systems(self, listgroup, listsys):
        """
        Testing list_systems with --group and without
        group.
        """
        listsys.return_value = [
            {
                'name': 'test',
                'id': 1
            }
        ]
        listgroup.return_value = [
            {
                'hostname': 'test',
                'id': 1
            }
        ]
        # test no args first
        args = []
        result = systems.list_systems(
            self.sw,
            args
        )
        self.assertEqual(
            result,
            [{'name': 'test', 'id': 1}],
            result
        )
        # test group arg
        args = ['-g', 'testgroup']
        result = systems.list_systems(
            self.sw,
            args
        )
        self.assertEqual(
            result,
            [{'hostname': 'test', 'id': 1}],
            result
        )

        # test no return
        listgroup.return_value = None
        listsys.return_value = None

        args = ['-g', 'testgroup']
        result = systems.list_systems(
            self.sw,
            args
        )
        self.assertEqual(
            result,
            False,
            "result not False"
        )

        args = []
        result = systems.list_systems(
            self.sw,
            args
        )
        self.assertEqual(
            result,
            False,
            "result not False"
        )

    @mock.patch('space.lib.system.listSystems')
    @mock.patch('space.lib.systemgroup.listSystems')
    def test_list_systems_fail(self, listgroup, listsys):
        listgroup.side_effect = Exception
        listsys.side_effect = Exception

        # test group arg
        args = [
            '--group', 'test'
        ]
        result = systems.list_systems(
            self.sw,
            args
        )
        self.assertEqual(
            result,
            False,
            "result not False: %s" % result
        )

        # test no args
        result = systems.list_systems(
            self.sw,
            []
        )
        self.assertEqual(
            result,
            False,
            "result not False: %s" % result
        )

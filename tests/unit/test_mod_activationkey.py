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
print(sys.path)
from space.modules import activationkey

TEST_DIR = os.path.dirname(os.path.normpath(os.path.abspath(__file__)))

CONFIG = '%s/test.ini' % TEST_DIR


class TestModActKey(unittest.TestCase):

    def setUp(self):
        self.sw = mock.Mock()

    @mock.patch('space.lib.activationkey.addChildChannels')
    def test_add_child_channels(self, act_patch):
        act_patch.return_value = True
        args = ['--keyname', 'test', '--channels', ['it']]
        result = activationkey.add_child_channels(self.sw, args)
        self.assertEqual(result, True, "Test failed, result not true")

    @mock.patch('space.lib.activationkey.create')
    def test_create(self, act_create):
        act_create.return_value = 'test'
        args = [
            '--keyname', 'test',
            '--basechannel', 'it',
            '--monitoring_entitled',
            '--provisioning_entitled',
            '--virtualization_host',
            '--virtualization_host_platform'
        ]
        result = activationkey.create(self.sw, args)
        self.assertEqual(result, 'test', "not returning 'test'")

        act_create.side_effect = Exception
        with self.assertRaises(Exception):
            activationkey.create(self.sw, args)

    @mock.patch('space.lib.systemgroup.getDetails')
    @mock.patch('space.lib.activationkey.addServerGroups')
    def test_add_group(self, add_groups, get_dets):
        get_dets.return_value = {'id': 1}
        add_groups.return_value = 1
        args = [
            '--keyname', 'test',
            '--groups', 'it'
        ]
        result = activationkey.add_group(self.sw, args)
        self.assertEqual(result, 1, 'Result not 1')

        get_dets.side_effect = Exception
        with self.assertRaises(Exception):
            activationkey.add_group(self.sw, args)

        #get_dets.side_effect = None
        add_groups.side_effect = Exception
        with self.assertRaises(Exception):
            activationkey.add_group(self.sw, args)


    @mock.patch('space.lib.systemgroup.getDetails')
    @mock.patch('space.lib.activationkey.addServerGroups')
    def test_add_group_fail_grp(self, add_groups, get_dets):
        get_dets.return_value = {'id': 1}
        add_groups.return_value = 1
        args = [
            '--keyname', 'test',
            '--groups', 'it'
        ]
        get_dets.side_effect = Exception
        with self.assertRaises(Exception):
            activationkey.add_group(self.sw, args)


    @mock.patch('space.lib.systemgroup.getDetails')
    @mock.patch('space.lib.activationkey.addServerGroups')
    def test_add_group_fail_dets(self, add_groups, get_dets):
        get_dets.return_value = {'id': 1}
        add_groups.return_value = 1
        args = [
            '--keyname', 'test',
            '--groups', 'it'
        ]
        add_groups.side_effect = Exception
        with self.assertRaises(Exception):
            activationkey.add_group(self.sw, args)
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

from space.lib import activationkey


class TestActivation(unittest.TestCase):

    def setUp(self):
        self.sw = mock.Mock()

    def test_addChildChannels(self):
        keyname = 'testkey'
        channels = ['MYBIGFATFAKECHANNEL']
        activationkey.addChildChannels(self.sw, keyname, channels)
        self.sw.session.activationkey.addChildChannels.\
            assert_called_with(
                self.sw.key,
                keyname,
                channels
            )

    def test_fail_addChildChannels(self):
        self.assertRaises(
            Exception,
            activationkey.addChildChannels,
            False,
            'test',
            False
        )

    def test_addConfigChannels(self):
        key = 'test'
        channellabels = ['test']
        addtotop = False
        activationkey.addConfigChannels(
            self.sw,
            key,
            channellabels,
            addtotop
        )
        self.sw.session.activationkey.addConfigChannels.\
            assert_called_with(
                self.sw.key,
                'test',
                ['test'],
                False
            )

    def test_fail_addConfigChannels(self):
        self.assertRaises(
            Exception,
            activationkey.addConfigChannels,
            False,
            'test',
            False,
            'test'
        )

    def test_addEntitlements(self):
        key = 'test'
        entitlement_label = 'test'
        activationkey.addEntitlements(
            self.sw,
            key,
            entitlement_label
        )
        self.sw.session.activationkey.addEntitlements.\
            assert_called_with(
                self.sw.key,
                'test',
                'test'
            )

    def test_fail_addEntitlements(self):
        self.assertRaises(
            Exception,
            activationkey.addEntitlements,
            False,
            'test',
            False)

    def test_addPackages(self):
        key = 'test'
        packages = [{}]
        activationkey.addPackages(
            self.sw,
            key,
            packages
        )
        self.sw.session.activationkey.addPackages.\
            assert_called_with(
                self.sw.key,
                'test',
                [{}]
            )

    def test_fail_addPackages(self):
        self.assertRaises(
            Exception,
            activationkey.addPackages,
            False,
            'test',
            False)

    def test_addServerGroups(self):
        keyname = 'testkey'
        groupid = 1
        activationkey.addServerGroups(self.sw, keyname, groupid)
        self.sw.session.activationkey.addServerGroups.\
            assert_called_with(self.sw.key, keyname, groupid)

    def test_fail_addServerGroups(self):
        self.assertRaises(
            Exception,
            activationkey.addServerGroups,
            'test',
            'test',
            'test'
        )

    def test_checkConfigDeployment(self):
        key = 'test'
        activationkey.checkConfigDeployment(
            self.sw,
            key
        )
        self.sw.session.activationkey.checkConfigDeployment.\
            assert_called_with(
                self.sw.key,
                'test')

    def test_fail_checkConfigDeployment(self):
        self.assertRaises(
            Exception,
            activationkey.checkConfigDeployment,
            False,
            'test')

    def test_create(self):
        keyname = 'testkey'
        description = 'blah'
        baseChannelLabel = 'base'
        activationkey.create(
            self.sw, keyname, description, baseChannelLabel, [], False)
        self.sw.session.activationkey.create.\
            assert_called_with(
                self.sw.key,
                keyname,
                description,
                baseChannelLabel,
                [],
                False
            )

    def test_create_fail(self):
        self.assertRaises(
            Exception,
            activationkey.create,
            'blah',
            'blah',
            'chan',
            [],
            True
        )

    def test_delete(self):
        keyname = 'testkey'
        activationkey.delete(
            self.sw,
            keyname
        )
        self.sw.session.activationkey.delete.\
            assert_called_with(
                self.sw.key,
                'testkey'
            )

    def test_fail_delete(self):
        self.assertRaises(
            Exception,
            activationkey.delete,
            False,
            'blah'
        )

    def test_disableConfigDeployment(self):
        keyname = 'testkey'
        activationkey.disableConfigDeployment(
            self.sw,
            keyname
        )
        self.sw.session.activationkey.disableConfigDeployment.\
            assert_called_with(
                self.sw.key,
                'testkey'
            )

    def test_fail_disableConfigDeployment(self):
        self.assertRaises(
            Exception,
            activationkey.disableConfigDeployment,
            False,
            'blah'
        )

    def test_enableConfigDeployment(self):
        keyname = 'testkey'
        activationkey.enableConfigDeployment(
            self.sw,
            keyname
        )
        self.sw.session.activationkey.enableConfigDeployment.\
            assert_called_with(
                self.sw.key,
                'testkey'
            )

    def test_fail_enableConfigDeployment(self):
        self.assertRaises(
            Exception,
            activationkey.enableConfigDeployment,
            False,
            'blah'
        )

    def test_getDetails(self):
        keyname = 'testkey'
        activationkey.getDetails(
            self.sw,
            keyname
        )
        self.sw.session.activationkey.getDetails.\
            assert_called_with(
                self.sw.key,
                'testkey'
            )

    def test_fail_getDetails(self):
        self.assertRaises(
            Exception,
            activationkey.getDetails,
            False,
            'blah'
        )

    def test_listActivatedSystems(self):
        keyname = 'testkey'
        activationkey.listActivatedSystems(
            self.sw,
            keyname
        )
        self.sw.session.activationkey.listActivatedSystems.\
            assert_called_with(
                self.sw.key,
                'testkey'
            )

    def test_fail_listActivatedSystems(self):
        self.assertRaises(
            Exception,
            activationkey.listActivatedSystems,
            False,
            'blah'
        )

    def test_listActivationKeys(self):
        activationkey.listActivationKeys(
            self.sw
        )
        self.sw.session.activationkey.listActivationKeys.\
            assert_called_with(
                self.sw.key
            )

    def test_fail_listActivationKeys(self):
        self.assertRaises(
            Exception,
            activationkey.listActivationKeys,
            False
        )

    def test_listConfigChannels(self):
        activationkey.listConfigChannels(
            self.sw,
            'test'
        )
        self.sw.session.activationkey.listConfigChannels.\
            assert_called_with(
                self.sw.key,
                'test'
            )

    def test_fail_listConfigChannels(self):
        self.assertRaises(
            Exception,
            activationkey.listConfigChannels,
            False,
            'test'
        )

    def test_removeChildChannels(self):
        activationkey.removeChildChannels(
            self.sw,
            'test',
            'test'
        )
        self.sw.session.activationkey.removeChildChannels.\
            assert_called_with(
                self.sw.key,
                'test',
                'test'
            )

    def test_fail_removeChildChannels(self):
        self.assertRaises(
            Exception,
            activationkey.removeChildChannels,
            False,
            'test',
            False
        )

    def test_removeConfigChannels(self):
        activationkey.removeConfigChannels(
            self.sw,
            ['test'],
            ['tests']
        )
        self.sw.session.activationkey.removeConfigChannels.\
            assert_called_with(
                self.sw.key,
                ['test'],
                ['tests']
            )

    def test_fail_removeConfigChannels(self):
        self.assertRaises(
            Exception,
            activationkey.removeConfigChannels,
            False,
            'test',
            False
        )

    def test_removeEntitlements(self):
        activationkey.removeEntitlements(
            self.sw,
            'test',
            ['tests']
        )
        self.sw.session.activationkey.removeEntitlements.\
            assert_called_with(
                self.sw.key,
                'test',
                ['tests']
            )

    def test_fail_removeEntitlements(self):
        self.assertRaises(
            Exception,
            activationkey.removeEntitlements,
            False,
            'test',
            []
        )

    def test_removePackages(self):
        activationkey.removePackages(
            self.sw,
            ['tests']
        )
        self.sw.session.activationkey.removePackages.\
            assert_called_with(
                self.sw.key,
                ['tests']
            )

    def test_fail_removePackages(self):
        self.assertRaises(
            Exception,
            activationkey.removePackages,
            False,
            'test'
        )

    def test_removeServerGroups(self):
        activationkey.removeServerGroups(
            self.sw,
            'tests',
            [1, 3, 5]
        )
        self.sw.session.activationkey.removeServerGroups.\
            assert_called_with(
                self.sw.key,
                'tests',
                [1, 3, 5]
            )

    def test_fail_removeServerGroups(self):
        self.assertRaises(
            Exception,
            activationkey.removeServerGroups,
            False,
            [1, 3, 5],
            'test'
        )

    def test_setConfigChannels(self):
        activationkey.setConfigChannels(
            self.sw,
            ['tests'],
            [1, 3, 5]
        )
        self.sw.session.activationkey.setConfigChannels.\
            assert_called_with(
                self.sw.key,
                ['tests'],
                [1, 3, 5]
            )

    def test_fail_setConfigChannels(self):
        self.assertRaises(
            Exception,
            activationkey.setConfigChannels,
            False,
            [1, 3, 5],
            'test'
        )

    def test_setDetails(self):
        activationkey.setDetails(
            self.sw,
            'tests',
            {'test': [1, 3, 5]}
        )
        self.sw.session.activationkey.setDetails.\
            assert_called_with(
                self.sw.key,
                'tests',
                {'test': [1, 3, 5]}
            )

    def test_fail_setDetails(self):
        self.assertRaises(
            Exception,
            activationkey.setDetails,
            False,
            [1, 3, 5],
            'test'
        )

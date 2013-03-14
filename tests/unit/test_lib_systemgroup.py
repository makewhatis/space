# -*- coding: utf-8 *-*
import sys
import os
import mock
if sys.version_info >= (3, 0):
    import xmlrpc.client
    xmlrpc = xmlrpc.client
    import unittest

if sys.version_info <= (2, 8):
    import unittest2 as unittest
    import xmlrpclib
    xmlrpc = xmlrpclib

import coverage

sys.path.insert(0, "../../")

from space.lib import systemgroup


class TestSystemGroup(unittest.TestCase):

    def setUp(self):
        self.sw = mock.Mock()

    def test_addOrRemoveAdmins(self):
        systemgroup.addOrRemoveAdmins(
            self.sw,
            'sysgroup',
            ['user'],
            1
        )
        self.sw.session.systemgroup.addOrRemoveAdmins.\
            assert_called_with(
                self.sw.key,
                'sysgroup',
                ['user'],
                1
            )

    def test_fail_addOrRemoveAdmins(self):
        self.assertRaises(
            Exception,
            systemgroup.addOrRemoveAdmins,
            False,
            'sysgroup',
            ['user'],
            1
        )

    def test_addOrRemoveSystems(self):
        systemgroup.addOrRemoveSystems(
            self.sw,
            'sysgroup',
            [1],
            1
        )
        self.sw.session.systemgroup.addOrRemoveSystems.\
            assert_called_with(
                self.sw.key,
                'sysgroup',
                [1],
                1
            )

    def test_fail_addOrRemoveSystems(self):
        self.assertRaises(
            Exception,
            systemgroup.addOrRemoveSystems,
            False,
            'sysgroup',
            [1],
            1
        )

    def test_create(self):
        systemgroup.create(
            self.sw,
            'name',
            'description'
        )
        self.sw.session.systemgroup.create.\
            assert_called_with(
                self.sw.key,
                'name',
                'description'
            )

    def test_fail_create(self):
        self.assertRaises(
            Exception,
            systemgroup.create,
            False,
            'name',
            'description'
        )

    def test_delete(self):
        systemgroup.delete(
            self.sw,
            'name'
        )
        self.sw.session.systemgroup.delete.\
            assert_called_with(
                self.sw.key,
                'name'
            )

    def test_fail_delete(self):
        self.assertRaises(
            Exception,
            systemgroup.delete,
            False,
            'name'
        )

    def test_getDetails(self):
        systemgroup.getDetails(
            self.sw,
            'system_group'
        )
        self.sw.session.systemgroup.getDetails.\
            assert_called_with(
                self.sw.key,
                'system_group'
            )

    def test_fail_getDetails(self):
        self.assertRaises(
            Exception,
            systemgroup.getDetails,
            False,
            'system_group'
        )

    def test_listActiveSystemsInGroup(self):
        systemgroup.listActiveSystemsInGroup(
            self.sw,
            'system_group'
        )
        self.sw.session.systemgroup.listActiveSystemsInGroup.\
            assert_called_with(
                self.sw.key,
                'system_group'
            )

    def test_fail_listActiveSystemsInGroup(self):
        self.assertRaises(
            Exception,
            systemgroup.listActiveSystemsInGroup,
            False,
            'system_group'
        )

    def test_listAdministrators(self):
        systemgroup.listAdministrators(
            self.sw,
            'system_group'
        )
        self.sw.session.systemgroup.listAdministrators.\
            assert_called_with(
                self.sw.key,
                'system_group'
            )

    def test_fail_listAdministrators(self):
        self.assertRaises(
            Exception,
            systemgroup.listAdministrators,
            False,
            'system_group'
        )

    def test_listAllGroups(self):
        systemgroup.listAllGroups(
            self.sw
        )
        self.sw.session.systemgroup.listAllGroups.\
            assert_called_with(
                self.sw.key
            )

    def test_fail_listAllGroups(self):
        self.assertRaises(
            Exception,
            systemgroup.listAllGroups,
            False
        )

    def test_listGroupsWithNoAssociatedAdmins(self):
        systemgroup.listGroupsWithNoAssociatedAdmins(
            self.sw
        )
        self.sw.session.systemgroup.listGroupsWithNoAssociatedAdmins.\
            assert_called_with(
                self.sw.key
            )

    def test_fail_listGroupsWithNoAssociatedAdmins(self):
        self.assertRaises(
            Exception,
            systemgroup.listGroupsWithNoAssociatedAdmins,
            False
        )

    def test_listInactiveSystemsInGroup(self):
        systemgroup.listInactiveSystemsInGroup(
            self.sw,
            'system_group'
        )
        self.sw.session.systemgroup.listInactiveSystemsInGroup.\
            assert_called_with(
                self.sw.key,
                'system_group'
            )
        systemgroup.listInactiveSystemsInGroup(
            self.sw,
            'system_group',
            days_inactive=1
        )
        self.sw.session.systemgroup.listInactiveSystemsInGroup.\
            assert_called_with(
                self.sw.key,
                'system_group',
                1
            )

    def test_fail_listInactiveSystemsInGroup(self):
        self.assertRaises(
            Exception,
            systemgroup.listInactiveSystemsInGroup,
            False,
            'system_group'
        )

    def test_listSystems(self):
        systemgroup.listSystems(
            self.sw,
            'system_group'
        )
        self.sw.session.systemgroup.listSystems.\
            assert_called_with(
                self.sw.key,
                'system_group'
            )

    def test_fail_listSystems(self):
        self.assertRaises(
            Exception,
            systemgroup.listSystems,
            False,
            'system_group'
        )

    def test_scheduleApplyErrataToActive(self):
        systemgroup.scheduleApplyErrataToActive(
            self.sw,
            'system_group',
            1,
            date_time='now'
        )
        self.sw.session.systemgroup.scheduleApplyErrataToActive.\
            assert_called_with(
                self.sw.key,
                'system_group',
                1,
                'now'
            )
        systemgroup.scheduleApplyErrataToActive(
            self.sw,
            'system_group',
            1
        )
        self.sw.session.systemgroup.scheduleApplyErrataToActive.\
            assert_called_with(
                self.sw.key,
                'system_group',
                1
            )

    def test_fail_scheduleApplyErrataToActive(self):
        self.assertRaises(
            Exception,
            systemgroup.scheduleApplyErrataToActive,
            False,
            'system_group',
            1,
            date_time='now'
        )

    def test_update(self):
        systemgroup.update(
            self.sw,
            'system_group',
            'description'
        )
        self.sw.session.systemgroup.update.\
            assert_called_with(
                self.sw.key,
                'system_group',
                'description'
            )

    def test_fail_update(self):
        self.assertRaises(
            Exception,
            systemgroup.update,
            False,
            'system_group',
            'description'
        )

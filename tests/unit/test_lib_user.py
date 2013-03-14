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

from space.lib import user


class TestUser(unittest.TestCase):

    def setUp(self):
        self.sw = mock.Mock()

    def test_addAssignedSystemGroup(self):
        user.addAssignedSystemGroup(
            self.sw,
            'login',
            'server_group_name',
            True
        )
        self.sw.session.user.addAssignedSystemGroup.\
            assert_called_with(
                self.sw.key,
                'login',
                'server_group_name',
                True
            )

    def test_fail_addAssignedSystemGroup(self):
        self.assertRaises(
            Exception,
            user.addAssignedSystemGroup,
            False,
            'login',
            'server_group_name',
            True
        )

    def test_addAssignedSystemGroups(self):
        user.addAssignedSystemGroups(
            self.sw,
            'login',
            'server_group_name',
            True
        )
        self.sw.session.user.addAssignedSystemGroups.\
            assert_called_with(
                self.sw.key,
                'login',
                'server_group_name',
                True
            )

    def test_fail_addAssignedSystemGroups(self):
        self.assertRaises(
            Exception,
            user.addAssignedSystemGroups,
            False,
            'login',
            'server_group_name',
            True
        )

    def test_addDefaultSystemGroup(self):
        user.addDefaultSystemGroup(
            self.sw,
            'login',
            'server_group_name'
        )
        self.sw.session.user.addDefaultSystemGroup.\
            assert_called_with(
                self.sw.key,
                'login',
                'server_group_name'
            )

    def test_fail_addDefaultSystemGroup(self):
        self.assertRaises(
            Exception,
            user.addDefaultSystemGroup,
            False,
            'login',
            'server_group_name'
        )

    def test_addDefaultSystemGroups(self):
        user.addDefaultSystemGroups(
            self.sw,
            'login',
            'server_group_name'
        )
        self.sw.session.user.addDefaultSystemGroups.\
            assert_called_with(
                self.sw.key,
                'login',
                'server_group_name'
            )

    def test_fail_addDefaultSystemGroups(self):
        self.assertRaises(
            Exception,
            user.addDefaultSystemGroups,
            False,
            'login',
            'server_group_name'
        )

    def test_addRole(self):
        user.addRole(
            self.sw,
            'login',
            'role'
        )
        self.sw.session.user.addRole.\
            assert_called_with(
                self.sw.key,
                'login',
                'role'
            )

    def test_fail_addRole(self):
        self.assertRaises(
            Exception,
            user.addRole,
            False,
            'login',
            'role'
        )

    def test_create(self):
        user.create(
            self.sw,
            'login',
            'password',
            'first_name',
            'last_name',
            'email',
            1
        )
        self.sw.session.user.create.\
            assert_called_with(
                self.sw.key,
                'login',
                'password',
                'first_name',
                'last_name',
                'email',
                1
            )
        user.create(
            self.sw,
            'login',
            'password',
            'first_name',
            'last_name',
            'email'
        )
        self.sw.session.user.create.\
            assert_called_with(
                self.sw.key,
                'login',
                'password',
                'first_name',
                'last_name',
                'email'
            )

    def test_fail_create(self):
        self.assertRaises(
            Exception,
            user.create,
            False,
            'login',
            'password',
            'first_name',
            'last_name',
            'email',
            1
        )

    def test_delete(self):
        user.delete(
            self.sw,
            'login'
        )
        self.sw.session.user.delete.\
            assert_called_with(
                self.sw.key,
                'login'
            )

    def test_fail_delete(self):
        self.assertRaises(
            Exception,
            user.delete,
            False,
            'login'
        )

    def test_disable(self):
        user.disable(
            self.sw,
            'login'
        )
        self.sw.session.user.disable.\
            assert_called_with(
                self.sw.key,
                'login'
            )

    def test_fail_disable(self):
        self.assertRaises(
            Exception,
            user.disable,
            False,
            'login'
        )

    def test_enable(self):
        user.enable(
            self.sw,
            'login'
        )
        self.sw.session.user.enable.\
            assert_called_with(
                self.sw.key,
                'login'
            )

    def test_fail_enable(self):
        self.assertRaises(
            Exception,
            user.enable,
            False,
            'login'
        )

    def test_getDetails(self):
        user.getDetails(
            self.sw,
            'login'
        )
        self.sw.session.user.getDetails.\
            assert_called_with(
                self.sw.key,
                'login'
            )

    def test_fail_getDetails(self):
        self.assertRaises(
            Exception,
            user.getDetails,
            False,
            'login'
        )

    def test_getLoggedInTime(self):
        user.getLoggedInTime(
            self.sw,
            'login'
        )
        self.sw.session.user.getLoggedInTime.\
            assert_called_with(
                self.sw.key,
                'login'
            )

    def test_fail_getLoggedInTime(self):
        self.assertRaises(
            Exception,
            user.getLoggedInTime,
            False,
            'login'
        )

    def test_listAssignableRoles(self):
        user.listAssignableRoles(
            self.sw
        )
        self.sw.session.user.listAssignableRoles.\
            assert_called_with(
                self.sw.key
            )

    def test_fail_listAssignableRoles(self):
        self.assertRaises(
            Exception,
            user.listAssignableRoles,
            False
        )

    def test_listAssignedSystemGroups(self):
        user.listAssignedSystemGroups(
            self.sw,
            'login'
        )
        self.sw.session.user.listAssignedSystemGroups.\
            assert_called_with(
                self.sw.key,
                'login'
            )

    def test_fail_listAssignedSystemGroups(self):
        self.assertRaises(
            Exception,
            user.listAssignedSystemGroups,
            False,
            'login'
        )

    def test_listDefaultSystemGroups(self):
        user.listDefaultSystemGroups(
            self.sw,
            'login'
        )
        self.sw.session.user.listDefaultSystemGroups.\
            assert_called_with(
                self.sw.key,
                'login'
            )

    def test_fail_listDefaultSystemGroups(self):
        self.assertRaises(
            Exception,
            user.listDefaultSystemGroups,
            False,
            'login'
        )

    def test_listRoles(self):
        user.listRoles(
            self.sw,
            'login'
        )
        self.sw.session.user.listRoles.\
            assert_called_with(
                self.sw.key,
                'login'
            )

    def test_fail_listRoles(self):
        self.assertRaises(
            Exception,
            user.listRoles,
            False,
            'login'
        )

    def test_listUsers(self):
        user.listUsers(
            self.sw
        )
        self.sw.session.user.listUsers.\
            assert_called_with(
                self.sw.key
            )

    def test_fail_listUsers(self):
        self.assertRaises(
            Exception,
            user.listUsers,
            False
        )

    def test_removeAssignedSystemGroup(self):
        user.removeAssignedSystemGroup(
            self.sw,
            'login',
            'server_group_name',
            False
        )
        self.sw.session.user.removeAssignedSystemGroup.\
            assert_called_with(
                self.sw.key,
                'login',
                'server_group_name',
                False
            )

    def test_fail_removeAssignedSystemGroup(self):
        self.assertRaises(
            Exception,
            user.removeAssignedSystemGroup,
            False,
            'login',
            'server_group_name',
            False
        )

    def test_removeAssignedSystemGroups(self):
        user.removeAssignedSystemGroups(
            self.sw,
            'login',
            ['server_group_name'],
            False
        )
        self.sw.session.user.removeAssignedSystemGroups.\
            assert_called_with(
                self.sw.key,
                'login',
                ['server_group_name'],
                False
            )

    def test_fail_removeAssignedSystemGroups(self):
        self.assertRaises(
            Exception,
            user.removeAssignedSystemGroups,
            False,
            'login',
            ['server_group_name'],
            False
        )

    def test_removeDefaultSystemGroup(self):
        user.removeDefaultSystemGroup(
            self.sw,
            'login',
            'server_group_name'
        )
        self.sw.session.user.removeDefaultSystemGroup.\
            assert_called_with(
                self.sw.key,
                'login',
                'server_group_name'
            )

    def test_fail_removeDefaultSystemGroup(self):
        self.assertRaises(
            Exception,
            user.removeDefaultSystemGroup,
            False,
            'login',
            'server_group_name'
        )

    def test_removeDefaultSystemGroups(self):
        user.removeDefaultSystemGroups(
            self.sw,
            'login',
            'server_group_name'
        )
        self.sw.session.user.removeDefaultSystemGroups.\
            assert_called_with(
                self.sw.key,
                'login',
                'server_group_name'
            )

    def test_fail_removeDefaultSystemGroups(self):
        self.assertRaises(
            Exception,
            user.removeDefaultSystemGroups,
            False,
            'login',
            'server_group_name'
        )

    def test_removeRole(self):
        user.removeRole(
            self.sw,
            'login',
            'role'
        )
        self.sw.session.user.removeRole.\
            assert_called_with(
                self.sw.key,
                'login',
                'role'
            )

    def test_fail_removeRole(self):
        self.assertRaises(
            Exception,
            user.removeRole,
            False,
            'login',
            'role'
        )

    def test_setDetails(self):
        user.setDetails(
            self.sw,
            'login',
            {'user_details': 'yessir'}
        )
        self.sw.session.user.setDetails.\
            assert_called_with(
                self.sw.key,
                'login',
                {'user_details': 'yessir'}
            )

    def test_fail_setDetails(self):
        self.assertRaises(
            Exception,
            user.setDetails,
            False,
            'login',
            {'user_details': 'yessir'}
        )

    def test_usePamAuthentication(self):
        user.usePamAuthentication(
            self.sw,
            'login',
            1
        )
        self.sw.session.user.usePamAuthentication.\
            assert_called_with(
                self.sw.key,
                'login',
                1
            )

    def test_fail_usePamAuthentication(self):
        self.assertRaises(
            Exception,
            user.usePamAuthentication,
            False,
            'login',
            1
        )

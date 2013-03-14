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

from space.lib import org
from space.lib.org import trusts as org_trusts


class TestOrg(unittest.TestCase):

    def setUp(self):
        self.sw = mock.Mock()

    def test_create(self):
        org.create(
            self.sw,
            'orgname',
            'adminlogin',
            'adminpassword',
            'prefix',
            'firstname',
            'lastname',
            'email',
            'usepamauth'
        )
        self.sw.session.org.create.\
            assert_called_with(
                self.sw.key,
                'orgname',
                'adminlogin',
                'adminpassword',
                'prefix',
                'firstname',
                'lastname',
                'email',
                'usepamauth'
            )

    def test_fail_create(self):
        self.assertRaises(
            Exception,
            org.create,
            False,
            'orgname',
            'adminlogin',
            'adminpassword',
            'prefix',
            'firstname',
            'lastname',
            'email',
            'usepamauth'
        )

    def test_delete(self):
        org.delete(
            self.sw,
            'orgid'
        )
        self.sw.session.org.delete.\
            assert_called_with(
                self.sw.key,
                'orgid'
            )

    def test_fail_delete(self):
        self.assertRaises(
            Exception,
            org.delete,
            False,
            'orgid'
        )

    def test_getDetails(self):
        org.getDetails(
            self.sw,
            'orgid'
        )
        self.sw.session.org.getDetails.\
            assert_called_with(
                self.sw.key,
                'orgid'
            )

    def test_fail_getDetails(self):
        self.assertRaises(
            Exception,
            org.getDetails,
            False,
            'orgid'
        )

    def test_listOrgs(self):
        org.listOrgs(
            self.sw
        )
        self.sw.session.org.listOrgs.\
            assert_called_with(
                self.sw.key
            )

    def test_fail_listOrgs(self):
        self.assertRaises(
            Exception,
            org.listOrgs,
            False,
        )

    def test_listSoftwareEntitlements(self):
        org.listSoftwareEntitlements(
            self.sw
        )
        self.sw.session.org.listSoftwareEntitlements.\
            assert_called_with(
                self.sw.key
            )
        org.listSoftwareEntitlements(
            self.sw,
            label='label',
            includeunentitled='includeunentitled'
        )
        self.sw.session.org.listSoftwareEntitlements.\
            assert_called_with(
                self.sw.key,
                'label',
                'includeunentitled'
            )

    def test_fail_listSoftwareEntitlements(self):
        self.assertRaises(
            Exception,
            org.listSoftwareEntitlements,
            False
        )
        self.assertRaises(
            Exception,
            org.listSoftwareEntitlements,
            False,
            label='label',
            includeunentitled='includeunentitled'
        )

    def test_listSoftwareEntitlementsForOrg(self):
        org.listSoftwareEntitlementsForOrg(
            self.sw,
            'orgid'
        )
        self.sw.session.org.listSoftwareEntitlementsForOrg.\
            assert_called_with(
                self.sw.key,
                'orgid'
            )

    def test_fail_listSoftwareEntitlementsForOrg(self):
        self.assertRaises(
            Exception,
            org.listSoftwareEntitlementsForOrg,
            False,
            'orgid'
        )

    def test_listSystemEntitlements(self):
        org.listSystemEntitlements(
            self.sw
        )
        self.sw.session.org.listSystemEntitlements.\
            assert_called_with(
                self.sw.key
            )
        org.listSystemEntitlements(
            self.sw,
            label='label'
        )
        self.sw.session.org.listSystemEntitlements.\
            assert_called_with(
                self.sw.key,
                'label'
            )
        org.listSystemEntitlements(
            self.sw,
            label='label',
            includeunentitled='includeunentitled'
        )
        self.sw.session.org.listSystemEntitlements.\
            assert_called_with(
                self.sw.key,
                'label',
                'includeunentitled'
            )

    def test_fail_listSystemEntitlements(self):
        self.assertRaises(
            Exception,
            org.listSystemEntitlements,
            False,
        )
        self.assertRaises(
            Exception,
            org.listSystemEntitlements,
            False,
            label='label'
        )
        self.assertRaises(
            Exception,
            org.listSystemEntitlements,
            False,
            label='label',
            includeunentitled='includeunentitled'
        )

    def test_listSystemEntitlementsForOrg(self):
        org.listSystemEntitlementsForOrg(
            self.sw,
            'orgid'
        )
        self.sw.session.org.listSystemEntitlementsForOrg.\
            assert_called_with(
                self.sw.key,
                'orgid'
            )

    def test_fail_listSystemEntitlementsForOrg(self):
        self.assertRaises(
            Exception,
            org.listSystemEntitlementsForOrg,
            False,
            'orgid'
        )

    def test_listUsers(self):
        org.listUsers(
            self.sw,
            'orgid'
        )
        self.sw.session.org.listUsers.\
            assert_called_with(
                self.sw.key,
                'orgid'
            )

    def test_fail_listUsers(self):
        self.assertRaises(
            Exception,
            org.listUsers,
            False,
            'orgid'
        )

    def test_migrateSystems(self):
        org.migrateSystems(
            self.sw,
            'orgid',
            'system_ids'
        )
        self.sw.session.org.migrateSystems.\
            assert_called_with(
                self.sw.key,
                'orgid',
                'system_ids'
            )

    def test_fail_migrateSystems(self):
        self.assertRaises(
            Exception,
            org.migrateSystems,
            False,
            'orgid',
            'system_ids'
        )

    def test_setSoftwareEntitlements(self):
        org.setSoftwareEntitlements(
            self.sw,
            'orgid',
            'label',
            'allocation'
        )
        self.sw.session.org.setSoftwareEntitlements.\
            assert_called_with(
                self.sw.key,
                'orgid',
                'label',
                'allocation'
            )

    def test_fail_setSoftwareEntitlements(self):
        self.assertRaises(
            Exception,
            org.setSoftwareEntitlements,
            False,
            'orgid',
            'label',
            'allocation'
        )

    def test_setSoftwareFlexEntitlements(self):
        org.setSoftwareFlexEntitlements(
            self.sw,
            'orgid',
            'label',
            'allocation'
        )
        self.sw.session.org.setSoftwareFlexEntitlements.\
            assert_called_with(
                self.sw.key,
                'orgid',
                'label',
                'allocation'
            )

    def test_fail_setSoftwareFlexEntitlements(self):
        self.assertRaises(
            Exception,
            org.setSoftwareFlexEntitlements,
            False,
            'orgid',
            'label',
            'allocation'
        )

    def test_setSystemEntitlements(self):
        org.setSystemEntitlements(
            self.sw,
            'orgid',
            'label',
            'allocation'
        )
        self.sw.session.org.setSystemEntitlements.\
            assert_called_with(
                self.sw.key,
                'orgid',
                'label',
                'allocation'
            )

    def test_fail_setSystemEntitlements(self):
        self.assertRaises(
            Exception,
            org.setSystemEntitlements,
            False,
            'orgid',
            'label',
            'allocation'
        )

    def test_updateName(self):
        org.updateName(
            self.sw,
            'orgid',
            'name'
        )
        self.sw.session.org.updateName.\
            assert_called_with(
                self.sw.key,
                'orgid',
                'name'
            )

    def test_fail_updateName(self):
        self.assertRaises(
            Exception,
            org.updateName,
            False,
            'orgid',
            'name'
        )


class TestOrgTrust(unittest.TestCase):

    def setUp(self):
        self.sw = mock.Mock()

    def test_addTrust(self):
        org_trusts.addTrust(
            self.sw,
            'orgid',
            'trust_org_id'
        )
        self.sw.session.org.trusts.addTrust.\
            assert_called_with(
                self.sw.key,
                'orgid',
                'trust_org_id'
            )

    def test_fail_addTrust(self):
        self.assertRaises(
            Exception,
            org_trusts.addTrust,
            False,
            'orgid',
            'trust_org_id'
        )

    def test_getDetails(self):
        org_trusts.getDetails(
            self.sw,
            'trust_org_id'
        )
        self.sw.session.org.trusts.getDetails.\
            assert_called_with(
                self.sw.key,
                'trust_org_id'
            )

    def test_fail_getDetails(self):
        self.assertRaises(
            Exception,
            org_trusts.getDetails,
            False,
            'trust_org_id'
        )

    def test_listChannelsConsumed(self):
        org_trusts.listChannelsConsumed(
            self.sw,
            'trust_org_id'
        )
        self.sw.session.org.trusts.listChannelsConsumed.\
            assert_called_with(
                self.sw.key,
                'trust_org_id'
            )

    def test_fail_listChannelsConsumed(self):
        self.assertRaises(
            Exception,
            org_trusts.listChannelsConsumed,
            False,
            'trust_org_id'
        )

    def test_listChannelsProvided(self):
        org_trusts.listChannelsProvided(
            self.sw,
            'trust_org_id'
        )
        self.sw.session.org.trusts.listChannelsProvided.\
            assert_called_with(
                self.sw.key,
                'trust_org_id'
            )

    def test_fail_listChannelsProvided(self):
        self.assertRaises(
            Exception,
            org_trusts.listChannelsProvided,
            False,
            'trust_org_id'
        )

    def test_listOrgs(self):
        org_trusts.listOrgs(
            self.sw
        )
        self.sw.session.org.trusts.listOrgs.\
            assert_called_with(
                self.sw.key
            )

    def test_fail_listOrgs(self):
        self.assertRaises(
            Exception,
            org_trusts.listOrgs,
            False,
        )

    def test_listSystemsAffected(self):
        org_trusts.listSystemsAffected(
            self.sw,
            'orgid',
            'trust_org_id'
        )
        self.sw.session.org.trusts.listSystemsAffected.\
            assert_called_with(
                self.sw.key,
                'orgid',
                'trust_org_id'
            )

    def test_fail_listSystemsAffected(self):
        self.assertRaises(
            Exception,
            org_trusts.listSystemsAffected,
            False,
            'orgid',
            'trust_org_id'
        )

    def test_listTrusts(self):
        org_trusts.listTrusts(
            self.sw,
            'orgid'
        )
        self.sw.session.org.trusts.listTrusts.\
            assert_called_with(
                self.sw.key,
                'orgid'
            )

    def test_fail_listTrusts(self):
        self.assertRaises(
            Exception,
            org_trusts.listTrusts,
            False,
            'orgid'
        )

    def test_removeTrust(self):
        org_trusts.removeTrust(
            self.sw,
            'orgid',
            'trust_org_id'
        )
        self.sw.session.org.trusts.removeTrust.\
            assert_called_with(
                self.sw.key,
                'orgid',
                'trust_org_id'
            )

    def test_fail_removeTrust(self):
        self.assertRaises(
            Exception,
            org_trusts.removeTrust,
            False,
            'orgid',
            'trust_org_id'
        )

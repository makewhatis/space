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

from space.lib import packages
from space.lib.packages import provider as packages_provider
from space.lib.packages import search as packages_search


class TestPackages(unittest.TestCase):

    def setUp(self):
        self.sw = mock.Mock()

    def test_findByNvrea(self):
        packages.findByNvrea(
            self.sw,
            'name',
            'version',
            'release',
            'epoch',
            'arch_label'
        )
        self.sw.session.packages.findByNvrea.\
            assert_called_with(
                self.sw.key,
                'name',
                'version',
                'release',
                'epoch',
                'arch_label'
            )

    def test_fail_findByNvrea(self):
        self.assertRaises(
            Exception,
            packages.findByNvrea,
            False,
            'name',
            'version',
            'release',
            'epoch',
            'arch_label'
        )

    def test_getDetails(self):
        packages.getDetails(
            self.sw,
            'package_id'
        )
        self.sw.session.packages.getDetails.\
            assert_called_with(
                self.sw.key,
                'package_id'
            )

    def test_fail_getDetails(self):
        self.assertRaises(
            Exception,
            packages.getDetails,
            False,
            'package_id'
        )

    def test_getPackage(self):
        packages.getPackage(
            self.sw,
            'package_id'
        )
        self.sw.session.packages.getPackage.\
            assert_called_with(
                self.sw.key,
                'package_id'
            )

    def test_fail_getPackage(self):
        self.assertRaises(
            Exception,
            packages.getPackage,
            False,
            'package_id'
        )

    def test_getPackageUrl(self):
        packages.getPackageUrl(
            self.sw,
            1
        )
        self.sw.session.packages.getPackageUrl.\
            assert_called_with(
                self.sw.key,
                1
            )

    def test_fail_getPackageUrl(self):
        self.assertRaises(
            Exception,
            packages.getPackageUrl,
            False,
            'package_id'
        )

    def test_listChangelog(self):
        packages.listChangelog(
            self.sw,
            'package_id'
        )
        self.sw.session.packages.listChangelog.\
            assert_called_with(
                self.sw.key,
                'package_id'
            )

    def test_fail_listChangelog(self):
        self.assertRaises(
            Exception,
            packages.listChangelog,
            False,
            'package_id'
        )

    def test_listDependencies(self):
        packages.listDependencies(
            self.sw,
            'package_id'
        )
        self.sw.session.packages.listDependencies.\
            assert_called_with(
                self.sw.key,
                'package_id'
            )

    def test_fail_listDependencies(self):
        self.assertRaises(
            Exception,
            packages.listDependencies,
            False,
            'package_id'
        )

    def test_listFiles(self):
        packages.listFiles(
            self.sw,
            'package_id'
        )
        self.sw.session.packages.listFiles.\
            assert_called_with(
                self.sw.key,
                'package_id'
            )

    def test_fail_listFiles(self):
        self.assertRaises(
            Exception,
            packages.listFiles,
            False,
            'package_id'
        )

    def test_listProvidingChannels(self):
        packages.listProvidingChannels(
            self.sw,
            'package_id'
        )
        self.sw.session.packages.listProvidingChannels.\
            assert_called_with(
                self.sw.key,
                'package_id'
            )

    def test_fail_listProvidingChannels(self):
        self.assertRaises(
            Exception,
            packages.listProvidingChannels,
            False,
            'package_id'
        )

    def test_listProvidingErrata(self):
        packages.listProvidingErrata(
            self.sw,
            'package_id'
        )
        self.sw.session.packages.listProvidingErrata.\
            assert_called_with(
                self.sw.key,
                'package_id'
            )

    def test_fail_listProvidingErrata(self):
        self.assertRaises(
            Exception,
            packages.listProvidingErrata,
            False,
            'package_id'
        )

    def test_removePackage(self):
        packages.removePackage(
            self.sw,
            'package_id'
        )
        self.sw.session.packages.removePackage.\
            assert_called_with(
                self.sw.key,
                'package_id'
            )

    def test_fail_removePackage(self):
        self.assertRaises(
            Exception,
            packages.removePackage,
            False,
            'package_id'
        )


class TestPackagesProvider(unittest.TestCase):

    def setUp(self):
        self.sw = mock.Mock()

    def test_associateKey(self):
        packages_provider.associateKey(
            self.sw,
            'provider_name',
            'key',
            'keytype'
        )
        self.sw.session.packages.provider.associateKey.\
            assert_called_with(
                self.sw.key,
                'provider_name',
                'key',
                'keytype'
            )

    def test_fail_associateKey(self):
        self.assertRaises(
            Exception,
            packages_provider.associateKey,
            False,
            'provider_name',
            'key',
            'keytype'
        )

    def test_list(self):
        packages_provider.list(
            self.sw
        )
        self.sw.session.packages.provider.list.\
            assert_called_with(
                self.sw.key
            )

    def test_fail_list(self):
        self.assertRaises(
            Exception,
            packages_provider.list,
            False,
        )

    def test_listKeys(self):
        packages_provider.listKeys(
            self.sw,
            'provider_name'
        )
        self.sw.session.packages.provider.listKeys.\
            assert_called_with(
                self.sw.key,
                'provider_name'
            )

    def test_fail_listKeys(self):
        self.assertRaises(
            Exception,
            packages_provider.listKeys,
            False,
            'provider_name'
        )


class TestPackagesSearch(unittest.TestCase):

    def setUp(self):
        self.sw = mock.Mock()

    def test_advanced(self):
        packages_search.advanced(
            self.sw,
            'name:kernel AND version:2.6.18 AND description:devel'
        )
        self.sw.session.packages.search.advanced.\
            assert_called_with(
                self.sw.key,
                'name:kernel AND version:2.6.18 AND description:devel'
            )

    def test_fail_advanced(self):
        self.assertRaises(
            Exception,
            packages_search.advanced,
            False,
            'name:kernel AND version:2.6.18 AND description:devel'
        )

    def test_advancedWithActKey(self):
        packages_search.advancedWithActKey(
            self.sw,
            'name:kernel AND version:2.6.18 AND description:devel',
            'actkey'
        )
        self.sw.session.packages.search.advancedWithActKey.\
            assert_called_with(
                self.sw.key,
                'name:kernel AND version:2.6.18 AND description:devel',
                'actkey'
            )

    def test_fail_advancedWithActKey(self):
        self.assertRaises(
            Exception,
            packages_search.advancedWithActKey,
            False,
            'name:kernel AND version:2.6.18 AND description:devel',
            'actkey'
        )

    def test_advancedWithChannel(self):
        packages_search.advancedWithChannel(
            self.sw,
            'name:kernel AND version:2.6.18 AND description:devel',
            'channel'
        )
        self.sw.session.packages.search.advancedWithChannel.\
            assert_called_with(
                self.sw.key,
                'name:kernel AND version:2.6.18 AND description:devel',
                'channel'
            )

    def test_fail_advancedWithChannel(self):
        self.assertRaises(
            Exception,
            packages_search.advancedWithChannel,
            False,
            'name:kernel AND version:2.6.18 AND description:devel',
            'channel'
        )

    def test_name(self):
        packages_search.name(
            self.sw,
            'name',
        )
        self.sw.session.packages.search.name.\
            assert_called_with(
                self.sw.key,
                'name'
            )

    def test_fail_name(self):
        self.assertRaises(
            Exception,
            packages_search.name,
            False,
            'name'
        )

    def test_nameAndDescription(self):
        packages_search.nameAndDescription(
            self.sw,
            'name:kernel AND description:devel'
        )
        self.sw.session.packages.search.nameAndDescription.\
            assert_called_with(
                self.sw.key,
                'name:kernel AND description:devel'
            )

    def test_fail_nameAndDescription(self):
        self.assertRaises(
            Exception,
            packages_search.nameAndDescription,
            False,
            'name:kernel AND description:devel'
        )

    def test_nameAndSummary(self):
        packages_search.nameAndSummary(
            self.sw,
            'name:kernel AND summary:devel'
        )
        self.sw.session.packages.search.nameAndSummary.\
            assert_called_with(
                self.sw.key,
                'name:kernel AND summary:devel'
            )

    def test_fail_nameAndSummary(self):
        self.assertRaises(
            Exception,
            packages_search.nameAndSummary,
            False,
            'name:kernel AND summary:devel'
        )

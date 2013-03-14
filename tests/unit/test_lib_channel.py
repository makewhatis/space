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
from space.lib import channel
from space.lib.channel import access
from space.lib.channel import org
from space.lib.channel import software

sys.path.insert(0, "../../")


class TestChannel(unittest.TestCase):

    def setUp(self):
        self.sw = mock.Mock()

    def test_listAllChannels(self):
        channel.listAllChannels(self.sw)
        self.sw.session.channel.listAllChannels.\
            assert_called_with(
                self.sw.key)

    def test_fail_listAllChannels(self):
        self.assertRaises(
            Exception,
            channel.listAllChannels,
            False)

    def test_listMyChannels(self):
        channel.listMyChannels(self.sw)
        self.sw.session.channel.listMyChannels.\
            assert_called_with(
                self.sw.key)

    def test_fail_listMyChannels(self):
        self.assertRaises(
            Exception,
            channel.listMyChannels,
            False)

    def test_listPopularChannels(self):
        popcount = 'test'
        channel.listPopularChannels(self.sw, popcount)
        self.sw.session.channel.listPopularChannels.\
            assert_called_with(
                self.sw.key, 'test')

    def test_fail_listPopularChannels(self):
        self.assertRaises(
            Exception,
            channel.listPopularChannels,
            False,
            'test')

    def test_listRetiredChannels(self):
        channel.listRetiredChannels(self.sw)
        self.sw.session.channel.listRetiredChannels.\
            assert_called_with(
                self.sw.key)

    def test_fail_listRetiredChannels(self):
        self.assertRaises(
            Exception,
            channel.listRetiredChannels,
            False)

    def test_listSharedChannels(self):
        channel.listSharedChannels(self.sw)
        self.sw.session.channel.listSharedChannels.\
            assert_called_with(
                self.sw.key)

    def test_fail_listSharedChannels(self):
        self.assertRaises(
            Exception,
            channel.listSharedChannels,
            False)

    def test_listSoftwareChannels(self):
        channel.listSoftwareChannels(self.sw)
        self.sw.session.channel.listSoftwareChannels.\
            assert_called_with(
                self.sw.key)

    def test_fail_listSoftwareChannels(self):
        self.assertRaises(
            Exception,
            channel.listSoftwareChannels,
            False)

    def test_listVendorChannels(self):
        channel.listVendorChannels(self.sw)
        self.sw.session.channel.listVendorChannels.\
            assert_called_with(
                self.sw.key)

    def test_fail_listVendorChannels(self):
        self.assertRaises(
            Exception,
            channel.listVendorChannels,
            False)


class TestChannelAccess(unittest.TestCase):

    def setUp(self):
        self.sw = mock.Mock()

    def test_disableUserRestrictions(self):
        channellabel = 'test'
        access.disableUserRestrictions(self.sw, channellabel)
        self.sw.session.channel.access.disableUserRestrictions.\
            assert_called_with(
                self.sw.key,
                'test')

    def test_fail_disableUserRestrictions(self):
        self.assertRaises(
            Exception,
            access.disableUserRestrictions,
            False,
            'test')

    def test_enableUserRestrictions(self):
        channellabel = 'test'
        access.enableUserRestrictions(self.sw, channellabel)
        self.sw.session.channel.access.enableUserRestrictions.\
            assert_called_with(
                self.sw.key,
                'test')

    def test_fail_enableUserRestrictions(self):
        self.assertRaises(
            Exception,
            access.enableUserRestrictions,
            False,
            'test')

    def test_getOrgSharing(self):
        channellabel = 'test'
        access.getOrgSharing(self.sw, channellabel)
        self.sw.session.channel.access.getOrgSharing.\
            assert_called_with(
                self.sw.key,
                'test'
            )

    def test_fail_getOrgSharing(self):
        self.assertRaises(
            Exception,
            access.getOrgSharing,
            False,
            'test')

    def test_setOrgSharing(self):
        channellabel = 'test'
        accesslevel = 'test'
        access.setOrgSharing(self.sw, channellabel, accesslevel)
        self.sw.session.channel.access.setOrgSharing.\
            assert_called_with(
                self.sw.key, 'test', 'test')

    def test_fail_setOrgSharing(self):
        self.assertRaises(
            Exception,
            access.setOrgSharing,
            False, False, True)


class TestChannelOrg(unittest.TestCase):

    def setUp(self):
        self.sw = mock.Mock()

    def test_disableAccess(self):
        channellabel = 'test'
        orgid = 1
        org.disableAccess(self.sw, channellabel, orgid)
        self.sw.session.channel.org.disableAccess.\
            assert_called_with(
                self.sw.key, 'test', 1)

    def test_fail_disableAccess(self):
        self.assertRaises(
            Exception,
            org.disableAccess,
            False,
            1,
            'test')

    def test_enableAccess(self):
        channellabel = 'test'
        orgid = 1
        org.enableAccess(self.sw, channellabel, orgid)
        self.sw.session.channel.org.enableAccess.\
            assert_called_with(
                self.sw.key, 'test', 1)

    def test_fail_enableAccess(self):
        self.assertRaises(
            Exception,
            org.enableAccess,
            False,
            'blah',
            False)

    def test_list(self):
        channellabel = 'test'
        org.list(self.sw, channellabel)
        self.sw.session.channel.org.list.\
            assert_called_with(
                self.sw.key,
                channellabel)

    def test_fail_list(self):
        self.assertRaises(
            Exception,
            org.list,
            False,
            1)


class TestChannelSoftware(unittest.TestCase):

    def setUp(self):
        self.sw = mock.Mock()

    def test_addPackages(self):
        channellabel = 'test'
        packagelist = ['one']
        software.addPackages(
            self.sw,
            channellabel,
            packagelist
        )
        self.sw.session.channel.software.addPackages.\
            assert_called_with(
                self.sw.key,
                'test',
                ['one'])

    def test_fail_addPackages(self):
        self.assertRaises(
            Exception,
            software.addPackages,
            False,
            'test',
            [])

    def test_associateRepo(self):
        channellabel = 'test'
        repositorylabel = 'test'
        software.associateRepo(
            self.sw,
            channellabel,
            repositorylabel
        )
        self.sw.session.channel.software.associateRepo.\
            assert_called_with(
                self.sw.key,
                'test',
                'test')

    def test_fail_associateRepo(self):
        self.assertRaises(
            Exception,
            software.associateRepo,
            False,
            'test',
            'test')

    def test_create_no_gpg_no_checksum(self):
        channellabel = 'test'
        channame = 'test'
        summary = 'nothing'
        arch = 'i386'
        parent = ''
        checksum = None
        gpgkey = None
        software.create(
            self.sw,
            channellabel,
            channame,
            summary,
            arch)
        self.sw.session.channel.software.create.\
            assert_called_with(
                self.sw.key,
                'test',
                'test',
                'nothing',
                'i386',
                '')

    def test_create_no_gpg_yes_checksum(self):
        channellabel = 'test'
        channame = 'test'
        summary = 'nothing'
        arch = 'i386'
        parent = ''
        checksum = '136415861231341564564sfdsfdsf4564645'
        gpgkey = None
        software.create(
            self.sw,
            channellabel,
            channame,
            summary,
            arch,
            checksum=checksum)
        self.sw.session.channel.software.create.\
            assert_called_with(
                self.sw.key,
                'test',
                'test',
                'nothing',
                'i386',
                '',
                '136415861231341564564sfdsfdsf4564645')

    def test_create_yes_gpg_yes_checksum(self):
        channellabel = 'test'
        channame = 'test'
        summary = 'nothing'
        arch = 'i386'
        parent = ''
        checksum = '136415861231341564564sfdsfdsf4564645'
        gpgkey = 's12d6r4fe6es1fs2de32sd1fs6d41r6sf45s1e5e'
        software.create(
            self.sw,
            channellabel,
            channame,
            summary,
            arch,
            checksum=checksum,
            gpgkey=gpgkey)
        self.sw.session.channel.software.create.\
            assert_called_with(
                self.sw.key,
                'test',
                'test',
                'nothing',
                'i386',
                '',
                '136415861231341564564sfdsfdsf4564645',
                's12d6r4fe6es1fs2de32sd1fs6d41r6sf45s1e5e')

    def test_fail_create(self):
        self.assertRaises(
            Exception,
            software.create,
            False,
            'test',
            False,
            1,
            1)

    def test_createRepo(self):
        repolabel = 'test'
        repotype = 'test'
        repourl = 'test'
        software.createRepo(
            self.sw,
            repolabel,
            repotype,
            repourl)
        self.sw.session.channel.software.createRepo.\
            assert_called_with(
                self.sw.key,
                repolabel,
                repotype,
                repourl)

    def test_fail_createRepo(self):
        self.assertRaises(
            Exception,
            software.createRepo,
            False,
            'test',
            'test',
            'test'
        )

    def test_availableEntitlements(self):
        channellabel = 'test'
        software.availableEntitlements(
            self.sw,
            channellabel)
        self.sw.session.channel.software.availableEntitlements.\
            assert_called_with(
                self.sw.key,
                'test')

    def test_fail_availableEntitlements(self):
        self.assertRaises(
            Exception,
            software.availableEntitlements,
            False,
            'test'
        )

    def test_clone(self):
        source_channel = 'test'
        name = 'test'
        label = 'test'
        summary = 'test'
        parent_label = None
        arch_label = None
        software.clone(
            self.sw,
            source_channel,
            name,
            label,
            summary,
            parent_label,
            arch_label)
        self.sw.session.channel.software.clone.\
            assert_called_with(
                self.sw.key,
                'test',
                {'name': 'test', 'summary': 'test', 'label': 'test'},
                False)

    def test_fail_clone(self):
        self.assertRaises(
            Exception,
            software.clone,
            False,
            False,
            False,
            'test',
            'test')

    def test_delete(self):
        channellabel = 'test'
        software.delete(self.sw, channellabel)
        self.sw.session.channel.software.delete.\
            assert_called_with(
                self.sw.key,
                'test')

    def test_fail_delete(self):
        self.assertRaises(
            Exception,
            software.delete,
            False,
            False)

    def test_getDetails(self):
        channellabel = 'test'
        software.getDetails(self.sw, channellabel)
        self.sw.session.channel.software.getDetails.\
            assert_called_with(
                self.sw.key,
                channellabel)

    def test_fail_getDetails(self):
        self.assertRaises(
            Exception,
            software.getDetails,
            'test',
            False)

    def test_availableEntitlements(self):
        channellabel = 'test'
        software.availableEntitlements(self.sw, channellabel)
        self.sw.session.channel.software.availableEntitlements.\
            assert_called_with(
                self.sw.key,
                channellabel)

    def test_fail_availableEntitlements(self):
        self.assertRaises(
            Exception,
            software.availableEntitlements,
            'test',
            False)

    def test_disassociateRepo(self):
        channellabel = 'test'
        repoLabel = 'test'
        software.disassociateRepo(
            self.sw,
            channellabel,
            repoLabel
        )
        self.sw.session.channel.software.disassociateRepo.\
            assert_called_with(
                self.sw.key,
                'test',
                'test'
            )

    def test_fail_disassociateRepo(self):
        self.assertRaises(
            Exception,
            software.disassociateRepo,
            False,
            False,
            'test'
        )

    def test_getChannelLastBuildById(self):
        channel_id = 1
        software.getChannelLastBuildById(
            self.sw,
            channel_id
        )
        self.sw.session.channel.software.getChannelLastBuildById.\
            assert_called_with(
                self.sw.key,
                1
            )

    def test_fail_getChannelLastBuildById(self):
        self.assertRaises(
            Exception,
            software.getChannelLastBuildById,
            False,
            False
        )

    def test_getDetails_name(self):
        chan = 'test'
        software.getDetails(
            self.sw,
            chan
        )
        self.sw.session.channel.software.getDetails.\
            assert_called_with(
                self.sw.key,
                'test'
            )

    def test_getDetails_id(self):
        chan = 1
        software.getDetails(
            self.sw,
            chan
        )
        self.sw.session.channel.software.getDetails.\
            assert_called_with(
                self.sw.key,
                1
            )

    def test_fail_getDetails(self):
        self.assertRaises(
            Exception,
            software.getDetails,
            False,
            False
        )

    def test_getRepoDetails(self):
        repolabel = 'test'
        software.getRepoDetails(
            self.sw,
            repolabel
        )
        self.sw.session.channel.software.getRepoDetails.\
            assert_called_with(
                self.sw.key,
                'test'
            )

    def test_fail_getRepoDetails(self):
        self.assertRaises(
            Exception,
            software.getRepoDetails,
            False,
            False
        )

    def test_getRepoSyncCronExpression(self):
        repolabel = 'test'
        software.getRepoSyncCronExpression(
            self.sw,
            repolabel
        )
        self.sw.session.channel.software.getRepoSyncCronExpression.\
            assert_called_with(
                self.sw.key,
                'test'
            )

    def test_fail_getRepoSyncCronExpression(self):
        self.assertRaises(
            Exception,
            software.getRepoSyncCronExpression,
            False,
            False
        )

    def test_isUserManageable(self):
        channellabel = 'test'
        login = 'user'
        software.isUserManageable(
            self.sw,
            channellabel,
            login
        )
        self.sw.session.channel.software.isUserManageable.\
            assert_called_with(
                self.sw.key,
                'test',
                'user'
            )

    def test_fail_isUserManageable(self):
        self.assertRaises(
            Exception,
            software.isUserManageable,
            False,
            False,
            'user'
        )

    def test_isGloballySubscribable(self):
        channellabel = 'test'
        software.isGloballySubscribable(self.sw, channellabel)
        self.sw.session.channel.software.isGloballySubscribable.\
            assert_called_with(
                self.sw.key,
                channellabel)

    def test_fail_isGloballySubscribable(self):
        self.assertRaises(
            Exception,
            software.isGloballySubscribable,
            False,
            False)

    def test_setGloballySubscribable(self):
        channellabel = 'test'
        software.setGloballySubscribable(self.sw, channellabel)
        self.sw.session.channel.software.setGloballySubscribable.\
            assert_called_with(
                self.sw.key,
                channellabel)

    def test_fail_setGloballySubscribable(self):
        self.assertRaises(
            Exception,
            software.setGloballySubscribable,
            False,
            False)

    def test_isUserSubscribable(self):
        channellabel = 'test'
        username = 'test'
        software.isUserSubscribable(self.sw, channellabel, username)
        self.sw.session.channel.software.isUserSubscribable.\
            assert_called_with(
                self.sw.key,
                'test',
                'test')

    def test_fail_isUserSubscribable(self):
        self.assertRaises(
            Exception,
            software.isUserSubscribable,
            False,
            False,
            'test')

    def test_setUserManageable(self):
        channellabel = 'test'
        login = 'test'
        action = 'action'
        software.setUserManageable(self.sw, channellabel, login, action)
        self.sw.session.channel.software.setUserManageable.\
            assert_called_with(
                self.sw.key,
                'test',
                'test',
                'action')

    def test_fail_setUserManageable(self):
        self.assertRaises(
            Exception,
            software.setUserManageable,
            False,
            False,
            'test',
            1)

    def test_setUserSubscribable(self):
        channellabel = 'test'
        username = 'test'
        software.setUserSubscribable(self.sw, channellabel, username)
        self.sw.session.channel.software.setUserSubscribable.\
            assert_called_with(
                self.sw.key,
                'test',
                'test')

    def test_fail_setUserSubscribable(self):
        self.assertRaises(
            Exception,
            software.setUserSubscribable,
            False,
            False,
            'test')

    def test_listAllPackages(self):
        channellabel = 'test'
        start_date = '00020202022'
        end_date = '000202020202'

        software.listAllPackages(
            self.sw,
            channellabel,
            start_date,
            end_date)
        self.sw.session.channel.software.listAllPackages.\
            assert_called_with(
                self.sw.key,
                'test',
                '00020202022',
                '000202020202'
            )

        software.listAllPackages(
            self.sw,
            channellabel,
            start_date)
        self.sw.session.channel.software.listAllPackages.\
            assert_called_with(
                self.sw.key,
                'test',
                '00020202022'
            )

        software.listAllPackages(
            self.sw,
            channellabel
        )
        self.sw.session.channel.software.listAllPackages.\
            assert_called_with(
                self.sw.key,
                'test'
            )

    def test_fail_listAllPackages(self):
        self.assertRaises(
            Exception,
            software.listAllPackages,
            False,
            False
        )

    def test_listArches(self):
        software.listArches(
            self.sw
        )
        self.sw.session.channel.software.listArches.\
            assert_called_with(
                self.sw.key
            )

    def test_fail_listArches(self):
        self.assertRaises(
            Exception,
            software.listArches,
            False
        )

    def test_listChannelRepos(self):
        software.listChannelRepos(
            self.sw,
            'test1'
        )
        self.sw.session.channel.software.listChannelRepos.\
            assert_called_with(
                self.sw.key,
                'test1'
            )

    def test_fail_listChannelRepos(self):
        self.assertRaises(
            Exception,
            software.listChannelRepos,
            False,
            'blah'
        )

    def test_listChildren(self):
        software.listChildren(
            self.sw,
            'test1'
        )
        self.sw.session.channel.software.listChildren.\
            assert_called_with(
                self.sw.key,
                'test1'
            )

    def test_fail_listChildren(self):
        self.assertRaises(
            Exception,
            software.listChildren,
            False,
            'blah'
        )

    def test_listErrata(self):
        software.listErrata(
            self.sw,
            'chanlabel',
            '0000000002',
            '0000000002'
        )
        self.sw.session.channel.software.listErrata.\
            assert_called_with(
                self.sw.key,
                'chanlabel',
                '0000000002',
                '0000000002'
            )
        software.listErrata(
            self.sw,
            'chanlabel',
            '0000000002'
        )
        self.sw.session.channel.software.listErrata.\
            assert_called_with(
                self.sw.key,
                'chanlabel',
                '0000000002'
            )
        software.listErrata(
            self.sw,
            'chanlabel'
        )
        self.sw.session.channel.software.listErrata.\
            assert_called_with(
                self.sw.key,
                'chanlabel'
            )

    def test_fail_listErrata(self):
        self.assertRaises(
            Exception,
            software.listErrata,
            False,
            'blah'
        )

    def test_listErrataByType(self):
        software.listErrataByType(
            self.sw,
            'test1',
            'test2'
        )
        self.sw.session.channel.software.listErrataByType.\
            assert_called_with(
                self.sw.key,
                'test1',
                'test2'
            )

    def test_fail_listErrataByType(self):
        self.assertRaises(
            Exception,
            software.listErrataByType,
            False,
            'blah',
            1
        )

    def test_listLatestPackagesself(self):
        software.listLatestPackages(
            self.sw,
            'test1'
        )
        self.sw.session.channel.software.listLatestPackages.\
            assert_called_with(
                self.sw.key,
                'test1'
            )

    def test_fail_listLatestPackages(self):
        self.assertRaises(
            Exception,
            software.listLatestPackages,
            False,
            1
        )

    def test_listPackagesWithoutChannel(self):
        software.listPackagesWithoutChannel(
            self.sw
        )
        self.sw.session.channel.software.listPackagesWithoutChannel.\
            assert_called_with(
                self.sw.key
            )

    def test_fail_listPackagesWithoutChannel(self):
        self.assertRaises(
            Exception,
            software.listPackagesWithoutChannel,
            False
        )

    def test_listRepoFilters(self):
        software.listRepoFilters(
            self.sw,
            'test'
        )
        self.sw.session.channel.software.listRepoFilters.\
            assert_called_with(
                self.sw.key,
                'test'
            )

    def test_fail_listRepoFilters(self):
        self.assertRaises(
            Exception,
            software.listRepoFilters,
            False,
            'not'
        )

    def test_listSubscribedSystems(self):
        software.listSubscribedSystems(
            self.sw,
            'test'
        )
        self.sw.session.channel.software.listSubscribedSystems.\
            assert_called_with(
                self.sw.key,
                'test'
            )

    def test_fail_listSubscribedSystems(self):
        self.assertRaises(
            Exception,
            software.listSubscribedSystems,
            False,
            'not'
        )

    def test_listSystemChannels(self):
        software.listSystemChannels(
            self.sw,
            1
        )
        self.sw.session.channel.software.listSystemChannels.\
            assert_called_with(
                self.sw.key,
                1
            )

    def test_fail_listSystemChannels(self):
        self.assertRaises(
            Exception,
            software.listSystemChannels,
            False,
            'not'
        )

    def test_setSystemChannels(self):
        software.setSystemChannels(
            self.sw,
            1,
            ['test']
        )
        self.sw.session.channel.software.setSystemChannels.\
            assert_called_with(
                self.sw.key,
                1,
                ['test']
            )

    def test_fail_setSystemChannels(self):
        self.assertRaises(
            Exception,
            software.setSystemChannels,
            False,
            1,
            ['test'])

    def test_listUserRepos(self):
        software.listUserRepos(
            self.sw
        )
        self.sw.session.channel.software.listUserRepos.\
            assert_called_with(
                self.sw.key
            )

    def test_fail_listUserRepos(self):
        self.assertRaises(
            Exception,
            software.listUserRepos,
            False
        )

    def test_mergeErrata(self):
        import time
        end_date = time.strftime(
            '%Y-%m-%d %H:%M:%S', time.localtime())

        software.mergeErrata(
            self.sw,
            'test',
            'dest',
            start_date='1980-01-01 00:00:00',
            end_date='1980-01-01 00:00:00'
        )
        self.sw.session.channel.software.mergeErrata.\
            assert_called_with(
                self.sw.key,
                'test',
                'dest',
                '1980-01-01 00:00:00',
                '1980-01-01 00:00:00'
            )
        software.mergeErrata(
            self.sw,
            'test',
            'dest',
            end_date=end_date
        )
        self.sw.session.channel.software.mergeErrata.\
            assert_called_with(
                self.sw.key,
                'test',
                'dest',
                '1980-01-01 00:00:00',
                end_date
            )
        software.mergeErrata(
            self.sw,
            'test',
            'dest'
        )
        self.sw.session.channel.software.mergeErrata.\
            assert_called_with(
                self.sw.key,
                'test',
                'dest',
                '1980-01-01 00:00:00',
                end_date
            )

    def test_fail_mergeErrata(self):
        self.assertRaises(
            Exception,
            software.mergeErrata,
            False,
            'test',
            'test'
        )

    def test_mergePackages(self):
        software.mergePackages(
            self.sw,
            'test',
            'dest'
        )
        self.sw.session.channel.software.mergePackages.\
            assert_called_with(
                self.sw.key,
                'test',
                'dest'
            )

    def test_fail_mergePackages(self):
        self.assertRaises(
            Exception,
            software.mergePackages,
            False,
            'none',
            'test'
        )

    def test_regenerateNeededCache(self):
        software.regenerateNeededCache(
            self.sw,
            channellabel='test'
        )
        self.sw.session.channel.software.regenerateNeededCache.\
            assert_called_with(
                self.sw.key,
                'test'
            )
        software.regenerateNeededCache(
            self.sw)
        self.sw.session.channel.software.regenerateNeededCache.\
            assert_called_with(
                self.sw.key)

    def test_fail_regenerateNeededCache(self):
        self.assertRaises(
            Exception,
            software.regenerateNeededCache,
            False,
            'none'
        )

    def test_regenerateYumCache(self):
        software.regenerateYumCache(
            self.sw,
            'test')
        self.sw.session.channel.software.regenerateYumCache.\
            assert_called_with(
                self.sw.key,
                'test')

    def test_fail_regenerateYumCache(self):
        self.assertRaises(
            Exception,
            software.regenerateYumCache,
            False,
            'test'
        )

    def test_removePackages(self):
        channellabel = 'test'
        package_ids = [1, 2]
        software.removePackages(
            self.sw,
            channellabel,
            package_ids
        )
        self.sw.session.channel.software.removePackages.\
            assert_called_with(
                self.sw.key,
                'test',
                [1, 2]
            )

    def test_fail_removePackages(self):
        self.assertRaises(
            Exception,
            software.removePackages,
            False,
            'not',
            'not'
        )

    def test_removeRepo(self):
        software.removeRepo(
            self.sw,
            'test'
        )
        self.sw.session.channel.software.removeRepo.\
            assert_called_with(
                self.sw.key,
                'test'
            )

    def test_fail_removeRepo(self):
        self.assertRaises(
            Exception,
            software.removeRepo,
            False,
            'test'
        )

    def test_setContactDetails(self):
        software.setContactDetails(
            self.sw,
            'label',
            'user',
            'email',
            '555-note',
            'none'
        )
        self.sw.session.channel.software.setContactDetails.\
            assert_called_with(
                self.sw.key,
                'label',
                'user',
                'email',
                '555-note',
                'none'
            )

    def test_fail_setContactDetails(self):
        self.assertRaises(
            Exception,
            software.setContactDetails,
            False,
            'blah',
            1,
            2,
            'test',
            'policy'
        )

    def test_setDetails(self):
        software.setDetails(
            self.sw,
            1,
            'map'
        )
        self.sw.session.channel.software.setDetails.\
            assert_called_with(
                self.sw.key,
                1,
                'map'
            )

    def test_fail_setDetails(self):
        self.assertRaises(
            Exception,
            software.setDetails,
            False,
            'test',
            'test'
        )

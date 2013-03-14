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

from space.lib import system
from space.lib.system import config
from space.lib.system import custominfo
from space.lib.system import scap
from space.lib.system import search


class TestSystem(unittest.TestCase):

    def setUp(self):
        self.sw = mock.Mock()

    def test_addEntitlements(self):
        system.addEntitlements(
            self.sw,
            1,
            'entitlement_label'
        )
        self.sw.session.system.addEntitlements.\
            assert_called_with(
                self.sw.key,
                1,
                'entitlement_label'
            )

    def test_fail_addEntitlements(self):
        self.assertRaises(
            Exception,
            system.addEntitlements,
            False,
            1,
            'entitlement_label'
        )

    def test_addNote(self):
        system.addNote(
            self.sw,
            1,
            'subject',
            'body'
        )
        self.sw.session.system.addNote.\
            assert_called_with(
                self.sw.key,
                1,
                'subject',
                'body'
            )

    def test_fail_addNote(self):
        self.assertRaises(
            Exception,
            system.addNote,
            False,
            1,
            'subject',
            'body'
        )

    def test_comparePackageProfile(self):
        system.comparePackageProfile(
            self.sw,
            1,
            'profile_label'
        )
        self.sw.session.system.comparePackageProfile.\
            assert_called_with(
                self.sw.key,
                1,
                'profile_label'
            )

    def test_fail_comparePackageProfile(self):
        self.assertRaises(
            Exception,
            system.comparePackageProfile,
            False,
            1,
            'profile_label'
        )

    def test_comparePackages(self):
        system.comparePackages(
            self.sw,
            'this_server_id',
            'other_server_id'
        )
        self.sw.session.system.comparePackages.\
            assert_called_with(
                self.sw.key,
                'this_server_id',
                'other_server_id'
            )

    def test_fail_comparePackages(self):
        self.assertRaises(
            Exception,
            system.comparePackages,
            False,
            'this_server_id',
            'other_server_id'
        )

    def test_convertToFlexEntitlement(self):
        system.convertToFlexEntitlement(
            self.sw,
            1,
            'channel_family_label'
        )
        self.sw.session.system.convertToFlexEntitlement.\
            assert_called_with(
                self.sw.key,
                1,
                'channel_family_label'
            )

    def test_fail_convertToFlexEntitlement(self):
        self.assertRaises(
            Exception,
            system.convertToFlexEntitlement,
            False,
            1,
            'channel_family_label'
        )

    def test_createPackageProfile(self):
        system.createPackageProfile(
            self.sw,
            1,
            'profile_label',
            'description'
        )
        self.sw.session.system.createPackageProfile.\
            assert_called_with(
                self.sw.key,
                1,
                'profile_label',
                'description'
            )

    def test_fail_createPackageProfile(self):
        self.assertRaises(
            Exception,
            system.createPackageProfile,
            False,
            1,
            'profile_label',
            'description'
        )

    def test_createSystemRecord(self):
        system.createSystemRecord(
            self.sw,
            1,
            'kslabel'
        )
        self.sw.session.system.createSystemRecord.\
            assert_called_with(
                self.sw.key,
                1,
                'kslabel'
            )

    def test_fail_createSystemRecord(self):
        self.assertRaises(
            Exception,
            system.createSystemRecord,
            False,
            1,
            'kslabel'
        )

    def test_deleteCustomValues(self):
        system.deleteCustomValues(
            self.sw,
            1,
            'custominfolabel'
        )
        self.sw.session.system.deleteCustomValues.\
            assert_called_with(
                self.sw.key,
                1,
                'custominfolabel'
            )

    def test_fail_deleteCustomValues(self):
        self.assertRaises(
            Exception,
            system.deleteCustomValues,
            False,
            1,
            'custominfolabel'
        )

    def test_deleteGuestProfiles(self):
        system.deleteGuestProfiles(
            self.sw,
            'hostid',
            'guestnames'
        )
        self.sw.session.system.deleteGuestProfiles.\
            assert_called_with(
                self.sw.key,
                'hostid',
                'guestnames'
            )

    def test_fail_deleteGuestProfiles(self):
        self.assertRaises(
            Exception,
            system.deleteGuestProfiles,
            False,
            'hostid',
            'guestnames'
        )

    def test_deleteNote(self):
        system.deleteNote(
            self.sw,
            1,
            'note_id'
        )
        self.sw.session.system.deleteNote.\
            assert_called_with(
                self.sw.key,
                1,
                'note_id'
            )

    def test_fail_deleteNote(self):
        self.assertRaises(
            Exception,
            system.deleteNote,
            False,
            1,
            'note_id'
        )

    def test_deleteNotes(self):
        system.deleteNotes(
            self.sw,
            1
        )
        self.sw.session.system.deleteNotes.\
            assert_called_with(
                self.sw.key,
                1
            )

    def test_fail_deleteNotes(self):
        self.assertRaises(
            Exception,
            system.deleteNotes,
            False,
            1
        )

    def test_deletePackageProfile(self):
        system.deletePackageProfile(
            self.sw,
            'profile_id'
        )
        self.sw.session.system.deletePackageProfile.\
            assert_called_with(
                self.sw.key,
                'profile_id'
            )

    def test_fail_deletePackageProfile(self):
        self.assertRaises(
            Exception,
            system.deletePackageProfile,
            False,
            'profile_id'
        )

    def test_deleteSystem(self):
        system.deleteSystem(
            self.sw,
            'system_id'
        )
        self.sw.session.system.deleteSystem.\
            assert_called_with(
                self.sw.key,
                'system_id'
            )

    def test_fail_deleteSystem(self):
        self.assertRaises(
            Exception,
            system.deleteSystem,
            False,
            'system_id'
        )

    def test_deleteSystems(self):
        system.deleteSystems(
            self.sw,
            ['server_ids']
        )
        self.sw.session.system.deleteSystems.\
            assert_called_with(
                self.sw.key,
                ['server_ids']
            )

    def test_fail_deleteSystems(self):
        self.assertRaises(
            Exception,
            system.deleteSystems,
            False,
            ['server_ids']
        )

    def test_deleteTagFromSnapshot(self):
        system.deleteTagFromSnapshot(
            self.sw,
            1,
            'tagname'
        )
        self.sw.session.system.deleteTagFromSnapshot.\
            assert_called_with(
                self.sw.key,
                1,
                'tagname'
            )

    def test_fail_deleteTagFromSnapshot(self):
        self.assertRaises(
            Exception,
            system.deleteTagFromSnapshot,
            False,
            1,
            'tagname'
        )

    def test_downloadSystemId(self):
        system.downloadSystemId(
            self.sw,
            1
        )
        self.sw.session.system.downloadSystemId.\
            assert_called_with(
                self.sw.key,
                1
            )

    def test_fail_downloadSystemId(self):
        self.assertRaises(
            Exception,
            system.downloadSystemId,
            False,
            1
        )

    def test_getConnectionPath(self):
        system.getConnectionPath(
            self.sw,
            1
        )
        self.sw.session.system.getConnectionPath.\
            assert_called_with(
                self.sw.key,
                1
            )

    def test_fail_getConnectionPath(self):
        self.assertRaises(
            Exception,
            system.getConnectionPath,
            False,
            1
        )

    def test_getCpu(self):
        system.getCpu(
            self.sw,
            1
        )
        self.sw.session.system.getCpu.\
            assert_called_with(
                self.sw.key,
                1
            )

    def test_fail_getCpu(self):
        self.assertRaises(
            Exception,
            system.getCpu,
            False,
            1
        )

    def test_getCustomValues(self):
        system.getCustomValues(
            self.sw,
            1
        )
        self.sw.session.system.getCustomValues.\
            assert_called_with(
                self.sw.key,
                1
            )

    def test_fail_getCustomValues(self):
        self.assertRaises(
            Exception,
            system.getCustomValues,
            False,
            1
        )

    def test_getDetails(self):
        system.getDetails(
            self.sw,
            1
        )
        self.sw.session.system.getDetails.\
            assert_called_with(
                self.sw.key,
                1
            )

    def test_fail_getDetails(self):
        self.assertRaises(
            Exception,
            system.getDetails,
            False,
            1
        )

    def test_getDevices(self):
        system.getDevices(
            self.sw,
            1
        )
        self.sw.session.system.getDevices.\
            assert_called_with(
                self.sw.key,
                1
            )

    def test_fail_getDevices(self):
        self.assertRaises(
            Exception,
            system.getDevices,
            False,
            1
        )

    def test_getDmi(self):
        system.getDmi(
            self.sw,
            1
        )
        self.sw.session.system.getDmi.\
            assert_called_with(
                self.sw.key,
                1
            )

    def test_fail_getDmi(self):
        self.assertRaises(
            Exception,
            system.getDmi,
            False,
            1
        )

    def test_getEntitlements(self):
        system.getEntitlements(
            self.sw,
            1
        )
        self.sw.session.system.getEntitlements.\
            assert_called_with(
                self.sw.key,
                1
            )

    def test_fail_getEntitlements(self):
        self.assertRaises(
            Exception,
            system.getEntitlements,
            False,
            1
        )

    def test_getEventHistory(self):
        system.getEventHistory(
            self.sw,
            1
        )
        self.sw.session.system.getEventHistory.\
            assert_called_with(
                self.sw.key,
                1
            )

    def test_fail_getEventHistory(self):
        self.assertRaises(
            Exception,
            system.getEventHistory,
            False,
            1
        )

    def test_getId(self):
        system.getId(
            self.sw,
            'servername'
        )
        self.sw.session.system.getId.\
            assert_called_with(
                self.sw.key,
                'servername'
            )

    def test_fail_getId(self):
        self.assertRaises(
            Exception,
            system.getId,
            False,
            'servername'
        )

    def test_getMemory(self):
        system.getMemory(
            self.sw,
            1
        )
        self.sw.session.system.getMemory.\
            assert_called_with(
                self.sw.key,
                1
            )

    def test_fail_getMemory(self):
        self.assertRaises(
            Exception,
            system.getMemory,
            False,
            1
        )

    def test_getName(self):
        system.getName(
            self.sw,
            1
        )
        self.sw.session.system.getName.\
            assert_called_with(
                self.sw.key,
                1
            )

    def test_fail_getName(self):
        self.assertRaises(
            Exception,
            system.getName,
            False,
            1
        )

    def test_getNetwork(self):
        system.getNetwork(
            self.sw,
            1
        )
        self.sw.session.system.getNetwork.\
            assert_called_with(
                self.sw.key,
                1
            )

    def test_fail_getNetwork(self):
        self.assertRaises(
            Exception,
            system.getNetwork,
            False,
            1
        )

    def test_getNetworkDevices(self):
        system.getNetworkDevices(
            self.sw,
            1
        )
        self.sw.session.system.getNetworkDevices.\
            assert_called_with(
                self.sw.key,
                1
            )

    def test_fail_getNetworkDevices(self):
        self.assertRaises(
            Exception,
            system.getNetworkDevices,
            False,
            1
        )

    def test_getRegistrationDate(self):
        system.getRegistrationDate(
            self.sw,
            1
        )
        self.sw.session.system.getRegistrationDate.\
            assert_called_with(
                self.sw.key,
                1
            )

    def test_fail_getRegistrationDate(self):
        self.assertRaises(
            Exception,
            system.getRegistrationDate,
            False,
            1
        )

    def test_getRelevantErrata(self):
        system.getRelevantErrata(
            self.sw,
            1
        )
        self.sw.session.system.getRelevantErrata.\
            assert_called_with(
                self.sw.key,
                1
            )

    def test_fail_getRelevantErrata(self):
        self.assertRaises(
            Exception,
            system.getRelevantErrata,
            False,
            1
        )

    def test_getRelevantErrataByType(self):
        system.getRelevantErrataByType(
            self.sw,
            1,
            'advisory_type'
        )
        self.sw.session.system.getRelevantErrataByType.\
            assert_called_with(
                self.sw.key,
                1,
                'advisory_type'
            )

    def test_fail_getRelevantErrataByType(self):
        self.assertRaises(
            Exception,
            system.getRelevantErrataByType,
            False,
            1,
            'advisory_type'
        )

    def test_getRunningKernel(self):
        system.getRunningKernel(
            self.sw,
            1
        )
        self.sw.session.system.getRunningKernel.\
            assert_called_with(
                self.sw.key,
                1
            )

    def test_fail_getRunningKernel(self):
        self.assertRaises(
            Exception,
            system.getRunningKernel,
            False,
            1
        )

    def test_getScriptActionDetails(self):
        system.getScriptActionDetails(
            self.sw,
            1
        )
        self.sw.session.system.getScriptActionDetails.\
            assert_called_with(
                self.sw.key,
                1
            )

    def test_fail_getScriptActionDetails(self):
        self.assertRaises(
            Exception,
            system.getScriptActionDetails,
            False,
            1
        )

    def test_getScriptResults(self):
        system.getScriptResults(
            self.sw,
            1
        )
        self.sw.session.system.getScriptResults.\
            assert_called_with(
                self.sw.key,
                1
            )

    def test_fail_getScriptResults(self):
        self.assertRaises(
            Exception,
            system.getScriptResults,
            False,
            1
        )

    def test_getSubscribedBaseChannel(self):
        system.getSubscribedBaseChannel(
            self.sw,
            1
        )
        self.sw.session.system.getSubscribedBaseChannel.\
            assert_called_with(
                self.sw.key,
                1
            )

    def test_fail_getSubscribedBaseChannel(self):
        self.assertRaises(
            Exception,
            system.getSubscribedBaseChannel,
            False,
            1
        )

    def test_getSystemCurrencyMultipliers(self):
        system.getSystemCurrencyMultipliers(
            self.sw
        )
        self.sw.session.system.getSystemCurrencyMultipliers.\
            assert_called_with(
                self.sw.key
            )

    def test_fail_getSystemCurrencyMultipliers(self):
        self.assertRaises(
            Exception,
            system.getSystemCurrencyMultipliers,
            False
        )

    def test_getSystemCurrencyScores(self):
        system.getSystemCurrencyScores(
            self.sw
        )
        self.sw.session.system.getSystemCurrencyScores.\
            assert_called_with(
                self.sw.key
            )

    def test_fail_getSystemCurrencyScores(self):
        self.assertRaises(
            Exception,
            system.getSystemCurrencyScores,
            False
        )

    def test_getUnscheduledErrata(self):
        system.getUnscheduledErrata(
            self.sw,
            1
        )
        self.sw.session.system.getUnscheduledErrata.\
            assert_called_with(
                self.sw.key,
                1
            )

    def test_fail_getUnscheduledErrata(self):
        self.assertRaises(
            Exception,
            system.getUnscheduledErrata,
            False,
            1
        )

    def test_getUuid(self):
        system.getUuid(
            self.sw,
            1
        )
        self.sw.session.system.getUuid.\
            assert_called_with(
                self.sw.key,
                1
            )

    def test_fail_getUuid(self):
        self.assertRaises(
            Exception,
            system.getUuid,
            False,
            1
        )

    def test_getVariables(self):
        system.getVariables(
            self.sw,
            1
        )
        self.sw.session.system.getVariables.\
            assert_called_with(
                self.sw.key,
                1
            )

    def test_fail_getVariables(self):
        self.assertRaises(
            Exception,
            system.getVariables,
            False,
            1
        )

    def test_isNvreInstalled(self):
        system.isNvreInstalled(
            self.sw,
            1,
            'name',
            'version',
            'release'
        )
        self.sw.session.system.isNvreInstalled.\
            assert_called_with(
                self.sw.key,
                1,
                'name',
                'version',
                'release'
            )
        system.isNvreInstalled(
            self.sw,
            1,
            'name',
            'version',
            'release',
            epoch='0000001'
        )
        self.sw.session.system.isNvreInstalled.\
            assert_called_with(
                self.sw.key,
                1,
                'name',
                'version',
                'release',
                '0000001'
            )

    def test_fail_isNvreInstalled(self):
        self.assertRaises(
            Exception,
            system.isNvreInstalled,
            False,
            1,
            'name',
            'version',
            'release'
        )

    def test_listActivationKeys(self):
        system.listActivationKeys(
            self.sw,
            1
        )
        self.sw.session.system.listActivationKeys.\
            assert_called_with(
                self.sw.key,
                1
            )

    def test_fail_listActivationKeys(self):
        self.assertRaises(
            Exception,
            system.listActivationKeys,
            False,
            1
        )

    def test_listActiveSystems(self):
        system.listActiveSystems(
            self.sw
        )
        self.sw.session.system.listActiveSystems.\
            assert_called_with(
                self.sw.key
            )

    def test_fail_listActiveSystems(self):
        self.assertRaises(
            Exception,
            system.listActiveSystems,
            False
        )

    def test_listActiveSystemsDetails(self):
        system.listActiveSystemsDetails(
            self.sw,
            [1]
        )
        self.sw.session.system.listActiveSystemsDetails.\
            assert_called_with(
                self.sw.key,
                [1]
            )

    def test_fail_listActiveSystemsDetails(self):
        self.assertRaises(
            Exception,
            system.listActiveSystemsDetails,
            False,
            [1]
        )

    def test_listAdministrators(self):
        system.listAdministrators(
            self.sw,
            1
        )
        self.sw.session.system.listAdministrators.\
            assert_called_with(
                self.sw.key,
                1
            )

    def test_fail_listAdministrators(self):
        self.assertRaises(
            Exception,
            system.listAdministrators,
            False,
            1
        )

    def test_listDuplicatesByHostname(self):
        system.listDuplicatesByHostname(
            self.sw
        )
        self.sw.session.system.listDuplicatesByHostname.\
            assert_called_with(
                self.sw.key
            )

    def test_fail_listDuplicatesByHostname(self):
        self.assertRaises(
            Exception,
            system.listDuplicatesByHostname,
            False
        )

    def test_listDuplicatesByIp(self):
        system.listDuplicatesByIp(
            self.sw
        )
        self.sw.session.system.listDuplicatesByIp.\
            assert_called_with(
                self.sw.key
            )

    def test_fail_listDuplicatesByIp(self):
        self.assertRaises(
            Exception,
            system.listDuplicatesByIp,
            False
        )

    def test_listDuplicatesByMac(self):
        system.listDuplicatesByMac(
            self.sw
        )
        self.sw.session.system.listDuplicatesByMac.\
            assert_called_with(
                self.sw.key
            )

    def test_fail_listDuplicatesByMac(self):
        self.assertRaises(
            Exception,
            system.listDuplicatesByMac,
            False
        )

    def test_listEligibleFlexGuests(self):
        system.listEligibleFlexGuests(
            self.sw
        )
        self.sw.session.system.listEligibleFlexGuests.\
            assert_called_with(
                self.sw.key
            )

    def test_fail_listEligibleFlexGuests(self):
        self.assertRaises(
            Exception,
            system.listEligibleFlexGuests,
            False
        )

    def test_listExtraPackages(self):
        system.listExtraPackages(
            self.sw,
            1
        )
        self.sw.session.system.listExtraPackages.\
            assert_called_with(
                self.sw.key,
                1
            )

    def test_fail_listExtraPackages(self):
        self.assertRaises(
            Exception,
            system.listExtraPackages,
            False,
            1
        )

    def test_listFlexGuests(self):
        system.listFlexGuests(
            self.sw
        )
        self.sw.session.system.listFlexGuests.\
            assert_called_with(
                self.sw.key
            )

    def test_fail_listFlexGuests(self):
        self.assertRaises(
            Exception,
            system.listFlexGuests,
            False
        )

    def test_listGroups(self):
        system.listGroups(
            self.sw,
            1
        )
        self.sw.session.system.listGroups.\
            assert_called_with(
                self.sw.key,
                1
            )

    def test_fail_listGroups(self):
        self.assertRaises(
            Exception,
            system.listGroups,
            False,
            1
        )

    def test_listInactiveSystems(self):
        system.listInactiveSystems(
            self.sw
        )
        self.sw.session.system.listInactiveSystems.\
            assert_called_with(
                self.sw.key
            )
        system.listInactiveSystems(
            self.sw,
            days=1
        )
        self.sw.session.system.listInactiveSystems.\
            assert_called_with(
                self.sw.key,
                1
            )

    def test_fail_listInactiveSystems(self):
        self.assertRaises(
            Exception,
            system.listInactiveSystems,
            False
        )

    def test_listLatestAvailablePackage(self):
        system.listLatestAvailablePackage(
            self.sw,
            1,
            'server_id'
        )
        self.sw.session.system.listLatestAvailablePackage.\
            assert_called_with(
                self.sw.key,
                1,
                'server_id'
            )

    def test_fail_listLatestAvailablePackage(self):
        self.assertRaises(
            Exception,
            system.listLatestAvailablePackage,
            False,
            1,
            'server_id'
        )

    def test_listLatestInstallablePackages(self):
        system.listLatestInstallablePackages(
            self.sw,
            1
        )
        self.sw.session.system.listLatestInstallablePackages.\
            assert_called_with(
                self.sw.key,
                1
            )

    def test_fail_listLatestInstallablePackages(self):
        self.assertRaises(
            Exception,
            system.listLatestInstallablePackages,
            False,
            1
        )

    def test_listLatestUpgradablePackages(self):
        system.listLatestUpgradablePackages(
            self.sw,
            1
        )
        self.sw.session.system.listLatestUpgradablePackages.\
            assert_called_with(
                self.sw.key,
                1
            )

    def test_fail_listLatestUpgradablePackages(self):
        self.assertRaises(
            Exception,
            system.listLatestUpgradablePackages,
            False,
            1
        )

    def test_listNewerInstalledPackages(self):
        system.listNewerInstalledPackages(
            self.sw,
            1,
            'package_name',
            'package_version',
            'package_release',
            'package_epoch'
        )
        self.sw.session.system.listNewerInstalledPackages.\
            assert_called_with(
                self.sw.key,
                1,
                'package_name',
                'package_version',
                'package_release',
                'package_epoch'
            )

    def test_fail_listNewerInstalledPackages(self):
        self.assertRaises(
            Exception,
            system.listNewerInstalledPackages,
            False,
            1,
            'package_name',
            'package_version',
            'package_release',
            'package_epoch'
        )

    def test_listNotes(self):
        system.listNotes(
            self.sw,
            1
        )
        self.sw.session.system.listNotes.\
            assert_called_with(
                self.sw.key,
                1
            )

    def test_fail_listNotes(self):
        self.assertRaises(
            Exception,
            system.listNotes,
            False,
            1
        )

    def test_listOlderInstalledPackages(self):
        system.listOlderInstalledPackages(
            self.sw,
            1,
            'name',
            'version',
            'release',
            'epoch'
        )
        self.sw.session.system.listOlderInstalledPackages.\
            assert_called_with(
                self.sw.key,
                1,
                'name',
                'version',
                'release',
                'epoch'
            )

    def test_fail_listOlderInstalledPackages(self):
        self.assertRaises(
            Exception,
            system.listOlderInstalledPackages,
            False,
            1,
            'name',
            'version',
            'release',
            'epoch'
        )

    def test_listOutOfDateSystems(self):
        system.listOutOfDateSystems(
            self.sw
        )
        self.sw.session.system.listOutOfDateSystems.\
            assert_called_with(
                self.sw.key
            )

    def test_fail_listOutOfDateSystems(self):
        self.assertRaises(
            Exception,
            system.listOutOfDateSystems,
            False
        )

    def test_listPackageProfiles(self):
        system.listPackageProfiles(
            self.sw
        )
        self.sw.session.system.listPackageProfiles.\
            assert_called_with(
                self.sw.key
            )

    def test_fail_listPackageProfiles(self):
        self.assertRaises(
            Exception,
            system.listPackageProfiles,
            False
        )

    def test_listPackages(self):
        system.listPackages(
            self.sw,
            1
        )
        self.sw.session.system.listPackages.\
            assert_called_with(
                self.sw.key,
                1
            )

    def test_fail_listPackages(self):
        self.assertRaises(
            Exception,
            system.listPackages,
            False,
            1
        )

    def test_listPackagesFromChannel(self):
        system.listPackagesFromChannel(
            self.sw,
            1,
            'channel_label'
        )
        self.sw.session.system.listPackagesFromChannel.\
            assert_called_with(
                self.sw.key,
                1,
                'channel_label'
            )

    def test_fail_listPackagesFromChannel(self):
        self.assertRaises(
            Exception,
            system.listPackagesFromChannel,
            False,
            1,
            'channel_label'
        )

    def test_listSubscribableBaseChannels(self):
        system.listSubscribableBaseChannels(
            self.sw,
            1
        )
        self.sw.session.system.listSubscribableBaseChannels.\
            assert_called_with(
                self.sw.key,
                1
            )

    def test_fail_listSubscribableBaseChannels(self):
        self.assertRaises(
            Exception,
            system.listSubscribableBaseChannels,
            False,
            1
        )

    def test_listSubscribableChildChannels(self):
        system.listSubscribableChildChannels(
            self.sw,
            1
        )
        self.sw.session.system.listSubscribableChildChannels.\
            assert_called_with(
                self.sw.key,
                1
            )

    def test_fail_listSubscribableChildChannels(self):
        self.assertRaises(
            Exception,
            system.listSubscribableChildChannels,
            False,
            1
        )

    def test_listSubscribedChildChannels(self):
        system.listSubscribedChildChannels(
            self.sw,
            1
        )
        self.sw.session.system.listSubscribedChildChannels.\
            assert_called_with(
                self.sw.key,
                1
            )

    def test_fail_listSubscribedChildChannels(self):
        self.assertRaises(
            Exception,
            system.listSubscribedChildChannels,
            False,
            1
        )

    def test_listSystemEvents(self):
        system.listSystemEvents(
            self.sw,
            1
        )
        self.sw.session.system.listSystemEvents.\
            assert_called_with(
                self.sw.key,
                1
            )

    def test_fail_listSystemEvents(self):
        self.assertRaises(
            Exception,
            system.listSystemEvents,
            False,
            1
        )

    def test_listSystems(self):
        system.listSystems(
            self.sw
        )
        self.sw.session.system.listSystems.\
            assert_called_with(
                self.sw.key
            )

    def test_fail_listSystems(self):
        self.assertRaises(
            Exception,
            system.listSystems,
            False
        )

    def test_listSystemsWithExtraPackages(self):
        system.listSystemsWithExtraPackages(
            self.sw
        )
        self.sw.session.system.listSystemsWithExtraPackages.\
            assert_called_with(
                self.sw.key
            )

    def test_fail_listSystemsWithExtraPackages(self):
        self.assertRaises(
            Exception,
            system.listSystemsWithExtraPackages,
            False
        )

    def test_listSystemsWithPackage(self):
        system.listSystemsWithPackage(
            self.sw,
            package_id=1
        )
        self.sw.session.system.listSystemsWithPackage.\
            assert_called_with(
                self.sw.key,
                1
            )
        system.listSystemsWithPackage(
            self.sw,
            name='name',
            version='1.1',
            release='1'
        )
        self.sw.session.system.listSystemsWithPackage.\
            assert_called_with(
                self.sw.key,
                'name',
                '1.1',
                '1'
            )

    def test_fail_listSystemsWithPackage(self):
        self.assertRaises(
            Exception,
            system.listSystemsWithPackage,
            False,
            1
        )

    def test_listUngroupedSystems(self):
        system.listUngroupedSystems(
            self.sw
        )
        self.sw.session.system.listUngroupedSystems.\
            assert_called_with(
                self.sw.key
            )

    def test_fail_listUngroupedSystems(self):
        self.assertRaises(
            Exception,
            system.listUngroupedSystems,
            False
        )

    def test_listUserSystems(self):
        system.listUserSystems(
            self.sw
        )
        self.sw.session.system.listUserSystems.\
            assert_called_with(
                self.sw.key
            )
        system.listUserSystems(
            self.sw,
            'login'
        )
        self.sw.session.system.listUserSystems.\
            assert_called_with(
                self.sw.key,
                'login'
            )

    def test_fail_listUserSystems(self):
        self.assertRaises(
            Exception,
            system.listUserSystems,
            False,
            'login'
        )

    def test_listVirtualGuests(self):
        system.listVirtualGuests(
            self.sw,
            1
        )
        self.sw.session.system.listVirtualGuests.\
            assert_called_with(
                self.sw.key,
                1
            )

    def test_fail_listVirtualGuests(self):
        self.assertRaises(
            Exception,
            system.listVirtualGuests,
            False,
            1
        )

    def test_listVirtualHosts(self):
        system.listVirtualHosts(
            self.sw
        )
        self.sw.session.system.listVirtualHosts.\
            assert_called_with(
                self.sw.key
            )

    def test_fail_listVirtualHosts(self):
        self.assertRaises(
            Exception,
            system.listVirtualHosts,
            False
        )

    def test_obtainReactivationKey(self):
        system.obtainReactivationKey(
            self.sw,
            1
        )
        self.sw.session.system.obtainReactivationKey.\
            assert_called_with(
                self.sw.key,
                1
            )

    def test_fail_obtainReactivationKey(self):
        self.assertRaises(
            Exception,
            system.obtainReactivationKey,
            False,
            1
        )

    def test_provisionSystem(self):
        system.provisionSystem(
            self.sw,
            1,
            'profile_name'
        )
        self.sw.session.system.provisionSystem.\
            assert_called_with(
                self.sw.key,
                1,
                'profile_name'
            )
        system.provisionSystem(
            self.sw,
            1,
            'profile_name',
            date_time='date'
        )
        self.sw.session.system.provisionSystem.\
            assert_called_with(
                self.sw.key,
                1,
                'profile_name',
                'date'
            )

    def test_fail_provisionSystem(self):
        self.assertRaises(
            Exception,
            system.provisionSystem,
            False,
            1,
            'profile_name'
        )

    def test_provisionVirtualGuest(self):
        system.provisionVirtualGuest(
            self.sw,
            1,
            'guest_name',
            'profile_name'
        )
        self.sw.session.system.provisionVirtualGuest.\
            assert_called_with(
                self.sw.key,
                1,
                'guest_name',
                'profile_name'
            )
        system.provisionVirtualGuest(
            self.sw,
            1,
            'guest_name',
            'profile_name',
            'memorymb',
            'vcpus',
            'storagegb'
        )
        self.sw.session.system.provisionVirtualGuest.\
            assert_called_with(
                self.sw.key,
                1,
                'guest_name',
                'profile_name',
                'memorymb',
                'vcpus',
                'storagegb'
            )
        system.provisionVirtualGuest(
            self.sw,
            1,
            'guest_name',
            'profile_name',
            'memorymb',
            'vcpus',
            'storagegb',
            'macaddress'
        )
        self.sw.session.system.provisionVirtualGuest.\
            assert_called_with(
                self.sw.key,
                1,
                'guest_name',
                'profile_name',
                'memorymb',
                'vcpus',
                'storagegb',
                'macaddress'
            )

    def test_fail_provisionVirtualGuest(self):
        self.assertRaises(
            Exception,
            system.provisionVirtualGuest,
            False,
            1,
            'profile_name',
            'date_time'
        )

    def test_removeEntitlements(self):
        system.removeEntitlements(
            self.sw,
            1,
            'entitlement_labels'
        )
        self.sw.session.system.removeEntitlements.\
            assert_called_with(
                self.sw.key,
                1,
                'entitlement_labels'
            )

    def test_fail_removeEntitlements(self):
        self.assertRaises(
            Exception,
            system.removeEntitlements,
            False,
            1,
            'entitlement_labels'
        )

    def test_scheduleApplyErrata(self):
        system.scheduleApplyErrata(
            self.sw,
            server_ids=['server_ids'],
            errata_ids=['errata_ids'],
            date_time='now'
        )
        self.sw.session.system.scheduleApplyErrata.\
            assert_called_with(
                self.sw.key,
                ['server_ids'],
                ['errata_ids'],
                'now'
            )
        system.scheduleApplyErrata(
            self.sw,
            server_ids=['server_ids'],
            errata_ids=['errata_ids']
        )
        self.sw.session.system.scheduleApplyErrata.\
            assert_called_with(
                self.sw.key,
                ['server_ids'],
                ['errata_ids']
            )
        system.scheduleApplyErrata(
            self.sw,
            server_ids=1,
            errata_ids=['errata_ids'],
            date_time='now'
        )
        self.sw.session.system.scheduleApplyErrata.\
            assert_called_with(
                self.sw.key,
                1,
                ['errata_ids'],
                'now'
            )
        system.scheduleApplyErrata(
            self.sw,
            server_ids=1,
            errata_ids=['errata_ids']
        )
        self.sw.session.system.scheduleApplyErrata.\
            assert_called_with(
                self.sw.key,
                1,
                ['errata_ids']
            )

    def test_fail_scheduleApplyErrata(self):
        self.assertRaises(
            Exception,
            system.scheduleApplyErrata,
            False,
            server_ids=1,
            errata_ids=['errata_ids']
        )

    def test_scheduleGuestAction(self):
        system.scheduleGuestAction(
            self.sw,
            1,
            'state',
            'date_time'
        )
        self.sw.session.system.scheduleGuestAction.\
            assert_called_with(
                self.sw.key,
                1,
                'state',
                'date_time'
            )
        system.scheduleGuestAction(
            self.sw,
            1,
            'state'
        )
        self.sw.session.system.scheduleGuestAction.\
            assert_called_with(
                self.sw.key,
                1,
                'state'
            )

    def test_fail_scheduleGuestAction(self):
        self.assertRaises(
            Exception,
            system.scheduleGuestAction,
            False,
            1,
            'state'
        )

    def test_scheduleHardwareRefresh(self):
        system.scheduleHardwareRefresh(
            self.sw,
            1,
            'date_time'
        )
        self.sw.session.system.scheduleHardwareRefresh.\
            assert_called_with(
                self.sw.key,
                1,
                'date_time'
            )

    def test_fail_scheduleHardwareRefresh(self):
        self.assertRaises(
            Exception,
            system.scheduleHardwareRefresh,
            False,
            1,
            'date_time'
        )

    def test_schedulePackageInstall(self):
        system.schedulePackageInstall(
            self.sw,
            1,
            'packagelist',
            'date_time'
        )
        self.sw.session.system.schedulePackageInstall.\
            assert_called_with(
                self.sw.key,
                1,
                'packagelist',
                'date_time'
            )

    def test_fail_schedulePackageInstall(self):
        self.assertRaises(
            Exception,
            system.schedulePackageInstall,
            False,
            1,
            'packagelist',
            'date_time'
        )

    def test_schedulePackageRefresh(self):
        system.schedulePackageRefresh(
            self.sw,
            1,
            'date_time'
        )
        self.sw.session.system.schedulePackageRefresh.\
            assert_called_with(
                self.sw.key,
                1,
                'date_time'
            )

    def test_fail_schedulePackageRefresh(self):
        self.assertRaises(
            Exception,
            system.schedulePackageRefresh,
            False,
            1,
            'date_time'
        )

    def test_schedulePackageRemove(self):
        system.schedulePackageRemove(
            self.sw,
            1,
            ['package_id'],
            'date_time'
        )
        self.sw.session.system.schedulePackageRemove.\
            assert_called_with(
                self.sw.key,
                1,
                ['package_id'],
                'date_time'
            )

    def test_fail_schedulePackageRemove(self):
        self.assertRaises(
            Exception,
            system.schedulePackageRemove,
            False,
            1,
            ['package_id'],
            'date_time'
        )

    def test_scheduleReboot(self):
        system.scheduleReboot(
            self.sw,
            1,
            'date_time'
        )
        self.sw.session.system.scheduleReboot.\
            assert_called_with(
                self.sw.key,
                1,
                'date_time'
            )

    def test_fail_scheduleReboot(self):
        self.assertRaises(
            Exception,
            system.scheduleReboot,
            False,
            1,
            'date_time'
        )

    def test_scheduleScriptRun(self):
        system.scheduleScriptRun(
            self.sw,
            'servers',
            'user',
            'group',
            'timeout',
            'script',
            'date_time'
        )
        self.sw.session.system.scheduleScriptRun.\
            assert_called_with(
                self.sw.key,
                'servers',
                'user',
                'group',
                'timeout',
                'script',
                'date_time'
            )

    def test_fail_scheduleScriptRun(self):
        self.assertRaises(
            Exception,
            system.scheduleScriptRun,
            False,
            'servers',
            'user',
            'group',
            'timeout',
            'script',
            'date_time'
        )

    def test_scheduleSyncPackagesWithSystem(self):
        system.scheduleSyncPackagesWithSystem(
            self.sw,
            1,
            2,
            ['package_info'],
            'date_time'
        )
        self.sw.session.system.scheduleSyncPackagesWithSystem.\
            assert_called_with(
                self.sw.key,
                1,
                2,
                ['package_info'],
                'date_time'
            )

    def test_fail_scheduleSyncPackagesWithSystem(self):
        self.assertRaises(
            Exception,
            system.scheduleSyncPackagesWithSystem,
            False,
            1,
            2,
            ['package_info'],
            'date_time'
        )

    def test_searchByName(self):
        system.searchByName(
            self.sw,
            'name'
        )
        self.sw.session.system.searchByName.\
            assert_called_with(
                self.sw.key,
                'name'
            )

    def test_fail_searchByName(self):
        self.assertRaises(
            Exception,
            system.searchByName,
            False,
            'name'
        )

    def test_setBaseChannel(self):
        system.setBaseChannel(
            self.sw,
            1,
            'channel_label'
        )
        self.sw.session.system.setBaseChannel.\
            assert_called_with(
                self.sw.key,
                1,
                'channel_label'
            )

    def test_fail_setBaseChannel(self):
        self.assertRaises(
            Exception,
            system.setBaseChannel,
            False,
            1,
            'channel_label'
        )

    def test_setChildChannels(self):
        system.setChildChannels(
            self.sw,
            1,
            'channel_label'
        )
        self.sw.session.system.setChildChannels.\
            assert_called_with(
                self.sw.key,
                1,
                'channel_label'
            )

    def test_fail_setChildChannels(self):
        self.assertRaises(
            Exception,
            system.setChildChannels,
            False,
            1,
            'channel_label'
        )

    def test_setCustomValues(self):
        system.setCustomValues(
            self.sw,
            1,
            {'label': 'value'}
        )
        self.sw.session.system.setCustomValues.\
            assert_called_with(
                self.sw.key,
                1,
                {'label': 'value'}
            )

    def test_fail_setCustomValues(self):
        self.assertRaises(
            Exception,
            system.setCustomValues,
            False,
            1,
            {'label': 'value'}
        )

    def test_setDetails(self):
        system.setDetails(
            self.sw,
            1,
            {'profile_name': 'test'}
        )
        self.sw.session.system.setDetails.\
            assert_called_with(
                self.sw.key,
                1,
                {'profile_name': 'test'}
            )

    def test_fail_setDetails(self):
        self.assertRaises(
            Exception,
            system.setDetails,
            False,
            1,
            {'profile_name': 'test'}
        )

    def test_setGroupMembership(self):
        system.setGroupMembership(
            self.sw,
            1,
            2,
            True
        )
        self.sw.session.system.setGroupMembership.\
            assert_called_with(
                self.sw.key,
                1,
                2,
                True
            )

    def test_fail_setGroupMembership(self):
        self.assertRaises(
            Exception,
            system.setGroupMembership,
            False,
            1,
            2,
            True
        )

    def test_setGuestCpus(self):
        system.setGuestCpus(
            self.sw,
            1,
            4
        )
        self.sw.session.system.setGuestCpus.\
            assert_called_with(
                self.sw.key,
                1,
                4
            )

    def test_fail_setGuestCpus(self):
        self.assertRaises(
            Exception,
            system.setGuestCpus,
            False,
            1,
            4
        )

    def test_setGuestMemory(self):
        system.setGuestMemory(
            self.sw,
            1,
            2048
        )
        self.sw.session.system.setGuestMemory.\
            assert_called_with(
                self.sw.key,
                1,
                2048
            )

    def test_fail_setGuestMemory(self):
        self.assertRaises(
            Exception,
            system.setGuestMemory,
            False,
            1,
            2048
        )

    def test_setLockStatus(self):
        system.setLockStatus(
            self.sw,
            1,
            True
        )
        self.sw.session.system.setLockStatus.\
            assert_called_with(
                self.sw.key,
                1,
                True
            )

    def test_fail_setLockStatus(self):
        self.assertRaises(
            Exception,
            system.setLockStatus,
            False,
            1,
            True
        )

    def test_setProfileName(self):
        system.setProfileName(
            self.sw,
            1,
            'name'
        )
        self.sw.session.system.setProfileName.\
            assert_called_with(
                self.sw.key,
                1,
                'name'
            )

    def test_fail_setProfileName(self):
        self.assertRaises(
            Exception,
            system.setProfileName,
            False,
            1,
            'name'
        )

    def test_setVariables(self):
        system.setVariables(
            self.sw,
            1,
            False,
            [{'ks': 'var'}]
        )
        self.sw.session.system.setVariables.\
            assert_called_with(
                self.sw.key,
                1,
                False,
                [{'ks': 'var'}]
            )

    def test_fail_setVariables(self):
        self.assertRaises(
            Exception,
            system.setVariables,
            False,
            1,
            False,
            [{'ks': 'var'}]
        )

    def test_tagLatestSnapshot(self):
        system.tagLatestSnapshot(
            self.sw,
            1,
            'tagname'
        )
        self.sw.session.system.tagLatestSnapshot.\
            assert_called_with(
                self.sw.key,
                1,
                'tagname'
            )

    def test_fail_tagLatestSnapshot(self):
        self.assertRaises(
            Exception,
            system.tagLatestSnapshot,
            False,
            1,
            'tagname'
        )

    def test_upgradeEntitlement(self):
        system.upgradeEntitlement(
            self.sw,
            1,
            'entitlementname'
        )
        self.sw.session.system.upgradeEntitlement.\
            assert_called_with(
                self.sw.key,
                1,
                'entitlementname'
            )

    def test_fail_upgradeEntitlement(self):
        self.assertRaises(
            Exception,
            system.upgradeEntitlement,
            False,
            1,
            'entitlementname'
        )

    def test_whoRegistered(self):
        system.whoRegistered(
            self.sw,
            1
        )
        self.sw.session.system.whoRegistered.\
            assert_called_with(
                self.sw.key,
                1
            )

    def test_fail_whoRegistered(self):
        self.assertRaises(
            Exception,
            system.whoRegistered,
            False,
            1
        )


class TestSystemConfig(unittest.TestCase):

    def setUp(self):
        self.sw = mock.Mock()

    def test_addChannels(self):
        config.addChannels(
            self.sw,
            ['system_ids'],
            ['configuration_channels'],
            True
        )
        self.sw.session.system.config.addChannels.\
            assert_called_with(
                self.sw.key,
                ['system_ids'],
                ['configuration_channels'],
                True
            )

    def test_fail_addChannels(self):
        self.assertRaises(
            Exception,
            config.addChannels,
            False,
            ['system_ids'],
            ['configuration_channels'],
            True
        )

    def test_createOrUpdatePath(self):
        config.createOrUpdatePath(
            self.sw,
            1,
            'path',
            True,
            {'path_info': 'blah'},
            1
        )
        self.sw.session.system.config.createOrUpdatePath.\
            assert_called_with(
                self.sw.key,
                1,
                'path',
                True,
                {'path_info': 'blah'},
                1
            )

    def test_fail_createOrUpdatePath(self):
        self.assertRaises(
            Exception,
            config.createOrUpdatePath,
            False,
            1,
            'path',
            True,
            {'path_info': 'blah'},
            1
        )

    def test_createOrUpdateSymlink(self):
        config.createOrUpdateSymlink(
            self.sw,
            1,
            'path',
            {'path_info': 'blah'},
            1
        )
        self.sw.session.system.config.createOrUpdateSymlink.\
            assert_called_with(
                self.sw.key,
                1,
                'path',
                {'path_info': 'blah'},
                1
            )

    def test_fail_createOrUpdateSymlink(self):
        self.assertRaises(
            Exception,
            config.createOrUpdateSymlink,
            False,
            1,
            'path',
            {'path_info': 'blah'},
            1
        )

    def test_deleteFiles(self):
        config.deleteFiles(
            self.sw,
            1,
            ['paths'],
            True
        )
        self.sw.session.system.config.deleteFiles.\
            assert_called_with(
                self.sw.key,
                1,
                ['paths'],
                True
            )

    def test_fail_deleteFiles(self):
        self.assertRaises(
            Exception,
            config.deleteFiles,
            False,
            1,
            ['paths'],
            True
        )

    def test_deployAll(self):
        config.deployAll(
            self.sw,
            ['system_ids']
        )
        self.sw.session.system.config.deployAll.\
            assert_called_with(
                self.sw.key,
                ['system_ids']
            )

    def test_fail_deployAll(self):
        self.assertRaises(
            Exception,
            config.deployAll,
            False,
            ['system_ids']
        )

    def test_listChannels(self):
        config.listChannels(
            self.sw,
            1
        )
        self.sw.session.system.config.listChannels.\
            assert_called_with(
                self.sw.key,
                1
            )

    def test_fail_listChannels(self):
        self.assertRaises(
            Exception,
            config.listChannels,
            False,
            1
        )

    def test_listFiles(self):
        config.listFiles(
            self.sw,
            1,
            0
        )
        self.sw.session.system.config.listFiles.\
            assert_called_with(
                self.sw.key,
                1,
                0
            )

    def test_fail_listFiles(self):
        self.assertRaises(
            Exception,
            config.listFiles,
            False,
            1,
            0
        )

    def test_lookupFileInfo(self):
        config.lookupFileInfo(
            self.sw,
            1,
            ['paths'],
            0
        )
        self.sw.session.system.config.lookupFileInfo.\
            assert_called_with(
                self.sw.key,
                1,
                ['paths'],
                0
            )

    def test_fail_lookupFileInfo(self):
        self.assertRaises(
            Exception,
            config.lookupFileInfo,
            False,
            1,
            ['paths'],
            0
        )

    def test_removeChannels(self):
        config.removeChannels(
            self.sw,
            [1],
            ['channel_labels']
        )
        self.sw.session.system.config.removeChannels.\
            assert_called_with(
                self.sw.key,
                [1],
                ['channel_labels']
            )

    def test_fail_removeChannels(self):
        self.assertRaises(
            Exception,
            config.removeChannels,
            False,
            [1],
            ['channel_labels']
        )

    def test_setChannels(self):
        config.setChannels(
            self.sw,
            [1],
            ['channel_labels']
        )
        self.sw.session.system.config.setChannels.\
            assert_called_with(
                self.sw.key,
                [1],
                ['channel_labels']
            )

    def test_fail_setChannels(self):
        self.assertRaises(
            Exception,
            config.setChannels,
            False,
            [1],
            ['channel_labels']
        )


class TestSystemCustomInfo(unittest.TestCase):

    def setUp(self):
        self.sw = mock.Mock()

    def test_createKey(self):
        custominfo.createKey(
            self.sw,
            'keylabel',
            'keydescription'
        )
        self.sw.session.system.custominfo.createKey.\
            assert_called_with(
                self.sw.key,
                'keylabel',
                'keydescription'
            )

    def test_fail_createKey(self):
        self.assertRaises(
            Exception,
            custominfo.createKey,
            False,
            'keylabel',
            'keydescription'
        )

    def test_deleteKey(self):
        custominfo.deleteKey(
            self.sw,
            'keylabel'
        )
        self.sw.session.system.custominfo.deleteKey.\
            assert_called_with(
                self.sw.key,
                'keylabel'
            )

    def test_fail_deleteKey(self):
        self.assertRaises(
            Exception,
            custominfo.deleteKey,
            False,
            'keylabel'
        )

    def test_listAllKeys(self):
        custominfo.listAllKeys(
            self.sw
        )
        self.sw.session.system.custominfo.listAllKeys.\
            assert_called_with(
                self.sw.key
            )

    def test_fail_listAllKeys(self):
        self.assertRaises(
            Exception,
            custominfo.listAllKeys,
            False
        )

    def test_updateKey(self):
        custominfo.updateKey(
            self.sw,
            'keylabel',
            'keydescription'
        )
        self.sw.session.system.custominfo.updateKey.\
            assert_called_with(
                self.sw.key,
                'keylabel',
                'keydescription'
            )

    def test_fail_updateKey(self):
        self.assertRaises(
            Exception,
            custominfo.updateKey,
            False,
            'keylabel',
            'keydescription'
        )


class TestSystemScap(unittest.TestCase):

    def setUp(self):
        self.sw = mock.Mock()

    def test_getXccdfScanDetails(self):
        scap.getXccdfScanDetails(
            self.sw,
            1
        )
        self.sw.session.system.scap.getXccdfScanDetails.\
            assert_called_with(
                self.sw.key,
                1
            )

    def test_fail_getXccdfScanDetails(self):
        self.assertRaises(
            Exception,
            scap.getXccdfScanDetails,
            False,
            1
        )

    def test_getXccdfScanRuleResults(self):
        scap.getXccdfScanRuleResults(
            self.sw,
            1
        )
        self.sw.session.system.scap.getXccdfScanRuleResults.\
            assert_called_with(
                self.sw.key,
                1
            )

    def test_fail_getXccdfScanRuleResults(self):
        self.assertRaises(
            Exception,
            scap.getXccdfScanRuleResults,
            False,
            1
        )

    def test_listXccdfScans(self):
        scap.listXccdfScans(
            self.sw,
            1
        )
        self.sw.session.system.scap.listXccdfScans.\
            assert_called_with(
                self.sw.key,
                1
            )

    def test_fail_listXccdfScans(self):
        self.assertRaises(
            Exception,
            scap.listXccdfScans,
            False,
            1
        )

    def test_scheduleXccdfScan(self):
        scap.scheduleXccdfScan(
            self.sw,
            1,
            '/path',
            'additional things',
            date_time='date_time'
        )
        self.sw.session.system.scap.scheduleXccdfScan.\
            assert_called_with(
                self.sw.key,
                1,
                '/path',
                'additional things',
                'date_time'
            )
        scap.scheduleXccdfScan(
            self.sw,
            1,
            '/path',
            'additional things'
        )
        self.sw.session.system.scap.scheduleXccdfScan.\
            assert_called_with(
                self.sw.key,
                1,
                '/path',
                'additional things',
            )

    def test_fail_scheduleXccdfScan(self):
        self.assertRaises(
            Exception,
            scap.scheduleXccdfScan,
            False,
            1,
            '/path',
            'additional things',
            date_time='date_time'
        )


class TestSystemSearch(unittest.TestCase):

    def setUp(self):
        self.sw = mock.Mock()

    def test_deviceDescription(self):
        search.deviceDescription(
            self.sw,
            'search_term'
        )
        self.sw.session.system.search.deviceDescription.\
            assert_called_with(
                self.sw.key,
                'search_term'
            )

    def test_fail_deviceDescription(self):
        self.assertRaises(
            Exception,
            search.deviceDescription,
            False,
            'search_term'
        )

    def test_deviceDriver(self):
        search.deviceDriver(
            self.sw,
            'search_term'
        )
        self.sw.session.system.search.deviceDriver.\
            assert_called_with(
                self.sw.key,
                'search_term'
            )

    def test_fail_deviceDriver(self):
        self.assertRaises(
            Exception,
            search.deviceDriver,
            False,
            'search_term'
        )

    def test_deviceId(self):
        search.deviceId(
            self.sw,
            'search_term'
        )
        self.sw.session.system.search.deviceId.\
            assert_called_with(
                self.sw.key,
                'search_term'
            )

    def test_fail_deviceId(self):
        self.assertRaises(
            Exception,
            search.deviceId,
            False,
            'search_term'
        )

    def test_deviceVendorId(self):
        search.deviceVendorId(
            self.sw,
            'search_term'
        )
        self.sw.session.system.search.deviceVendorId.\
            assert_called_with(
                self.sw.key,
                'search_term'
            )

    def test_fail_deviceVendorId(self):
        self.assertRaises(
            Exception,
            search.deviceVendorId,
            False,
            'search_term'
        )

    def test_hostname(self):
        search.hostname(
            self.sw,
            'search_term'
        )
        self.sw.session.system.search.hostname.\
            assert_called_with(
                self.sw.key,
                'search_term'
            )

    def test_fail_hostname(self):
        self.assertRaises(
            Exception,
            search.hostname,
            False,
            'search_term'
        )

    def test_ip(self):
        search.ip(
            self.sw,
            'search_term'
        )
        self.sw.session.system.search.ip.\
            assert_called_with(
                self.sw.key,
                'search_term'
            )

    def test_fail_ip(self):
        self.assertRaises(
            Exception,
            search.ip,
            False,
            'search_term'
        )

    def test_nameAndDescription(self):
        search.nameAndDescription(
            self.sw,
            'search_term'
        )
        self.sw.session.system.search.nameAndDescription.\
            assert_called_with(
                self.sw.key,
                'search_term'
            )

    def test_fail_nameAndDescription(self):
        self.assertRaises(
            Exception,
            search.nameAndDescription,
            False,
            'search_term'
        )

    def test_uuid(self):
        search.uuid(
            self.sw,
            'search_term'
        )
        self.sw.session.system.search.uuid.\
            assert_called_with(
                self.sw.key,
                'search_term'
            )

    def test_fail_uuid(self):
        self.assertRaises(
            Exception,
            search.uuid,
            False,
            'search_term'
        )

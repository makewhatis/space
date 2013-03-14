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

from space.lib import kickstart
from space.lib.kickstart import filepreservation
from space.lib.kickstart import keys
from space.lib.kickstart import profile
from space.lib.kickstart.profile import keys as profile_keys
from space.lib.kickstart.profile import software as profile_software
from space.lib.kickstart.profile import system as profile_system
from space.lib.kickstart import snippet
from space.lib.kickstart import tree


class TestKickstart(unittest.TestCase):

    def setUp(self):
        self.sw = mock.Mock()

    def test_cloneProfile(self):
        kickstart.cloneProfile(
            self.sw,
            'test',
            'test'
        )
        self.sw.session.kickstart.cloneProfile.\
            assert_called_with(
                self.sw.key,
                'test',
                'test'
            )

    def test_fail_cloneProfile(self):
        self.assertRaises(
            Exception,
            kickstart.cloneProfile,
            False,
            'test',
            'test'
        )

    def test_createProfile(self):
        kickstart.createProfile(
            self.sw,
            'test',
            'test',
            'test',
            'test',
            'test'
        )
        self.sw.session.kickstart.createProfile.\
            assert_called_with(
                self.sw.key,
                'test',
                'test',
                'test',
                'test',
                'test'
            )

    def test_fail_createProfile(self):
        self.assertRaises(
            Exception,
            kickstart.createProfile,
            False,
            'test',
            'test',
            'test',
            'test',
            'test'
        )

    def test_createProfileWithCustomUrl(self):
        kickstart.createProfileWithCustomUrl(
            self.sw,
            'test',
            'test',
            'test',
            'test',
            'test'

        )
        self.sw.session.kickstart.createProfileWithCustomUrl.\
            assert_called_with(
                self.sw.key,
                'test',
                'test',
                'test',
                'test',
                'test'
            )

    def test_fail_createProfileWithCustomUrl(self):
        self.assertRaises(
            Exception,
            kickstart.createProfileWithCustomUrl,
            False,
            'test',
            'test',
            'test',
            'test',
            'test'
        )

    def test_deleteProfile(self):
        kickstart.deleteProfile(
            self.sw,
            'test'
        )
        self.sw.session.kickstart.deleteProfile.\
            assert_called_with(
                self.sw.key,
                'test'
            )

    def test_fail_deleteProfile(self):
        self.assertRaises(
            Exception,
            kickstart.deleteProfile,
            False,
            'test'
        )

    def test_disableProfile(self):
        kickstart.disableProfile(
            self.sw,
            'test',
            'test'
        )
        self.sw.session.kickstart.disableProfile.\
            assert_called_with(
                self.sw.key,
                'test',
                'test'
            )

    def test_fail_disableProfile(self):
        self.assertRaises(
            Exception,
            kickstart.disableProfile,
            False,
            'test',
            'test'
        )

    def test_findKickstartForIp(self):
        kickstart.findKickstartForIp(
            self.sw,
            'test'
        )
        self.sw.session.kickstart.findKickstartForIp.\
            assert_called_with(
                self.sw.key,
                'test'
            )

    def test_fail_findKickstartForIp(self):
        self.assertRaises(
            Exception,
            kickstart.findKickstartForIp,
            False,
            'test'
        )

    def test_importFile(self):
        kickstart.importFile(
            self.sw,
            'test',
            'test',
            'test',
            'test'
        )
        self.sw.session.kickstart.importFile.\
            assert_called_with(
                self.sw.key,
                'test',
                'test',
                'test',
                'test'
            )
        kickstart.importFile(
            self.sw,
            'test',
            'test',
            'test',
            'test',
            kickstarthost='test'
        )
        self.sw.session.kickstart.importFile.\
            assert_called_with(
                self.sw.key,
                'test',
                'test',
                'test',
                'test',
                'test'
            )

    def test_fail_importFile(self):
        self.assertRaises(
            Exception,
            kickstart.importFile,
            False,
            'test',
            'test',
            'test',
            'test'
        )
        self.assertRaises(
            Exception,
            kickstart.importFile,
            False,
            'test',
            'test',
            'test',
            'test',
            kickstarthost='blah'
        )

    def test_importRawFile(self):
        kickstart.importRawFile(
            self.sw,
            'test',
            'test',
            'test',
            'test'
        )
        self.sw.session.kickstart.importRawFile.\
            assert_called_with(
                self.sw.key,
                'test',
                'test',
                'test',
                'test'
            )

    def test_fail_importRawFile(self):
        self.assertRaises(
            Exception,
            kickstart.importRawFile,
            False,
            'test',
            'test',
            'test',
            'test'
        )

    def test_isProfileDisabled(self):
        kickstart.isProfileDisabled(
            self.sw,
            'test'
        )
        self.sw.session.kickstart.isProfileDisabled.\
            assert_called_with(
                self.sw.key,
                'test'
            )

    def test_fail_isProfileDisabled(self):
        self.assertRaises(
            Exception,
            kickstart.isProfileDisabled,
            False,
            'test'
        )

    def test_listAllIpRanges(self):
        kickstart.listAllIpRanges(
            self.sw
        )
        self.sw.session.kickstart.listAllIpRanges.\
            assert_called_with(
                self.sw.key
            )

    def test_fail_listAllIpRanges(self):
        self.assertRaises(
            Exception,
            kickstart.listAllIpRanges,
            False,
        )

    def test_listKickstartableChannels(self):
        kickstart.listKickstartableChannels(
            self.sw
        )
        self.sw.session.kickstart.listKickstartableChannels.\
            assert_called_with(
                self.sw.key
            )

    def test_fail_listKickstartableChannels(self):
        self.assertRaises(
            Exception,
            kickstart.listKickstartableChannels,
            False,
        )

    def test_listKickstarts(self):
        kickstart.listKickstarts(
            self.sw
        )
        self.sw.session.kickstart.listKickstarts.\
            assert_called_with(
                self.sw.key
            )

    def test_fail_listKickstarts(self):
        self.assertRaises(
            Exception,
            kickstart.listKickstarts,
            False,
        )

    def test_renameProfile(self):
        kickstart.renameProfile(
            self.sw,
            'test',
            'test'
        )
        self.sw.session.kickstart.renameProfile.\
            assert_called_with(
                self.sw.key,
                'test',
                'test'
            )

    def test_fail_renameProfile(self):
        self.assertRaises(
            Exception,
            kickstart.renameProfile,
            False,
            'test',
            'test'
        )


class TestKickstartFilepreservation(unittest.TestCase):

    def setUp(self):
        self.sw = mock.Mock()

    def test_create(self):
        filepreservation.create(
            self.sw,
            'test',
            'test'
        )
        self.sw.session.kickstart.filepreservation.create.\
            assert_called_with(
                self.sw.key,
                'test',
                'test'
            )

    def test_fail_create(self):
        self.assertRaises(
            Exception,
            filepreservation.create,
            False,
            'test',
            'test'
        )

    def test_delete(self):
        filepreservation.delete(
            self.sw,
            'test'

        )
        self.sw.session.kickstart.filepreservation.delete.\
            assert_called_with(
                self.sw.key,
                'test'
            )

    def test_fail_delete(self):
        self.assertRaises(
            Exception,
            filepreservation.delete,
            False,
            'test'
        )

    def test_getDetails(self):
        filepreservation.getDetails(
            self.sw,
            'test'
        )
        self.sw.session.kickstart.filepreservation.getDetails.\
            assert_called_with(
                self.sw.key,
                'test'
            )

    def test_fail_getDetails(self):
        self.assertRaises(
            Exception,
            filepreservation.getDetails,
            False,
            'test'
        )

    def test_listAllFilePreservations(self):
        filepreservation.listAllFilePreservations(
            self.sw
        )
        self.sw.session.kickstart.filepreservation.listAllFilePreservations.\
            assert_called_with(
                self.sw.key
            )

    def test_fail_listAllFilePreservations(self):
        self.assertRaises(
            Exception,
            filepreservation.listAllFilePreservations,
            False
        )


class TestKickstartKeys(unittest.TestCase):

    def setUp(self):
        self.sw = mock.Mock()

    def test_create(self):
        keys.create(
            self.sw,
            'test',
            'test',
            'test'
        )
        self.sw.session.kickstart.keys.create.\
            assert_called_with(
                self.sw.key,
                'test',
                'test',
                'test'
            )

    def test_fail_create(self):
        self.assertRaises(
            Exception,
            keys.create,
            False,
            'test',
            'test',
            'test'
        )

    def test_delete(self):
        keys.delete(
            self.sw,
            'test'
        )
        self.sw.session.kickstart.keys.delete.\
            assert_called_with(
                self.sw.key,
                'test'
            )

    def test_fail_delete(self):
        self.assertRaises(
            Exception,
            keys.delete,
            False,
            'test'
        )

    def test_getDetails(self):
        keys.getDetails(
            self.sw,
            'test'
        )
        self.sw.session.kickstart.keys.getDetails.\
            assert_called_with(
                self.sw.key,
                'test'
            )

    def test_fail_getDetails(self):
        self.assertRaises(
            Exception,
            keys.getDetails,
            False,
            'test'
        )

    def test_listAllKeys(self):
        keys.listAllKeys(
            self.sw
        )
        self.sw.session.kickstart.keys.listAllKeys.\
            assert_called_with(
                self.sw.key
            )

    def test_fail_listAllKeys(self):
        self.assertRaises(
            Exception,
            keys.listAllKeys,
            False,
        )

    def test_update(self):
        keys.update(
            self.sw,
            'test',
            'test',
            'test'
        )
        self.sw.session.kickstart.keys.update.\
            assert_called_with(
                self.sw.key,
                'test',
                'test',
                'test'
            )

    def test_fail_update(self):
        self.assertRaises(
            Exception,
            keys.update,
            False,
            'test',
            'test',
            'test'
        )


class TestKickstartProfile(unittest.TestCase):

    def setUp(self):
        self.sw = mock.Mock()

    def test_addIpRange(self):
        profile.addIpRange(
            self.sw,
            'test',
            'test',
            'test',
        )
        self.sw.session.kickstart.profile.addIpRange.\
            assert_called_with(
                self.sw.key,
                'test',
                'test',
                'test',
            )

    def test_fail_addIpRange(self):
        self.assertRaises(
            Exception,
            profile.addIpRange,
            False,
            'test',
            'test',
            'test',
        )

    def test_addScript(self):
        profile.addScript(
            self.sw,
            'test',
            'test',
            'test',
            'test',
            'test',
            'test'
        )
        self.sw.session.kickstart.profile.addScript.\
            assert_called_with(
                self.sw.key,
                'test',
                'test',
                'test',
                'test',
                'test',
                'test'
            )

    def test_fail_addScript(self):
        self.assertRaises(
            Exception,
            profile.addScript,
            False,
            'test',
            'test',
            'test',
            'test',
            'test',
            'test'
        )

    def test_compareActivationKeys(self):
        profile.compareActivationKeys(
            self.sw,
            'kickstartlabel1',
            'kickstartlabel2'
        )
        self.sw.session.kickstart.profile.compareActivationKeys.\
            assert_called_with(
                self.sw.key,
                'kickstartlabel1',
                'kickstartlabel2'
            )

    def test_fail_compareActivationKeys(self):
        self.assertRaises(
            Exception,
            profile.compareActivationKeys,
            False,
            'kickstartlabel1',
            'kickstartlabel2'
        )

    def test_compareAdvancedOptions(self):
        profile.compareAdvancedOptions(
            self.sw,
            'kickstartlabel1',
            'kickstartlabel2'
        )
        self.sw.session.kickstart.profile.compareAdvancedOptions.\
            assert_called_with(
                self.sw.key,
                'kickstartlabel1',
                'kickstartlabel2'
            )

    def test_fail_compareAdvancedOptions(self):
        self.assertRaises(
            Exception,
            profile.compareAdvancedOptions,
            False,
            'kickstartlabel1',
            'kickstartlabel2'
        )

    def test_comparePackages(self):
        profile.comparePackages(
            self.sw,
            'kickstartlabel1',
            'kickstartlabel2'
        )
        self.sw.session.kickstart.profile.comparePackages.\
            assert_called_with(
                self.sw.key,
                'kickstartlabel1',
                'kickstartlabel2'
            )

    def test_fail_comparePackages(self):
        self.assertRaises(
            Exception,
            profile.comparePackages,
            False,
            'kickstartlabel1',
            'kickstartlabel2'
        )

    def test_downloadKickstart(self):
        profile.downloadKickstart(
            self.sw,
            'kslabel',
            'host'
        )
        self.sw.session.kickstart.profile.downloadKickstart.\
            assert_called_with(
                self.sw.key,
                'kslabel',
                'host'
            )

    def test_fail_downloadKickstart(self):
        self.assertRaises(
            Exception,
            profile.downloadKickstart,
            False,
            'kslabel',
            'host'
        )

    def test_downloadRenderedKickstart(self):
        profile.downloadRenderedKickstart(
            self.sw,
            'kslabel'
        )
        self.sw.session.kickstart.profile.downloadRenderedKickstart.\
            assert_called_with(
                self.sw.key,
                'kslabel'
            )

    def test_fail_downloadRenderedKickstart(self):
        self.assertRaises(
            Exception,
            profile.downloadRenderedKickstart,
            False,
            'kslabel'
        )

    def test_getAdvancedOptions(self):
        profile.getAdvancedOptions(
            self.sw,
            'kslabel'
        )
        self.sw.session.kickstart.profile.getAdvancedOptions.\
            assert_called_with(
                self.sw.key,
                'kslabel'
            )

    def test_fail_getAdvancedOptions(self):
        self.assertRaises(
            Exception,
            profile.getAdvancedOptions,
            False,
            'kslabel'
        )

    def test_getCfgPreservation(self):
        profile.getCfgPreservation(
            self.sw,
            'kslabel'
        )
        self.sw.session.kickstart.profile.getCfgPreservation.\
            assert_called_with(
                self.sw.key,
                'kslabel'
            )

    def test_fail_getCfgPreservation(self):
        self.assertRaises(
            Exception,
            profile.getCfgPreservation,
            False,
            'kslabel'
        )

    def test_getChildChannels(self):
        profile.getChildChannels(
            self.sw,
            'kslabel'
        )
        self.sw.session.kickstart.profile.getChildChannels.\
            assert_called_with(
                self.sw.key,
                'kslabel'
            )

    def test_fail_getChildChannels(self):
        self.assertRaises(
            Exception,
            profile.getChildChannels,
            False,
            'kslabel'
        )

    def test_getCustomOptions(self):
        profile.getCustomOptions(
            self.sw,
            'kslabel'
        )
        self.sw.session.kickstart.profile.getCustomOptions.\
            assert_called_with(
                self.sw.key,
                'kslabel'
            )

    def test_fail_getCustomOptions(self):
        self.assertRaises(
            Exception,
            profile.getCustomOptions,
            False,
            'kslabel'
        )

    def test_getKickstartTree(self):
        profile.getKickstartTree(
            self.sw,
            'kslabel'
        )
        self.sw.session.kickstart.profile.getKickstartTree.\
            assert_called_with(
                self.sw.key,
                'kslabel'
            )

    def test_fail_getKickstartTree(self):
        self.assertRaises(
            Exception,
            profile.getKickstartTree,
            False,
            'kslabel'
        )

    def test_getVariables(self):
        profile.getVariables(
            self.sw,
            'kslabel'
        )
        self.sw.session.kickstart.profile.getVariables.\
            assert_called_with(
                self.sw.key,
                'kslabel'
            )

    def test_fail_getVariables(self):
        self.assertRaises(
            Exception,
            profile.getVariables,
            False,
            'kslabel'
        )

    def test_listIpRanges(self):
        profile.listIpRanges(
            self.sw,
            'kslabel'
        )
        self.sw.session.kickstart.profile.listIpRanges.\
            assert_called_with(
                self.sw.key,
                'kslabel'
            )

    def test_fail_listIpRanges(self):
        self.assertRaises(
            Exception,
            profile.listIpRanges,
            False,
            'kslabel'
        )

    def test_listScripts(self):
        profile.listScripts(
            self.sw,
            'kslabel'
        )
        self.sw.session.kickstart.profile.listScripts.\
            assert_called_with(
                self.sw.key,
                'kslabel'
            )

    def test_fail_listScripts(self):
        self.assertRaises(
            Exception,
            profile.listScripts,
            False,
            'kslabel'
        )

    def test_removeIpRange(self):
        profile.removeIpRange(
            self.sw,
            'kslabel'
        )
        self.sw.session.kickstart.profile.removeIpRange.\
            assert_called_with(
                self.sw.key,
                'kslabel'
            )

    def test_fail_removeIpRange(self):
        self.assertRaises(
            Exception,
            profile.removeIpRange,
            False,
            'kslabel'
        )

    def test_removeScript(self):
        profile.removeScript(
            self.sw,
            'kslabel',
            1
        )
        self.sw.session.kickstart.profile.removeScript.\
            assert_called_with(
                self.sw.key,
                'kslabel',
                1
            )

    def test_fail_removeScript(self):
        self.assertRaises(
            Exception,
            profile.removeScript,
            False,
            'kslabel',
            1
        )

    def test_setAdvancedOptions(self):
        profile.setAdvancedOptions(
            self.sw,
            'kslabel',
            ['options']
        )
        self.sw.session.kickstart.profile.setAdvancedOptions.\
            assert_called_with(
                self.sw.key,
                'kslabel',
                ['options']
            )

    def test_fail_setAdvancedOptions(self):
        self.assertRaises(
            Exception,
            profile.setAdvancedOptions,
            False,
            'kslabel',
            ['options']
        )

    def test_setCfgPreservation(self):
        profile.setCfgPreservation(
            self.sw,
            'kslabel',
            False
        )
        self.sw.session.kickstart.profile.setCfgPreservation.\
            assert_called_with(
                self.sw.key,
                'kslabel',
                False
            )

    def test_fail_setCfgPreservation(self):
        self.assertRaises(
            Exception,
            profile.setCfgPreservation,
            False,
            'kslabel',
            False
        )

    def test_setChildChannels(self):
        profile.setChildChannels(
            self.sw,
            'kslabel',
            ['channellabels']
        )
        self.sw.session.kickstart.profile.setChildChannels.\
            assert_called_with(
                self.sw.key,
                'kslabel',
                ['channellabels']
            )

    def test_fail_setChildChannels(self):
        self.assertRaises(
            Exception,
            profile.setChildChannels,
            False,
            'kslabel',
            ['channellabels']
        )

    def test_setCustomOptions(self):
        profile.setCustomOptions(
            self.sw,
            'kslabel',
            ['options']
        )
        self.sw.session.kickstart.profile.setCustomOptions.\
            assert_called_with(
                self.sw.key,
                'kslabel',
                ['options']
            )

    def test_fail_setCustomOptions(self):
        self.assertRaises(
            Exception,
            profile.setCustomOptions,
            False,
            'kslabel',
            ['options']
        )

    def test_setKickstartTree(self):
        profile.setKickstartTree(
            self.sw,
            'kslabel',
            'kstreelable'
        )
        self.sw.session.kickstart.profile.setKickstartTree.\
            assert_called_with(
                self.sw.key,
                'kslabel',
                'kstreelable'
            )

    def test_fail_setKickstartTree(self):
        self.assertRaises(
            Exception,
            profile.setKickstartTree,
            False,
            'kslabel',
            'kstreelable'
        )

    def test_setLogging(self):
        profile.setLogging(
            self.sw,
            'kslabel',
            False,
            True
        )
        self.sw.session.kickstart.profile.setLogging.\
            assert_called_with(
                self.sw.key,
                'kslabel',
                False,
                True
            )

    def test_fail_setLogging(self):
        self.assertRaises(
            Exception,
            profile.setLogging,
            False,
            'kslabel',
            False,
            True
        )

    def test_setVariables(self):
        profile.setVariables(
            self.sw,
            'kslabel',
            ['ksvars']
        )
        self.sw.session.kickstart.profile.setVariables.\
            assert_called_with(
                self.sw.key,
                'kslabel',
                ['ksvars']
            )

    def test_fail_setVariables(self):
        self.assertRaises(
            Exception,
            profile.setVariables,
            False,
            'kslabel',
            ['ksvars']
        )

    def test_addActivationKey(self):
        profile_keys.addActivationKey(
            self.sw,
            'kslabel',
            'keyname'
        )
        self.sw.session.kickstart.profile.keys.addActivationKey.\
            assert_called_with(
                self.sw.key,
                'kslabel',
                'keyname'
            )

    def test_fail_addActivationKey(self):
        self.assertRaises(
            Exception,
            profile_keys.addActivationKey,
            False,
            'kslabel',
            'keyname'
        )

    def test_getActivationKeys(self):
        profile_keys.getActivationKeys(
            self.sw,
            'kslabel'
        )
        self.sw.session.kickstart.profile.keys.getActivationKeys.\
            assert_called_with(
                self.sw.key,
                'kslabel'
            )

    def test_fail_getActivationKeys(self):
        self.assertRaises(
            Exception,
            profile_keys.getActivationKeys,
            False,
            'kslabel'
        )

    def test_removeActivationKey(self):
        profile_keys.removeActivationKey(
            self.sw,
            'kslabel',
            'keyname'
        )
        self.sw.session.kickstart.profile.keys.removeActivationKey.\
            assert_called_with(
                self.sw.key,
                'kslabel',
                'keyname'
            )

    def test_fail_removeActivationKey(self):
        self.assertRaises(
            Exception,
            profile_keys.removeActivationKey,
            False,
            'kslabel',
            'keyname'
        )

    def test_appendToSoftwareList(self):
        profile_software.appendToSoftwareList(
            self.sw,
            'kslabel'
        )
        self.sw.session.kickstart.profile.software.appendToSoftwareList.\
            assert_called_with(
                self.sw.key,
                'kslabel'
            )

    def test_fail_appendToSoftwareList(self):
        self.assertRaises(
            Exception,
            profile_software.appendToSoftwareList,
            False,
            'kslabel'
        )

    def test_getSoftwareList(self):
        profile_software.getSoftwareList(
            self.sw,
            'kslabel'
        )
        self.sw.session.kickstart.profile.software.getSoftwareList.\
            assert_called_with(
                self.sw.key,
                'kslabel'
            )

    def test_fail_getSoftwareList(self):
        self.assertRaises(
            Exception,
            profile_software.getSoftwareList,
            False,
            'kslabel'
        )

    def test_setSoftwareList(self):
        profile_software.setSoftwareList(
            self.sw,
            'kslabel',
            'packagelist'
        )
        self.sw.session.kickstart.profile.software.setSoftwareList.\
            assert_called_with(
                self.sw.key,
                'kslabel',
                'packagelist'
            )

    def test_fail_setSoftwareList(self):
        self.assertRaises(
            Exception,
            profile_software.setSoftwareList,
            False,
            'kslabel',
            'packagelist'
        )

    def test_addFilePreservations(self):
        profile_system.addFilePreservations(
            self.sw,
            'kslabel',
            'filepreservations'
        )
        self.sw.session.kickstart.profile.system.addFilePreservations.\
            assert_called_with(
                self.sw.key,
                'kslabel',
                'filepreservations'
            )

    def test_fail_addFilePreservations(self):
        self.assertRaises(
            Exception,
            profile_system.addFilePreservations,
            False,
            'kslabel',
            'filepreservations'
        )

    def test_addKeys(self):
        profile_system.addKeys(
            self.sw,
            'kslabel',
            'keydesc'
        )
        self.sw.session.kickstart.profile.system.addKeys.\
            assert_called_with(
                self.sw.key,
                'kslabel',
                'keydesc'
            )

    def test_fail_addKeys(self):
        self.assertRaises(
            Exception,
            profile_system.addKeys,
            False,
            'kslabel',
            'keydesc'
        )

    def test_checkConfigManagement(self):
        profile_system.checkConfigManagement(
            self.sw,
            'kslabel'
        )
        self.sw.session.kickstart.profile.system.checkConfigManagement.\
            assert_called_with(
                self.sw.key,
                'kslabel'
            )

    def test_fail_checkConfigManagement(self):
        self.assertRaises(
            Exception,
            profile_system.checkConfigManagement,
            False,
            'kslabel'
        )

    def test_checkRemoteCommands(self):
        profile_system.checkRemoteCommands(
            self.sw,
            'kslabel'
        )
        self.sw.session.kickstart.profile.system.checkRemoteCommands.\
            assert_called_with(
                self.sw.key,
                'kslabel'
            )

    def test_fail_checkRemoteCommands(self):
        self.assertRaises(
            Exception,
            profile_system.checkRemoteCommands,
            False,
            'kslabel'
        )

    def test_disableConfigManagement(self):
        profile_system.disableConfigManagement(
            self.sw,
            'kslabel'
        )
        self.sw.session.kickstart.profile.system.disableConfigManagement.\
            assert_called_with(
                self.sw.key,
                'kslabel'
            )

    def test_fail_disableConfigManagement(self):
        self.assertRaises(
            Exception,
            profile_system.disableConfigManagement,
            False,
            'kslabel'
        )

    def test_disableRemoteCommands(self):
        profile_system.disableRemoteCommands(
            self.sw,
            'kslabel'
        )
        self.sw.session.kickstart.profile.system.disableRemoteCommands.\
            assert_called_with(
                self.sw.key,
                'kslabel'
            )

    def test_fail_disableRemoteCommands(self):
        self.assertRaises(
            Exception,
            profile_system.disableRemoteCommands,
            False,
            'kslabel'
        )

    def test_enableConfigManagement(self):
        profile_system.enableConfigManagement(
            self.sw,
            'kslabel'
        )
        self.sw.session.kickstart.profile.system.enableConfigManagement.\
            assert_called_with(
                self.sw.key,
                'kslabel'
            )

    def test_fail_enableConfigManagement(self):
        self.assertRaises(
            Exception,
            profile_system.enableConfigManagement,
            False,
            'kslabel'
        )

    def test_enableRemoteCommands(self):
        profile_system.enableRemoteCommands(
            self.sw,
            'kslabel'
        )
        self.sw.session.kickstart.profile.system.enableRemoteCommands.\
            assert_called_with(
                self.sw.key,
                'kslabel'
            )

    def test_fail_enableRemoteCommands(self):
        self.assertRaises(
            Exception,
            profile_system.enableRemoteCommands,
            False,
            'kslabel'
        )

    def test_getLocale(self):
        profile_system.getLocale(
            self.sw,
            'kslabel',
        )
        self.sw.session.kickstart.profile.system.getLocale.\
            assert_called_with(
                self.sw.key,
                'kslabel'
            )

    def test_fail_getLocale(self):
        self.assertRaises(
            Exception,
            profile_system.getLocale,
            False,
            'kslabel'
        )

    def test_getPartitioningScheme(self):
        profile_system.getPartitioningScheme(
            self.sw,
            'kslabel'
        )
        self.sw.session.kickstart.profile.system.getPartitioningScheme.\
            assert_called_with(
                self.sw.key,
                'kslabel'
            )

    def test_fail_getPartitioningScheme(self):
        self.assertRaises(
            Exception,
            profile_system.getPartitioningScheme,
            False,
            'kslabel'
        )

    def test_getRegistrationType(self):
        profile_system.getRegistrationType(
            self.sw,
            'kslabel'
        )
        self.sw.session.kickstart.profile.system.getRegistrationType.\
            assert_called_with(
                self.sw.key,
                'kslabel'
            )

    def test_fail_getRegistrationType(self):
        self.assertRaises(
            Exception,
            profile_system.getRegistrationType,
            False,
            'kslabel'
        )

    def test_getSELinux(self):
        profile_system.getSELinux(
            self.sw,
            'kslabel'
        )
        self.sw.session.kickstart.profile.system.getSELinux.\
            assert_called_with(
                self.sw.key,
                'kslabel'
            )

    def test_fail_getSELinux(self):
        self.assertRaises(
            Exception,
            profile_system.getSELinux,
            False,
            'kslabel'
        )

    def test_listFilePreservations(self):
        profile_system.listFilePreservations(
            self.sw,
            'kslabel'
        )
        self.sw.session.kickstart.profile.system.listFilePreservations.\
            assert_called_with(
                self.sw.key,
                'kslabel'
            )

    def test_fail_listFilePreservations(self):
        self.assertRaises(
            Exception,
            profile_system.listFilePreservations,
            False,
            'kslabel'
        )

    def test_listKeys(self):
        profile_system.listKeys(
            self.sw,
            'kslabel'
        )
        self.sw.session.kickstart.profile.system.listKeys.\
            assert_called_with(
                self.sw.key,
                'kslabel'
            )

    def test_fail_listKeys(self):
        self.assertRaises(
            Exception,
            profile_system.listKeys,
            False,
            'kslabel'
        )

    def test_removeFilePreservations(self):
        profile_system.removeFilePreservations(
            self.sw,
            'kslabel',
            'filepreservations'
        )
        self.sw.session.kickstart.profile.system.removeFilePreservations.\
            assert_called_with(
                self.sw.key,
                'kslabel',
                'filepreservations'
            )

    def test_fail_removeFilePreservations(self):
        self.assertRaises(
            Exception,
            profile_system.removeFilePreservations,
            False,
            'kslabel',
            'filepreservations'
        )

    def test_removeKeys(self):
        profile_system.removeKeys(
            self.sw,
            'kslabel',
            'keydesc'
        )
        self.sw.session.kickstart.profile.system.removeKeys.\
            assert_called_with(
                self.sw.key,
                'kslabel',
                'keydesc'
            )

    def test_fail_removeKeys(self):
        self.assertRaises(
            Exception,
            profile_system.removeKeys,
            False,
            'kslabel',
            'keydesc'
        )

    def test_setLocale(self):
        profile_system.setLocale(
            self.sw,
            'kslabel',
            'locale',
            'useutc'
        )
        self.sw.session.kickstart.profile.system.setLocale.\
            assert_called_with(
                self.sw.key,
                'kslabel',
                'locale',
                'useutc'
            )

    def test_fail_setLocale(self):
        self.assertRaises(
            Exception,
            profile_system.setLocale,
            False,
            'kslabel',
            'locale',
            'useutc'
        )

    def test_setPartitioningScheme(self):
        profile_system.setPartitioningScheme(
            self.sw,
            'kslabel',
            'scheme'
        )
        self.sw.session.kickstart.profile.system.setPartitioningScheme.\
            assert_called_with(
                self.sw.key,
                'kslabel',
                'scheme'
            )

    def test_fail_setPartitioningScheme(self):
        self.assertRaises(
            Exception,
            profile_system.setPartitioningScheme,
            False,
            'kslabel',
            'scheme'
        )

    def test_setRegistrationType(self):
        profile_system.setRegistrationType(
            self.sw,
            'kslabel',
            'regtype'
        )
        self.sw.session.kickstart.profile.system.setRegistrationType.\
            assert_called_with(
                self.sw.key,
                'kslabel',
                'regtype'
            )

    def test_fail_setRegistrationType(self):
        self.assertRaises(
            Exception,
            profile_system.setRegistrationType,
            False,
            'kslabel',
            'regtype'
        )

    def test_setSELinux(self):
        profile_system.setSELinux(
            self.sw,
            'kslabel',
            'enforcingmode'
        )
        self.sw.session.kickstart.profile.system.setSELinux.\
            assert_called_with(
                self.sw.key,
                'kslabel',
                'enforcingmode'
            )

    def test_fail_setSELinux(self):
        self.assertRaises(
            Exception,
            profile_system.setSELinux,
            False,
            'kslabel',
            'enforcingmode'
        )


class TestKickstartSnippet(unittest.TestCase):

    def setUp(self):
        self.sw = mock.Mock()

    def test_createOrUpdate(self):
        snippet.createOrUpdate(
            self.sw,
            'name',
            'contents'
        )
        self.sw.session.kickstart.snippet.createOrUpdate.\
            assert_called_with(
                self.sw.key,
                'name',
                'contents'
            )

    def test_fail_createOrUpdate(self):
        self.assertRaises(
            Exception,
            snippet.createOrUpdate,
            False,
            'name',
            'contents'
        )

    def test_delete(self):
        snippet.delete(
            self.sw,
            'name'
        )
        self.sw.session.kickstart.snippet.delete.\
            assert_called_with(
                self.sw.key,
                'name'
            )

    def test_fail_delete(self):
        self.assertRaises(
            Exception,
            snippet.delete,
            False,
            'name'
        )

    def test_listAll(self):
        snippet.listAll(
            self.sw
        )
        self.sw.session.kickstart.snippet.listAll.\
            assert_called_with(
                self.sw.key
            )

    def test_fail_listAll(self):
        self.assertRaises(
            Exception,
            snippet.listAll,
            False,
        )

    def test_listCustom(self):
        snippet.listCustom(
            self.sw
        )
        self.sw.session.kickstart.snippet.listCustom.\
            assert_called_with(
                self.sw.key
            )

    def test_fail_listCustom(self):
        self.assertRaises(
            Exception,
            snippet.listCustom,
            False
        )

    def test_listDefault(self):
        snippet.listDefault(
            self.sw
        )
        self.sw.session.kickstart.snippet.listDefault.\
            assert_called_with(
                self.sw.key
            )

    def test_fail_listDefault(self):
        self.assertRaises(
            Exception,
            snippet.listDefault,
            False
        )


class TestKickstartTree(unittest.TestCase):

    def setUp(self):
        self.sw = mock.Mock()

    def test_create(self):
        tree.create(
            self.sw,
            'treelabel',
            'basepath',
            'channellabel',
            'installtype'

        )
        self.sw.session.kickstart.tree.create.\
            assert_called_with(
                self.sw.key,
                'treelabel',
                'basepath',
                'channellabel',
                'installtype'
            )

    def test_fail_create(self):
        self.assertRaises(
            Exception,
            tree.create,
            False,
            'treelabel',
            'basepath',
            'channellabel',
            'installtype'
        )

    def test_delete(self):
        tree.delete(
            self.sw,
            'treelabel'
        )
        self.sw.session.kickstart.tree.delete.\
            assert_called_with(
                self.sw.key,
                'treelabel'
            )

    def test_fail_delete(self):
        self.assertRaises(
            Exception,
            tree.delete,
            False,
            'treelabel'
        )

    def test_deleteTreeAndProfiles(self):
        tree.deleteTreeAndProfiles(
            self.sw,
            'treelabel'
        )
        self.sw.session.kickstart.tree.deleteTreeAndProfiles.\
            assert_called_with(
                self.sw.key,
                'treelabel'
            )

    def test_fail_deleteTreeAndProfiles(self):
        self.assertRaises(
            Exception,
            tree.deleteTreeAndProfiles,
            False,
            'treelabel'
        )

    def test_getDetails(self):
        tree.getDetails(
            self.sw,
            'treelabel'
        )
        self.sw.session.kickstart.tree.getDetails.\
            assert_called_with(
                self.sw.key,
                'treelabel'
            )

    def test_fail_getDetails(self):
        self.assertRaises(
            Exception,
            tree.getDetails,
            False,
            'treelabel'
        )

    def test_list(self):
        tree.list(
            self.sw,
            'channellabel'
        )
        self.sw.session.kickstart.tree.list.\
            assert_called_with(
                self.sw.key,
                'channellabel'
            )

    def test_fail_list(self):
        self.assertRaises(
            Exception,
            tree.list,
            False,
            'channellabel'
        )

    def test_listInstallTypes(self):
        tree.listInstallTypes(
            self.sw
        )
        self.sw.session.kickstart.tree.listInstallTypes.\
            assert_called_with(
                self.sw.key
            )

    def test_fail_listInstallTypes(self):
        self.assertRaises(
            Exception,
            tree.listInstallTypes,
            False,
        )

    def test_rename(self):
        tree.rename(
            self.sw,
            'originallabel',
            'newlabel'
        )
        self.sw.session.kickstart.tree.rename.\
            assert_called_with(
                self.sw.key,
                'originallabel',
                'newlabel'
            )

    def test_fail_rename(self):
        self.assertRaises(
            Exception,
            tree.rename,
            False,
            'originallabel',
            'newlabel'
        )

    def test_update(self):
        tree.update(
            self.sw,
            'treelabel',
            'basepath',
            'channellabel',
            'installtype'
        )
        self.sw.session.kickstart.tree.update.\
            assert_called_with(
                self.sw.key,
                'treelabel',
                'basepath',
                'channellabel',
                'installtype'
            )

    def test_fail_update(self):
        self.assertRaises(
            Exception,
            tree.update,
            False,
            'treelabel',
            'basepath',
            'channellabel',
            'installtype'
        )

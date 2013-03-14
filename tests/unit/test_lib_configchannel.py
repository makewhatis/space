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

from space.lib import configchannel


class TestConfigChannel(unittest.TestCase):

    def setUp(self):
        self.sw = mock.Mock()

    def test_channelExists(self):
        channellabel = 'test'
        configchannel.channelExists(
            self.sw,
            channellabel
        )
        self.sw.session.configchannel.channelExists.\
            assert_called_with(
                self.sw.key,
                'test'
            )

    def test_fail_channelExists(self):
        self.assertRaises(
            Exception,
            configchannel.channelExists,
            False,
            'test'
        )

    def test_create(self):
        channellabel = 'test'
        channelname = 'test'
        channeldescription = 'test'
        configchannel.create(
            self.sw,
            channellabel,
            channelname,
            channeldescription
        )
        self.sw.session.configchannel.create.\
            assert_called_with(
                self.sw.key,
                'test',
                'test',
                'test'
            )

    def test_fail_create(self):
        self.assertRaises(
            Exception,
            configchannel.create,
            False,
            False,
            False,
            False
        )

    def test_createOrUpdatePath(self):
        configlabel = 'test'
        path = 'test'
        isdir = True
        path_info = 'test'
        configchannel.createOrUpdatePath(
            self.sw,
            configlabel,
            path,
            isdir,
            path_info
        )
        self.sw.session.configchannel.createOrUpdatePath.\
            assert_called_with(
                self.sw.key,
                'test',
                'test',
                True,
                'test'
            )

    def test_fail_createOrUpdatePath(self):
        self.assertRaises(
            Exception,
            configchannel.createOrUpdatePath,
            False,
            'test',
            'test',
            False,
            'test'
        )

    def test_createOrUpdateSymlink(self):
        configlabel = 'test'
        path = 'test'
        isdir = False
        path_info = 'test'
        configchannel.createOrUpdateSymlink(
            self.sw,
            configlabel,
            path,
            isdir,
            path_info
        )
        self.sw.session.configchannel.createOrUpdateSymlink.\
            assert_called_with(
                self.sw.key,
                'test',
                'test',
                False,
                'test'
            )

    def test_fail_createOrUpdateSymlink(self):
        self.assertRaises(
            Exception,
            configchannel.createOrUpdateSymlink,
            False,
            'test',
            'test',
            False,
            'test'
        )

    def test_deleteChannels(self):
        channellabels = 'test'
        configchannel.deleteChannels(
            self.sw,
            channellabels
        )
        self.sw.session.configchannel.deleteChannels.\
            assert_called_with(
                self.sw.key,
                'test'
            )

    def test_fail_deleteChannels(self):
        self.assertRaises(
            Exception,
            configchannel.deleteChannels,
            False,
            'test'
        )

    def test_deleteFileRevisions(self):
        channellabel = 'test'
        filepath = 'test'
        revisions = 'test'
        configchannel.deleteFileRevisions(
            self.sw,
            channellabel,
            filepath,
            revisions
        )
        self.sw.session.configchannel.deleteFileRevisions.\
            assert_called_with(
                self.sw.key,
                'test',
                'test',
                'test'
            )

    def test_fail_deleteFileRevisions(self):
        self.assertRaises(
            Exception,
            configchannel.deleteFileRevisions,
            False,
            'test',
            'test',
            'test'
        )

    def test_deleteFiles(self):
        channellabel = 'test'
        filepaths = 'test'
        configchannel.deleteFiles(
            self.sw,
            channellabel,
            filepaths
        )
        self.sw.session.configchannel.deleteFiles.\
            assert_called_with(
                self.sw.key,
                'test',
                'test'
            )

    def test_fail_deleteFiles(self):
        self.assertRaises(
            Exception,
            configchannel.deleteFiles,
            False,
            'test',
            'test'
        )

    def test_deployAllSystems(self):
        channellabel = 'test'
        date_time = 'test'
        configchannel.deployAllSystems(
            self.sw,
            channellabel,
            date_time
        )
        self.sw.session.configchannel.deployAllSystems.\
            assert_called_with(
                self.sw.key,
                'test',
                'test'
            )

    def test_fail_deployAllSystems(self):
        self.assertRaises(
            Exception,
            configchannel.deployAllSystems,
            False,
            'test',
            'test'
        )

    def test_getDetails(self):
        channellabel = 'test'
        configchannel.getDetails(
            self.sw,
            channellabel
        )
        self.sw.session.configchannel.getDetails.\
            assert_called_with(
                self.sw.key,
                'test'
            )

    def test_fail_getDetails(self):
        self.assertRaises(
            Exception,
            configchannel.getDetails,
            False,
            'test'
        )

    def test_getEncodedFileRevision(self):
        configchan = 'test'
        filepath = 'test'
        revision = 'test'
        configchannel.getEncodedFileRevision(
            self.sw,
            configchan,
            filepath,
            revision
        )
        self.sw.session.configchannel.getEncodedFileRevision.\
            assert_called_with(
                self.sw.key,
                'test',
                'test',
                'test'
            )

    def test_fail_getEncodedFileRevision(self):
        self.assertRaises(
            Exception,
            configchannel.getEncodedFileRevision,
            False,
            'test',
            'test',
            'test'
        )

    def test_getFileRevision(self):
        configchan = 'test'
        filepath = 'test'
        revision = 'test'
        configchannel.getFileRevision(
            self.sw,
            configchan,
            filepath,
            revision
        )
        self.sw.session.configchannel.getFileRevision.\
            assert_called_with(
                self.sw.key,
                'test',
                'test',
                'test'
            )

    def test_fail_getFileRevision(self):
        self.assertRaises(
            Exception,
            configchannel.getFileRevision,
            False,
            'test',
            'test',
            'test'
        )

    def test_getFileRevisions(self):
        channellabel = 'test'
        filepath = 'test'
        configchannel.getFileRevisions(
            self.sw,
            channellabel,
            filepath
        )
        self.sw.session.configchannel.getFileRevisions.\
            assert_called_with(
                self.sw.key,
                'test',
                'test'
            )

    def test_fail_getFileRevisions(self):
        self.assertRaises(
            Exception,
            configchannel.getFileRevisions,
            False,
            'test',
            'test'
        )

    def test_listFiles(self):
        channellabel = 'test'
        configchannel.listFiles(
            self.sw,
            channellabel
        )
        self.sw.session.configchannel.listFiles.\
            assert_called_with(
                self.sw.key,
                'test'
            )

    def test_fail_listFiles(self):
        self.assertRaises(
            Exception,
            configchannel.listFiles,
            False,
            'test'
        )

    def test_listGlobals(self):
        configchannel.listGlobals(
            self.sw
        )
        self.sw.session.configchannel.listGlobals.\
            assert_called_with(
                self.sw.key
            )

    def test_fail_listGlobals(self):
        self.assertRaises(
            Exception,
            configchannel.listGlobals,
            False
        )

    def test_listSubscribedSystems(self):
        channellabel = 'test'
        configchannel.listSubscribedSystems(
            self.sw,
            channellabel
        )
        self.sw.session.configchannel.listSubscribedSystems.\
            assert_called_with(
                self.sw.key,
                'test'
            )

    def test_fail_listSubscribedSystems(self):
        self.assertRaises(
            Exception,
            configchannel.listSubscribedSystems,
            False,
            'test'
        )

    def test_lookupChannelInfo(self):
        channellabel = 'test'
        configchannel.lookupChannelInfo(
            self.sw,
            channellabel
        )
        self.sw.session.configchannel.lookupChannelInfo.\
            assert_called_with(
                self.sw.key,
                'test'
            )

    def test_fail_lookupChannelInfo(self):
        self.assertRaises(
            Exception,
            configchannel.lookupChannelInfo,
            False,
            'test'
        )

    def test_lookupFileInfo(self):
        channellabel = 'test'
        filepaths = 'test'
        configchannel.lookupFileInfo(
            self.sw,
            channellabel,
            filepaths
        )
        self.sw.session.configchannel.lookupFileInfo.\
            assert_called_with(
                self.sw.key,
                'test',
                'test'
            )

    def test_fail_lookupFileInfo(self):
        self.assertRaises(
            Exception,
            configchannel.lookupFileInfo,
            False,
            'test',
            'test'
        )

    def test_scheduleFileComparisons(self):
        channellabel = 'test'
        filepath = 'test'
        serverids = 'test'
        configchannel.scheduleFileComparisons(
            self.sw,
            channellabel,
            filepath,
            serverids
        )
        self.sw.session.configchannel.scheduleFileComparisons.\
            assert_called_with(
                self.sw.key,
                'test',
                'test',
                'test'
            )

    def test_fail_scheduleFileComparisons(self):
        self.assertRaises(
            Exception,
            configchannel.scheduleFileComparisons,
            False,
            'test',
            'test',
            'test'
        )

    def test_update(self):
        channellabel = 'test'
        channelname = 'test'
        description = 'test'
        configchannel.update(
            self.sw,
            channellabel,
            channelname,
            description
        )
        self.sw.session.configchannel.update.\
            assert_called_with(
                self.sw.key,
                'test',
                'test',
                'test'
            )

    def test_fail_update(self):
        self.assertRaises(
            Exception,
            configchannel.update,
            False,
            'test',
            'test',
            'test'
        )

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

from space.lib import distchannel


class TestDistChannel(unittest.TestCase):

    def setUp(self):
        self.sw = mock.Mock()

    def test_listDefaultMaps(self):
        distchannel.listDefaultMaps(
            self.sw
        )
        self.sw.session.distchannel.listDefaultMaps.\
            assert_called_with(
                self.sw.key
            )

    def test_fail_listDefaultMaps(self):
        self.assertRaises(
            Exception,
            distchannel.listDefaultMaps,
            False
        )

    def test_listMapsForOrg(self):
        distchannel.listMapsForOrg(self.sw)
        self.sw.session.distchannel.listMapsForOrg.\
            assert_called_with(
                self.sw.key
            )

    def test_listMapsForOrg_arg(self):
        distchannel.listMapsForOrg(
            self.sw,
            'test'
        )
        self.sw.session.distchannel.listMapsForOrg.\
            assert_called_with(
                self.sw.key,
                'test'
            )

    def test_fail_listMapsForOrg(self):
        self.assertRaises(
            Exception,
            distchannel.listMapsForOrg,
            False
        )

    def test_fail_listMapsForOrg_arg(self):
        self.assertRaises(
            Exception,
            distchannel.listMapsForOrg,
            False,
            'test'
        )

    def test_setMapForOrg(self):
        distchannel.setMapForOrg(
            self.sw,
            'testos',
            'testrelease',
            'testarchname',
            'channellabel'
        )
        self.sw.session.distchannel.setMapForOrg.\
            assert_called_with(
                self.sw.key,
                'testos',
                'testrelease',
                'testarchname',
                'channellabel'
            )

    def test_fail_setMapForOrg(self):
        self.assertRaises(
            Exception,
            distchannel.setMapForOrg,
            False,
            'test',
            'test',
            'test',
            'test'
        )

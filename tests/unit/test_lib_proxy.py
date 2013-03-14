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

from space.lib import proxy


class TestProxy(unittest.TestCase):

    def setUp(self):
        self.sw = mock.Mock()

    def test_activateProxy(self):
        proxy.activateProxy(
            self.sw,
            'systemid',
            'version'
        )
        self.sw.session.proxy.activateProxy.\
            assert_called_with(
                self.sw.key,
                'systemid',
                'version'
            )

    def test_fail_activateProxy(self):
        self.assertRaises(
            Exception,
            proxy.activateProxy,
            False,
            'systemid',
            'version'
        )

    def test_createMonitoringScout(self):
        proxy.createMonitoringScout(
            self.sw,
            'systemid'
        )
        self.sw.session.proxy.createMonitoringScout.\
            assert_called_with(
                self.sw.key,
                'systemid'
            )

    def test_fail_createMonitoringScout(self):
        self.assertRaises(
            Exception,
            proxy.createMonitoringScout,
            False,
            'systemid'
        )

    def test_deactivateProxy(self):
        proxy.deactivateProxy(
            self.sw,
            'systemid'
        )
        self.sw.session.proxy.deactivateProxy.\
            assert_called_with(
                self.sw.key,
                'systemid'
            )

    def test_fail_deactivateProxy(self):
        self.assertRaises(
            Exception,
            proxy.deactivateProxy,
            False,
            'systemid'
        )

    def test_isProxy(self):
        proxy.isProxy(
            self.sw,
            'systemid'
        )
        self.sw.session.proxy.isProxy.\
            assert_called_with(
                self.sw.key,
                'systemid'
            )

    def test_fail_isProxy(self):
        self.assertRaises(
            Exception,
            proxy.isProxy,
            False,
            'systemid'
        )

    def test_listAvailableProxyChannels(self):
        proxy.listAvailableProxyChannels(
            self.sw,
            'systemid'
        )
        self.sw.session.proxy.listAvailableProxyChannels.\
            assert_called_with(
                self.sw.key,
                'systemid'
            )

    def test_fail_listAvailableProxyChannels(self):
        self.assertRaises(
            Exception,
            proxy.listAvailableProxyChannels,
            False,
            'systemid'
        )

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

from space.lib import satellite

class TestSatellite(unittest.TestCase):

    def setUp(self):
        self.sw = mock.Mock()

    def test_getCertificateExpirationDate(self):
        satellite.getCertificateExpirationDate(
            self.sw
        )
        self.sw.session.satellite.getCertificateExpirationDate.\
            assert_called_with(
                self.sw.key
            )

    def test_fail_getCertificateExpirationDate(self):
        self.assertRaises(
            Exception,
            satellite.getCertificateExpirationDate,
            False,
        )

    def test_isMonitoringEnabled(self):
        satellite.isMonitoringEnabled(
            self.sw
        )
        self.sw.session.satellite.isMonitoringEnabled.\
            assert_called_with(
                self.sw.key
            )

    def test_fail_isMonitoringEnabled(self):
        self.assertRaises(
            Exception,
            satellite.isMonitoringEnabled,
            False
        )

    def test_isMonitoringEnabledBySystemId(self):
        satellite.isMonitoringEnabledBySystemId(
            self.sw,
            'systemid'
        )
        self.sw.session.satellite.isMonitoringEnabledBySystemId.\
            assert_called_with(
                self.sw.key,
                'systemid'
            )

    def test_fail_isMonitoringEnabledBySystemId(self):
        self.assertRaises(
            Exception,
            satellite.isMonitoringEnabledBySystemId,
            False,
            'systemid'
        )

    def test_listEntitlements(self):
        satellite.listEntitlements(
            self.sw
        )
        self.sw.session.satellite.listEntitlements.\
            assert_called_with(
                self.sw.key
            )

    def test_fail_listEntitlements(self):
        self.assertRaises(
            Exception,
            satellite.listEntitlements,
            False,
        )

    def test_listProxies(self):
        satellite.listProxies(
            self.sw
        )
        self.sw.session.satellite.listProxies.\
            assert_called_with(
                self.sw.key
            )

    def test_fail_listProxies(self):
        self.assertRaises(
            Exception,
            satellite.listProxies,
            False,
        )

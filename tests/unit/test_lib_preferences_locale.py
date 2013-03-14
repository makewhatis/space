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

from space.lib.preferences import locale

class TestPreferencesLocale(unittest.TestCase):

    def setUp(self):
        self.sw = mock.Mock()

    def test_listLocales(self):
        locale.listLocales(self.sw)
        self.sw.session.preferences.locale.listLocales.\
            assert_called_with()

    def test_fail_listLocales(self):
        self.assertRaises(
            Exception,
            locale.listLocales,
            False,
        )

    def test_listTimeZones(self):
        locale.listTimeZones(
            self.sw
        )
        self.sw.session.preferences.locale.listTimeZones.\
            assert_called_with()

    def test_fail_listTimeZones(self):
        self.assertRaises(
            Exception,
            locale.listTimeZones,
            False,
        )

    def test_setLocale(self):
        locale.setLocale(
            self.sw,
            'login',
            'locale'
        )
        self.sw.session.preferences.locale.setLocale.\
            assert_called_with(
                self.sw.key,
                'login',
                'locale'
            )

    def test_fail_setLocale(self):
        self.assertRaises(
            Exception,
            locale.setLocale,
            False,
            'login',
            'locale'
        )

    def test_setTimeZone(self):
        locale.setTimeZone(
            self.sw,
            'login',
            'tzid'
        )
        self.sw.session.preferences.locale.setTimeZone.\
            assert_called_with(
                self.sw.key,
                'login',
                'tzid'
            )

    def test_fail_setTimeZone(self):
        self.assertRaises(
            Exception,
            locale.setTimeZone,
            False,
            'login',
            'tzid'
        )
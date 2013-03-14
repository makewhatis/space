# -*- coding: utf-8 *-*
import sys
import os
import mock
if sys.version_info >= (3, 0):
    import unittest

if sys.version_info <= (2, 8):
    import unittest2 as unittest

import coverage

sys.path.insert(0, "../../")

from space.lib import api


class TestApi(unittest.TestCase):

    def setUp(self):
        self.sw = mock.Mock()

    def test_getApiCallList(self):
        api.getApiCallList(self.sw)
        self.sw.session.api.getApiCallList.assert_call_with(
            self.sw.key)

    def test_fail_getApiCallList(self):
        self.assertRaises(
            Exception,
            api.getApiCallList,
            False)

    def test_getApiNamespaceCallList(self):
        api.getApiNamespaceCallList(self.sw, 'test')
        self.sw.session.api.getApiNamespaceCallList.assert_call_with(
            self.sw.key, 'test')

    def test_fail_getApiNamespaceCallList(self):
        self.assertRaises(
            Exception,
            api.getApiNamespaceCallList,
            False, 1)

    def test_getApiNamespaces(self):
        api.getApiNamespaces(self.sw)
        self.sw.session.api.getApiNamespaces.assert_call_with(
            self.sw.key)

    def test_fail_getApiNamespaces(self):
        self.assertRaises(
            Exception,
            api.getApiNamespaces,
            False)

    def test_getVersion(self):
        api.getVersion(self.sw)
        self.sw.session.api.getVersion.assert_call_with(
            self.sw.key)

    def test_fail_getVersion(self):
        self.assertRaises(
            Exception,
            api.getVersion,
            False)

    def test_systemVersion(self):
        api.systemVersion(self.sw)
        self.sw.session.api.systemVersion.assert_call_with(
            self.sw.key)

    def test_fail_systemVersion(self):
        self.assertRaises(
            Exception,
            api.systemVersion,
            False)

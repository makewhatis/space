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

from space.lib import errata


class TestErrata(unittest.TestCase):

    def setUp(self):
        self.sw = mock.Mock()

    def test_addPackages(self):
        errata.addPackages(
            self.sw,
            'test',
            'test'
        )
        self.sw.session.errata.addPackages.\
            assert_called_with(
                self.sw.key,
                'test',
                'test'
            )

    def test_fail_addPackages(self):
        self.assertRaises(
            Exception,
            errata.addPackages,
            False,
            'test',
            'test'
        )

    def test_applicableToChannels(self):
        errata.applicableToChannels(
            self.sw,
            'test'
        )
        self.sw.session.errata.applicableToChannels.\
            assert_called_with(
                self.sw.key,
                'test'
            )

    def test_fail_applicableToChannels(self):
        self.assertRaises(
            Exception,
            errata.applicableToChannels,
            False,
            'test'
        )

    def test_bugzillaFixes(self):
        errata.bugzillaFixes(
            self.sw,
            'test'
        )
        self.sw.session.errata.bugzillaFixes.\
            assert_called_with(
                self.sw.key,
                'test'
            )

    def test_fail_bugzillaFixes(self):
        self.assertRaises(
            Exception,
            errata.bugzillaFixes,
            False,
            'test'
        )

    def test_clone(self):
        errata.clone(
            self.sw,
            'test',
            'test'
        )
        self.sw.session.errata.clone.\
            assert_called_with(
                self.sw.key,
                'test',
                'test'
            )

    def test_fail_clone(self):
        self.assertRaises(
            Exception,
            errata.clone,
            False,
            'test',
            'test'
        )

    def test_cloneAsOriginal(self):
        errata.cloneAsOriginal(
            self.sw,
            'test',
            'test'
        )
        self.sw.session.errata.cloneAsOriginal.\
            assert_called_with(
                self.sw.key,
                'test',
                'test'
            )

    def test_fail_cloneAsOriginal(self):
        self.assertRaises(
            Exception,
            errata.cloneAsOriginal,
            False,
            'test',
            'test'
        )

    def test_cloneAsOriginalAsync(self):
        errata.cloneAsOriginalAsync(
            self.sw,
            'test',
            'test'
        )
        self.sw.session.errata.cloneAsOriginalAsync.\
            assert_called_with(
                self.sw.key,
                'test',
                'test'
            )

    def test_fail_cloneAsOriginalAsync(self):
        self.assertRaises(
            Exception,
            errata.cloneAsOriginalAsync,
            False,
            'test',
            'test'
        )

    def test_cloneAsync(self):
        errata.cloneAsync(
            self.sw,
            'test',
            'test'
        )
        self.sw.session.errata.cloneAsync.\
            assert_called_with(
                self.sw.key,
                'test',
                'test'
            )

    def test_fail_cloneAsync(self):
        self.assertRaises(
            Exception,
            errata.cloneAsync,
            False,
            'test',
            'test'
        )

    def test_create(self):
        errata.create(
            self.sw,
            {'test': 'test'},
            [{'test': 'test'}],
            ['test'],
            [1],
            False,
            ['test']
        )
        self.sw.session.errata.create.\
            assert_called_with(
                self.sw.key,
                {'test': 'test'},
                [{'test': 'test'}],
                ['test'],
                [1],
                False,
                ['test']
            )

    def test_fail_create(self):
        self.assertRaises(
            Exception,
            errata.create,
            False,
            {'test': 'test'},
            [{'test': 'test'}],
            ['test'],
            [1],
            False,
            ['test']
        )

    def test_delete(self):
        errata.delete(
            self.sw,
            'test'
        )
        self.sw.session.errata.delete.\
            assert_called_with(
                self.sw.key,
                'test'
            )

    def test_fail_delete(self):
        self.assertRaises(
            Exception,
            errata.delete,
            False,
            'test'
        )

    def test_findByCve(self):
        errata.findByCve(
            self.sw,
            'test'
        )
        self.sw.session.errata.findByCve.\
            assert_called_with(
                self.sw.key,
                'test'
            )

    def test_fail_findByCve(self):
        self.assertRaises(
            Exception,
            errata.findByCve,
            False,
            'test'
        )

    def test_getDetails(self):
        errata.getDetails(
            self.sw,
            'test'
        )
        self.sw.session.errata.getDetails.\
            assert_called_with(
                self.sw.key,
                'test'
            )

    def test_fail_getDetails(self):
        self.assertRaises(
            Exception,
            errata.getDetails,
            False,
            'test'
        )

    def test_listAffectedSystems(self):
        errata.listAffectedSystems(
            self.sw,
            'test'
        )
        self.sw.session.errata.listAffectedSystems.\
            assert_called_with(
                self.sw.key,
                'test'
            )

    def test_fail_listAffectedSystems(self):
        self.assertRaises(
            Exception,
            errata.listAffectedSystems,
            False,
            'test'
        )

    def test_listCves(self):
        errata.listCves(
            self.sw,
            'test'
        )
        self.sw.session.errata.listCves.\
            assert_called_with(
                self.sw.key,
                'test'
            )

    def test_fail_listCves(self):
        self.assertRaises(
            Exception,
            errata.listCves,
            False,
            'test'
        )

    def test_listKeywords(self):
        errata.listKeywords(
            self.sw,
            'test'
        )
        self.sw.session.errata.listKeywords.\
            assert_called_with(
                self.sw.key,
                'test'
            )

    def test_fail_listKeywords(self):
        self.assertRaises(
            Exception,
            errata.listKeywords,
            False,
            'test'
        )

    def test_listPackages(self):
        errata.listPackages(
            self.sw,
            'test'
        )
        self.sw.session.errata.listPackages.\
            assert_called_with(
                self.sw.key,
                'test'
            )

    def test_fail_listPackages(self):
        self.assertRaises(
            Exception,
            errata.listPackages,
            False,
            'test'
        )

    def test_listUnpublishedErrata(self):
        errata.listUnpublishedErrata(
            self.sw
        )
        self.sw.session.errata.listUnpublishedErrata.\
            assert_called_with(
                self.sw.key
            )

    def test_fail_listUnpublishedErrata(self):
        self.assertRaises(
            Exception,
            errata.listUnpublishedErrata,
            False,
        )

    def test_publish(self):
        errata.publish(
            self.sw,
            'test',
            'test'
        )
        self.sw.session.errata.publish.\
            assert_called_with(
                self.sw.key,
                'test',
                'test'
            )

    def test_fail_publish(self):
        self.assertRaises(
            Exception,
            errata.publish,
            False,
            'test',
            'test'
        )

    def test_publishAsOriginal(self):
        errata.publishAsOriginal(
            self.sw,
            'test',
            'test'
        )
        self.sw.session.errata.publishAsOriginal.\
            assert_called_with(
                self.sw.key,
                'test',
                'test'
            )

    def test_fail_publishAsOriginal(self):
        self.assertRaises(
            Exception,
            errata.publishAsOriginal,
            False,
            'test',
            'test'
        )

    def test_removePackages(self):
        errata.removePackages(
            self.sw,
            'test',
            'test'
        )
        self.sw.session.errata.removePackages.\
            assert_called_with(
                self.sw.key,
                'test',
                'test'
            )

    def test_fail_removePackages(self):
        self.assertRaises(
            Exception,
            errata.removePackages,
            False,
            'test',
            'test'
        )

    def test_setDetails(self):
        errata.setDetails(
            self.sw,
            'test',
            'test'
        )
        self.sw.session.errata.setDetails.\
            assert_called_with(
                self.sw.key,
                'test',
                'test'
            )

    def test_fail_setDetails(self):
        self.assertRaises(
            Exception,
            errata.setDetails,
            False,
            'test',
            'test'
        )

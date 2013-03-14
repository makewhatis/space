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

from space.lib import schedule


class TestSchedule(unittest.TestCase):

    def setUp(self):
        self.sw = mock.Mock()

    def test_archiveActions(self):
        schedule.archiveActions(
            self.sw,
            ['action_ids']
        )
        self.sw.session.schedule.archiveActions.\
            assert_called_with(
                self.sw.key,
                ['action_ids']
            )

    def test_fail_archiveActions(self):
        self.assertRaises(
            Exception,
            schedule.archiveActions,
            False,
            ['action_ids']
        )

    def test_cancelActions(self):
        schedule.cancelActions(
            self.sw,
            ['action_ids']
        )
        self.sw.session.schedule.cancelActions.\
            assert_called_with(
                self.sw.key,
                ['action_ids']
            )

    def test_fail_cancelActions(self):
        self.assertRaises(
            Exception,
            schedule.cancelActions,
            False,
            ['action_ids']
        )

    def test_deleteActions(self):
        schedule.deleteActions(
            self.sw,
            ['action_ids']
        )
        self.sw.session.schedule.deleteActions.\
            assert_called_with(
                self.sw.key,
                ['action_ids']
            )

    def test_fail_deleteActions(self):
        self.assertRaises(
            Exception,
            schedule.deleteActions,
            False,
            ['action_ids']
        )

    def test_listAllActions(self):
        schedule.listAllActions(
            self.sw
        )
        self.sw.session.schedule.listAllActions.\
            assert_called_with(
                self.sw.key
            )

    def test_fail_listAllActions(self):
        self.assertRaises(
            Exception,
            schedule.listAllActions,
            False
        )

    def test_listArchivedActions(self):
        schedule.listArchivedActions(
            self.sw
        )
        self.sw.session.schedule.listArchivedActions.\
            assert_called_with(
                self.sw.key
            )

    def test_fail_listArchivedActions(self):
        self.assertRaises(
            Exception,
            schedule.listArchivedActions,
            False
        )

    def test_listCompletedActions(self):
        schedule.listCompletedActions(
            self.sw
        )
        self.sw.session.schedule.listCompletedActions.\
            assert_called_with(
                self.sw.key
            )

    def test_fail_listCompletedActions(self):
        self.assertRaises(
            Exception,
            schedule.listCompletedActions,
            False
        )

    def test_listCompletedSystems(self):
        schedule.listCompletedSystems(
            self.sw,
            ['action_ids']
        )
        self.sw.session.schedule.listCompletedSystems.\
            assert_called_with(
                self.sw.key,
                ['action_ids']
            )

    def test_fail_listCompletedSystems(self):
        self.assertRaises(
            Exception,
            schedule.listCompletedSystems,
            False,
            ['action_ids']
        )

    def test_listFailedActions(self):
        schedule.listFailedActions(
            self.sw
        )
        self.sw.session.schedule.listFailedActions.\
            assert_called_with(
                self.sw.key
            )

    def test_fail_listFailedActions(self):
        self.assertRaises(
            Exception,
            schedule.listFailedActions,
            False
        )

    def test_listFailedSystems(self):
        schedule.listFailedSystems(
            self.sw,
            'action_id'
        )
        self.sw.session.schedule.listFailedSystems.\
            assert_called_with(
                self.sw.key,
                'action_id'
            )

    def test_fail_listFailedSystems(self):
        self.assertRaises(
            Exception,
            schedule.listFailedSystems,
            False,
            'action_id'
        )

    def test_listInProgressActions(self):
        schedule.listInProgressActions(
            self.sw
        )
        self.sw.session.schedule.listInProgressActions.\
            assert_called_with(
                self.sw.key
            )

    def test_fail_listInProgressActions(self):
        self.assertRaises(
            Exception,
            schedule.listInProgressActions,
            False
        )

    def test_listInProgressSystems(self):
        schedule.listInProgressSystems(
            self.sw,
            'action_id'
        )
        self.sw.session.schedule.listInProgressSystems.\
            assert_called_with(
                self.sw.key,
                'action_id'
            )

    def test_fail_listInProgressSystems(self):
        self.assertRaises(
            Exception,
            schedule.listInProgressSystems,
            False,
            'action_id',
        )

    def test_rescheduleActions(self):
        schedule.rescheduleActions(
            self.sw,
            ['action_ids'],
            True
        )
        self.sw.session.schedule.rescheduleActions.\
            assert_called_with(
                self.sw.key,
                ['action_ids'],
                True
            )

    def test_fail_rescheduleActions(self):
        self.assertRaises(
            Exception,
            schedule.rescheduleActions,
            False,
            ['action_ids'],
            True
        )

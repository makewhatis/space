# -*- coding: utf-8 *-*
from space.modules import systems
from space.main import _session

import sys
if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest
import sys
import os
import mock

sys.path.insert(0, "../../")

TEST_DIR = os.path.dirname(os.path.normpath(os.path.abspath(__file__)))
CONFIG = '%s/test.ini' % TEST_DIR

SERVER_GROUP = 'space'

if sys.version_info >= (3, 0):
    from configparser import SafeConfigParser

if sys.version_info <= (2, 8):
    from ConfigParser import SafeConfigParser


class TestSystems(unittest.TestCase):

    def test_listsystems(self):
        sw = _session(config=CONFIG)
        args = ['-g', SERVER_GROUP]
        result = systems.listsystems(sw, args)

        self.assertIsInstance(result, list, result)

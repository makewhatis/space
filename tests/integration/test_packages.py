# -*- coding: utf-8 *-*
from space.modules import packages
from space.main import _session

import unittest
import sys
import os

sys.path.insert(0, "../../")

TEST_DIR = os.path.dirname(os.path.normpath(os.path.abspath(__file__)))
CONFIG = '%s/test.ini' % TEST_DIR

if sys.version_info >= (3, 0):
    from configparser import SafeConfigParser

if sys.version_info <= (2, 8):
    from ConfigParser import SafeConfigParser

if os.path.exists(CONFIG):
    confparse = SafeConfigParser()
    confparse.read(CONFIG)
    if confparse.has_section('tests'):
        if confparse.has_option('tests', 'pkgid'):
            PKGID = confparse.get('tests', 'pkgid')


class TestPackages(unittest.TestCase):

    def test_getpackage(self):
        #space.main._session = mock.Mock()
        #space.main._session.return_value = True
        sw = _session(config=CONFIG)

        args = ['-p', PKGID]
        result = packages.getpackage(sw, args)

        full_path = "%s/%s" % (os.getcwd(), result)
        self.assertEqual(
            os.path.exists(full_path), True, full_path)
        os.remove(full_path)


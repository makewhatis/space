# -*- coding: utf-8 *-*
import sys
import os
import mock
if sys.version_info < (2, 8):
    import unittest2 as unittest
    from io import BytesIO as strio
else:
    import unittest
    from io import StringIO as strio
import coverage

TEST_DIR = os.path.dirname(os.path.normpath(os.path.abspath(__file__)))

CONFIG = '%s/test.ini' % TEST_DIR


def login_name(prompt):
    return 'testuser'


def t_password(prompt):
    return 'letmein'


class TestUtil(unittest.TestCase):

    def setUp(self):
        self.output = strio()
        self.saved_stdout = sys.stdout
        sys.stdout = self.output

    def tearDown(self):
        self.output.close()
        sys.stdout = self.saved_stdout

    def test_load_funcs(self):
        from space.util import load_funcs
        functions = load_funcs()
        self.assertIsInstance(functions, dict, "not a dict")

    def test_load_funcs_no_main(self):
        from space.util import load_funcs
        cfg = os.path.join(
            os.path.dirname(
                os.path.abspath(__file__)), 'test-nomain.conf'
        )
        functions = load_funcs(config=cfg)
        self.assertIsInstance(functions, dict, "not a dict")

    def test_load_funcs_no_conf(self):
        from space.util import load_funcs
        cfg = os.path.join(
            os.path.dirname(
                os.path.abspath(__file__)), 'NOT_HERE.conf'
        )
        functions = load_funcs(config=cfg)
        self.assertIsInstance(functions, dict, "not a dict")

    def test_print_help(self):
        from space.util import print_help
        functions = print_help()
        self.assertIsInstance(functions, dict, "not a dictionary")

    def test_get_username(self):
        from space.util import get_username

        if sys.version_info >= (3, 0):
            with mock.patch('builtins.input') as mockraw:
                mockraw.return_value = 'testuser'
                user = get_username(config=CONFIG)
                self.assertEqual(user, 'testuser', user)

        if sys.version_info <= (2, 8):
            with mock.patch('__builtin__.raw_input') as mockraw:
                mockraw.return_value = 'testuser'
                user = get_username(config=CONFIG)
                self.assertEqual(user, 'testuser', user)        


    def test_get_password(self):
        from space.util import get_password

        if sys.version_info >= (3, 0):
            with mock.patch('builtins.input') as mockraw:
                passwd = get_password(config=CONFIG)
                self.assertEqual(passwd, 'letmein', passwd)

        if sys.version_info <= (2, 8):
            with mock.patch('__builtin__.raw_input') as mockraw:
                passwd = get_password(config=CONFIG)
                self.assertEqual(passwd, 'letmein', passwd)


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
        if os.path.exists("%s/session.new" % TEST_DIR):
            os.remove("%s/session.new" % TEST_DIR)

    def test_load_funcs(self):
        from space.util import load_funcs
        import re
        functions = load_funcs()
        self.assertIsInstance(functions, dict, "not a dict")

        # check for any loaded defs that begin with _
        for key, value in functions.items():
            f = re.match('(\w)._(\w)', key)
            if f:
                self.fail(
                    "%s: should not be in list of loaded defs" % f.group(1)
                )

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

    def test_print_short_help(self):
        from space.util import print_short_help
        functions = print_short_help()
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

    @mock.patch('getpass.getpass')
    def test_get_password_badger(self, gp):
        from space.util import get_password
        gp.return_value = "booya"
        result = get_password(getpass=gp)

        self.assertEqual(result, 'booya', result)

    def test_get_hostname(self):
        from space.util import get_hostname

        if sys.version_info >= (3, 0):
            with mock.patch('builtins.input') as mockraw:
                mockraw.return_value = 'localhost'
                host = get_hostname(config=None)
                self.assertEqual(host, 'localhost', host)

        if sys.version_info <= (2, 8):
            with mock.patch('__builtin__.raw_input') as mockraw:
                mockraw.return_value = 'localhost'
                host = get_hostname(config=None)
                self.assertEqual(host, 'localhost', host)

    @mock.patch('os.remove')
    def test_check_session_user(self, os_rm):
        from space.util import check_session_user
        os_rm.return_value = True

        result = check_session_user(
            'username',
            session_file="%s/session.test" % TEST_DIR)
        self.assertEqual(result, False, "Should be False")

        lines = [
        '1195xc476906524215c806e08bd5c61f7901b',
        'spacewalk.local.makewhatis.com',
        '300'
        ]

        with open("%s/session.new" % TEST_DIR, 'w+') as n:
            lines[2] = '300'
            n.write(' '.join(lines))

        result = check_session_user(
            'username',
            session_file="%s/session.new" % TEST_DIR
        )

        self.assertEqual(
            result.key,
            '1195xc476906524215c806e08bd5c61f7901b',
            "Should be 1195xc476906524215c806e08bd5c61f7901b"
        )

    def test_check_length(self):
        from space.util import _check_length
        with self.assertRaises(ValueError):
            result = _check_length("")

    def test_get_config_value(self):
        from space.util import get_config_value
        result = get_config_value(CONFIG, 'hostname')
        self.assertEqual(result, 'localhost', "%s should be hostname" % result)

    @mock.patch('os.path.exists')
    @mock.patch('os.path.expanduser')
    def test_get_config(self, expand, exists):
        """
        Test get_config, make sure if os.expanduser returns
        a home dir, that it is picked up on the first iteration.
        """
        from space.util import get_config

        exists.return_value = True
        expand.return_value = "/home/blahuser"

        result = get_config()
        self.assertEqual(result, "/home/blahuser/.space/config.ini", result)

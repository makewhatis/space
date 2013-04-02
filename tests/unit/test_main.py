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

sys.path.insert(0, "../../")

TEST_DIR = os.path.dirname(os.path.normpath(os.path.abspath(__file__)))

CONFIG = '%s/test.ini' % TEST_DIR


def login_name(prompt):
    return 'testuser'


def t_password(prompt):
    return 'letmein'


class TestMain(unittest.TestCase):

    def setUp(self):
        self.output = strio()
        self.saved_stdout = sys.stdout
        sys.stdout = self.output

    def tearDown(self):
        self.output.close()
        sys.stdout = self.saved_stdout

    def test_main(self):
        from space.main import main
        sys.argv = ['space', 'system', 'listSystems']

        result = main(config=CONFIG)
        self.assertEqual(result, None, result)

    def test_main_unrecognized_arg(self):
        from space.main import main
        sys.argv = ['space', '--dogman', 'list_dogs']

        result = main(config=CONFIG)
        self.assertEqual(result, None, result)

    def test_main_args_version(self):
        from space.main import main
        sys.argv = ['space', '--version']
        result = main()

        self.assertEqual(result, '1.1', result)

    def test_main_args_others(self):
        """
        Test to make sure variables are set from
        flag options.
        """
        from space.main import main
        sys.argv = ['space', '--docs']
        main()
        result = self.output.getvalue()
        self.assertRegexpMatches(result, '^Help Docs.*', result)

        sys.argv = [
            'space',
            '--user=test',
            '--config=test',
            '--host=test'
        ]
        main()
        result = self.output.getvalue()
        self.assertRegexpMatches(result, '^Help Docs.*', result)

    def test_print_help(self):
        from space.main import print_help
        functions = print_help()
        self.assertIsInstance(functions, dict, "not a dictionary")

    def test_load_funcs(self):
        from space.main import load_funcs
        functions = load_funcs()
        self.assertIsInstance(functions, dict, "not a dict")

    def test_load_funcs_no_main(self):
        from space.main import load_funcs
        cfg = os.path.join(
            os.path.dirname(
                os.path.abspath(__file__)), 'test-nomain.conf'
        )
        functions = load_funcs(config=cfg)
        self.assertEqual(functions, False, "main should have failed")

    def test_load_funcs_no_conf(self):
        from space.main import load_funcs
        cfg = os.path.join(
            os.path.dirname(
                os.path.abspath(__file__)), 'NOT_HERE.conf'
        )
        functions = load_funcs(config=cfg)
        self.assertEqual(functions, False, "Should have returned False")

    def test_no_args(self):
        from space.main import main
        out = strio()
        sys.stdout = out
        sys.argv = ['space']
        main()

        output = out.getvalue().strip()

        self.assertRegexpMatches(
            output,
            '^Usage: space \[options\].*',
            output)

    def test_top_level_arg_only(self):
        from space.main import main
        out = strio()
        sys.stdout = out
        sys.argv = ['space', 'packages']
        main()
        output = out.getvalue().strip()
        self.assertRegexpMatches(
            output,
            '^Usage: space \[options\].*',
            output)
            #'result does not contain proper text')

    def test_get_user(self):
        from space.main import get_user
        user = get_user(user=login_name)
        self.assertEqual(user, 'testuser', user)

    def test_get_password(self):
        from space.main import get_pass
        passwd = get_pass('testuser', getpass=t_password)
        self.assertEqual(passwd, 'letmein', passwd)

    def test_get_auth(self):
        from space.main import getauth
        cfg = os.path.join(
            os.path.dirname(
                os.path.abspath(__file__)), 'test.ini'
        )
        moduledir = os.path.join(
            os.path.dirname(
                os.path.abspath(__file__)), 'testmodules'
        )
        with open(cfg, 'w+') as c:
            c.write(
                "[spacewalk]\n" +
                "hostname = localhost \n" +
                "login = testuser\n" +
                "password = letmein\n" +
                "[localhost]\n" +
                "login = testuser\n" +
                "password = letmein\n" +
                "[main]\n" +
                "module_dir = %s" % moduledir
            )
        auth = getauth(cfg, 'localhost')
        self.assertEqual(auth, ('testuser', 'letmein'), auth)

    @mock.patch('space.main.get_user')
    @mock.patch('space.main.get_pass')
    def test_swsession(self, get_pass, get_user):
        import space
        get_user.return_value = 'testuser'
        get_pass.return_value = 'letmein'

        if sys.version_info >= (3, 0):
            with mock.patch('xmlrpc.client.Server') as xml:
                l = xml.return_value = mock.Mock()
                l.login.return_value = True
                sess = space.main.swSession(config=CONFIG)
                self.assertIsInstance(sess, object, sess)
                self.assertIsInstance(
                    space.main.swSession(config=CONFIG),
                    object,
                    'Session not created')
                sw = space.main.swSession(config=CONFIG, url="babylon.local")
                self.assertIsInstance(sw, object)
                self.assertEqual(sw.hostname, 'babylon.local', sw.hostname)

        if sys.version_info <= (2, 8):
            with mock.patch('xmlrpclib.Server') as xml:
                l = xml.return_value = mock.Mock()
                l.login.return_value = True
                sess = space.main.swSession(config=CONFIG)
                self.assertIsInstance(sess, object, sess)
                self.assertIsInstance(
                    space.main.swSession(config=CONFIG),
                    object,
                    'Session not created')
                sw = space.main.swSession(config=CONFIG, url="babylon.local")
                self.assertIsInstance(sw, object)
                self.assertEqual(sw.hostname, 'babylon.local', sw.hostname)

    def test_session(self):
        session_dir = TEST_DIR
        session_file = 'session.test'

        import datetime
        import json
        import space

        now = datetime.datetime.now()
        user = 'testuser'
        session_data = {
            '%s' % user: 'blah',
            'hostname': 'spacewalk.test',
            'time': '%s' % int(now.strftime('%s'))
        }
        s = json.dumps(session_data, session_file)
        with open(session_file, 'w+') as f:
            f.write(s)

        # test session
        space.main._session(
            user=user,
            now=now.strftime('%s'),
            session_dir=session_dir,
            session_file=session_file,
            config=CONFIG
        )
        with mock.patch('space.main.swSession') as user:
            user.return_value = 1234
            sw = space.main._session(
                now=now.strftime('%s'),
                session_dir=session_dir,
                session_file=session_file,
                config='%s/test-nologin.ini' % TEST_DIR
            )
            self.assertIsInstance(sw, object, "not object")

        # test without config arg
        with mock.patch('space.main.swSession') as user:
            user.return_value = mock.Mock()
            user.key.return_value = 'key'
            with mock.patch('space.main.getuser') as getu:
                getu.return_value = 'test'
                sw = space.main._session(
                    now=now.strftime('%s'),
                    session_dir=session_dir,
                    session_file=session_file,
                    config=None
                )
                self.assertIsInstance(sw, object, "not object")

                getu.return_value = 'test_me'
                sw = space.main._session(
                    now=None,
                    session_dir=None,
                    session_file=None,
                    url='test',
                    config='/fake/path'
                )
                self.assertIsInstance(sw, object, "not object")

        with mock.patch('space.main.swSession') as m:
            m.key.return_value = 1234

            sw = space.main._session(
                now=now.strftime('%s'),
                session_file='session.test',
                session_dir='testdir',
                config=CONFIG
            )
            self.assertIsInstance(sw, object, "not object")

            # test for expired login
            future = int(now.strftime('%s'))
            future = future + 40000
            sw = space.main._session(
                now=future,
                session_file='session.test',
                session_dir='testdir',
                config=CONFIG
            )
            self.assertIsInstance(sw, object, "not object")

        os.rmdir('testdir')
        os.remove('session.test')

    def test_cmd_login(self):
        import space
        with mock.patch('space.main._session') as m:
            sys.argv = ['space', '--login']
            m.args.login = True
            space.main.main()

    def test_cmd_logout(self):
        import space
        with mock.patch('space.main._session') as m:
            sys.argv = ['space', '--logout']
            m.args.logout = True
            space.main.main()

    def test_cmd_doc(self):
        import space
        with mock.patch('space.main.print_help') as m:
            sys.argv = ['space', '--doc']
            m.args.doc = "DOCS"
            space.main.main()

    def test_parse_args(self):
        import space

        sys.argv = ['space', 'fakemodule', 'dosomething']
        with mock.patch('space.main._session') as m:
            m.return_value = True
            space.main.main(
                config='%s/test.ini' % os.path.join(
                    os.path.dirname(
                        os.path.abspath(__file__))))


def suite():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMain)

    return suite

if __name__ == '__main__':

    # Cover any subprocess
    coverage.process_startup()
    # Setup coverage
    code_coverage = coverage.coverage(
        branch=True,
        source=[os.path.dirname(TEST_DIR)],
    )
    #Starting and saving coverage info
    code_coverage.start()

    runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run(test_suite)

    #Stopping and saving coverage info
    code_coverage.stop()
    code_coverage.save()

    report_dir = os.path.join(os.path.dirname(__file__), 'coverage-report')
    print(
        '\nGenerating Coverage HTML Report Under {0!r} ...'.format(
            report_dir
        )
    ),
    sys.stdout.flush()

    if os.path.isdir(report_dir):
        import shutil
        shutil.rmtree(report_dir)
    code_coverage.html_report(directory=report_dir)
    print('Done.\n')

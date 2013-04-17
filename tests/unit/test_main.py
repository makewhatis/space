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

    def test_main_one_carg(self):
        from space.main import main
        sys.argv = ['space', 'systems']

        result = main(config=CONFIG)
        self.assertEqual(result, None, result)

    @mock.patch('space.main.swSession')
    def test_main_test_funcs(self, sw_mock):
        sw_mock.return_value = mock.Mock()
        from space.main import main
        sys.argv = ['space', 'fakemodule', 'dosomething']

        result = main(config=CONFIG)
        self.assertEqual(result, True, result)

    def test_cmd_doc(self):
        from space.main import main
        sys.argv = ['space', '--docs']
        docs = main()
        self.assertIsInstance(docs, dict, docs)

    def test_main_args_version(self):
        from space.main import main
        sys.argv = ['space', '--version']
        result = main()

        self.assertRegexpMatches(result, '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}', result)

    @mock.patch('space.main.swSession')
    @mock.patch('space.modules.systems.list')
    def test_main_args(self, sys_list, sw_mock):
        """
        Test to make sure variables are set from
        flag options.
        """
        sys_list.return_value = mock.Mock()
        sw_mock.return_value = mock.Mock()
        from space.main import main

        sys.argv = [
            'space',
            '--username=test',
            '--config=test.ini',
            '--host=test',
            '--password=test',
            'fakemodule',
            'listSystems'
        ]
        main()
        result = self.output.getvalue()
        self.assertRegexpMatches(result, '^Usage: space.*', result)

    def test_main_args_others(self):
        """
        Test to make sure variables are set from
        flag options.
        """
        from space.main import main

        sys.argv = [
            'space',
            '--username=test',
            '--config=test',
            '--host=test',
            '--password=test'
        ]
        main()
        result = self.output.getvalue()
        self.assertRegexpMatches(result, '^Usage: space.*', result)

    def test_main_args_only_module_arg(self):
        """
        Test to make sure variables are set from
        flag options.
        """
        from space.main import main        
        sys.argv = [
            'space',
            '--username=test',
            '--config=test',
            '--host=test',
            '--password=test',
            'systems'
        ]
        main()
        result = self.output.getvalue()
        self.assertRegexpMatches(result, '^Usage: space.*', result)

    def test_main_args_only_module_arg_that_doesnt_exist(self):
        """
        Test to make sure variables are set from
        flag options.
        """
        from space.main import main        
        sys.argv = [
            'space',
            '--username=test',
            '--config=test',
            '--host=test',
            '--password=test',
            'bigbird'
        ]
        main()
        result = self.output.getvalue()
        self.assertRegexpMatches(result, '^Usage: space.*', result)

    @mock.patch('space.main.load_funcs')
    @mock.patch('space.main.get_hostname')
    @mock.patch('space.main.get_username')
    @mock.patch('space.main.get_password')
    def test_flags_patched(self, get_password, get_username, get_hostname, load_funcs):
        from space.main import main  
        load_funcs.return_value = {'tulips.list':'test', 'roses.list':'test'}
        get_hostname.return_value = 'localhost'
        get_username.return_value = 'bob'
        get_password.return_value = 'pass'
        
        # test with no flags
        sys.argv = [
            'space',
            'systems',
            'list'
        ]
        result = main()        
        self.assertEqual(result, None, result)

        # test --logout
        sys.argv = [
            'space',
            '--logout',
        ]
        result = main()
        self.assertEqual(result, 'User logged out', result)

    @mock.patch('space.main.load_funcs')
    def test_key_error(self, load_funcs):
        from space.main import main  
        load_funcs.return_value = dict()
        sys.argv = [
            'space',
            'systems',
            'list'
        ]
        with self.assertRaises(IOError):
            main()        


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

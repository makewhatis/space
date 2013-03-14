#from distutils.core import setup
import sys
from setuptools import setup
from setuptools import find_packages
from setuptools.command.test import test as TestCommand

py_version = sys.version_info[:2]

PY3 = py_version[0] == 3

if PY3:
    if py_version < (3, 2):
        raise RuntimeError('On Python 3, Pyramid requires Python 3.2 or better')
else:
    if py_version < (2, 6):
        raise RuntimeError('On Python 2, Pyramid requires Python 2.6 or better')

version =  "0.0.1"
tests_require = [
    'mock >= 1.0.1',
    'py',
    'pytest',
    'pytest-cov',
    'coverage'
    ]

if not PY3:
    tests_require.append('unittest2>=0.5.1')


from setuptools.command.test import test as TestCommand
import sys

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True
    def run_tests(self):
         #import here, cause outside the eggs aren&#039;t loaded 
        import pytest
        errno = pytest.main('tests/unit')
        sys.exit(errno)


setup(name='space',
        version=version,
        description='Spacewalk Cli',
        author='David Johansen',
        packages=find_packages(),
        setup_requires=['argparse'],
        namespace_packages=['space'],
        entry_points={
            'console_scripts': [
                'space = space.main:main',
            ],
        },
        tests_require = tests_require,
        cmdclass = {'test': PyTest},
      )

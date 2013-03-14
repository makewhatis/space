#from distutils.core import setup
from setuptools import setup, find_packages

version =  "0.0.1"
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
        }
      )

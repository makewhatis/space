# -*- coding: utf-8 *-*
import argparse
import re
import sys
import subprocess

from space.main import getauth, get_user, get_pass

if sys.version_info >= (3, 0):
    import urllib.request as urllib
if sys.version_info <= (2, 8):
    import urllib


def getpackage(sw, args):
    """
    Download a package to the current directory

        -p, --pid       define a group to list systems in.

    """
    parser = argparse.ArgumentParser(
        prog='space packages getpackage',
        description='Download a package.'
    )
    parser.add_argument(
        '-p',
        '--pid',
        default=None,
        required=True,
        help="Package ID"
    )

    argobj = parser.parse_args(args)

    pkg_url = packages.getPackageUrl(sw, argobj.pid)

    pkg = re.match(".*/(.*.rpm$)", pkg_url)
    result = urllib.urlretrieve(pkg_url, pkg.group(1))

    return result[0]


def push(sw, args):
    """
    Push a package into a channel of your choice
    """
    parser = argparse.ArgumentParser(
        prog='space packages push',
        description='Push a package into a channel of your choice'
    )

    parser.add_argument(
        '-c',
        '--channel',
        default=None,
        required=True,
        help='Channel to push package to.'
    )

    parser.add_argument(
        'package',
        default=None,
        help='pass path to package'
    )
    
    p = parser.parse_args(args)

    if len(sw._password) is 0:
        auth = getauth(sw.config, sw.hostname)
    
    if auth[0] == 'None':
        login = get_user()
    
    if auth[1] == 'None':
        _pass = get_pass(username=login)

    command = (
        "/usr/bin/rhnpush --nosig -vvv " +
        "--channel=%s --username=%s " % (
        p.channel, login
        ) +
        "--password=%s --server=%s %s" % (
            _pass,
            sw.hostname,
            p.package
        )
    )
    s = subprocess.Popen([command], shell=True)
    result = s.communicate()
    return True

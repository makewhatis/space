# -*- coding: utf-8 *-*
import argparse
import re
import sys
import subprocess

from space.main import getauth as _getauth
from space.main import get_user as _get_user
from space.main import get_pass as _get_pass

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
    Push a package into a channel of your choice. Probably the most
    common command. 
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
        auth = _getauth(sw.config, sw.hostname)

    if auth[0] == 'None':
        login = _get_user()

    if auth[1] == 'None':
        _pass = _get_pass(username=login)

    #rhncache stuff although no idea if this will work. depending on
    # if the rhncache stuff is the session. if not its totally hosed.
    # and we will have to revert to the user/pass in the config. which
    # would be laaaaameee
    # maybe we can build the rhnpushcache file on authentication. idea.
    with open("%s/%s" % (os.path.expanduser('~'), '.rhnpushcache')) as f:
        f.write(self.session)

    command = (
        "/usr/bin/rhnpush --nosig -vvv " +
        "--channel=%s " % (
        p.channel
        ) +
        "--server=https://%s %s" % (
            sw.hostname,
            p.package
        )
    )

    s = subprocess.Popen([command], shell=True)
    result = s.communicate()
    return True

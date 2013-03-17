# -*- coding: utf-8 *-*
import argparse
import re
import sys

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
    parser.add_argument('-p', '--pid',
                            default=None,
                            required=True,
                            help="Package ID")

    argobj = parser.parse_args(args)

    pkg_url = packages.getPackageUrl(sw, argobj.pid)

    pkg = re.match(".*/(.*.rpm$)", pkg_url)
    result = urllib.urlretrieve(pkg_url, pkg.group(1))

    return result[0]

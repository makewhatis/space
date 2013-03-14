# -*- coding: utf-8 *-*
import argparse
from space.lib import system

def listsystems(sw, args):
    """
    List Systems in spacewalk

        -g       define a group to list systems in.
        --raw    get a raw listing (helpful for scripts)
    """

    parser = argparse.ArgumentParser(prog='space systems listsystems',
                        epilog='For detailed help ' +
                       'pass --help to a target',
                        description=('This command will ' +
                        'list all spacewalk systems.')
                        )
    parser.add_argument('-g', '--group',
                        default=None,
                        required=True,
                        help="System Group Name")
    parser.add_argument('--raw',
                        action='store_true',
                        help="Output a raw text list of servers.")

    parser.parse_args(args)

    servers = system.listSystems(sw)

    if servers:
        for server in servers:
            print("%s : %s" % (server['name'], server['id']))
    else:
        print("No servers in group")
    return servers

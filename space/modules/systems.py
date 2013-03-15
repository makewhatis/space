# -*- coding: utf-8 *-*
import argparse
from space.lib import system


def child_channels(
    sw,
    args
):
    """
    List child channels for system
    """
    parser = argparse.ArgumentParser(
        prog='space systems child_channels',
        description=(
            'This command lists child' +
            'channels assigned to a server'
        )
    )
    parser.add_argument(
        '--sid',
        default=None,
        required=False,
        help="Server ID number"
    )
    parser.add_argument(
        '--server',
        default=None,
        required=False,
        help="Servername"
    )

    p = parser.parse_args(args)

    if p.sid:
        channels = system.listSubscribedChildChannels(
            sw,
            int(server)
        )

    elif p.server:
        server = system.searchByName(sw, p.server)

        if len(server) > 1:
            print("multiple servers by that name, please use server id")
            return False

        channels = system.listSubscribedChildChannels(
            sw,
            server[0]['id']
        )

    else:
        print("Need to give me something to work with here.")
        return False

    for channel in channels:
        print(channel['name'])
    
    return channels


def listsystems(sw, args):
    """
    List Systems in spacewalk

        -g       define a group to list systems in.
        --raw    get a raw listing (helpful for scripts)
    """

    parser = argparse.ArgumentParser(
        prog='space systems listsystems',
        epilog='For detailed help ' +
        'pass --help to a target',
        description=('This command will ' +
        'list all spacewalk systems.')
    )
    parser.add_argument(
        '-g', '--group',
        default=None,
        required=True,
        help="System Group Name"
    )
    parser.add_argument(
        '--raw',
        action='store_true',
        help="Output a raw text list of servers."
    )

    p = parser.parse_args(args)

    servers = system.listSystems(sw)

    if servers:
        for server in servers:
            print("%s : %s" % (server['name'], server['id']))
    else:
        print("No servers in group")
    return servers

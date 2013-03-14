# -*- coding: utf-8 *-*
import argparse
from space.lib import activationkey

def add_child_channels(sw, args):
    """
    Add child channels to an activation key
    """
    parser = argparse.ArgumentParser(
        prog='space activationkey add_child_channels',
        description='Add child channels to an activation key.'
    )

    parser.add_argument(
        '--keyname',
        default=None,
        required=True,
        help="Name of the activationkey"
    )
    parser.add_argument(
        '--channels',
        default=None,
        required=True,
        nargs='+',
        type=str,
        help="Channels listed in space delimitted list."
    )
    parser.parse_args(args)


def create(sw, args):
    """
    Create new activation key

    """
    parser = argparse.ArgumentParser(
        prog='space activationkey create',
        description='Create a new activation key with unlimited usage.' +
        ' The activation key parameter passed in will be prefixed ' +
        'with the organization ID, and this value will be returned from ' +
        'the create call. Eg. If the caller passes in the key "foo" and ' +
        'belong to an organization with the ID 100, the actual activation ' +
        'key will be "100-foo"'
    )
    parser.add_argument(
        '-k', '--keyname',
        default=None,
        required=True,
        help="Name of the activationkey"
    )
    parser.add_argument(
        '-b',
        '--basechannel',
        default=None,
        required=True,
        help="baseChannelLabel, "
    )
    parser.add_argument(
        '--monitoring_entitled',
        action='store_true',
        help="monitoring_entitled?"
    )
    parser.add_argument(
        '--provisioning_entitled',
        action='store_true',
        help="provisioning_entitled?"
    )
    parser.add_argument(
        '--virtualization_host',
        action='store_true',
        help="virtualization_host?"
    )
    parser.add_argument(
        '--virtualization_host_platform',
        action='store_true',
        help="virtualization_host_platform?"
    )
    p = parser.parse_args(args)


def add_group(sw, args):
    """
    Provided a group and a activationkey adds the group to the activationkey
    """
    parser = argparse.ArgumentParser(
        prog='space activationkey add_group',
        description='Provided a group and a activationkey ' +
        'adds the group to the activationkey'
    )
    parser.add_argument(
        '-k',
        '--keyname',
        default=None,
        required=True,
        help="Name of the activationkey"
    )
    parser.add_argument(
        '-g',
        '--groups',
        default=None,
        required=True,
        nargs='+',
        type=str,
        help='Space delimitted list of system groups'
    )
    print(dir(parser))
    print(args)
    p = parser.parse_args(args)

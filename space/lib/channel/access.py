"""
``Namespace: channel.access``
=============================

Provides methods to retrieve and alter channel access restrictions.

- :func:`disableUserRestrictions`
- :func:`enableUserRestrictions`
- :func:`getOrgSharing`
- :func:`setOrgSharing`
"""


def disableUserRestrictions(
    sw,
    channellabel
):
    """
    Description:
        Disable user restrictions for the given channel. If disabled,
        all users within the organization may subscribe to the channel.

    Parameters:
        - sw session
        - string channellabel - label of the channel

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.channel.access.disableUserRestrictions(
            sw.key,
            channellabel
        )
    except Exception as e:
        raise e

    return result


def enableUserRestrictions(
    sw,
    channellabel
):
    """
    Description:
        Enable user restrictions for the given channel. If enabled,
        only selected users within the organization may subscribe to
        the channel.

    Parameters:
        - sw session
        - string channellabel - label of the channel

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.channel.access.enableUserRestrictions(
            sw.key,
            channellabel
        )
    except Exception as e:
        raise e

    return result


def getOrgSharing(
    sw,
    channellabel
):
    """
    Description:
        Get organization sharing access control.

    Parameters:
        - sw session
        - string channellabel - label of the channel

    Returns:
        - string - The access value (one of the following: 'public',
            'private', or 'protected'.
    """
    try:
        result = sw.session.channel.access.getOrgSharing(
            sw.key,
            channellabel
        )
    except Exception as e:
        raise e

    return result


def setOrgSharing(
    sw,
    channellabel,
    accesslevel
):
    """
    Description:
        Set organization sharing access control.

    Parameters:
        - sw session
        - string channelLabel - label of the channel
        - string "access" - Access (one of the following: 'public', 'private',
            or 'protected'

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.channel.access.setOrgSharing(
            sw.key,
            channellabel,
            accesslevel
        )
    except Exception as e:
        raise e

    return result

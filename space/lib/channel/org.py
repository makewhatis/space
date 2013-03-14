"""
``Namespace: channel.org``
==========================

Provides methods to retrieve and alter organization trust relationships
 for a channel.

- :func:`disableAccess`
- :func:`enableAccess`
- :func:`list`
"""


def disableAccess(
    sw,
    channellabel,
    orgid
):
    """
    Description:
        Disable access to the channel for the given organization.

    Parameters:
        - sw session
        - string channelLabel - label of the channel
        - int orgId - id of org being removed access

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.channel.org.disableAccess(
            sw.key,
            channellabel,
            orgid
        )
    except Exception as e:
        raise e

    return result


def enableAccess(
    sw,
    channellabel,
    orgid
):
    """
    Description:
    Enable access to the channel for the given organization.

    Parameters:
        - sw session
        - string channelLabel - label of the channel
        - int orgId - id of org being granted access

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.channel.org.enableAccess(
            sw.key,
            channellabel,
            orgid
        )
    except Exception as e:
        raise e

    return result


def list(
    sw,
    channellabel
):
    """
    Description:
    List the organizations associated with the given channel that may be
    trusted.

    Parameters:
        - sw session
        - string channelLabel - label of the channel

    Returns:
        - struct - org
        - int "org_id"
        - string "org_name"
        - boolean "access_enabled"
    """
    try:
        result = sw.session.channel.org.list(
            sw.key,
            channellabel
        )
    except Exception as e:
        raise e

    return result

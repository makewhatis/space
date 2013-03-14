"""
``Namespace: distchannel``
======================

Provides methods to access and modify distribution channel information.

Available methods:

- :func:`listDefaultMaps`
- :func:`listMapsForOrg`
- :func:`setMapForOrg`
"""


def listDefaultMaps(
    sw
):
    """
    Description:
    Lists the default distribution channel maps

    Parameters:
        - string sessionKey

    Returns:
        - struct - distChannelMap
            - string "os" - Operationg System
            - string "release" - OS Relase
            - string "arch_name" - Channel architecture
            - string "channel_label" - Channel label
            - string "org_specific" - 'Y' organization specific, 'N' default
    """
    try:
        result = sw.session.distchannel.listDefaultMaps(
            sw.key
        )
    except Exception as e:
        raise e

    return result


def listMapsForOrg(
    sw,
    orgid=None
):
    """
    Description:
    Lists distribution channel maps valid for an organization, satellite admin
    right needed
    Parameters:
    string sessionKey
    int orgId
    Returns:

    struct - distChannelMap
    string "os" - Operationg System
    string "release" - OS Relase
    string "arch_name" - Channel architecture
    string "channel_label" - Channel label
    string "org_specific" - 'Y' organization specific, 'N' default
    """
    if orgid:
        try:
            result = sw.session.distchannel.listMapsForOrg(
                sw.key,
                orgid
            )
        except Exception as e:
            raise e
    else:
        try:
            result = sw.session.distchannel.listMapsForOrg(
                sw.key
            )
        except Exception as e:
            raise e

    return result


def setMapForOrg(
    sw,
    os,
    release,
    archname,
    channellabel
):
    """
    Description:
    Sets, overrides (/removes if channelLabel empty) a distribution channel map
    within an organization
    Parameters:
    string sessionKey
    string os
    string release
    string archName
    string channelLabel
    Returns:

    int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.distchannel.setMapForOrg(
            sw.key,
            os,
            release,
            archname,
            channellabel
        )
    except Exception as e:
        raise e

    return result

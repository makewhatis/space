"""
``Namespace: channel``
======================

Provides method to get back a list of Software Channels.

Available methods:

- :func:`listAllChannels` *
- :func:`listMyChannels`
- :func:`listPopularChannels`
- :func:`listRetiredChannels`
- :func:`listSharedChannels`
- :func:`listSoftwareChannels`
- :func:`listVendorChannels`
"""


def listAllChannels(
    sw
):
    """
    Description:
    List all software channels that belong to the user's organization.

    Parameters:
        - sw session object

    Returns:
        - array:
            - struct - channel info
                - int "id"
                - string "label"
                - string "name"
                - string "provider_name"
                - int "packages"
                - int "systems"
                - string "arch_name"
    """
    try:
        result = sw.session.channel.listAllChannels(
            sw.key
        )
    except Exception as e:
        raise e

    return result


def listMyChannels(
    sw
):
    """
    Description:
        List all software channels that belong to the user's organization.

    Parameters:
        - sw session object

    Returns:
        - array:
            - struct - channel info
                - int "id"
                - string "label"
                - string "name"
                - string "provider_name"
                - int "packages"
                - int "systems"
                - string "arch_name"
    """
    try:
        result = sw.session.channel.listMyChannels(
            sw.key
        )
    except Exception as e:
        raise e

    return result


def listPopularChannels(
    sw,
    popcount
):
    """
    Description:
    List the most popular software channels. Channels that
    have at least the number of systems subscribed as specified by
    the popularity count will be returned.

    Parameters:
        - sw session
        - int "popularityCount"

    Returns:
        - array:
            - struct - channel info
                - int "id"
                - string "label"
                - string "name"
                - string "provider_name"
                - int "packages"
                - int "systems"
                - string "arch_name"
    """
    try:
        result = sw.session.channel.listPopularChannels(
            sw.key,
            popcount
        )
    except Exception as e:
        raise e

    return result


def listRetiredChannels(
    sw
):
    """
    Description:
        List all retired software channels. These are channels that the
        user's organization is entitled to, but are no longer supported
        because they have reached their 'end-of-life' date.

    Parameters:
        - sw session object

    Returns:
        - array:
            - struct - channel info
            - int "id"
            - string "label"
            - string "name"
            - string "provider_name"
            - int "packages"
            - int "systems"
            - string "arch_name"
    """
    try:
        result = sw.session.channel.listRetiredChannels(
            sw.key
        )
    except Exception as e:
        raise e

    return result


def listSharedChannels(
    sw
):
    """
    Description:
    List all software channels that may be shared by the user's organization.

    Parameters:
        - sw session object

    Returns:

        - array:
            - struct - channel info
                - int "id"
                - string "label"
                - string "name"
                - string "provider_name"
                - int "packages"
                - int "systems"
                - string "arch_name"

    """
    try:
        result = sw.session.channel.listSharedChannels(
            sw.key
        )
    except Exception as e:
        raise e

    return result


def listSoftwareChannels(
    sw
):
    """
    Description:
    List all software channels that the user's organization is
    entitled to.

    Parameters:
        - sw session object

    Returns:
        - array:
            - struct - channel info
            - int "id"
            - string "label"
            - string "name"
            - string "provider_name"
            - int "packages"
            - int "systems"
            - string "arch_name"
    """
    try:
        result = sw.session.channel.listSoftwareChannels(
            sw.key
        )
    except Exception as e:
        raise e

    return result


def  listVendorChannels(
    sw
):
    """
    Description:
        Lists all the vendor software channels that the user's
        organization is entitled to.

    Parameters:
        - sw session

    Returns:
        - array:
            - struct - channel info
                - int "id"
                - string "label"
                - string "name"
                - string "provider_name"
                - int "packages"
                - int "systems"
                - string "arch_name"
    """
    try:
        result = sw.session.channel.listVendorChannels(
            sw.key
        )
    except Exception as e:
        raise e

    return result

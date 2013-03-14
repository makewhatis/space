"""
``Namespace: proxy``
======================

Provides methods to activate/deactivate a proxy server.

- :func:`activateProxy`
- :func:`createMonitoringScout`
- :func:`deactivateProxy`
- :func:`isProxy`
- :func:`listAvailableProxyChannels`
"""


def activateProxy(
    sw,
    systemid,
    version
):
    """
    Description:
    Activates the proxy identified by the given client certificate
    i.e. systemid file.

    Parameters:
        - session
        - string systemid - systemid file
        - string version - Version of proxy to be registered.

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.proxy.activateProxy(
            sw.key,
            systemid,
            version
        )
    except Exception as e:
        raise e

    return result


def createMonitoringScout(
    sw,
    systemid
):
    """
    Description:
    Create Monitoring Scout for proxy.

    Parameters:
        - session
        - string systemid - systemid file

    Returns:
        - string

    Available since: 10.7
    """
    try:
        result = sw.session.proxy.createMonitoringScout(
            sw.key,
            systemid
        )
    except Exception as e:
        raise e

    return result


def deactivateProxy(
    sw,
    systemid
):
    """
    Description:
    Deactivates the proxy identified by the given client certificate
    i.e. systemid file.

    Parameters:
    string systemid - systemid file

    Returns:
    int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.proxy.deactivateProxy(
            sw.key,
            systemid
        )
    except Exception as e:
        raise e

    return result


def isProxy(
    sw,
    systemid
):
    """
    Description:
    Test, if the system identified by the given client certificate
    i.e. systemid file, is proxy.

    Parameters:
        - string systemid - systemid file

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.proxy.isProxy(
            sw.key,
            systemid
        )
    except Exception as e:
        raise e

    return result


def listAvailableProxyChannels(
    sw,
    systemid
):
    """
    Description:
    List available version of proxy channel for system identified by the given
    client certificate i.e. systemid file.

    Parameters:
        - string systemid - systemid file

    Returns:
        - array:
            - string - version

    Available since: 10.5
    """
    try:
        result = sw.session.proxy.listAvailableProxyChannels(
            sw.key,
            systemid
        )
    except Exception as e:
        raise e

    return result

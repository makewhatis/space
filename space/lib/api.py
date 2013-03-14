"""
``Namespace: api``
======================

Methods providing information about the API.

Available methods:

- :func:`getApiCallList`
- :func:`getApiNamespaceCallList`
- :func:`getApiNamespaces`
- :func:`getVersion`
- :func:`systemVersion`
"""


def getApiCallList(
    sw
):
    """
    Description:
    Lists all available api calls grouped by namespace

    Parameters:

        - string sessionKey

    Returns:

        - struct - method_info
            - string "name" - method name
            - string "parameters" - method parameters
            - string "exceptions" - method exceptions
            - string "return" - method return type

    """

    try:
        result = sw.session.api.getApiCallList(sw.key)
    except Exception as e:
        raise e

    return result


def getApiNamespaceCallList(
    sw,
    namespace
):
    """
    Description:
    Lists all available api calls for the specified namespace

    Parameters:

        - string sessionKey
        - string namespace

    Returns:

        - struct - method_info
            - string "name" - method name
            - string "parameters" - method parameters
            - string "exceptions" - method exceptions
            - string "return" - method return type
    """

    try:
        result = sw.session.api.getApiNamespaceCallList(
            sw.key,
            namespace
        )
    except Exception as e:
        raise e

    return result


def getApiNamespaces(
    sw
):
    """
    Description:
    Lists available API namespaces

    Parameters:

        - string sessionKey

    Returns:

        - struct - namespace
            - string "namespace" - API namespace
            - string "handler" - API Handler
    """

    try:
        result = sw.session.api.getApiNamespaces(
            sw.key
        )
    except Exception as e:
        raise e

    return result


def getVersion(
    sw
):
    """
    Description:
        Returns the version of the API. Since Spacewalk 0.4 (Satellie 5.3)
         it is no more related to server version.

    Parameters:

    Returns:
        - string
    """

    try:
        result = sw.session.api.getVersion()
    except Exception as e:
        raise e

    return result


def systemVersion(
    sw
):
    """
    Description:
    Returns the server version.

    Parameters:

    Returns:

        - string
    """

    try:
        result = sw.session.api.systemVersion()
    except Exception as e:
        raise e

    return result

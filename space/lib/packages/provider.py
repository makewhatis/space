"""
``Namespace: packages.search``
======================

Methods to interface to package search capabilities in search server.

- :func:`associateKey`
- :func:`list`
- :func:`listKeys`
"""


def associateKey(
    sw,
    provider_name,
    key,
    keytype
):
    """
    Description:
    Associate a package security key and with the package provider. If the
    provider or key doesn't exist, it is created. User executing the request
    must be a Satellite administrator.

    Parameters:
        - string sessionKey
        - string providerName - The provider name
        - string key - The actual key
        - string type - The type of the key. Currently, only 'gpg' is supported

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.packages.provider.associateKey(
            sw.key,
            provider_name,
            key,
            keytype
        )
    except Exception as e:
        raise e

    return result


def list(
    sw
):
    """
    Description:
    List all Package Providers. User executing the request must be a Satellite
    administrator.

    Parameters:
        - string sessionKey

    Returns:
        - array:
            - struct - package provider
                - string "name"
                - array "keys"
                    - struct - package security key
                        - string "key"
                        - string "type"
    """
    try:
        result = sw.session.packages.provider.list(
            sw.key
        )
    except Exception as e:
        raise e

    return result


def listKeys(
    sw,
    provider_name
):
    """
    Description:
    List all security keys associated with a package provider. User executing
    the request must be a Satellite administrator.

    Parameters:
        - string sessionKey
        - string provider_name - The provider name

    Returns:
        - array:
            - struct - package security key
                - string "key"
                - string "type"
    """
    try:
        result = sw.session.packages.provider.listKeys(
            sw.key,
            provider_name
        )
    except Exception as e:
        raise e

    return result

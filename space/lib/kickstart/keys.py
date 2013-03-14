"""
``Namespace: kickstart.keys``
=============================

Provides methods to manipulate kickstart keys.

Available methods:


- :func:`create`
- :func:`delete`
- :func:`getDetails`
- :func:`listAllKeys`
- :func:`update`
"""


def create(
    sw,
    description,
    keytype,
    content
):
    """
    Description:
    creates a new key with the given parameters

    Parameters:
        - string session_key
        - string description
        - string type - valid values are GPG or SSL
        - string content

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.kickstart.keys.create(
            sw.key,
            description,
            keytype,
            content
        )
    except Exception as e:
        raise e

    return result


def delete(
    sw,
    description
):
    """
    Description:
    deletes the key identified by the given parameters

    Parameters:
        - string session_key
        - string description

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.kickstart.keys.delete(
            sw.key,
            description
        )
    except Exception as e:
        raise e

    return result


def getDetails(
    sw,
    description
):
    """
    Description:
    returns all of the data associated with the given key

    Parameters:
        - string session_key
        - string description

    Returns:
        - struct - key
            - string "description"
            - string "type"
            - string "content"
    """
    try:
        result = sw.session.kickstart.keys.getDetails(
            sw.key,
            description
        )
    except Exception as e:
        raise e

    return result


def listAllKeys(
    sw
):
    """
    Description:
    list all keys for the org associated with the user logged into the given
    session

    Parameters:
        - string sessionKey

    Returns:
        - array:
            - struct - key
                - string "description"
                - string "type"
    """
    try:
        result = sw.session.kickstart.keys.listAllKeys(
            sw.key
        )
    except Exception as e:
        raise e

    return result


def update(
    sw,
    description,
    keytype,
    content
):
    """
    Description:
    Updates type and content of the key identified by the description

    Parameters:
        - string session_key
        - string description
        - string type - valid values are GPG or SSL
        - string content

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.kickstart.keys.update(
            sw.key,
            description,
            keytype,
            content
        )
    except Exception as e:
        raise e

    return result

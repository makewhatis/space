"""
``Namespace: system.custominfo``
======================

Provides methods to access and modify custom system information.

- :func:`createKey`
- :func:`deleteKey`
- :func:`listAllKeys`
- :func:`updateKey`
"""


def createKey(
    sw,
    keylabel,
    keydescription
):
    """
    Description:
    Create a new custom key

    Parameters:
        - object session
        - string keylabel - new key's label
        - string keydescription - new key's description

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.system.custominfo.createKey(
            sw.key,
            keylabel,
            keydescription
        )
    except Exception as e:
        raise e

    return result


def deleteKey(
    sw,
    keylabel
):
    """
    Description:
    Delete an existing custom key and all systems' values for the key.

    Parameters:
        - object session
        - string keylabel - new key's label

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.system.custominfo.deleteKey(
            sw.key,
            keylabel
        )
    except Exception as e:
        raise e

    return result


def listAllKeys(
    sw
):
    """
    Description:
    List the custom information keys defined for the user's organization.

    Parameters:
        - object session

    Returns:
        - array:
            - struct - custom info
                - int "id"
                - string "label"
                - string "description"
                - int "system_count"
                - dateTime.iso8601 "last_modified"
    """
    try:
        result = sw.session.system.custominfo.listAllKeys(
            sw.key
        )
    except Exception as e:
        raise e

    return result


def updateKey(
    sw,
    keylabel,
    keydescription
):
    """
    Description:
    Update description of a custom key

    Parameters:
        - object session
        - string keylabel - key to change
        - string keydescription - new key's description

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.system.custominfo.updateKey(
            sw.key,
            keylabel,
            keydescription
        )
    except Exception as e:
        raise e

    return result

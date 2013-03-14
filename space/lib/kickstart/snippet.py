"""
``Namespace: kickstart.snippet``
================================

Provides methods to create kickstart files

Available methods:

- :func:`createOrUpdate`
- :func:`delete`
- :func:`listAll`
- :func:`listCustom`
- :func:`listDefault`
"""


def createOrUpdate(
    sw,
    name,
    contents
):
    """
    Description:
    Will create a snippet with the given name and contents if it doesn't exist.
    If it does exist, the existing snippet will be updated.

    Parameters:
        - string sessionKey
        - string name
        - string contents

    Returns:
        - struct - snippet
            - string "name"
            - string "contents"
            - string "fragment" - The string to include in a kickstart file
                                  that will generate this snippet.
            - string "file" - The local path to the file containing this
                              snippet.
    """
    try:
        result = sw.session.kickstart.snippet.createOrUpdate(
            sw.key,
            name,
            contents
        )
    except Exception as e:
        raise e

    return result


def delete(
    sw,
    name
):
    """
    Description:
    Delete the specified snippet. If the snippet is not found, 0 is returned.

    Parameters:
        - string sessionKey
        - string name

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.kickstart.snippet.delete(
            sw.key,
            name
        )
    except Exception as e:
        raise e

    return result


def listAll(
    sw
):
    """
    Parameters:
    string sessionKey

    Returns:
        - array:
            - struct - snippet
                - string "name"
                - string "contents"
                - string "fragment" - The string to include in a kickstart file
                                      that will generate this snippet.
                - string "file" - The local path to the file containing this
                                  snippet.
    """
    try:
        result = sw.session.kickstart.snippet.listAll(
            sw.key
        )
    except Exception as e:
        raise e

    return result


def listCustom(
    sw
):
    """
    Description:
    List only custom snippets for the logged in user. These snipppets are
    editable.

    Parameters:
        - string sessionKey

    Returns:
        - array:
            - struct - snippet
                - string "name"
                - string "contents"
                - string "fragment" - The string to include in a kickstart file
                                       that will generate this snippet.
                - string "file" - The local path to the file containing this
                                  snippet.
    """
    try:
        result = sw.session.kickstart.snippet.listCustom(
            sw.key
        )
    except Exception as e:
        raise e

    return result


def listDefault(
    sw
):
    """
    Description:
    List only pre-made default snippets for the logged in user. These snipppets
    are not editable.

    Parameters:
    -   string sessionKey

    Returns:
        - array:
            - struct - snippet
                - string "name"
                - string "contents"
                - string "fragment" - The string to include in a kickstart
                                      file that will generate this snippet.
                - string "file" - The local path to the file containing this
                                  snippet.
    """
    try:
        result = sw.session.kickstart.snippet.listDefault(
            sw.key
        )
    except Exception as e:
        raise e

    return result

"""
``Namespace: kickstart.filepreservation``
======================

Provides methods to retrieve and manipulate kickstart file preservation lists.

Available methods:


- :func:`create`
- :func:`delete`
- :func:`getDetails`
- :func:`listAllFilePreservations`
"""


def create(
    sw,
    name,
    filenames
):
    """
    Description:
    Create a new file preservation list.

    Parameters:
        - string session_key
        - string name - name of the file list to create
        - array:
            - string - name - file names to include

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.kickstart.filepreservation.create(
            sw.key,
            name,
            filenames
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
    Delete a file preservation list.

    Parameters:
        - string session_key
        - string name - name of the file list to delete

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.kickstart.filepreservation.delete(
            sw.key,
            name
        )
    except Exception as e:
        raise e

    return result


def getDetails(
    sw,
    name
):
    """
    Description:
    Returns all of the data associated with the given file preservation list.

    Parameters:
        - string session_key
        - string name - name of the file list to retrieve details for

    Returns:
        - struct - file list
            - string "name"
            - array "file_names"
                - string name
    """
    try:
        result = sw.session.kickstart.filepreservation.getDetails(
            sw.key,
            name
        )
    except Exception as e:
        raise e

    return result


def listAllFilePreservations(
    sw
):
    """
    Description:
    List all file preservation lists for the organization associated with the
    user logged into the given session

    Parameters:
        - string sessionKey

    Returns:
        - array:
            - struct - file preservation
                - int "id"
                - string "name"
                - dateTime.iso8601 "created"
                - dateTime.iso8601 "last_modified"
    """
    try:
        result = sw.session.kickstart.filepreservation.\
            listAllFilePreservations(
                sw.key
            )
    except Exception as e:
        raise e

    return result

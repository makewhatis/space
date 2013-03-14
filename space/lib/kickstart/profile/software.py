"""
``Namespace: kickstart.profile.software``
======================

Provides methods to access and modify the list of
activation keys associated with a kickstart profile.

Available methods:

- :func:`appendToSoftwareList`
- :func:`getSoftwareList`
- :func:`setSoftwareList`
"""


def appendToSoftwareList(
    sw,
    kslabel
):
    """
    Description:
    Append the list of software packages to a kickstart profile.
    Duplicate packages will be ignored.

    Parameters:
        - string sessionKey
        - string ksLabel - The label of a kickstart profile.
        - string[] packageList - A list of package names to be added
                                to the profile.

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.kickstart.profile.software.appendToSoftwareList(
            sw.key,
            kslabel
        )
    except Exception as e:
        raise e

    return result


def getSoftwareList(
    sw,
    kslabel
):
    """
    Description:
    Get a list of a kickstart profile's software packages.

    Parameters:
        - string sessionKey
        - string ksLabel - The label of a kickstart profile.

    Returns:

        - string[] - Get a list of a kickstart profile's software packages.
    """
    try:
        result = sw.session.kickstart.profile.software.getSoftwareList(
            sw.key,
            kslabel
        )
    except Exception as e:
        raise e

    return result


def setSoftwareList(
    sw,
    kslabel,
    packagelist
):
    """
    Description:
    Set the list of software packages for a kickstart profile.

    Parameters:
        - string sessionKey
        - string ksLabel - The label of a kickstart profile.
        - string[] packageList - A list of package names to be set on the
                                 profile.

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.kickstart.profile.software.setSoftwareList(
            sw.key,
            kslabel,
            packagelist
        )
    except Exception as e:
        raise e

    return result

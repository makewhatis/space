"""
``Namespace: kickstart.profile.system``
=======================================

Provides methods to set various properties of a kickstart profile.

Available methods:

- :func:`addFilePreservations`
- :func:`addKeys`
- :func:`checkConfigManagement`
- :func:`checkRemoteCommands`
- :func:`disableConfigManagement`
- :func:`disableRemoteCommands`
- :func:`enableConfigManagement`
- :func:`enableRemoteCommands`
- :func:`getLocale`
- :func:`getPartitioningScheme`
- :func:`getRegistrationType`
- :func:`getSELinux`
- :func:`listFilePreservations`
- :func:`listKeys`
- :func:`removeFilePreservations`
- :func:`removeKeys`
- :func:`setLocale`
- :func:`setPartitioningScheme`
- :func:`setRegistrationType`
- :func:`setSELinux`
"""


def addFilePreservations(
    sw,
    kslabel,
    filepreservations
):
    """
    Description:
    Adds the given list of file preservations to the specified kickstart
    profile.

    Parameters:
        - string sessionKey
        - string kickstartLabel
        - array:
            - string - filePreservations

    Returns:
    int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.kickstart.profile.system.addFilePreservations(
            sw.key,
            kslabel,
            filepreservations
        )
    except Exception as e:
        raise e

    return result


def addKeys(
    sw,
    kslabel,
    keydescription
):
    """
    Description:
    Adds the given list of keys to the specified kickstart profile.

    Parameters:
        - string sessionKey
        - string kickstartLabel
        - array:
            - string - keyDescription

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.kickstart.profile.system.addKeys(
            sw.key,
            kslabel,
            keydescription
        )
    except Exception as e:
        raise e

    return result


def checkConfigManagement(
    sw,
    kslabel
):
    """
    Description:
    Check the configuration management status for a kickstart profile.

    Parameters:
        - string sessionKey
        - string kslabel - the kickstart profile label

    Returns:
        - boolean enabled - true if configuration management is enabled;
                            otherwise, false
    """
    try:
        result = sw.session.kickstart.profile.system.checkConfigManagement(
            sw.key,
            kslabel
        )
    except Exception as e:
        raise e

    return result


def checkRemoteCommands(
    sw,
    kslabel
):
    """
    Description:
    Check the remote commands status flag for a kickstart profile.

    Parameters:
        - string sessionKey
        - string ksLabel - the kickstart profile label

    Returns:
        - boolean enabled - true if remote commands support is enabled;
                            otherwise, false
    """
    try:
        result = sw.session.kickstart.profile.system.checkRemoteCommands(
            sw.key,
            kslabel
        )
    except Exception as e:
        raise e

    return result


def disableConfigManagement(
    sw,
    kslabel
):
    """
    Description:
    Disables the configuration management flag in a kickstart profile so
    that a system created using this profile will be NOT be configuration
    capable.

    Parameters:
        - string sessionKey
        - string ksLabel - the kickstart profile label

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.kickstart.profile.system.disableConfigManagement(
            sw.key,
            kslabel
        )
    except Exception as e:
        raise e

    return result


def disableRemoteCommands(
    sw,
    kslabel
):
    """
    Description:
    Disables the remote command flag in a kickstart profile so that a system
    created using this profile will be capable of running remote commands

    Parameters:
        - string sessionKey
        - string ksLabel - the kickstart profile label

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.kickstart.profile.system.disableRemoteCommands(
            sw.key,
            kslabel
        )
    except Exception as e:
        raise e

    return result


def enableConfigManagement(
    sw,
    kslabel
):
    """
    Description:
    Enables the configuration management flag in a kickstart profile so that
    a system created using this profile will be configuration capable.

    Parameters:
        - string sessionKey
        - string kslabel - the kickstart profile label

    Returns:
    int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.kickstart.profile.system.enableConfigManagement(
            sw.key,
            kslabel
        )
    except Exception as e:
        raise e

    return result


def enableRemoteCommands(
    sw,
    kslabel
):
    """
    Description:
    Enables the remote command flag in a kickstart profile so that a system
    created using this profile will be capable of running remote commands

    Parameters:
        - string sessionKey
        - string ksLabel - the kickstart profile label

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.kickstart.profile.system.enableRemoteCommands(
            sw.key,
            kslabel
        )
    except Exception as e:
        raise e

    return result


def getLocale(
    sw,
    kslabel
):
    """
    Description:
    Retrieves the locale for a kickstart profile.

    Parameters:
        - string sessionKey
        - string kslabel - the kickstart profile label

    Returns:
        - struct - locale info
            - string "locale"
            - boolean "useUtc"
                - true - the hardware clock uses UTC
                - false - the hardware clock does not use UTC
    """
    try:
        result = sw.session.kickstart.profile.system.getLocale(
            sw.key,
            kslabel
        )
    except Exception as e:
        raise e

    return result


def getPartitioningScheme(
    sw,
    kslabel
):
    """
    Description:
    Get the partitioning scheme for a kickstart profile.

    Parameters:
        - string sessionKey
        - string kslabel - The label of a kickstart profile.

    Returns:
        - string[] - A list of partitioning commands used to setup the
                     partitions, logical volumes and volume groups.
    """
    try:
        result = sw.session.kickstart.profile.system.getPartitioningScheme(
            sw.key,
            kslabel
        )
    except Exception as e:
        raise e

    return result


def getRegistrationType(
    sw,
    kslabel
):
    """
    Description:
    returns the registration type of a given kickstart profile. Registration
    Type can be one of reactivation/deletion/none These types determine the
    behaviour of the registration when using this profile for reprovisioning.

    Parameters:
        - string sessionKey
        - string kslabel

    Returns:
        - string registrationType
            - reactivation
            - deletion
    none

    """
    try:
        result = sw.session.kickstart.profile.system.getRegistrationType(
            sw.key,
            kslabel
        )
    except Exception as e:
        raise e

    return result


def getSELinux(
    sw,
    kslabel
):
    """
    Description:
    Retrieves the SELinux enforcing mode property of a kickstart profile.

    Parameters:
    string sessionKey
    string kslabel - the kickstart profile label

    Returns:
        - string enforcingMode
            - enforcing
            - permissive
            - disabled
    """
    try:
        result = sw.session.kickstart.profile.system.getSELinux(
            sw.key,
            kslabel
        )
    except Exception as e:
        raise e

    return result


def listFilePreservations(
    sw,
    kslabel
):
    """
    Description:
    Returns the set of all file preservations associated with the given
    kickstart profile.

    Parameters:
        - string sessionKey
        - string kslabel

    Returns:
        - array:
            - struct - file list
                - string "name"
                - array "file_names"
                    - string name
    """
    try:
        result = sw.session.kickstart.profile.system.listFilePreservations(
            sw.key,
            kslabel
        )
    except Exception as e:
        raise e

    return result


def listKeys(
    sw,
    kslabel
):
    """
    Description:
    Returns the set of all keys associated with the given kickstart profile.

    Parameters:
        - string sessionKey
        - string kslabel

    Returns:
        - array:
            - struct - key
                - string "description"
                - string "type"
                - string "content"
    """
    try:
        result = sw.session.kickstart.profile.system.listKeys(
            sw.key,
            kslabel
        )
    except Exception as e:
        raise e

    return result


def removeFilePreservations(
    sw,
    kslabel,
    filepreservations
):
    """
    Description:
    Removes the given list of file preservations from the specified kickstart
    profile.

    Parameters:
        - string sessionKey
        - string kslabel
        - array:
            - string - filePreservations

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.kickstart.profile.system.removeFilePreservations(
            sw.key,
            kslabel,
            filepreservations
        )
    except Exception as e:
        raise e

    return result


def removeKeys(
    sw,
    kslabel,
    keydescription
):
    """
    Description:
    Removes the given list of keys from the specified kickstart profile.

    Parameters:
        - string sessionKey
        - string kslabel
        - array:
            - string - keyDescription

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.kickstart.profile.system.removeKeys(
            sw.key,
            kslabel,
            keydescription
        )
    except Exception as e:
        raise e

    return result


def setLocale(
    sw,
    kslabel,
    locale,
    useutc
):
    """
    Description:
    Sets the locale for a kickstart profile.

    Parameters:
        - string sessionKey
        - string kslabel - the kickstart profile label
        - string locale - the locale
        - boolean useUtc
            true - the hardware clock uses UTC
            false - the hardware clock does not use UTC

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.kickstart.profile.system.setLocale(
            sw.key,
            kslabel,
            locale,
            useutc
        )
    except Exception as e:
        raise e

    return result


def setPartitioningScheme(
    sw,
    kslabel,
    scheme
):
    """
    Description:
    Set the partitioning scheme for a kickstart profile.

    Parameters:
        - string sessionKey
        - string kslabel - The label of the kickstart profile to update.
        - string[] scheme - The partitioning scheme is a list of partitioning
                           command strings used to setup the partitions, volume
                           groups and logical volumes.

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.kickstart.profile.system.setPartitioningScheme(
            sw.key,
            kslabel,
            scheme
        )
    except Exception as e:
        raise e

    return result


def setRegistrationType(
    sw,
    kslabel,
    registrationtype
):
    """
    Description:
    Sets the registration type of a given kickstart profile. Registration Type
    can be one of reactivation/deletion/none These types determine the
    behaviour of the re registration when using this profile.

    Parameters:
        - string sessionKey
        - string kslabel
        - string registrationType
            - reactivation - to try and generate a reactivation key and use
                             that to register the system when reprovisioning a
                             system.
            - deletion - to try and delete the existing system profile and
                         reregister the system being reprovisioned as new
            - none - to preserve the status quo and leave the current system as
                     a duplicate on a reprovision.

    Returns:
    int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.kickstart.profile.system.setRegistrationType(
            sw.key,
            kslabel,
            registrationtype
        )
    except Exception as e:
        raise e

    return result


def setSELinux(
    sw,
    kslabel,
    enforcingmode
):
    """
    Description:
    Sets the SELinux enforcing mode property of a kickstart profile so that
    a system created using this profile will be have the appropriate SELinux
    enforcing mode.

    Parameters:
        - string sessionKey
        - string kslabel - the kickstart profile label
        - string enforcingMode - the selinux enforcing mode
            - enforcing
            - permissive
            - disabled

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.kickstart.profile.system.setSELinux(
            sw.key,
            kslabel,
            enforcingmode
        )
    except Exception as e:
        raise e

    return result

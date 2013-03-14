"""
``Namespace: kickstart``
========================

Provides methods to access and modify distribution channel information.

Available methods:


- :func:`cloneProfile`
- :func:`createProfile`
- :func:`createProfileWithCustomUrl`
- :func:`deleteProfile`
- :func:`disableProfile`
- :func:`findKickstartForIp`
- :func:`importFile`
- :func:`importFile`
- :func:`importRawFile`
- :func:`isProfileDisabled`
- :func:`listAllIpRanges`
- :func:`listKickstartableChannels`
- :func:`listKickstartableTrees`
- :func:`listKickstarts`
- :func:`renameProfile`

"""


def cloneProfile(
    sw,
    kslabeltoclone,
    newkslabel
):
    """
    Description:
    Clone a Kickstart Profile

    Parameters:
        - string sessionKey
        - string ksLabelToClone - Label of the kickstart profile to clone
        - string newKsLabel - label of the cloned profile

    Returns:
    int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.kickstart.cloneProfile(
            sw.key,
            kslabeltoclone,
            newkslabel
        )
    except Exception as e:
        raise e

    return result


def createProfile(
    sw,
    profilelabel,
    virtualizationtype,
    kickstartabletreelabel,
    kickstarthost,
    rootpassword
):
    """
    Description:
    Import a kickstart profile into RHN.

    Parameters:
        - string sessionKey
        - string profileLabel - Label for the new kickstart profile.
        - string virtualizationType - none, para_host, qemu, xenfv or xenpv.
        - string kickstartableTreeLabel - Label of a kickstartable tree to
                                          associate the new profile with.
        - string kickstartHost - Kickstart hostname (of a satellite or proxy)
                                used to construct the default download URL for
                                the new kickstart profile.
        - string rootPassword - Root password.

    Returns:
    int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.kickstart.createProfile(
            sw.key,
            profilelabel,
            virtualizationtype,
            kickstartabletreelabel,
            kickstarthost,
            rootpassword
        )
    except Exception as e:
        raise e

    return result


def createProfileWithCustomUrl(
    sw,
    profilelabel,
    virtualizationtype,
    kickstartabletreelabel,
    downloadurl,
    rootpassword
):
    """
    Description:
    Import a kickstart profile into RHN.

    Parameters:
        - string sessionKey
        - string profileLabel - Label for the new kickstart profile.
        - string virtualizationType - none, para_host, qemu, xenfv or xenpv.
        - string kickstartableTreeLabel - Label of a kickstartable tree to
                                          associate the new profile with.
        - boolean downloadUrl - Download URL, or 'default' to use the kickstart
                                tree's default URL.
        - string rootPassword - Root password.

    Returns:
    int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.kickstart.createProfileWithCustomUrl(
            sw.key,
            profilelabel,
            virtualizationtype,
            kickstartabletreelabel,
            downloadurl,
            rootpassword
        )
    except Exception as e:
        raise e

    return result


def deleteProfile(
    sw,
    kslabel
):
    """
    Description:
    Delete a kickstart profile

    Parameters:
        - string sessionKey
        - string ksLabel - The label of the kickstart profile you want to
                           remove

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.kickstart.deleteProfile(
            sw.key,
            kslabel
        )
    except Exception as e:
        raise e

    return result


def disableProfile(
    sw,
    profilelabel,
    disabled
):
    """
    Description:
    Enable/Disable a Kickstart Profile

    Parameters:
        - string sessionKey
        - string profileLabel - Label for the kickstart tree you want to
                                en/disable
        - string disabled - true to disable the profile

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.kickstart.disableProfile(
            sw.key,
            profilelabel,
            disabled
        )
    except Exception as e:
        raise e

    return result


def findKickstartForIp(
    sw,
    ipaddress
):
    """
    Description:
    Find an associated kickstart for a given ip address.

    Parameters:
        - string sessionKey
        - string ipAddress - The ip address to search for (i.e. 192.168.0.1)

    Returns:
        - string - label of the kickstart. Empty string ("") if not found.
    """
    try:
        result = sw.session.kickstart.findKickstartForIp(
            sw.key,
            ipaddress
        )
    except Exception as e:
        raise e

    return result


def importFile(
    sw,
    profilelabel,
    virtualizationtype,
    kickstartabletreelabel,
    kickstartfilecontents,
    kickstarthost=None
):
    """
    Description:
    Import a kickstart profile into RHN.

    Parameters:
        - string sessionKey
        - string profileLabel - Label for the new kickstart profile.
        - string virtualizationType - none, para_host, qemu, xenfv or xenpv.
        - string kickstartableTreeLabel - Label of a kickstartable tree to
                                          associate the new profile with.
        - string kickstartHost - Kickstart hostname (of a satellite or proxy)
                                 used to construct the default download URL for
                                 the new kickstart profile. Using this option
                                 signifies that this default URL will be used
                                 instead of any url/nfs/cdrom/harddrive
                                 commands in the kickstart file itself.
        - string kickstartFileContents - Contents of the kickstart file to
                                         import.

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    if kickstarthost:
        try:
            result = sw.session.kickstart.importFile(
                sw.key,
                profilelabel,
                virtualizationtype,
                kickstartabletreelabel,
                kickstartfilecontents,
                kickstarthost
            )
        except Exception as e:
            raise e
    else:
        try:
            result = sw.session.kickstart.importFile(
                sw.key,
                profilelabel,
                virtualizationtype,
                kickstartabletreelabel,
                kickstartfilecontents
            )
        except Exception as e:
            raise e

    return result


def importRawFile(
    sw,
    profilelabel,
    virtualizationtype,
    kickstartabletreelabel,
    kickstartfilecontents
):
    """
    Description:
    Import a raw kickstart file into satellite.

    Parameters:
        - string sessionKey
        - string profileLabel - Label for the new kickstart profile.
        - string virtualizationType - none, para_host, qemu, xenfv or xenpv.
        - string kickstartableTreeLabel - Label of a kickstartable tree to
                                          associate the new profile with.
        - string kickstartFileContents - Contents of the kickstart file to
                                        import.

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.kickstart.importRawFile(
            sw.key,
            profilelabel,
            virtualizationtype,
            kickstartabletreelabel,
            kickstartfilecontents
        )
    except Exception as e:
        raise e

    return result


def isProfileDisabled(
    sw,
    profilelabel
):
    """
    Description:
    Returns whether a kickstart profile is disabled

    Parameters:
        - string sessionKey
        - string profileLabel - kickstart profile label

    Returns:
        - true if profile is disabled
    """
    try:
        result = sw.session.kickstart.isProfileDisabled(
            sw.key,
            profilelabel
        )
    except Exception as e:
        raise e

    return result


def listAllIpRanges(
    sw
):
    """
    Description:
    List all Ip Ranges and their associated kickstarts available in the user's
    org.

    Parameters:
        - string sessionKey

    Returns:
        - array:
            - struct - Kickstart Ip Range
                - string "ksLabel" - The kickstart label associated with the ip
                                    range
                - string "max" - The max ip of the range
                - string "min" - The min ip of the range
    """
    try:
        result = sw.session.kickstart.listAllIpRanges(
            sw.key
        )
    except Exception as e:
        raise e

    return result


def listKickstartableChannels(
    sw
):
    """
    Description:
    List kickstartable channels for the logged in user.

    Parameters:
        - string sessionKey

    Returns:
        - array:
            - struct - channel
                - int "id"
                - string "name"
                - string "label"
                - string "arch_name"
                - string "summary"
                - string "description"
                - string "checksum_label"
                - dateTime.iso8601 "last_modified"
                - string "maintainer_name"
                - string "maintainer_email"
                - string "maintainer_phone"
                - string "support_policy"
                - string "gpg_key_url"
                - string "gpg_key_id"
                - string "gpg_key_fp"
                - dateTime.iso8601 "yumrepo_last_sync" - (optional)
                - string "end_of_life"
                - string "parent_channel_label"
                - string "clone_original"
                - array:
                    - struct - contentSources
                        - int "id"
                        - string "label"
                        - string "sourceUrl"
                        - string "type"
    """
    try:
        result = sw.session.kickstart.listKickstartableChannels(
            sw.key
        )
    except Exception as e:
        raise e

    return result


def listKickstarts(
    sw
):
    """
    Description:
    Provides a list of kickstart profiles visible to the user's org

    Parameters:
        - string sessionKey

    Returns:
        - array:
        - struct - kickstart
            - string "label"
            - string "tree_label"
            - string "name"
            - boolean "advanced_mode"
            - boolean "org_default"
            - boolean "active"

    """
    try:
        result = sw.session.kickstart.listKickstarts(
            sw.key
        )
    except Exception as e:
        raise e

    return result


def renameProfile(
    sw,
    originallabel,
    newlabel
):
    """
    Description:
    Rename a Kickstart Profile in Satellite

    Parameters:
        - string sessionKey
        - string originalLabel - Label for the kickstart profile you want to
                                rename
        - string newLabel - new label to change to

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.kickstart.renameProfile(
            sw.key,
            originallabel,
            newlabel
        )
    except Exception as e:
        raise e

    return result

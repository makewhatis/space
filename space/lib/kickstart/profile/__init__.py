"""
``Namespace: kickstart.profile``
======================

Provides methods to access and modify many aspects of a kickstart profile.

Available methods:


- :func:`addIpRange`
- :func:`addScript`
- :func:`addScript`
- :func:`compareActivationKeys`
- :func:`compareAdvancedOptions`
- :func:`comparePackages`
- :func:`downloadKickstart`
- :func:`downloadRenderedKickstart`
- :func:`getAdvancedOptions`
- :func:`getCfgPreservation`
- :func:`getChildChannels`
- :func:`getCustomOptions`
- :func:`getKickstartTree`
- :func:`getVariables`
- :func:`listIpRanges`
- :func:`listScripts`
- :func:`removeIpRange`
- :func:`removeScript`
- :func:`setAdvancedOptions`
- :func:`setCfgPreservation`
- :func:`setChildChannels`
- :func:`setCustomOptions`
- :func:`setKickstartTree`
- :func:`setLogging`
- :func:`setVariables`
"""


def addIpRange(
    sw,
    label,
    minrange,
    maxrange
):
    """
    Description:
    Add an ip range to a kickstart profile.

    Parameters:
        - string sessionKey
        - string label - The label of the kickstart
        - string min - The ip address making up the minimum of the range
                       (i.e. 192.168.0.1)
        - string max - The ip address making up the maximum of the range
                       (i.e. 192.168.0.254)

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.kickstart.profile.addIpRange(
            sw.key,
            label,
            minrange,
            maxrange
        )
    except Exception as e:
        raise e

    return result


def addScript(
    sw,
    kslabel,
    contents,
    interpreter,
    script_type,
    chroot,
    template
):
    """
    Description:
    Add a pre/post script to a kickstart profile.

    Parameters:
        - string sessionKey
        - string ksLabel - The kickstart label to add the script to.
        - string contents - The full script to add.
        - string interpreter - The path to the interpreter to use
                              (i.e. /bin/bash). An empty string will use the
                              kickstart default interpreter.
        - string type - The type of script (either 'pre' or 'post').
        - boolean chroot - Whether to run the script in the chrooted install
                           location (recommended) or not.
        - boolean template - Enable templating using cobbler.

    Returns:
        - int id - the id of the added script
    """
    try:
        result = sw.session.kickstart.profile.addScript(
            sw.key,
            kslabel,
            contents,
            interpreter,
            script_type,
            chroot,
            template
        )
    except Exception as e:
        raise e

    return result


def compareActivationKeys(
    sw,
    kickstartlabel1,
    kickstartlabel2
):
    """
    Description:
    Returns a list for each kickstart profile; each list will contain
    activation keys not present on the other profile.

    Parameters:
        - string sessionKey
        - string kickstartlabel1
        - string kickstartlabel2

    Returns:
        - struct - Comparison Info
            - array "kickstartLabel1" - Actual label of the first kickstart
                                        profile is the key into the struct
                - struct - activation key
                    - string "key"
                    - string "description"
                    - int "usage_limit"
                    - string "base_channel_label"
                    - array "child_channel_labels"
                        - string childChannelLabel
                    - array "entitlements"
                        - string entitlementLabel
                    - array "server_group_ids"
                        - string serverGroupId
                    - array "package_names"
                        - string packageName - (deprecated by packages)
                    - array "packages"
                        - struct - package
                            - string "name" - packageName
                            - string "arch" - archLabel - optional
                    - boolean "universal_default"
                    - boolean "disabled"
            - array "kickstartLabel2" - Actual label of the second kickstart
                                        profile is the key into the struct
                - struct - activation key
                    - string "key"
                    - string "description"
                    - int "usage_limit"
                    - string "base_channel_label"
                    - array "child_channel_labels"
                        - string childChannelLabel
                    - array "entitlements"
                        - string entitlementLabel
                    - array "server_group_ids"
                        - string serverGroupId
                    - array "package_names"
                        - string packageName - (deprecated by packages)
                    - array "packages"
                        - struct - package
                            - string "name" - packageName
                            - string "arch" - archLabel - optional
                    - boolean "universal_default"
                    - boolean "disabled"
    """
    try:
        result = sw.session.kickstart.profile.compareActivationKeys(
            sw.key,
            kickstartlabel1,
            kickstartlabel2
        )
    except Exception as e:
        raise e

    return result


def compareAdvancedOptions(
    sw,
    kickstartlabel1,
    kickstartlabel2

):
    """
    Description:
    Returns a list for each kickstart profile; each list will contain the
    properties that differ between the profiles and their values for that
    specific profile .

    Parameters:
        - string sessionKey
        - string kickstartlabel1
        - string kickstartlabel2

    Returns:
        - struct - Comparison Info
            - array "kickstartlabel1" - Actual label of the first kickstart
                                        profile is the key into the struct
                - struct - value
                    - string "name"
                    - string "value"
                    - boolean "enabled"
            - array "kickstartlabel2" - Actual label of the second kickstart
                                        profile is the key into the struct
                - struct - value
                    - string "name"
                    - string "value"
                    - boolean "enabled"
    """
    try:
        result = sw.session.kickstart.profile.compareAdvancedOptions(
            sw.key,
            kickstartlabel1,
            kickstartlabel2
        )
    except Exception as e:
        raise e

    return result


def comparePackages(
    sw,
    kickstartlabel1,
    kickstartlabel2
):
    """
    Description:
    Returns a list for each kickstart profile; each list will contain package
    names not present on the other profile.

    Parameters:
        - string sessionKey
        - string kickstartlabel1
        - string kickstartlabel2

    Returns:
        - struct - Comparison Info
            - array "kickstartlabel1" - Actual label of the first kickstart
                                        profile is the key into the struct
                - string - package name
            - array "kickstartlabel2" - Actual label of the second kickstart
                                        profile is the key into the struct
                - string - package name
    """
    try:
        result = sw.session.kickstart.profile.comparePackages(
            sw.key,
            kickstartlabel1,
            kickstartlabel2
        )
    except Exception as e:
        raise e

    return result


def downloadKickstart(
    sw,
    kslabel,
    host
):
    """
    Description:
    Download the full contents of a kickstart file.

    Parameters:
    string sessionKey
    string kslabel - The label of the kickstart to download.
    string host - The host to use when referring to the satellite itself

    Returns:
    string - The contents of the kickstart file.
    """
    try:
        result = sw.session.kickstart.profile.downloadKickstart(
            sw.key,
            kslabel,
            host
        )
    except Exception as e:
        raise e

    return result


def downloadRenderedKickstart(
    sw,
    kslabel
):
    """
    Description:
    Downloads the Cobbler-rendered Kickstart file.

    Parameters:
        - string sessionKey
        - string kslabel - The label of the kickstart to download.

    Returns:
        - string - The contents of the kickstart file.
    """
    try:
        result = sw.session.kickstart.profile.downloadRenderedKickstart(
            sw.key,
            kslabel
        )
    except Exception as e:
        raise e

    return result


def getAdvancedOptions(
    sw,
    kslabel
):
    """
    Description:
    Get advanced options for a kickstart profile.

    Parameters:
    string sessionKey
    string kslabel - Label of kickstart profile to be changed.

    Returns:
        - array:
            - struct - option
                - string "name"
                - string "arguments"
    """
    try:
        result = sw.session.kickstart.profile.getAdvancedOptions(
            sw.key,
            kslabel
        )
    except Exception as e:
        raise e

    return result


def getCfgPreservation(
    sw,
    kslabel
):
    """
    Description:
    Get ks.cfg preservation option for a kickstart profile.

    Parameters:
        - string sessionKey
        - string kslabel - Label of kickstart profile to be changed.

    Returns:
        - boolean - The value of the option. True means that ks.cfg will be
                    copied to /root, false means that it will not.
    """
    try:
        result = sw.session.kickstart.profile.getCfgPreservation(
            sw.key,
            kslabel
        )
    except Exception as e:
        raise e

    return result


def getChildChannels(
    sw,
    kslabel
):
    """
    Description:
    Get the child channels for a kickstart profile.

    Parameters:
        - string sessionKey
        - string kslabel - Label of kickstart profile.

    Returns:
        - string - channelLabel
    """
    try:
        result = sw.session.kickstart.profile.getChildChannels(
            sw.key,
            kslabel
        )
    except Exception as e:
        raise e

    return result


def getCustomOptions(
    sw,
    kslabel
):
    """
    Description:
    Get custom options for a kickstart profile.

    Parameters:
        - string sessionKey
        - string kslabel

    Returns:
        - struct - option
            - int "id"
            - string "arguments"
    """
    try:
        result = sw.session.kickstart.profile.getCustomOptions(
            sw.key,
            kslabel
        )
    except Exception as e:
        raise e

    return result


def getKickstartTree(
    sw,
    kslabel
):
    """
    Description:
    Get the kickstart tree for a kickstart profile.

    Parameters:
        - string sessionKey
        - string kslabel - Label of kickstart profile to be changed.

    Returns:
        - string kstreeLabel - Label of the kickstart tree.
    """
    try:
        result = sw.session.kickstart.profile.getKickstartTree(
            sw.key,
            kslabel
        )
    except Exception as e:
        raise e

    return result


def getVariables(
    sw,
    kslabel
):
    """
    Description:
    Returns a list of variables associated with the specified kickstart profile

    Parameters:
        - string sessionKey
        - string ksLabel

    Returns:
        - struct - kickstart variable
            - string "key"
            - string or int "value"
    """
    try:
        result = sw.session.kickstart.profile.getVariables(
            sw.key,
            kslabel
        )
    except Exception as e:
        raise e

    return result


def listIpRanges(
    sw,
    label
):
    """
    Description:
    List all ip ranges for a kickstart profile.

    Parameters:
        - string sessionKey
        - string label - The label of the kickstart

    Returns:
        - struct - Kickstart Ip Range
            - string "ksLabel" - The kickstart label associated with the ip
                                 range
            - string "max" - The max ip of the range
            - string "min" - The min ip of the range
    """
    try:
        result = sw.session.kickstart.profile.listIpRanges(
            sw.key,
            label
        )
    except Exception as e:
        raise e

    return result


def listScripts(
    sw,
    kslabel
):
    """
    Description:
    List the pre and post scripts for a kickstart profile. profile

    Parameters:
        - string sessionKey
        - string kslabel - The label of the kickstart

    Returns:
        - struct - kickstart script
            - int "id"
            - string "contents"
            - string "script_type" - Which type of script ('pre' or 'post').
            - string "interpreter" - The scripting language interpreter to use
                                    for this script. An empty string indicates
                                    the default kickstart shell.
            - boolean "chroot" - True if the script will be executed within the
                                 chroot environment.
            - boolean "template" - True if templating using cobbler is enabled
    """
    try:
        result = sw.session.kickstart.profile.listScripts(
            sw.key,
            kslabel
        )
    except Exception as e:
        raise e

    return result


def removeIpRange(
    sw,
    kslabel
):
    """
    Description:
    Remove an ip range from a kickstart profile.

    Parameters:
        - string sessionKey
        - string kslabel - The kickstart label of the ip range you want to
                           remove
        - string ip_address - An Ip Address that falls within the range that
                              you are wanting to remove. The min or max of the
                              range will work.

    Returns:
        - int - 1 on successful removal, 0 if range wasn't found for the
                specified kickstart, exception otherwise.
    """
    try:
        result = sw.session.kickstart.profile.removeIpRange(
            sw.key,
            kslabel
        )
    except Exception as e:
        raise e

    return result


def removeScript(
    sw,
    kslabel,
    scriptid
):
    """
    Description:
    Remove a script from a kickstart profile.

    Parameters:
        - string sessionKey
        - string kslabel - The kickstart from which to remove the script from.
        - int scriptid - The id of the script to remove.

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.kickstart.profile.removeScript(
            sw.key,
            kslabel,
            scriptid
        )
    except Exception as e:
        raise e

    return result


def setAdvancedOptions(
    sw,
    kslabel,
    options
):
    """
    Description:
    Set advanced options for a kickstart profile.
    Parameters:
        - string sessionKey
        - string kslabel
        - options - array:
            - struct - advanced options
            - string "name" - Name of the advanced option. Valid Option names:
                              autostep, interactive, install, upgrade, text,
                              network, cdrom, harddrive, nfs, url, lang,
                              langsupport keyboard, mouse, device, deviceprobe,
                              zerombr, clearpart, bootloader, timezone, auth,
                              rootpw, selinux, reboot, firewall, xconfig,
                              skipx, key, ignoredisk, autopart, cmdline,
                              firstboot, graphical, iscsi, iscsiname, logging,
                              monitor, multipath, poweroff, halt, services,
                              shutdown, user, vnc, zfcp, driverdisk
            - string "arguments" - Arguments of the option

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.kickstart.profile.setAdvancedOptions(
            sw.key,
            kslabel,
            options
        )
    except Exception as e:
        raise e

    return result


def setCfgPreservation(
    sw,
    kslabel,
    preserve
):
    """
    Description:
    Set ks.cfg preservation option for a kickstart profile.

    Parameters:
        - string sessionKey
        - string kslabel - Label of kickstart profile to be changed.
        - boolean preserve - whether or not ks.cfg and all include fragments
          will be copied to /root.

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.kickstart.profile.setCfgPreservation(
            sw.key,
            kslabel,
            preserve
        )
    except Exception as e:
        raise e

    return result


def setChildChannels(
    sw,
    kslabel,
    channellabels
):
    """
    Description:
    Set the child channels for a kickstart profile.

    Parameters:
        - string sessionKey
        - string kslabel - Label of kickstart profile to be changed.
        - array: channellabels - List of labels of child channels

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.kickstart.profile.setChildChannels(
            sw.key,
            kslabel,
            channellabels
        )
    except Exception as e:
        raise e

    return result


def setCustomOptions(
    sw,
    kslabel,
    options
):
    """
    Description:
    Set custom options for a kickstart profile.

    Parameters:
        - string sessionKey
        - string kslabel
        - array: [] options

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.kickstart.profile.setCustomOptions(
            sw.key,
            kslabel,
            options
        )
    except Exception as e:
        raise e

    return result


def setKickstartTree(
    sw,
    kslabel,
    kstreelabel
):
    """
    Description:
    Set the kickstart tree for a kickstart profile.

    Parameters:
        - string sessionKey
        - string kslabel - Label of kickstart profile to be changed.
        - string kstreelabel - Label of new kickstart tree.

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.kickstart.profile.setKickstartTree(
            sw.key,
            kslabel,
            kstreelabel
        )
    except Exception as e:
        raise e

    return result


def setLogging(
    sw,
    kslabel,
    preks,
    postks
):
    """
    Description:
    Set logging options for a kickstart profile.

    Parameters:
        - string sessionKey
        - string kslabel - Label of kickstart profile to be changed.
        - boolean preks - whether or not to log the pre section of a kickstart
                          to /root/ks-pre.log
        - boolean postks - whether or not to log the post section of a
                          kickstart to /root/ks-post.log

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.kickstart.profile.setLogging(
            sw.key,
            kslabel,
            preks,
            postks
        )
    except Exception as e:
        raise e

    return result


def setVariables(
    sw,
    kslabel,
    ksvars
):
    """
    Description:
    Associates list of kickstart variables with the specified kickstart profile

    Parameters:
        - string sessionKey
        - string kslabel
        - ksvars: array:
            - struct - kickstart variable
                - string "key"
                - string or int "value"

    Returns:
    int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.kickstart.profile.setVariables(
            sw.key,
            kslabel,
            ksvars
        )
    except Exception as e:
        raise e

    return result

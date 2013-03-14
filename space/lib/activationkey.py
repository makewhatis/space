"""
``Namespace: activationkey``
============================

Contains methods to access common activation key functions available
from the web interface.

- :func:`addChildChannels`
- :func:`addConfigChannels`
- :func:`addEntitlements`
- :func:`addPackages`
- :func:`addServerGroups`
- :func:`checkConfigDeployment`
- :func:`create`
- :func:`create`
- :func:`delete`
- :func:`disableConfigDeployment`
- :func:`enableConfigDeployment`
- :func:`getDetails`
- :func:`listActivatedSystems`
- :func:`listActivationKeys`
- :func:`listConfigChannels`
- :func:`removeChildChannels`
- :func:`removeConfigChannels`
- :func:`removeEntitlements`
- :func:`removePackages`
- :func:`removeServerGroups`
- :func:`setConfigChannels`
- :func:`setDetails`
"""


def addChildChannels(
    sw,
    keyname,
    channels
):
    """

    *Description*:
    Add child channels to an activation key.

    *Parameters*:
        - string sessionKey
        - string key

    array:
        - string - childChannelLabel

    *Returns*:

    int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.activationkey.addChildChannels(
            sw.key, keyname, channels
        )
    except Exception as e:
        raise e
    return result


def addConfigChannels(
    sw,
    key,
    channellabels,
    addtotop=False
):
    """
    *Description*:
    Given a list of activation keys and configuration channels, this method
    adds given configuration channels to either the top or the bottom
    (whichever you specify) of an activation key's configuration channels
    list. The ordering of the configuration channels provided in the add
    list is maintained while adding.
    If one of the configuration channels in the 'add' list already exists in
    an activation key, the configuration channel will be re-ranked to the
    appropriate place.

    *Parameters*:
        - string sessionKey
        - array:
            - string - activationKey
        - array:
            - string - List of configuration channel labels in the ranked
                       order.
        - boolean addToTop
            - true - To prepend the given channels to the beginning of
                     the activation key's config channel list
            - false - To append the given channels to the end of the
                      activation key's config channel list

    *Returns*:
        -int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.activationkey.addConfigChannels(
            sw.key,
            key,
            channellabels,
            addtotop
        )
    except Exception as e:
        raise e

    return result


def addEntitlements(
    sw,
    key,
    entitlement_label
):
    """
    *Description*:
    Add entitlements to an activation key. Currently only add-on
    entitlements are permitted. (monitoring_entitled, provisioning_entitled,
     virtualization_host, virtualization_host_platform)
    *Parameters*:
        - string sessionKey
        - string key
        - array:
            - string - entitlement label
                - monitoring_entitled
                - provisioning_entitled
                - virtualization_host
                - virtualization_host_platform
    *Returns*:

        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.activationkey.addEntitlements(
            sw.key,
            key,
            entitlement_label
        )
    except Exception as e:
        raise e

    return result


def addPackages(
    sw,
    key,
    packages
):
    """
    *Description*:
    -  Add packages to an activation key.

    *Parameters*:
       - string sessionKey
       - string key
       - array:
            - struct - packages
                - string "name" - Package name
                - string "arch" - Arch label - Optional

    *Returns*:

        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.activationkey.addPackages(
            sw.key,
            key,
            packages
        )
    except Exception as e:
        raise e

    return result


def addServerGroups(
    sw,
    keyname,
    groupid
):
    """
    *Description*:
        Add server groups to an activation key.

    *Parameters*:
        string sessionKey
        string key
        array:
            int - serverGroupId

    *Returns*:

    int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.activationkey.addServerGroups(
            sw.key,
            keyname,
            groupid
        )
    except Exception as e:
        raise e

    return result


def checkConfigDeployment(
    sw,
    key
):
    """
    *Description*:
        - Check configuration file deployment status for the activation
          key specified.

    *Parameters*:
        - string sessionKey
        - string key

    *Returns*:

        - 1 if enabled, 0 if disabled, exception thrown otherwise.
    """
    try:
        result = sw.session.activationkey.checkConfigDeployment(
            sw.key,
            key
        )
    except Exception as e:
        raise e

    return result


def create(
    sw,
    keyname,
    description,
    baseChannelLabel,
    entitlements=[],
    universalDefault=False
):
    """
    *Description*:
    Create a new activation key with unlimited usage. The activation key
    parameter passed in will be prefixed with the organization ID, and
    this value will be returned from the create call. Eg. If the caller
    passes in the key "foo" and belong to an organization with the ID 100,
    the actual activation key will be "100-foo".

    *Parameters*:
        - string sessionKey
        - string key - Leave empty to have new key autogenerated.
        - string description
        - string baseChannelLabel - Leave empty to accept default.
        - array:
            - string - Add-on entitlement label to associate with the key.
            - monitoring_entitled
            - provisioning_entitled
            - virtualization_host
            - virtualization_host_platform
        - boolean universalDefault

    *Returns*:
        - string - The new activation key.
    """
    try:
        result = sw.session.activationkey.create(
            sw.key,
            keyname,
            description,
            baseChannelLabel,
            entitlements,
            universalDefault
        )
    except Exception as e:
        raise e

    return result


def delete(
    sw,
    keyname
):
    """
    *Description*:
    Delete an activation key.

    *Parameters*:
        - string sessionKey
        - string key

    *Returns*:

        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.activationkey.delete(
            sw.key,
            keyname
        )
    except Exception as e:
        raise e

    return result


def disableConfigDeployment(
    sw,
    keyname
):
    """
    *Description*:
    Disable configuration file deployment for the specified
    activation key.

    *Parameters*:
        - string sessionKey
        - string key

    *Returns*:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.activationkey.disableConfigDeployment(
            sw.key,
            keyname
        )
    except Exception as e:
        raise e

    return result


def enableConfigDeployment(
    sw,
    keyname
):
    """
    *Description*:
    Enable configuration file deployment for the specified
    activation key.

    *Parameters*:
        - string sessionKey
        - string key

    *Returns*:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.activationkey.enableConfigDeployment(
            sw.key,
            keyname
        )
    except Exception as e:
        raise e

    return result


def getDetails(
    sw,
    keyname
):
    """
    *Description*:
    Lookup an activation key's details.

    *Parameters*:

        - string sessionKey
        - string key

    *Returns*:

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
        result = sw.session.activationkey.getDetails(
            sw.key,
            keyname
        )
    except Exception as e:
        raise e

    return result


def listActivatedSystems(
    sw,
    keyname
):
    """
    *Description*:
    List the systems activated with the key provided.

    *Parameters*:
    string sessionKey
    string key

    *Returns*:
        - array:
            - struct - system structure
                - int "id" - System id
                - string "hostname"
                - dateTime.iso8601 "last_checkin" - Last time server
                  successfully checked in
    """
    try:
        result = sw.session.activationkey.listActivatedSystems(
            sw.key,
            keyname
        )
    except Exception as e:
        raise e

    return result


def listActivationKeys(
    sw
):
    """
    *Description*:
    List activation keys that are visible to the user.

    *Parameters*:
        - string sessionKey

    *Returns*:
        - array:
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
        result = sw.session.activationkey.listActivationKeys(
            sw.key
        )
    except Exception as e:
        raise e

    return result


def listConfigChannels(
    sw,
    keyname
):
    """
    *Description*:
    List configuration channels associated to an activation key.

    *Parameters*:
        - string sessionKey
        - string key

    *Returns*:
        - array:
        - struct - Configuration Channel information
            - int "id"
            - int "orgId"
            - string "label"
            - string "name"
            - string "description"
            - struct "configChannelType"
            - struct - Configuration Channel Type information
                - int "id"
                - string "label"
                - string "name"
                - int "priority"
    """
    try:
        result = sw.session.activationkey.listConfigChannels(
            sw.key,
            keyname
        )
    except Exception as e:
        raise e

    return result


def removeChildChannels(
    sw,
    keyname,
    channellabel
):
    """
    *Description*:
    Remove child channels from an activation key.

    *Parameters*:
        - string sessionKey
        - string key
        - array:
            = string - childChannelLabel

    *Returns*:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.activationkey.removeChildChannels(
            sw.key,
            keyname,
            channellabel
        )
    except Exception as e:
        raise e

    return result


def removeConfigChannels(
    sw,
    activationkeys,
    channellabels
):
    """
    *Description*:
    Remove configuration channels from the given activation keys.

    *Parameters*:
        - string sessionKey
        - array:
            - string - activationKey
        - array:
            - string - configChannelLabel

    *Returns*:
    - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.activationkey.removeConfigChannels(
            sw.key,
            activationkeys,
            channellabels
        )
    except Exception as e:
        raise e

    return result


def removeEntitlements(
    sw,
    keyname,
    entitlements
):
    """
    *Description*:
    Remove entitlements (by label) from an activation key. Currently only
    add-on entitlements are permitted.
        - monitoring_entitled,
        - provisioning_entitled,
        - virualization_host,
        - virtualization_host_platform

    *Parameters*:
        - string sessionKey
        - string key
        - array:
            -string - entitlement label
            - monitoring_entitled
            - provisioning_entitled
            - virtualization_host
            - virtualization_host_platform

    *Returns*:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.activationkey.removeEntitlements(
            sw.key,
            keyname,
            entitlements
        )
    except Exception as e:
        raise e

    return result


def removePackages(
    sw,
    packages
):
    """
    *Description*:
    Remove package names from an activation key.

    *Parameters*:
        - string key
        - array:
            - struct - packages
                - string "name" - Package name
                - string "arch" - Arch label - Optional

    *Returns*:
       - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.activationkey.removePackages(
            sw.key,
            packages
        )
    except Exception as e:
        raise e

    return result


def removeServerGroups(
    sw,
    keyname,
    servergroups
):
    """
    *Description*:
    Remove server groups from an activation key.

    *Parameters*:
       - string sessionKey
       - string key
       - array:
            - int - serverGroupId

    *Returns*:
       - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.activationkey.removeServerGroups(
            sw.key,
            keyname,
            servergroups
        )
    except Exception as e:
        raise e

    return result


def setConfigChannels(
    sw,
    activationkeys,
    channellabels
):
    """
    *Description*:
    Replace the existing set of configuration channels on the
    given activation keys. Channels are ranked by their order in the array.

    *Parameters*:
       - string sessionKey
       - array:
            - string - activationKey
       - array:
            - string - configChannelLabel

    *Returns*:
       - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.activationkey.setConfigChannels(
            sw.key,
            activationkeys,
            channellabels
        )
    except Exception as e:
        raise e

    return result


def setDetails(
    sw,
    keyname,
    keystruct
):
    """
    *Description*:
    Update the details of an activation key.
    *Parameters*:
       - string sessionKey
       - string key
       - struct - activation key
           - string "description" - optional
           - string "base_channel_label" - optional
           - int "usage_limit" - optional
           - boolean "unlimited_usage_limit" - Set true for unlimited
             usage and to override usage_limit
          -  boolean "universal_default" - optional
           - boolean "disabled" - optional

    *Returns*:
       - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.activationkey.setDetails(
            sw.key,
            keyname,
            keystruct
        )
    except Exception as e:
        raise e

    return result

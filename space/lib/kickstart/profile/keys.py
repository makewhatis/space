"""
``Namespace: kickstart.profile.keys``
=====================================

Provides methods to access and modify the list of
activation keys associated with a kickstart profile.

Available methods:

- :func:`addActivationKey`
- :func:`getActivationKeys`
- :func:`removeActivationKey`
"""


def addActivationKey(
    sw,
    kslabel,
    keyname
):
    """
    Description:
    Add an activation key association to the kickstart profile

    Parameters:
        - string sessionKey
        - string ksLabel - the kickstart profile label
        - string key - the activation key

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.kickstart.profile.keys.addActivationKey(
            sw.key,
            kslabel,
            keyname
        )
    except Exception as e:
        raise e

    return result


def getActivationKeys(
    sw,
    kslabel
):
    """
    Description:
    Lookup the activation keys associated with the kickstart profile.

    Parameters:
        - string sessionKey
        - string ksLabel - the kickstart profile label

    Returns:
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
        result = sw.session.kickstart.profile.keys.getActivationKeys(
            sw.key,
            kslabel
        )
    except Exception as e:
        raise e

    return result


def removeActivationKey(
    sw,
    kslabel,
    keyname
):
    """
    Description:
    Remove an activation key association from the kickstart profile

    Parameters:
        - string sessionKey
        - string ksLabel - the kickstart profile label
        - string keyname - the activation key

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.kickstart.profile.keys.removeActivationKey(
            sw.key,
            kslabel,
            keyname
        )
    except Exception as e:
        raise e

    return result

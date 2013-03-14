"""
``Namespace: kickstart.tree``
=============================

Provides methods to access and modify the kickstart trees.

Available methods:

- :func:`create`
- :func:`delete`
- :func:`deleteTreeAndProfiles`
- :func:`getDetails`
- :func:`list`
- :func:`listInstallTypes`
- :func:`rename`
- :func:`update`
"""


def create(
    sw,
    treelabel,
    basepath,
    channellabel,
    installtype
):
    """
    Description:
    Create a Kickstart Tree (Distribution) in Satellite.

    Parameters:
        - string sessionKey
        - string treeLabel - The new kickstart tree label.
        - string basePath - Path to the base or root of the kickstart tree.
        - string channelLabel - Label of channel to associate with the
                                kickstart tree.
        - string installType - Label for KickstartInstallType
                               (rhel_2.1, rhel_3, rhel_4, rhel_5, fedora_9).

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.kickstart.tree.create(
            sw.key,
            treelabel,
            basepath,
            channellabel,
            installtype
        )
    except Exception as e:
        raise e

    return result


def delete(
    sw,
    treelabel
):
    """
    Description:
    Delete a Kickstart Tree (Distribution) in Satellite.

    Parameters:
        - string sessionKey
        - string treelabel - Label for the kickstart tree to delete.

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.kickstart.tree.delete(
            sw.key,
            treelabel
        )
    except Exception as e:
        raise e

    return result


def deleteTreeAndProfiles(
    sw,
    treelabel
):
    """
    Description:
    Delete a kickstarttree and any profiles associated with this kickstart
    tree.
    WARNING: This will delete all profiles associated with this kickstart tree!

    Parameters:
        - string sessionKey
        - string treeLabel - Label for the kickstart tree to delete.

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.kickstart.tree.deleteTreeAndProfiles(
            sw.key,
            treelabel
        )
    except Exception as e:
        raise e

    return result


def getDetails(
    sw,
    treelabel
):
    """
    Description:
    The detailed information about a kickstartable tree given the tree name.

    Parameters:
        - string sessionKey
        - string treeLabel - Label of kickstartable tree to search.

    Returns:
        - struct - kickstartable tree
            - int "id"
            - string "label"
            - string "abs_path"
            - int "channel_id"
            - struct - kickstart install type
                - int "id"
                - string "label"
                - string "name"
    """
    try:
        result = sw.session.kickstart.tree.getDetails(
            sw.key,
            treelabel
        )
    except Exception as e:
        raise e

    return result


def list(
    sw,
    channellabel
):
    """
    Description:
    List the available kickstartable trees for the given channel.

    Parameters:
        - string sessionKey
        - string channellabel - Label of channel to search.

    Returns:
        - array:
            - struct - kickstartable tree
                - int "id"
                - string "label"
                - string "base_path"
                - int "channel_id"
    """
    try:
        result = sw.session.kickstart.tree.list(
            sw.key,
            channellabel
        )
    except Exception as e:
        raise e

    return result


def listInstallTypes(
    sw
):
    """
    Description:
    List the available kickstartable install types (rhel2,3,4,5 and fedora9+).

    Parameters:
        - string sessionKey

    Returns:
        - array:
            - struct - kickstart install type
                - int "id"
                - string "label"
                - string "name"
    """
    try:
        result = sw.session.kickstart.tree.listInstallTypes(
            sw.key
        )
    except Exception as e:
        raise e

    return result


def rename(
    sw,
    originallabel,
    newlabel
):
    """
    Description:
    Rename a Kickstart Tree (Distribution) in Satellite.

    Parameters:
        - string sessionKey
        - string originalLabel - Label for the kickstart tree to rename.
        - string newLabel - The kickstart tree's new label.

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.kickstart.tree.rename(
            sw.key,
            originallabel,
            newlabel
        )
    except Exception as e:
        raise e

    return result


def update(
    sw,
    treelabel,
    basepath,
    channellabel,
    installtype
):
    """
    Description:
    Edit a Kickstart Tree (Distribution) in Satellite.

    Parameters:
        - string sessionKey
        - string treelabel - Label for the kickstart tree.
        - string basepath - Path to the base or root of the kickstart tree.
        - string channellabel - Label of channel to associate with kickstart
                                tree.
        - string installtype - Label for KickstartInstallType
                              (rhel_2.1, rhel_3, rhel_4, rhel_5, fedora_9).

    Returns:
    int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.kickstart.tree.update(
            sw.key,
            treelabel,
            basepath,
            channellabel,
            installtype
        )
    except Exception as e:
        raise e

    return result

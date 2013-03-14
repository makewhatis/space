"""
``Namespace: systemgroup``
==========================

Provides methods to access and modify system groups.

- :func:`addOrRemoveAdmins`
- :func:`addOrRemoveSystems`
- :func:`create`
- :func:`delete`
- :func:`getDetails`
- :func:`listActiveSystemsInGroup`
- :func:`listAdministrators`
- :func:`listAllGroups`
- :func:`listGroupsWithNoAssociatedAdmins`
- :func:`listInactiveSystemsInGroup`
- :func:`listSystems`
- :func:`scheduleApplyErrataToActive`
- :func:`update`
"""


def addOrRemoveAdmins(
    sw,
    system_group,
    login,
    add
):
    """
    Description:
    Add or remove administrators to/from the given group. Satellite and
    Organization administrators are granted access to groups within their
    organization by default; therefore, users with those roles should not be
    included in the array provided. Caller must be an organization
    administrator.

    Parameters:
        - string sessionKey
        - string system_group
        - array:
            - string - login - User's loginName
        - int add - 1 to add administrators, 0 to remove.

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.systemgroup.addOrRemoveAdmins(
            sw.key,
            system_group,
            login,
            add
        )
    except Exception as e:
        raise e

    return result


def addOrRemoveSystems(
    sw,
    system_group,
    server_id,
    add
):
    """
    Description:
    Add/remove the given servers to a system group.

    Parameters:
        - string sessionKey
        - string system_group
        - array:
            - int - server_id
        - boolean add - True to add to the group, False to remove.

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.systemgroup.addOrRemoveSystems(
            sw.key,
            system_group,
            server_id,
            add
        )
    except Exception as e:
        raise e

    return result


def create(
    sw,
    name,
    description
):
    """
    Description:
    Create a new system group.

    Parameters:
        - string sessionKey
        - string name - Name of the system group.
        - string description - Description of the system group.

    Returns:
        - struct - Server Group
            - int "id"
            - string "name"
            - string "description"
            - int "org_id"
            - int "system_count"
    """
    try:
        result = sw.session.systemgroup.create(
            sw.key,
            name,
            description
        )
    except Exception as e:
        raise e

    return result


def delete(
    sw,
    system_group
):
    """
    Description:
    Delete a system group.

    Parameters:
        - string sessionKey
        - string system_group

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.systemgroup.delete(
            sw.key,
            system_group
        )
    except Exception as e:
        raise e

    return result


def getDetails(
    sw,
    system_group
):
    """
    Description:
    Retrieve details of a ServerGroup based on it's id

    Parameters:
        - string sessionKey
        - int system_group || string system_group

    Returns:
        - struct - Server Group
            - int "id"
            - string "name"
            - string "description"
            - int "org_id"
            - int "system_count"
    """
    try:
        result = sw.session.systemgroup.getDetails(
            sw.key,
            system_group
        )
    except Exception as e:
        raise e

    return result


def listActiveSystemsInGroup(
    sw,
    system_group
):
    """
    Description:
    Lists active systems within a server group

    Parameters:
        - string sessionKey
        - string system_group

    Returns:
        - array:
            - int - server_id
    """
    try:
        result = sw.session.systemgroup.listActiveSystemsInGroup(
            sw.key,
            system_group
        )
    except Exception as e:
        raise e

    return result


def listAdministrators(
    sw,
    system_group
):
    """
    Description:
    Returns the list of users who can administer the given group. Caller
    must be a system group admin or an organization administrator.

    Parameters:
        - string sessionKey
        - string system_group

    Returns:
        - array:
            - struct - user
                - int "id"
                - string "login"
                - string "login_uc" - upper case version of the login
                - boolean "enabled" - true if user is enabled, false if the
                                      user is disabled
    """
    try:
        result = sw.session.systemgroup.listAdministrators(
            sw.key,
            system_group
        )
    except Exception as e:
        raise e

    return result


def listAllGroups(
    sw
):
    """
    Description:
    Retrieve a list of system groups that are accessible by the logged in user.

    Parameters:
        - string sessionKey

    Returns:
        - array:
            - struct - Server Group
                - int "id"
                - string "name"
                - string "description"
                - int "org_id"
                - int "system_count"
    """
    try:
        result = sw.session.systemgroup.listAllGroups(
            sw.key
        )
    except Exception as e:
        raise e

    return result


def listGroupsWithNoAssociatedAdmins(
    sw
):
    """
    Description:
    Returns a list of system groups that do not have an administrator.
    (who is not an organization administrator, as they have implicit access
    to system groups) Caller must be an organization administrator.

    Parameters:
        - string sessionKey

    Returns:
        - array:
            - struct - Server Group
                - int "id"
                - string "name"
                - string "description"
                - int "org_id"
                - int "system_count"
    """
    try:
        result = sw.session.systemgroup.listGroupsWithNoAssociatedAdmins(
            sw.key
        )
    except Exception as e:
        raise e

    return result


def listInactiveSystemsInGroup(
    sw,
    system_group,
    days_inactive=None
):
    """
    Description:
    Lists inactive systems within a server group using a specified inactivity
    time.

    Parameters:
        - string sessionKey
        - string system_group
        - int days_inactive - Number of days a system must not check in
                            to be considered inactive.

    Returns:
        - array:
            - int - server_id
    """
    try:
        if days_inactive:
            result = sw.session.systemgroup.listInactiveSystemsInGroup(
                sw.key,
                system_group,
                days_inactive
            )
        else:
            result = sw.session.systemgroup.listInactiveSystemsInGroup(
                sw.key,
                system_group
            )
    except Exception as e:
        raise e

    return result


def listSystems(
    sw,
    system_group
):
    """
    Description:
    Return a list of systems associated with this system group. User must have
    access to this system group.

    Parameters:
        - string sessionKey
        - string system_group

    Returns:
        - array:
            - struct - server details
                - int "id" - System id
                - string "profile_name"
                - string "base_entitlement" - System's base entitlement label.
                    (enterprise_entitled or sw_mgr_entitled)
                - array "string"
                    - addon_entitlements System's addon entitlements labels,
                        including monitoring_entitled, provisioning_entitled,
                        virtualization_host, virtualization_host_platform
                - boolean "auto_update" - True if system has auto errata
                                          updates enabled.
                - string "release" - The Operating System release
                                     (i.e. 4AS, 5Server
                - string "address1"
                - string "address2"
                - string "city"
                - string "state"
                - string "country"
                - string "building"
                - string "room"
                - string "rack"
                - string "description"
                - string "hostname"
                - dateTime.iso8601 "last_boot"
                - string "osa_status" - Either 'unknown', 'offline',
                                        or 'online'.
                - boolean "lock_status" - True indicates that the system is
                                          locked.
                                          False indicates that the system is
                                          unlocked.
    """
    try:
        result = sw.session.systemgroup.listSystems(
            sw.key,
            system_group
        )
    except Exception as e:
        raise e

    return result


def scheduleApplyErrataToActive(
    sw,
    system_group,
    errata_id,
    date_time=None
):
    """
    Description:
    Schedules an action to apply errata updates to active systems from a group.

    Parameters:
        - string sessionKey
        - string system_group
        - array:
            - int - errataId
        - dateTime.iso8601 earliestOccurrence (Optional)

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        if date_time:
            result = sw.session.systemgroup.scheduleApplyErrataToActive(
                sw.key,
                system_group,
                errata_id,
                date_time
            )
        else:
            result = sw.session.systemgroup.scheduleApplyErrataToActive(
                sw.key,
                system_group,
                errata_id
            )
    except Exception as e:
        raise e

    return result


def update(
    sw,
    system_group,
    description
):
    """
    Description:
    Update an existing system group.

    Parameters:
        - string sessionKey
        - string system_group
        - string description

    Returns:
        - struct - Server Group
            - int "id"
            - string "name"
            - string "description"
            - int "org_id"
            - int "system_count"
    """
    try:
        result = sw.session.systemgroup.update(
            sw.key,
            system_group,
            description
        )
    except Exception as e:
        raise e

    return result

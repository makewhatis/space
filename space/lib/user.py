"""
``Namespace: user``
======================

User namespace contains methods to access common user functions available
from the web user interface..

- :func:`addAssignedSystemGroup`
- :func:`addAssignedSystemGroups`
- :func:`addDefaultSystemGroup`
- :func:`addDefaultSystemGroups`
- :func:`addRole`
- :func:`create`
- :func:`delete`
- :func:`disable`
- :func:`enable`
- :func:`getDetails`
- :func:`getLoggedInTime`
- :func:`listAssignableRoles`
- :func:`listAssignedSystemGroups`
- :func:`listDefaultSystemGroups`
- :func:`listRoles`
- :func:`listUsers`
- :func:`removeAssignedSystemGroup`
- :func:`removeAssignedSystemGroups`
- :func:`removeDefaultSystemGroup`
- :func:`removeDefaultSystemGroups`
- :func:`removeRole`
- :func:`setDetails`
- :func:`usePamAuthentication`
"""


def addAssignedSystemGroup(
    sw,
    login,
    server_group_name,
    set_default
):
    """
    Description:
    Add system group to user's list of assigned system groups.

    Parameters:
        - string sessionKey
        - string login - User's login name.
        - string server_group_name
        - boolean set_default - Should system group also be added to user's
                                list of default system groups.

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.user.addAssignedSystemGroup(
            sw.key,
            login,
            server_group_name,
            set_default
        )
    except Exception as e:
        raise e

    return result


def addAssignedSystemGroups(
    sw,
    login,
    server_group_name,
    set_default
):
    """
    Description:
    Add system groups to user's list of assigned system groups.

    Parameters:
        - string sessionKey
        - string login - User's login name.
        - array:
            - string - server_group_name
        - boolean set_default - Should system groups also be added to user's
                                list of default system groups.

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.user.addAssignedSystemGroups(
            sw.key,
            login,
            server_group_name,
            set_default
        )
    except Exception as e:
        raise e

    return result


def addDefaultSystemGroup(
    sw,
    login,
    server_group_name
):
    """
    Description:
    Add system group to user's list of default system groups.

    Parameters:
        - string sessionKey
        - string login - User's login name.
        - string server_group_name

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.user.addDefaultSystemGroup(
            sw.key,
            login,
            server_group_name
        )
    except Exception as e:
        raise e

    return result


def addDefaultSystemGroups(
    sw,
    login,
    server_group_name
):
    """
    Description:
    Add system groups to user's list of default system groups.

    Parameters:
        - string sessionKey
        - string login - User's login name.
        - array:
            - string - serverGroupName

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.user.addDefaultSystemGroups(
            sw.key,
            login,
            server_group_name
        )
    except Exception as e:
        raise e

    return result


def addRole(
    sw,
    login,
    role
):
    """
    Description:
    Adds a role to a user.

    Parameters:
        - string sessionKey
        - string login - User login name to update.
        - string role - Role label to add. Can be any of: satellite_admin,
                        org_admin, channel_admin, config_admin,
                        system_group_admin, activation_key_admin,
                        or monitoring_admin.

    Returns:
    int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.user.addRole(
            sw.key,
            login,
            role
        )
    except Exception as e:
        raise e

    return result


def create(
    sw,
    login,
    password,
    first_name,
    last_name,
    email,
    use_pamauth=None
):
    """
    Description:
    Create a new user.

    Parameters:
        - string sessionKey
        - string login - Desired login name, will fail if already in use.
        - string password
        - string first_name
        - string last_name
        - string email - User's e-mail address.
        - int use_pamauth - 1 if you wish to use PAM authentication for
                            this user, 0 otherwise. (OPTIONAL)

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        if use_pamauth:
            result = sw.session.user.create(
                sw.key,
                login,
                password,
                first_name,
                last_name,
                email,
                use_pamauth
            )
        else:
            result = sw.session.user.create(
                sw.key,
                login,
                password,
                first_name,
                last_name,
                email
            )
    except Exception as e:
        raise e

    return result


def delete(
    sw,
    login
):
    """
    Description:
    Delete a user.

    Parameters:
        - string sessionKey
        - string login - User login name to delete.

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.user.delete(
            sw.key,
            login
        )
    except Exception as e:
        raise e

    return result


def disable(
    sw,
    login
):
    """
    Description:
    Disable a user.

    Parameters:
        - string sessionKey
        - string login - User login name to disable.

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.user.disable(
            sw.key,
            login
        )
    except Exception as e:
        raise e

    return result


def enable(
    sw,
    login
):
    """
    Description:
    Enable a user.

    Parameters:
        - string sessionKey
        - string login - User login name to enable.

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.user.enable(
            sw.key,
            login
        )
    except Exception as e:
        raise e

    return result


def getDetails(
    sw,
    login
):
    """
    Description:
    Returns the details about a given user.

    Parameters:
        - string sessionKey
        - string login - User's login name.

    Returns:
        - struct - user details
            - string "first_names" - deprecated, use first_name
            - string "first_name"
            - string "last_name"
            - string "email"
            - int "org_id"
            - string "prefix"
            - string "last_login_date"
            - string "created_date"
            - boolean "enabled" - true if user is enabled, false if the user
                                    is disabled
            - boolean "use_pam" - true if user is configured to use PAM
                                    authentication
    """
    try:
        result = sw.session.user.getDetails(
            sw.key,
            login
        )
    except Exception as e:
        raise e

    return result


def getLoggedInTime(
    sw,
    login
):
    """
    Description:
    Returns the time user last logged in.

    Parameters:
        - string sessionKey
        - string login - User's login name.

    Returns:
        - dateTime.iso8601
    """
    try:
        result = sw.session.user.getLoggedInTime(
            sw.key,
            login
        )
    except Exception as e:
        raise e

    return result


def listAssignableRoles(
    sw
):
    """
    Description:
    Returns a list of user roles that this user can assign to others.

    Parameters:
        - string sessionKey

    Returns:
        - array:
            - string - (role label)
    """
    try:
        result = sw.session.user.listAssignableRoles(
            sw.key
        )
    except Exception as e:
        raise e

    return result


def listAssignedSystemGroups(
    sw,
    login
):
    """
    Description:
    Returns the system groups that a user can administer.

    Parameters:
        - string sessionKey
        - string login - User's login name.

    Returns:
        - array:
            - struct - system group
                - int "id"
                - string "name"
                - string "description"
                - int "system_count"
                - int "org_id" - Organization ID for this system group.
    """
    try:
        result = sw.session.user.listAssignedSystemGroups(
            sw.key,
            login
        )
    except Exception as e:
        raise e

    return result


def listDefaultSystemGroups(
    sw,
    login
):
    """
    Description:
    Returns a user's list of default system groups.

    Parameters:
        - string sessionKey
        - string login - User's login name.

    Returns:
        - array:
            - struct - system group
                - int "id"
                - string "name"
                - string "description"
                - int "system_count"
                - int "org_id" - Organization ID for this system group.
    """
    try:
        result = sw.session.user.listDefaultSystemGroups(
            sw.key,
            login
        )
    except Exception as e:
        raise e

    return result


def listRoles(
    sw,
    login
):
    """
    Description:
    Returns a list of the user's roles.

    Parameters:
        - string sessionKey
        - string login - User's login name.

    Returns:
        - array:
        - string - (role label)
    """
    try:
        result = sw.session.user.listRoles(
            sw.key,
            login
        )
    except Exception as e:
        raise e

    return result


def listUsers(
    sw
):
    """
    Description:
    Returns a list of users in your organization.

    Parameters:
        - string sessionKey

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
        result = sw.session.user.listUsers(
            sw.key
        )
    except Exception as e:
        raise e

    return result


def removeAssignedSystemGroup(
    sw,
    login,
    server_group_name,
    set_default
):
    """
    Description:
    Remove system group from the user's list of assigned system groups.

    Parameters:
        - string sessionKey
        - string login - User's login name.
        - string serverGroupName
        - boolean setDefault - Should system group also be removed from the
                            user's list of default system groups.

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.user.removeAssignedSystemGroup(
            sw.key,
            login,
            server_group_name,
            set_default
        )
    except Exception as e:
        raise e

    return result


def removeAssignedSystemGroups(
    sw,
    login,
    server_group_name,
    set_default
):
    """
    Description:
    Remove system groups from a user's list of assigned system groups.

    Parameters:
        - string sessionKey
        - string login - User's login name.
        - array:
            - string - serverGroupName
        - boolean setDefault - Should system groups also be removed from the
                               user's list of default system groups.

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.user.removeAssignedSystemGroups(
            sw.key,
            login,
            server_group_name,
            set_default
        )
    except Exception as e:
        raise e

    return result


def removeDefaultSystemGroup(
    sw,
    login,
    server_group_name
):
    """
    Description:
    Remove a system group from user's list of default system groups.

    Parameters:
        - string sessionKey
        - string login - User's login name.
        - string server_group_name

    Returns:
    int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.user.removeDefaultSystemGroup(
            sw.key,
            login,
            server_group_name
        )
    except Exception as e:
        raise e

    return result


def removeDefaultSystemGroups(
    sw,
    login,
    server_group_name
):
    """
    Description:
    Remove system groups from a user's list of default system groups.

    Parameters:
        string sessionKey
        string login - User's login name.
        array:
            string - serverGroupName

    Returns:
    int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.user.removeDefaultSystemGroups(
            sw.key,
            login,
            server_group_name
        )
    except Exception as e:
        raise e

    return result


def removeRole(
    sw,
    login,
    role
):
    """
    Description:
    Remove a role from a user.

    Parameters:
        - string sessionKey
        - string login - User login name to update.
        - string role - Role label to remove. Can be any of: satellite_admin,
                        org_admin, channel_admin, config_admin,
                        system_group_admin, activation_key_admin,
                        or monitoring_admin.

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.user.removeRole(
            sw.key,
            login,
            role
        )
    except Exception as e:
        raise e

    return result


def setDetails(
    sw,
    login,
    user_details
):
    """
    Description:
    Updates the details of a user.

    Parameters:
        - string sessionKey
        - string login - User's login name.
        - struct - user details
            - string "first_names" - deprecated, use first_name
            - string "first_name"
            - string "last_name"
            - string "email"
            - string "prefix"
            - string "password"

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.user.setDetails(
            sw.key,
            login,
            user_details
        )
    except Exception as e:
        raise e

    return result


def usePamAuthentication(
    sw,
    login,
    pam_value
):
    """
    Description:
    Toggles whether or not a user uses PAM authentication or basic
    RHN authentication.

    Parameters:
        - string sessionKey
        - string login - User's login name.
        - int pam_value
            - 1 to enable PAM authentication
            - 0 to disable.

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.user.usePamAuthentication(
            sw.key,
            login,
            pam_value
        )
    except Exception as e:
        raise e

    return result

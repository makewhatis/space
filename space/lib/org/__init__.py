"""
``Namespace: org``
======================

Contains methods to access common organization management functions available
from the web interface.

- :func:`create`
- :func:`delete`
- :func:`getDetails`
- :func:`listOrgs`
- :func:`listSoftwareEntitlements`
- :func:`listSoftwareEntitlementsForOrg`
- :func:`listSystemEntitlements`
- :func:`listSystemEntitlementsForOrg`
- :func:`listUsers`
- :func:`migrateSystems`
- :func:`setSoftwareEntitlements`
- :func:`setSoftwareFlexEntitlements`
- :func:`setSystemEntitlements`
- :func:`updateName`
"""


def create(
    sw,
    orgname,
    adminlogin,
    adminpassword,
    prefix,
    firstname,
    lastname,
    email,
    usepamauth
):
    """
    Description:
    Create a new organization and associated administrator account.

    Parameters:
        - string sessionkey
        - string orgname - Organization name. Must meet same criteria as in the
                           web UI.
        - string adminLogin - New administrator login name.
        - string adminPassword - New administrator password.
        - string prefix - New administrator's prefix. Must match one of the
                          values available in the web UI.
                          (i.e. Dr., Mr., Mrs., Sr., etc.)
        - string firstName - New administrator's first name.
        - string lastName - New administrator's first name.
        - string email - New administrator's e-mail.
        - boolean usePamAuth - True if PAM authentication should be used for
                               the new administrator account.

    Returns:
        struct - organization info
            - int "id"
            - string "name"
            - int "active_users" - Number of active users in the organization.
            - int "systems" - Number of systems in the organization.
            - int "trusts" - Number of trusted organizations.
            - int "system_groups" - Number of system groups in the
                                    organization. (optional)
            - int "activation_keys" - Number of activation keys in the
                                      organization. (optional)
            - int "kickstart_profiles" - Number of kickstart profiles in the
                                         organization. (optional)
            - int "configuration_channels" - Number of configuration channels
                                             in the organization. (optional)
    """
    try:
        result = sw.session.org.create(
            sw.key,
            orgname,
            adminlogin,
            adminpassword,
            prefix,
            firstname,
            lastname,
            email,
            usepamauth
        )
    except Exception as e:
        raise e

    return result


def delete(
    sw,
    orgid
):
    """
    Description:
    Delete an organization. The default organization (i.e. orgId=1)
    cannot be deleted.

    Parameters:
        - string sessionkey
        - int orgid

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.org.delete(
            sw.key,
            orgid
        )
    except Exception as e:
        raise e

    return result


def getDetails(
    sw,
    orgid
):
    """
    Description:
    The detailed information about an organization given the organization ID.

    Parameters:
        - string sessionkey
        - int orgId or string name

    Returns:
        - struct - organization info
            - int "id"
            - string "name"
            - int "active_users" - Number of active users in the organization.
            - int "systems" - Number of systems in the organization.
            - int "trusts" - Number of trusted organizations.
            - int "system_groups" - Number of system groups in the
                                    organization. (optional)
            - int "activation_keys" - Number of activation keys in the
                                      organization. (optional)
            - int "kickstart_profiles" - Number of kickstart profiles in the
                                         organization. (optional)
            - int "configuration_channels" - Number of configuration channels
                                             in the organization. (optional)
    """
    try:
        result = sw.session.org.getDetails(
            sw.key,
            orgid
        )
    except Exception as e:
        raise e

    return result


def listOrgs(
    sw
):
    """
    Description:
    Returns the list of organizations.

    Parameters:
        - string sessionkey

    Returns:
        - struct - organization info
            - int "id"
            - string "name"
            - int "active_users" - Number of active users in the organization.
            - int "systems" - Number of systems in the organization.
            - int "trusts" - Number of trusted organizations.
            - int "system_groups" - Number of system groups in the
                                    organization. (optional)
            - int "activation_keys" - Number of activation keys in the
                                      organization. (optional)
            - int "kickstart_profiles" - Number of kickstart profiles in the
                                         organization. (optional)
            - int "configuration_channels" - Number of configuration channels
                                             in the organization. (optional)
    """
    try:
        result = sw.session.org.listOrgs(
            sw.key
        )
    except Exception as e:
        raise e

    return result


def listSoftwareEntitlements(
    sw,
    label=None,
    includeunentitled=None
):
    """
    Description:
    List software entitlement allocation information across all organizations.
    Caller must be a satellite administrator.

    Parameters:
        - string sessionkey

    Returns:
        - array:
            - struct - entitlement usage
                - string "label"
                - string "name"
                - int "free"
                - int "used"
                - int "allocated"
                - int "unallocated"
                - int "free_flex"
                - int "used_flex"
                - int "allocated_flex"
                - int "unallocated_flex"
    """
    if label is not None and includeunentitled is not None:
        try:
            result = sw.session.org.listSoftwareEntitlements(
                sw.key,
                label,
                includeunentitled
            )
        except Exception as e:
            raise e
    else:
        try:
            result = sw.session.org.listSoftwareEntitlements(
                sw.key
            )
        except Exception as e:
            raise e

    return result


def listSoftwareEntitlementsForOrg(
    sw,
    orgid
):
    """
    Description:
    List an organization's allocation of each software entitlement.
    A value of -1 indicates unlimited entitlements.

    Parameters:
        - string sw
        - int orgid

    Returns:
        - array:
            - struct - entitlement usage
                - string "label"
                - string "name"
                - int "allocated"
                - int "unallocated"
                - int "free"
                - int "used"
                - int "allocated_flex"
                - int "unallocated_flex"
                - int "free_flex"
                - int "used_flex"
    """
    try:
        result = sw.session.org.listSoftwareEntitlementsForOrg(
            sw.key,
            orgid
        )
    except Exception as e:
        raise e

    return result


def listSystemEntitlements(
    sw,
    label=None,
    includeunentitled=None
):
    """
    Description:
    Lists system entitlement allocation information across all organizations.
    Caller must be a satellite administrator.

    Parameters:
        - string sessionkey

    Returns:
        - array:
            - struct - entitlement usage
                - string "label"
                - string "name"
                - int "free"
                - int "used"
                - int "allocated"
                - int "unallocated"
                - int "free_flex"
                - int "used_flex"
                - int "allocated_flex"
                - int "unallocated_flex"
    """
    if label is None and includeunentitled is None:
        try:
            result = sw.session.org.listSystemEntitlements(
                sw.key
            )
        except Exception as e:
            raise e

    elif label and includeunentitled is None:
        try:
            result = sw.session.org.listSystemEntitlements(
                sw.key,
                label
            )
        except Exception as e:
            raise e

    elif label and includeunentitled:
        try:
            result = sw.session.org.listSystemEntitlements(
                sw.key,
                label,
                includeunentitled
            )
        except Exception as e:
            raise e

    return result


def listSystemEntitlementsForOrg(
    sw,
    orgid
):
    """
    Description:
    List an organization's allocation of each system entitlement.

    Parameters:
        - string sw
        - int orgid

    Returns:
        - array:
            - struct - entitlement usage
                - string "label"
                - string "name"
                - int "free"
                - int "used"
                - int "allocated"
                - int "unallocated"
    """
    try:
        result = sw.session.org.listSystemEntitlementsForOrg(
            sw.key,
            orgid
        )
    except Exception as e:
        raise e

    return result


def listUsers(
    sw,
    orgid
):
    """
    Description:
    Returns the list of users in a given organization.

    Parameters:
        - string sessionkey
        - int orgid

    Returns:
        - array:
            - struct - user
                - string "login"
                - string "login_uc"
                - string "name"
                - string "email"
                - boolean "is_org_admin"
    """
    try:
        result = sw.session.org.listUsers(
            sw.key,
            orgid
        )
    except Exception as e:
        raise e

    return result


def migrateSystems(
    sw,
    orgid,
    system_ids
):
    """
    Description:
    Migrate systems from one organization to another. If executed by a
    Satellite administrator, the systems will be migrated from their current
    organization to the organization specified by the toOrgId. If executed by
    an organization administrator, the systems must exist in the same
    organization as that administrator and the systems will be migrated to the
    organization specified by the toOrgId. In any scenario, the origination and
    destination organizations must be defined in a trust.

    Parameters:
        - string sessionKey
        - int orgid - ID of the organization where the system(s) will be
                        migrated to.
        - array:
            - int - systeids

    Returns:
        - array:
            - int - serverIdMigrated
    """
    try:
        result = sw.session.org.migrateSystems(
            sw.key,
            orgid,
            system_ids
        )
    except Exception as e:
        raise e

    return result


def setSoftwareEntitlements(
    sw,
    orgid,
    label,
    allocation
):
    """
    Description:
    Set an organization's entitlement allocation for the given software
    entitlement. If increasing the entitlement allocation, the default
    organization (i.e. orgId=1) must have a sufficient number of free
    entitlements.

    Parameters:
        - string sessionkey
        - int orgid
        - string label - Software entitlement label.
        - int allocation

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.org.setSoftwareEntitlements(
            sw.key,
            orgid,
            label,
            allocation
        )
    except Exception as e:
        raise e

    return result


def setSoftwareFlexEntitlements(
    sw,
    orgid,
    label,
    allocation
):
    """
    Description:
    Set an organization's flex entitlement allocation for the given software
    entitlement. If increasing the flex entitlement allocation, the default
    organization (i.e. orgId=1) must have a sufficient number of free flex
    entitlements.

    Parameters:
        - string sessionkey
        - int orgid
        - string label - Software entitlement label.
        - int allocation

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.org.setSoftwareFlexEntitlements(
            sw.key,
            orgid,
            label,
            allocation
        )
    except Exception as e:
        raise e

    return result


def setSystemEntitlements(
    sw,
    orgid,
    label,
    allocation
):
    """
    Description:
    Set an organization's entitlement allocation for the given software
    entitlement. If increasing the entitlement allocation, the default
    organization (i.e. orgId=1) must have a sufficient number of free
    entitlements.

    Parameters:
        - string sessionKey
        - int orgid
        - string label - System entitlement label. Valid values include:
            - enterprise_entitled
            - monitoring_entitled
            - provisioning_entitled
            - virtualization_host
            - virtualization_host_platform
        - int allocation

    Returns:
    int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.org.setSystemEntitlements(
            sw.key,
            orgid,
            label,
            allocation
        )
    except Exception as e:
        raise e

    return result


def updateName(
    sw,
    orgid,
    name
):
    """
    Description:
    Updates the name of an organization

    Parameters:
        - string sessionkey
        - int orgid
        - string name - Organization name. Must meet same criteria as in the
                        web UI.

    Returns:
        struct - organization info
            int "id"
            string "name"
            int "active_users" - Number of active users in the organization.
            int "systems" - Number of systems in the organization.
            int "trusts" - Number of trusted organizations.
            int "system_groups" - Number of system groups in the organization.
                                  (optional)
            int "activation_keys" - Number of activation keys in the
                                    organization. (optional)
            int "kickstart_profiles" - Number of kickstart profiles in the
                                       organization. (optional)
            int "configuration_channels" - Number of configuration channels in
                                           the organization. (optional)
    """
    try:
        result = sw.session.org.updateName(
            sw.key,
            orgid,
            name
        )
    except Exception as e:
        raise e

    return result

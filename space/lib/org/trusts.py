"""
``Namespace: org.trusts``
=========================

Contains methods to access common organization management functions available
from the web interface.

- :func:`addTrust`
- :func:`getDetails`
- :func:`listChannelsConsumed`
- :func:`listChannelsProvided`
- :func:`listOrgs`
- :func:`listSystemsAffected`
- :func:`listTrusts`
- :func:`removeTrust`
"""


def addTrust(
    sw,
    orgid,
    trust_org_id
):
    """
    Description:
    Add an organization to the list of trusted organizations.

    Parameters:
        - string sessionKey
        - int orgid
        - int trust_org_id

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.org.trusts.addTrust(
            sw.key,
            orgid,
            trust_org_id
        )
    except Exception as e:
        raise e

    return result


def getDetails(
    sw,
    trust_org_id
):
    """
    Description:
    The trust details about an organization given the organization's ID.

    Parameters:
        - string sessionKey
        - int trust_org_id - Id of the trusted organization

    Returns:
        - struct - org trust details
            - dateTime.iso8601 "created" - Date the organization was created
            - dateTime.iso8601 "trusted_since" - Date the organization was
                                                 defined as trusted
            - int "channels_provided" - Number of channels provided by the
                                        organization.
            - int "channels_consumed" - Number of channels consumed by the
                                        organization.
            - int "systems_migrated_to" - Number of systems migrated to the
                                          organization.
            - int "systems_migrated_from" - Number of systems migrated from the
                                            organization.
    """
    try:
        result = sw.session.org.trusts.getDetails(
            sw.key,
            trust_org_id
        )
    except Exception as e:
        raise e

    return result


def listChannelsConsumed(
    sw,
    trust_org_id
):
    """
    Description:
    Lists all software channels that the organization given may consume from
    the user's organization.

    Parameters:
        - string sessionKey
        - int trust_org_id - Id of the trusted organization

    Returns:
        - array:
            - struct - channel info
                - int "channel_id"
                - string "channel_name"
                - int "packages"
                - int "systems"
    """
    try:
        result = sw.session.org.trusts.listChannelsConsumed(
            sw.key,
            trust_org_id
        )
    except Exception as e:
        raise e

    return result


def listChannelsProvided(
    sw,
    trust_org_id
):
    """
    Description:
    Lists all software channels that the organization given is providing to
    the user's organization.

    Parameters:
        - string sessionkey
        - int trust_org_id - Id of the trusted organization

    Returns:
        - array:
            - struct - channel info
                - int "channel_id"
                - string "channel_name"
                - int "packages"
                - int "systems"
    """
    try:
        result = sw.session.org.trusts.listChannelsProvided(
            sw.key,
            trust_org_id
        )
    except Exception as e:
        raise e

    return result


def listOrgs(
    sw
):
    """
    Description:
    List all organanizations trusted by the user's organization.

    Parameters:
        - string sessionKey

    Returns:
        - array:
            - struct - trusted organizations
                - int "org_id"
                - string "org_name"
                - int "shared_channels"
    """
    try:
        result = sw.session.org.trusts.listOrgs(
            sw.key
        )
    except Exception as e:
        raise e

    return result


def listSystemsAffected(
    sw,
    orgid,
    trust_org_id
):
    """
    Description:
    Get a list of systems within the trusted organization that would be
    affected if the trust relationship was removed. This basically lists
    systems that are sharing at least (1) package.

    Parameters:
        - string sessionKey
        - int orgId
        - string trustOrgId

    Returns:
        - array:
            - struct - affected systems
                - int "systemId"
    """
    try:
        result = sw.session.org.trusts.listSystemsAffected(
            sw.key,
            orgid,
            trust_org_id
        )
    except Exception as e:
        raise e

    return result


def listTrusts(
    sw,
    orgid
):
    """
    Description:
    Returns the list of trusted organizations.

    Parameters:
        - string sessionKey
        - int orgid

    Returns:
        - array:
            - struct - trusted organizations
                - int "orgId"
                - string "orgName"
                - bool "trustEnabled"
    """
    try:
        result = sw.session.org.trusts.listTrusts(
            sw.key,
            orgid
        )
    except Exception as e:
        raise e

    return result


def removeTrust(
    sw,
    orgid,
    trust_org_id
):
    """
    Description:
    Remove an organization to the list of trusted organizations.

    Parameters:
        - string sessionKey
        - int orgId
        - int trustOrgId

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.org.trusts.removeTrust(
            sw.key,
            orgid,
            trust_org_id
        )
    except Exception as e:
        raise e

    return result

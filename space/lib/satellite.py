"""
``Namespace: satellite``
======================

Provides methods to obtain details on the Satellite.

- :func:`getCertificateExpirationDate`
- :func:`isMonitoringEnabled`
- :func:`isMonitoringEnabledBySystemId`
- :func:`listEntitlements`
- :func:`listProxies`
"""


def getCertificateExpirationDate(
    sw
):
    """
    Description:
    Retrieves the certificate expiration date of the activated certificate.

    Parameters:
        - session

    Returns:
        - dateTime.iso8601

    """
    try:
        result = sw.session.satellite.getCertificateExpirationDate(
            sw.key
        )
    except Exception as e:
        raise e

    return result


def isMonitoringEnabled(
    sw
):
    """
    Description:
    Indicates if monitoring is enabled on the satellite

    Parameters:
        - session

    Returns:
        - boolean True if monitoring is enabled
    """
    try:
        result = sw.session.satellite.isMonitoringEnabled(
            sw.key
        )
    except Exception as e:
        raise e

    return result


def isMonitoringEnabledBySystemId(
    sw,
    systemid
):
    """
    Description:
    Indicates if monitoring is enabled on the satellite

    Parameters:
        - session
        - string systemid - systemid file

    Returns:
        - boolean True if monitoring is enabled
    """
    try:
        result = sw.session.satellite.isMonitoringEnabledBySystemId(
            sw.key,
            systemid
        )
    except Exception as e:
        raise e

    return result


def listEntitlements(
    sw
):
    """
    Description:
    Lists all channel and system entitlements for the organization associated
    with the user executing the request.

    Parameters:
        - session

    Returns:
        - struct - channel/system entitlements
            - array "system"
                - struct - system entitlement
                    - string "label"
                    - string "name"
                    - int "used_slots"
                    - int "free_slots"
                    - int "total_slots"
            - array "channel"
                - struct - channel entitlement
                    - string "label"
                    - string "name"
                    - int "used_slots"
                    - int "free_slots"
                    - int "total_slots"
                    - int "used_flex"
                    - int "free_flex"
                    - int "total_flex"
    """
    try:
        result = sw.session.satellite.listEntitlements(
            sw.key
        )
    except Exception as e:
        raise e

    return result


def listProxies(
    sw
):
    """
    Description:
    List the proxies within the user's organization.

    Parameters:
        - session

    Returns:
        - array:
            - struct - system
                - int "id"
                - string "name"
                - dateTime.iso8601 "last_checkin" - Last time server
                                                    successfully checked in
    """
    try:
        result = sw.session.satellite.listProxies(
            sw.key
        )
    except Exception as e:
        raise e

    return result

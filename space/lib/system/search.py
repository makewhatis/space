"""
``Namespace: system.search``
============================

Provides methods to perform system search requests using the
search server.

- :func:`deviceDescription`
- :func:`deviceDriver`
- :func:`deviceId`
- :func:`deviceVendorId`
- :func:`hostname`
- :func:`ip`
- :func:`nameAndDescription`
- :func:`uuid`
"""


def deviceDescription(
    sw,
    search_term
):
    """
    Description:
    List the systems which match the device description.

    Parameters:
        - string sessionKey
        - string search_term

    Returns:
        - array:
            - struct - system
                - int "id"
                - string "name"
                - dateTime.iso8601 "last_checkin" - Last time server
                                                    successfully checked in
                - string "hostname"
                - string "ip"
                - string "hw_description" - hw description if not null
                - string "hw_device_id" - hw device id if not null
                - string "hw_vendor_id" - hw vendor id if not null
                - string "hw_driver" - hw driver if not null
    """
    try:
        result = sw.session.system.search.deviceDescription(
            sw.key,
            search_term
        )
    except Exception as e:
        raise e

    return result


def deviceDriver(
    sw,
    search_term
):
    """
    Description:
    List the systems which match this device driver.

    Parameters:
        - string sessionKey
        - string search_term

    Returns:
        - array:
            - struct - system
                - int "id"
                - string "name"
                - dateTime.iso8601 "last_checkin" - Last time server
                                                    successfully checked in
                - string "hostname"
                - string "ip"
                - string "hw_description" - hw description if not null
                - string "hw_device_id" - hw device id if not null
                - string "hw_vendor_id" - hw vendor id if not null
                - string "hw_driver" - hw driver if not null
    """
    try:
        result = sw.session.system.search.deviceDriver(
            sw.key,
            search_term
        )
    except Exception as e:
        raise e

    return result


def deviceId(
    sw,
    search_term
):
    """
    Description:
    List the systems which match this device id

    Parameters:
        - string sessionKey
        - string search_term

    Returns:
        - array:
            - struct - system
                - int "id"
                - string "name"
                - dateTime.iso8601 "last_checkin" - Last time server
                                                    successfully checked in
                - string "hostname"
                - string "ip"
                - string "hw_description" - hw description if not null
                - string "hw_device_id" - hw device id if not null
                - string "hw_vendor_id" - hw vendor id if not null
                - string "hw_driver" - hw driver if not null
    """
    try:
        result = sw.session.system.search.deviceId(
            sw.key,
            search_term
        )
    except Exception as e:
        raise e

    return result


def deviceVendorId(
    sw,
    search_term
):
    """
    Description:
    List the systems which match this device vendor_id

    Parameters:
        - string sessionKey
        - string search_term

    Returns:
        - array:
            - struct - system
                - int "id"
                - string "name"
                - dateTime.iso8601 "last_checkin" - Last time server
                                                    successfully checked in
                - string "hostname"
                - string "ip"
                - string "hw_description" - hw description if not null
                - string "hw_device_id" - hw device id if not null
                - string "hw_vendor_id" - hw vendor id if not null
                - string "hw_driver" - hw driver if not null
    """
    try:
        result = sw.session.system.search.deviceVendorId(
            sw.key,
            search_term
        )
    except Exception as e:
        raise e

    return result


def hostname(
    sw,
    search_term
):
    """
    Description:
    List the systems which match this hostname

    Parameters:
        - string sessionKey
        - string search_term

    Returns:
        - array:
            - struct - system
                - int "id"
                - string "name"
                - dateTime.iso8601 "last_checkin" - Last time server
                                                    successfully checked in
                - string "hostname"
                - string "ip"
                - string "hw_description" - hw description if not null
                - string "hw_device_id" - hw device id if not null
                - string "hw_vendor_id" - hw vendor id if not null
                - string "hw_driver" - hw driver if not null
    """
    try:
        result = sw.session.system.search.hostname(
            sw.key,
            search_term
        )
    except Exception as e:
        raise e

    return result


def ip(
    sw,
    search_term
):
    """
    Description:
    List the systems which match this ip.

    Parameters:
        - string sessionKey
        - string search_term

    Returns:
        - array:
            - struct - system
                - int "id"
                - string "name"
                - dateTime.iso8601 "last_checkin" - Last time server
                                                    successfully checked in
                - string "hostname"
                - string "ip"
                - string "hw_description" - hw description if not null
                - string "hw_device_id" - hw device id if not null
                - string "hw_vendor_id" - hw vendor id if not null
                - string "hw_driver" - hw driver if not null
    """
    try:
        result = sw.session.system.search.ip(
            sw.key,
            search_term
        )
    except Exception as e:
        raise e

    return result


def nameAndDescription(
    sw,
    search_term
):
    """
    Description:
    List the systems which match this name or description

    Parameters:
        - string sessionKey
        - string search_term

    Returns:
        - array:
            - struct - system
                - int "id"
                - string "name"
                - dateTime.iso8601 "last_checkin" - Last time server
                                                    successfully checked in
                - string "hostname"
                - string "ip"
                - string "hw_description" - hw description if not null
                - string "hw_device_id" - hw device id if not null
                - string "hw_vendor_id" - hw vendor id if not null
                - string "hw_driver" - hw driver if not null
    """
    try:
        result = sw.session.system.search.nameAndDescription(
            sw.key,
            search_term
        )
    except Exception as e:
        raise e

    return result


def uuid(
    sw,
    search_term
):
    """
    Description:
    List the systems which match this UUID

    Parameters:
        - string sessionKey
        - string search_term

    Returns:
        - array:
            - struct - system
                - int "id"
                - string "name"
                - dateTime.iso8601 "last_checkin" - Last time server
                                                    successfully checked in
                - string "hostname"
                - string "ip"
                - string "hw_description" - hw description if not null
                - string "hw_device_id" - hw device id if not null
                - string "hw_vendor_id" - hw vendor id if not null
                - string "hw_driver" - hw driver if not null
    """
    try:
        result = sw.session.system.search.uuid(
            sw.key,
            search_term
        )
    except Exception as e:
        raise e

    return result

"""
``Namespace: preferences.locale``
======================

Provides methods to access and modify user locale information

- :func:`listLocales`
- :func:`listTimeZones`
- :func:`setLocale`
- :func:`setTimeZone`
"""


def listLocales(
    sw
):
    """
    Description:
    Returns a list of all understood locales. Can be used as input to
    setLocale.

    Parameters:

    Returns:
    array:
    string - Locale code.
    """
    try:
        result = sw.session.preferences.locale.listLocales()
    except Exception as e:
        raise e

    return result


def listTimeZones(
    sw
):
    """
    Description:
    Returns a list of all understood timezones. Results can be used as input
    to setTimeZone.

    Parameters:

    Returns:
        - array:
            - struct - timezone
                - int "time_zone_id" - Unique identifier for timezone.
                - string "olson_name" - Name as identified by the Olson
                                        database.
    """
    try:
        result = sw.session.preferences.locale.listTimeZones()
    except Exception as e:
        raise e

    return result


def setLocale(
    sw,
    login,
    locale
):
    """
    Description:
    Set a user's locale.

    Parameters:
        - string sessionKey
        - string login - User's login name.
        - string locale - Locale to set. (from listLocales)

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.preferences.locale.setLocale(
            sw.key,
            login,
            locale
        )
    except Exception as e:
        raise e

    return result


def setTimeZone(
    sw,
    login,
    tzid
):
    """
    Description:
    Set a user's timezone.

    Parameters:
        - string sessionKey
        - string login - User's login name.
        - int tzid - Timezone ID. (from listTimeZones)

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.preferences.locale.setTimeZone(
            sw.key,
            login,
            tzid
        )
    except Exception as e:
        raise e

    return result

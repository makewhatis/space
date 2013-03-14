"""
``Namespace: errata``
======================

Provides methods to access and modify distribution channel information.

Available methods:

- :func:`addPackages`
- :func:`applicableToChannels`
- :func:`bugzillaFixes`
- :func:`clone`
- :func:`cloneAsOriginal`
- :func:`cloneAsOriginalAsync`
- :func:`cloneAsync`
- :func:`create`
- :func:`delete`
- :func:`findByCve`
- :func:`getDetails`
- :func:`listAffectedSystems`
- :func:`listCves`
- :func:`listKeywords`
- :func:`listPackages`
- :func:`listUnpublishedErrata`
- :func:`publish`
- :func:`publishAsOriginal`
- :func:`removePackages`
- :func:`setDetails`

"""


def addPackages(
    sw,
    advisoryname,
    packageids
):
    """
    *Description*:
    Add a set of packages to an erratum with the given advisory name.
    This method will only allow for modification of custom errata created
    either through the UI or API.

    *Parameters*:
        - string sessionKey
        - string advisoryName
        - array:
            - int - packageId

    *Returns*:

    int - representing the number of packages added, exception otherwise
    """
    try:
        result = sw.session.errata.addPackages(
            sw.key,
            advisoryname,
            packageids
        )
    except Exception as e:
        raise e

    return result


def applicableToChannels(
    sw,
    advisoryname
):
    """
    *Description*:
    Returns a list of channels applicable to the erratum with the given
    advisory name.

    *Parameters*:
        - string sessionKey
        - string advisoryName

    *Returns*:
        - array:
            - struct - channel
                - int "channel_id"
                - string "label"
                - string "name"
                - string "parent_channel_label"
    """
    try:
        result = sw.session.errata.applicableToChannels(
            sw.key,
            advisoryname
        )
    except Exception as e:
        raise e

    return result


def bugzillaFixes(
    sw,
    advisoryname
):
    """
    *Description*:
    Get the Bugzilla fixes for an erratum matching the given advisoryName. The
    bugs will be returned in a struct where the bug id is the key.
    i.e. 208144="errata.bugzillaFixes Method Returns different results than
    docs say"

    *Parameters*:
        - string sessionKey
        - string advisoryName

    *Returns*:
        - struct - Bugzilla info
        - string "bugzilla_id" - actual bug number is the key into the struct
        - string "bug_summary" - summary who's key is the bug id
    """
    try:
        result = sw.session.errata.bugzillaFixes(
            sw.key,
            advisoryname
        )
    except Exception as e:
        raise e

    return result


def clone(
    sw,
    channel_label,
    advisories
):
    """
    *Description*:
    Clone a list of errata into the specified channel.

    *Parameters*:
        - string sessionKey
        - string channel_label
        - array:
            - string - advisory - The advisory name of the errata to clone.

    *Returns*:
        - array:
            - struct - errata
                - int "id" - Errata Id
                - string "date" - Date erratum was created.
                - string "advisory_type" - Type of the advisory.
                - string "advisory_name" - Name of the advisory.
                - string "advisory_synopsis" - Summary of the erratum.
    """
    try:
        result = sw.session.errata.clone(
            sw.key,
            channel_label,
            advisories
        )
    except Exception as e:
        raise e

    return result


def cloneAsOriginal(
    sw,
    channel_label,
    advisories
):
    """
    *Description*:
    Clones a list of errata into a specified cloned channel according the
    original erratas.

    *Parameters*:
        - string sessionKey
        - string channel_label
        - array:
            - string - advisory - The advisory name of the errata to clone.

    *Returns*:
        - array:
            - struct - errata
                - int "id" - Errata Id
                - string "date" - Date erratum was created.
                - string "advisory_type" - Type of the advisory.
                - string "advisory_name" - Name of the advisory.
                - string "advisory_synopsis" - Summary of the erratum.
    """
    try:
        result = sw.session.errata.cloneAsOriginal(
            sw.key,
            channel_label,
            advisories
        )
    except Exception as e:
        raise e

    return result


def cloneAsOriginalAsync(
    sw,
    channel_label,
    advisories
):
    """
    *Description*:
    Asynchronously clones a list of errata into a specified cloned channel
    according the original erratas

    *Parameters*:
        - string sessionKey
        - string channel_label
        - array:
            - string - advisory - The advisory name of the errata to clone.

    *Returns*:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.errata.cloneAsOriginalAsync(
            sw.key,
            channel_label,
            advisories
        )
    except Exception as e:
        raise e

    return result


def cloneAsync(
    sw,
    channel_label,
    advisories
):
    """
    *Description*:
    Asynchronously clone a list of errata into the specified channel.

    *Parameters*:
        - string sessionKey
        - string channel_label
        - array:
            - string - advisory - The advisory name of the errata to clone.

    *Returns*:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.errata.cloneAsync(
            sw.key,
            channel_label,
            advisories
        )
    except Exception as e:
        raise e

    return result


def create(
    sw,
    errata_info,
    bug_dict,
    keywords,
    packageids,
    publish,
    channel_labels
):
    """
    *Description*:
    Create a custom errata. If "publish" is set to true, the errata will be
    published as well

    *Parameters*:
        - string sessionKey
        - struct - errata info
            - string "synopsis"
            - string "advisory_name"
            - int "advisory_release"
            - string "advisory_type" - Type of advisory (one of the following:
                                      'Security Advisory',
                                      'Product Enhancement Advisory', or
                                      'Bug Fix Advisory'
            - string "product"
            - string "errataFrom"
            - string "topic"
            - string "description"
            - string "references"
            - string "notes"
            - string "solution"
        - array:
            - struct - bug
                - int "id" - Bug Id
                - string "summary"
                - string "url"
        - array:
            - string - keyword - List of keywords to associate with the errata.
        - array:
            - int - packageId
        - boolean publish - Should the errata be published.
        - array:
            - string - channelLabel - list of channels the errata should be
                                      published too, ignored if publish is set
                                      to false

    *Returns*:
        - struct - errata
            - int "id" - Errata Id
            - string "date" - Date erratum was created.
            - string "advisory_type" - Type of the advisory.
            - string "advisory_name" - Name of the advisory.
            - string "advisory_synopsis" - Summary of the erratum.
    """
    try:
        result = sw.session.errata.create(
            sw.key,
            errata_info,
            bug_dict,
            keywords,
            packageids,
            publish,
            channel_labels
        )
    except Exception as e:
        raise e

    return result


def delete(
    sw,
    advisoryname
):
    """
    *Description*:
    Delete an erratum. This method will only allow for deletion of custom
    errata created either through the UI or API.

    *Parameters*:
        - string sessionKey
        - string advisoryName

    *Returns*:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.errata.delete(
            sw.key,
            advisoryname
        )
    except Exception as e:
        raise e

    return result


def findByCve(
    sw,
    cvename
):
    """
    *Description*:
    Lookup the details for errata associated with the given CVE
    (e.g. CVE-2008-3270)

    *Parameters*:
        - string sessionKey
        - string cveName

    *Returns*:
        - array:
            - struct - errata
                - int "id" - Errata Id
                - string "date" - Date erratum was created.
                - string "advisory_type" - Type of the advisory.
                - string "advisory_name" - Name of the advisory.
                - string "advisory_synopsis" - Summary of the erratum.
    """
    try:
        result = sw.session.errata.findByCve(
            sw.key,
            cvename
        )
    except Exception as e:
        raise e

    return result


def getDetails(
    sw,
    advisoryname
):
    """
    *Description*:
    Retrieves the details for the erratum matching the given advisory name.

    *Parameters*:
        - string sessionKey
        - string advisoryName

    *Returns*:
        - struct - erratum
            - string "issue_date"
            - string "update_date"
            - string "last_modified_date" - This date is only included for
                                            published erratum and it represents
                                            the last time the erratum was
                                            modified.
            - string "synopsis"
            - int "release"
            - string "type"
            - string "product"
            - string "errataFrom"
            - string "topic"
            - string "description"
            - string "references"
            - string "notes"
            - string "solution"
    """
    try:
        result = sw.session.errata.getDetails(
            sw.key,
            advisoryname
        )
    except Exception as e:
        raise e

    return result


def listAffectedSystems(
    sw,
    advisoryname
):
    """
    *Description*:
    Return the list of systems affected by the erratum with advisory name.

    *Parameters*:
        - string sessionKey
        - string advisoryName

    *Returns*:
        - array:
            - struct - system
                - int "id"
                - string "name"
                - dateTime.iso8601 "last_checkin" - Last time server
                                                    successfully checked in
    """
    try:
        result = sw.session.errata.listAffectedSystems(
            sw.key,
            advisoryname
        )
    except Exception as e:
        raise e

    return result


def listCves(
    sw,
    advisoryname
):
    """
    *Description*:
    Returns a list of CVEs applicable to the erratum with the given advisory
    name.

    *Parameters*:
        - string sessionKey
        - string advisoryName

    *Returns*:
        - array:
            - string - cveName
    """
    try:
        result = sw.session.errata.listCves(
            sw.key,
            advisoryname
        )
    except Exception as e:
        raise e

    return result


def listKeywords(
    sw,
    advisoryname
):
    """
    *Description*:
    Get the keywords associated with an erratum matching the given advisory
    name.

    *Parameters*:
        - string sessionKey
        - string advisoryName

    *Returns*:
        - array:
            - string - Keyword associated with erratum.
    """
    try:
        result = sw.session.errata.listKeywords(
            sw.key,
            advisoryname
        )
    except Exception as e:
        raise e

    return result


def listPackages(
    sw,
    advisoryname
):
    """
    *Description*:
    Returns a list of the packages affected by the erratum with the given
    advisory name.

    *Parameters*:
        - string sessionKey
        - string advisoryName

    *Returns*:
        - array:
            - struct - package
                - int "id"
                - string "name"
                - string "epoch"
                - string "version"
                - string "release"
                - string "arch_label"
                - array "providing_channels"
                    - string - Channel label providing this package.
                - string "build_host"
                - string "description"
                - string "checksum"
                - string "checksum_type"
                - string "vendor"
                - string "summary"
                - string "cookie"
                - string "license"
                - string "path"
                - string "file"
                - string "build_date"
                - string "last_modified_date"
                - string "size"
                - string "payload_size"
    """
    try:
        result = sw.session.errata.listPackages(
            sw.key,
            advisoryname
        )
    except Exception as e:
        raise e

    return result


def listUnpublishedErrata(
    sw
):
    """
    *Description*:
    Returns a list of unpublished errata

    *Parameters*:
        - string sessionKey

    *Returns*:
        - array:
            - struct - erratum
                - int "id"
                - int "published"
                - string "advisory"
                - string "advisory_name"
                - string "advisory_type"
                - string "synopsis"
                - dateTime.iso8601 "created"
                - dateTime.iso8601 "update_date"
    """
    try:
        result = sw.session.errata.listUnpublishedErrata(
            sw.key
        )
    except Exception as e:
        raise e

    return result


def publish(
    sw,
    advisoryname,
    channel_labels
):
    """
    *Description*:
    Publish an existing (unpublished) errata to a set of channels.

    *Parameters*:
        - string sessionKey
        - string advisoryName
        - array:
            - string - channelLabel - list of channel labels to publish to

    *Returns*:
        - struct - errata
            - int "id" - Errata Id
            - string "date" - Date erratum was created.
            - string "advisory_type" - Type of the advisory.
            - string "advisory_name" - Name of the advisory.
            - string "advisory_synopsis" - Summary of the erratum.
    """
    try:
        result = sw.session.errata.publish(
            sw.key,
            advisoryname,
            channel_labels
        )
    except Exception as e:
        raise e

    return result


def publishAsOriginal(
    sw,
    advisoryname,
    channel_labels
):
    """
    *Description*:
    Publishes an existing (unpublished) cloned errata to a set of cloned
    channels according to its original erratum

    *Parameters*:
        - string sessionKey
        - string advisoryName
        - array:
            - string - channelLabel - list of channel labels to publish to

    *Returns*:
        - struct - errata
            - int "id" - Errata Id
            - string "date" - Date erratum was created.
            - string "advisory_type" - Type of the advisory.
            - string "advisory_name" - Name of the advisory.
            - string "advisory_synopsis" - Summary of the erratum.
    """
    try:
        result = sw.session.errata.publishAsOriginal(
            sw.key,
            advisoryname,
            channel_labels
        )
    except Exception as e:
        raise e

    return result


def removePackages(
    sw,
    advisoryname,
    packageids
):
    """
    *Description*:
    Remove a set of packages from an erratum with the given advisory name. This
    method will only allow for modification of custom errata created either
    through the UI or API.

    *Parameters*:
        - string sessionKey
        - string advisoryName
        - array:
            - int - packageId

    *Returns*:
        - int - representing the number of packages removed, exception
                otherwise
    """
    try:
        result = sw.session.errata.removePackages(
            sw.key,
            advisoryname,
            packageids
        )
    except Exception as e:
        raise e

    return result


def setDetails(
    sw,
    advisoryname,
    errata_info
):
    """
    *Description*:
    Set erratum details. All arguments are optional and will only be modified
    if included in the struct. This method will only allow for modification of
    custom errata created either through the UI or API.

    *Parameters*:
        - string sessionKey
        - string advisoryName
        - struct - errata details
            - string "synopsis"
            string "advisory_name"
            - int "advisory_release"
            - string "advisory_type" - Type of advisory (one of the following:
                                       'Security Advisory',
                                       'Product Enhancement Advisory', or
                                       'Bug Fix Advisory'
            - string "product"
            - string "errataFrom"
            - string "topic"
            - string "description"
            - string "references"
            - string "notes"
            - string "solution"
            - array "bugs" - 'bugs' is the key into the struct
                - struct - bug
                    - int "id" - Bug Id
                    - string "summary"
                    - string "url"
            - array "keywords" - 'keywords' is the key into the struct
                - string - keyword - List of keywords to associate with the
                                     errata.
            - array "CVEs" - 'cves' is the key into the struct
                - string - cves - List of CVEs to associate with the errata.

    *Returns*:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.errata.setDetails(
            sw.key,
            advisoryname,
            errata_info
        )
    except Exception as e:
        raise e

    return result

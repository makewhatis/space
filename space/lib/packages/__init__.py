"""
``Namespace: packages``
======================

Methods to retrieve information about the Packages contained within
this server.

- :func:`findByNvrea`
- :func:`getDetails`
- :func:`getPackage`
- :func:`getPackageUrl`
- :func:`listChangelog`
- :func:`listDependencies`
- :func:`listFiles`
- :func:`listProvidingChannels`
- :func:`listProvidingErrata`
- :func:`removePackage`
"""


def findByNvrea(
    sw,
    name,
    version,
    release,
    epoch,
    arch_label
):
    """
    Description:
    Lookup the details for packages with the given name, version, release,
    architecture label, and (optionally) epoch.

    Parameters:
        - string sw
        - string name
        - string version
        - string release
        - string epoch - If set to something other than empty string, strict
                         matching will be used and the epoch string must be
                         correct. If set to an empty string, if the epoch is
                         null or there is only one NVRA combination, it will
                         be returned. (Empty string is recommended.)
        - string arch_label

    Returns:
        - array:
            - struct - package
                - string "name"
                - string "version"
                - string "release"
                - string "epoch"
                - int "id"
                - string "arch_label"
                - string "path" - The path on that file system that the
                                  package resides
                - string "provider" - The provider of the package,
                                      determined by the gpg key it was signed
                                      with.
                - dateTime.iso8601 "last_modified"
    """
    try:
        result = sw.session.packages.findByNvrea(
            sw.key,
            name,
            version,
            release,
            epoch,
            arch_label
        )
    except Exception as e:
        raise e

    return result


def getDetails(
    sw,
    package_id
):
    """
    Description:
    Retrieve details for the package with the ID.

    Parameters:
        - string sessionKey
        - int package_id

    Returns:
        - struct - package
            - int "id"
            - string "name"
            - string "epoch"
            - string "version"
            - string "release"
            - string "arch_label"
            - array "providing_channels"
                - string Channel label providing this package.
            - string "build_host"
            - string "description"
            - string "checksum"
            - string "checksum_type"
            - string "vendor"
            - string "summary"
            - string "cookie"
            - string "license"
            - string "file"
            - string "build_date"
            - string "last_modified_date"
            - string "size"
            - string "path" - The path on the Satellite's file system that the
                              package resides.
            - string "payload_size"
    """
    try:
        result = sw.session.packages.getDetails(
            sw.key,
            package_id
        )
    except Exception as e:
        raise e

    return result


def getPackage(
    sw,
    package_id
):
    """
    Description:
    Retrieve the package file associated with a package.

    Parameters:
        - string sessionKey
        - int package_id

    Returns:
        - base64 - base64 encoded package
    """
    try:
        result = sw.session.packages.getPackage(
            sw.key,
            package_id
        )
    except Exception as e:
        raise e

    return result


def getPackageUrl(
    sw,
    package_id
):
    """
    Description:
         - Retrieve the url that can be used to download a package. This will
           expire after a certain time period.

    Parameters:
        - string sessionKey
        - int package_id

    Returns:
        - string - the download url
    """
    try:
        result = sw.session.packages.getPackageUrl(
            sw.key,
            int(package_id)
        )
    except Exception as e:
        raise e

    return result


def listChangelog(
    sw,
    package_id
):
    """
    Description:
    List the change log for a package.

    Parameters:
        - string sessionKey
        - int package_id

    Returns:
        - string
    """
    try:
        result = sw.session.packages.listChangelog(
            sw.key,
            package_id
        )
    except Exception as e:
        raise e

    return result


def listDependencies(
    sw,
    package_id
):
    """
    Description:
    List the dependencies for a package.

    Parameters:
        - string sessionKey
        - int package_id

    Returns:
        - array:
            - struct - dependency
                - string "dependency"
                - string "dependency_type" - One of the following:
                - requires
                - conflicts
                - obsoletes
                - provides
                - string "dependency_modifier"
    """
    try:
        result = sw.session.packages.listDependencies(
            sw.key,
            package_id
        )
    except Exception as e:
        raise e

    return result


def listFiles(
    sw,
    package_id
):
    """
    Description:
    List the files associated with a package.

    Parameters:
        - string sessionKey
        - int package_id

    Returns:
        - array:
            - struct - file info
                - string "path"
                - string "type"
                - string "last_modified_date"
                - string "checksum"
                - string "checksum_type"
                - int "size"
                - string "linkto"
    """
    try:
        result = sw.session.packages.listFiles(
            sw.key,
            package_id
        )
    except Exception as e:
        raise e

    return result


def listProvidingChannels(
    sw,
    package_id
):
    """
    Description:
    List the channels that provide the a package.

    Parameters:
        - string sessionKey
        - int package_id

    Returns:
        - array:
            - struct - channel
                - string "label"
                - string "parent_label"
                - string "name"
    """
    try:
        result = sw.session.packages.listProvidingChannels(
            sw.key,
            package_id
        )
    except Exception as e:
        raise e

    return result


def listProvidingErrata(
    sw,
    package_id
):
    """
    Description:
    List the errata providing the a package.

    Parameters:
        - string sessionKey
        - int package_id

    Returns:
        - array:
            - struct - errata
                - string "advisory"
                - string "issue_date"
                - string "last_modified_date"
                - string "update_date"
                - string "synopsis"
                - string "type"
    """
    try:
        result = sw.session.packages.listProvidingErrata(
            sw.key,
            package_id
        )
    except Exception as e:
        raise e

    return result


def removePackage(
    sw,
    package_id
):
    """
    Description:
    Remove a package from the satellite.

    Parameters:
        - string sessionKey
        - int package_id

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.packages.removePackage(
            sw.key,
            package_id
        )
    except Exception as e:
        raise e

    return result

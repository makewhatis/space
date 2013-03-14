"""
``Namespace: packages.search``
======================

Methods to interface to package search capabilities in search server.

- :func:`advanced`
- :func:`advancedWithActKey`
- :func:`advancedWithChannel`
- :func:`name`
- :func:`nameAndDescription`
- :func:`nameAndSummary`
"""


def advanced(
    sw,
    lucene_query
):
    """
    Description:
    Advanced method to search lucene indexes with a passed in query written
    in Lucene Query Parser syntax.
    Lucene Query Parser syntax is defined at lucene.apache.org.
    Fields searchable for Packages: name, epoch, version, release, arch,
    description, summary

    Lucene Query Example::

        "name:kernel AND version:2.6.18 AND -description:devel"

    Parameters:
        - string sessionKey
        - string lucene_query - a query written in the form of Lucene
                                QueryParser Syntax

    Returns:
        - array:
            - struct - package overview
                - int "id"
                - string "name"
                - string "summary"
                - string "description"
                - string "version"
                - string "release"
                - string "arch"
                - string "epoch"
                - string "provider"
    """
    try:
        result = sw.session.packages.search.advanced(
            sw.key,
            lucene_query
        )
    except Exception as e:
        raise e

    return result


def advancedWithActKey(
    sw,
    lucene_query,
    actkey
):
    """
    Description:
    Advanced method to search lucene indexes with a passed in query written in
    Lucene Query Parser syntax, additionally this method will limit results to
    those which are associated with a given activation key.
    Lucene Query Parser syntax is defined at lucene.apache.org.

    Fields searchable for Packages: name, epoch, version, release, arch,
    description, summary

    Lucene Query Example::

        "name:kernel AND version:2.6.18 AND -description:devel"

    Parameters:
        - string sessionKey
        - string lucene_query - a query written in the form of Lucene
                                QueryParser Syntax
        - string actkey - activation key to look for packages in

    Returns:
        - array:
            - struct - package overview
                - int "id"
                - string "name"
                - string "summary"
                - string "description"
                - string "version"
                - string "release"
                - string "arch"
                - string "epoch"
                - string "provider"
    """
    try:
        result = sw.session.packages.search.advancedWithActKey(
            sw.key,
            lucene_query,
            actkey
        )
    except Exception as e:
        raise e

    return result


def advancedWithChannel(
    sw,
    lucene_query,
    channel
):
    """
    Description:
    Advanced method to search lucene indexes with a passed in query
    written in Lucene Query Parser syntax, additionally this method
    will limit results to those which are in the passed in channel
    label.
    Lucene Query Parser syntax is defined at lucene.apache.org.

    Fields searchable for Packages: name, epoch, version, release, arch,
    description, summary

    Lucene Query Example::

        "name:kernel AND version:2.6.18 AND -description:devel"

    Parameters:
        - string sessionKey
        - string luceneQuery - a query written in the form of Lucene
                              QueryParser Syntax
        - string channelLabel - Channel Label

    Returns:
        - array:
            - struct - package overview
                - int "id"
                - string "name"
                - string "summary"
                - string "description"
                - string "version"
                - string "release"
                - string "arch"
                - string "epoch"
                - string "provider"
    """
    try:
        result = sw.session.packages.search.advancedWithChannel(
            sw.key,
            lucene_query,
            channel
        )
    except Exception as e:
        raise e

    return result


def name(
    sw,
    name
):
    """
    Description:
    Search the lucene package indexes for all packages which match the given
    name.

    Parameters:
    string sessionKey
    string name - package name to search for

    Returns:
        - array:
            - struct - package overview
                - int "id"
                - string "name"
                - string "summary"
                - string "description"
                - string "version"
                - string "release"
                - string "arch"
                - string "epoch"
                - string "provider"
    """
    try:
        result = sw.session.packages.search.name(
            sw.key,
            name
        )
    except Exception as e:
        raise e

    return result


def nameAndDescription(
    sw,
    query
):
    """
    Description:
    Search the lucene package indexes for all packages which match the given
    query in name or description

    Parameters:
        - string sessionKey
        - string query - text to match in package name or description

    Returns:
        - array:
            - struct - package overview
                - int "id"
                - string "name"
                - string "summary"
                - string "description"
                - string "version"
                - string "release"
                - string "arch"
                - string "epoch"
                - string "provider
    """
    try:
        result = sw.session.packages.search.nameAndDescription(
            sw.key,
            query
        )
    except Exception as e:
        raise e

    return result


def nameAndSummary(
    sw,
    query
):
    """
    Description:
    Search the lucene package indexes for all packages which match the given
    query in name or summary.

    Parameters:
        - string sessionKey
        - string query - text to match in package name or summary

    Returns:
        - array:
            - struct - package overview
                - int "id"
                - string "name"
                - string "summary"
                - string "description"
                - string "version"
                - string "release"
                - string "arch"
                - string "epoch"
                - string "provider
    """
    try:
        result = sw.session.packages.search.nameAndSummary(
            sw.key,
            query
        )
    except Exception as e:
        raise e

    return result

"""
``Namespace: channel.software``
===============================

Provides methods to access and modify many aspects of a channel.

- :func:`addPackages`
- :func:`availableEntitlements`
- :func:`clone`
- :func:`create`
- :func:`delete`
- :func:`disassociateRepo`
- :func:`getChannelLastBuildById`
- :func:`getDetails`
- :func:`getRepoDetails`
- :func:`getRepoSyncCronExpression`
- :func:`isGloballySubscribable`
- :func:`isUserManageable`
- :func:`isUserSubscribable`
- :func:`listAllPackages`
- :func:`listArches`
- :func:`listChannelRepos`
- :func:`listChildren`
- :func:`listErrata`
- :func:`listErrataByType`
- :func:`listLatestPackages`
- :func:`listPackagesWithoutChannel`
- :func:`listRepoFilters`
- :func:`listSubscribedSystems`
- :func:`listSystemChannels`
- :func:`listUserRepos`
- :func:`mergeErrata`
- :func:`mergePackages`
- :func:`regenerateYumCache`
- :func:`removeErrata`
- :func:`removePackages`
- :func:`removeRepo`
- :func:`removeRepoFilter`
- :func:`setContactDetails`
- :func:`setDetails`
- :func:`setGloballySubscribable`
- :func:`setRepoFilters`
- :func:`setSystemChannels`
- :func:`setUserManageable`
- :func:`setUserSubscribable`
- :func:`subscribeSystem`
- :func:`syncRepo`
- :func:`updateRepo`
- :func:`updateRepoLabel`
- :func:`updateRepoUrl`
"""
import time


def addPackages(
    sw,
    channellabel,
    packagelist
):
    """
    Description:
        Adds a given list of packages to the given channel.

    Parameters:
        - sw session
        - string channelLabel - target channel.
        - array:
            - int - packageId - id of a package to add to the channel.

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.channel.software.addPackages(
            sw.key,
            channellabel,
            packagelist
        )
    except Exception as e:
        raise e

    return result


def associateRepo(
    sw,
    channellabel,
    repositorylabel
):
    """
    Description:
        Associates a repository with a channel

    Parameters:
        - sw session
        - string channelLabel - channel label
        - string repoLabel - repository label

    Returns:
        - struct - channel
            - int "id"
            - string "name"
            - string "label"
            - string "arch_name"
            - string "summary"
            - string "description"
            - string "checksum_label"
            - dateTime.iso8601 "last_modified"
            - string "maintainer_name"
            - string "maintainer_email"
            - string "maintainer_phone"
            - string "support_policy"
            - string "gpg_key_url"
            - string "gpg_key_id"
            - string "gpg_key_fp"
            - string "yumrepo_source_url"
            - string "yumrepo_label"
            - dateTime.iso8601 "yumrepo_last_sync"
            - string "end_of_life"
            - string "parent_channel_label"
            - string "clone_original"
    """
    try:
        result = sw.session.channel.software.associateRepo(
            sw.key,
            channellabel,
            repositorylabel
        )
    except Exception as e:
        raise e

    return result


def availableEntitlements(
    sw,
    channellabel
):
    """
    channel.software.availableEntitlements

    Parameters:
        - channellabel

    description:
        - Reports the number of available entitlements
          for the given channel

    returns:
        - available entitlement count (int)
    """
    try:
        result = sw.session.channel.software.availableEntitlements(
            sw.key,
            channellabel
        )
    except Exception as e:
        raise e

    return result


def clone(
    sw,
    source_channel,
    name,
    label,
    summary,
    parent_label=None,
    arch_label=None,
    gpg_url=None,
    gpg_id=None,
    gpg_fingerprint=None,
    description=None,
    no_errata=False
):
    """
    Description:
        Clone a channel. If arch_label is omitted, the arch label of the
        original channel will be used. If parent_label is omitted, the
        clone will be a base channel.

    Parameters:
        - string sessionKey
        - string original_label
        - struct - channel details
            - string "name"
            - string "label"
            - string "summary"
            - string "parent_label" - (optional)
            - string "arch_label" - (optional)
            - string "gpg_key_url" - (optional), gpg_url
            - string "gpg_key_id" - (optional), gpg_id
            - string "gpg_key_fp" - (optional), gpg_fingerprint
            - string "description" - (optional)
        - boolean original_state
    Returns:

        - int the cloned channel ID
    """
    clone_details = {
        'name': name,
        'label': label,
        'summary': summary,
        'parent_label': parent_label,
        'arch_label': arch_label,
        'gpg_url': gpg_url,
        'gpg_id': gpg_id,
        'gpg_fingerprint': gpg_fingerprint,
        'description': description,
    }

    details = dict()

    for k, v in clone_details.items():
        if clone_details[k] is not None:
            details[k] = v
    try:
        result = sw.session.channel.software.clone(
            sw.key,
            source_channel,
            details,
            no_errata
        )
    except Exception as e:
        raise e

    return result


def create(
    sw,
    channellabel,
    channame,
    summary,
    arch,
    parent='',
    checksum=None,
    gpgkey=None
):
    """

    Description:
        - Creates a software channel

    Parameters:
        - string sessionKey
        - string label - label of the new channel
        - string name - name of the new channel
        - string summary - summary of the channel
        - string archLabel - the label of the architecture the channel
                            corresponds to
            - channel-ia32 - For 32 bit channel architecture
            - channel-ia64 - For 64 bit channel architecture
            - channel-sparc - For Sparc channel architecture
            - channel-alpha - For Alpha channel architecture
            - channel-s390 - For s390 channel architecture
            - channel-s390x - For s390x channel architecture
            - channel-iSeries - For i-Series channel architecture
            - channel-pSeries - For p-Series channel architecture
            - channel-x86_64 - For x86_64 channel architecture
            - channel-ppc - For PPC channel architecture
            - channel-sparc-sun-solaris - For Sparc Solaris channel
                                          architecture
            - channel-i386-sun-solaris - For i386 Solaris channel architecture
        - string parentLabel - label of the parent of this channel, an empty
                               string if it does not have one
        - string checksumType - checksum type for this channel, used for yum
                                repository metadata generation
            - sha1 - Offers widest compatibility with clients
            - sha256 - Offers highest security, but is compatible only with
                       newer clients: Fedora 11 and newer, or Enterprise Linux
                       6 and newer.
        - struct - gpgKey
            - string "url" - GPG key URL
            - string "id" - GPG key ID
            - string "fingerprint" - GPG key Fingerprint
    """
    try:
        if gpgkey is not None and checksum is not None:
            result = sw.session.channel.software.create(
                sw.key,
                channellabel,
                channame,
                summary,
                arch,
                parent,
                checksum,
                gpgkey
            )

        elif checksum is not None:
            result = sw.session.channel.software.create(
                sw.key,
                channellabel,
                channame,
                summary,
                arch,
                parent,
                checksum
            )
        else:
            result = sw.session.channel.software.create(
                sw.key,
                channellabel,
                channame,
                summary,
                arch,
                parent
            )
    except Exception as e:
        raise e

    return result


def createRepo(
    sw,
    repolabel,
    repotype,
    repourl
):
    """
    Description:
        - Creates a repository

    Parameters:
        - string sessionKey
        - string label - repository label
        - string type - repository type (only YUM is supported)
        - string url - repository url

    Returns:

    struct - channel
        - int "id"
        - string "label"
        - string "sourceUrl"
        - string "type"
    """
    try:
        result = sw.session.channel.software.createRepo(
            sw.key,
            repolabel,
            repotype,
            repourl
        )
    except Exception as e:
        raise e

    return result


def delete(
    sw,
    channellabel
):
    """
    Description:
        - Deletes a custom software channel

    Parameters:
        - string sessionKey
        - string channelLabel - channel to delete

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.channel.software.delete(
            sw.key,
            channellabel
        )
    except Exception as e:
        raise e

    return result


def disassociateRepo(
    sw,
    channellabel,
    repoLabel
):
    """
    Description:
    Disassociates a repository from a channel

    Parameters:
        - string sessionKey
        - string channelLabel - channel label
        - string repoLabel - repository label

    Returns:
        - struct - channel
        - int "id"
        - string "name"
        - string "label"
        - string "arch_name"
        - string "summary"
        - string "description"
        - string "checksum_label"
        - dateTime.iso8601 "last_modified"
        - string "maintainer_name"
        - string "maintainer_email"
        - string "maintainer_phone"
        - string "support_policy"
        - string "gpg_key_url"
        - string "gpg_key_id"
        - string "gpg_key_fp"
        - dateTime.iso8601 "yumrepo_last_sync" - (optional)
        - string "end_of_life"
        - string "parent_channel_label"
        - string "clone_original"
        - array:
            - struct - contentSources
                - int "id"
                - string "label"
                - string "sourceUrl"
                - string "type"
    """
    try:
        result = sw.session.channel.software.disassociateRepo(
            sw.key,
            channellabel,
            repoLabel
        )
    except Exception as e:
        raise e

    return result


def getChannelLastBuildById(
    sw,
    channel_id
):
    """
    Description:
    Returns the last build date of the repomd.xml file for the given
    channel as a localised string.

    Parameters:
        - string sessionKey
        - int id - id of channel wanted

    Returns:

    the last build date of the repomd.xml file as a localised string
    """
    try:
        result = sw.session.channel.software.getChannelLastBuildById(
            sw.key,
            channel_id
        )
    except Exception as e:
        raise e

    return result


def getDetails(
    sw,
    chan
):
    """
    Description:
    Returns details of the given channel as a map

    Parameters:
        - string sessionKey
        - int id | string name - channel to query

    Returns:
        - struct - channel
            - int "id"
            - string "name"
            - string "label"
            - string "arch_name"
            - string "summary"
            - string "description"
            - string "checksum_label"
            - dateTime.iso8601 "last_modified"
            - string "maintainer_name"
            - string "maintainer_email"
            - string "maintainer_phone"
            - string "support_policy"
            - string "gpg_key_url"
            - string "gpg_key_id"
            - string "gpg_key_fp"
            - dateTime.iso8601 "yumrepo_last_sync" - (optional)
            - string "end_of_life"
            - string "parent_channel_label"
            - string "clone_original"
            - array:
                - struct - contentSources
                    - int "id"
                    - string "label"
                    - string "sourceUrl"
                    - string "type"
    """
    try:
        result = sw.session.channel.software.getDetails(
            sw.key,
            chan
        )
    except Exception as e:
        raise e

    return result


def getRepoDetails(
    sw,
    repolabel
):
    """
    Description:
    Returns details of the given repository

    Parameters:
        - string sessionKey
        - string repoLabel - repo to query

    Returns:
        - struct - channel
            - int "id"
            - string "label"
            - string "sourceUrl"
            - string "type"

    """
    try:
        result = sw.session.channel.software.getRepoDetails(
            sw.key,
            repolabel
        )
    except Exception as e:
        raise e

    return result


def getRepoSyncCronExpression(
    sw,
    channellabel
):
    """
    Description:
    Returns repo synchronization cron expression

    Parameters:

        - string sessionKey
        - string channelLabel - channel label

    Returns:
        - string quartz expression

    """
    try:
        result = sw.session.channel.software.getRepoSyncCronExpression(
            sw.key,
            channellabel
        )
    except Exception as e:
        raise e

    return result


def isGloballySubscribable(
    sw,
    channellabel
):
    """
    channel.software.isGloballySubscribable

    Description:
        Returns whether the channel is subscribable by any user in the
        organization

    Parameters:

        - string sessionKey
        - string channelLabel - channel to query

    Returns:
        - int - 1 if true, 0 otherwise
    """
    try:
        result = sw.session.channel.software.isGloballySubscribable(
            sw.key,
            channellabel
        )
    except Exception as e:
        raise e

    return result


def isUserManageable(
    sw,
    channellabel,
    login
):
    """
    Description:
    Returns whether the channel may be managed by the given user.

    Parameters:
        - string sessionKey
        - string channelLabel - label of the channel
        - string login - login of the target user

    Returns:
        - int - 1 if manageable, 0 if not
    """
    try:
        result = sw.session.channel.software.isUserManageable(
            sw.key,
            channellabel,
            login
        )
    except Exception as e:
        raise e

    return result


def isUserSubscribable(
    sw,
    channellabel,
    username
):
    """
    Description:
    Returns whether the channel may be subscribed to by the given user.

    Parameters:
        - string sessionKey
        - string channelLabel - label of the channel
        - string login - login of the target user

    Returns:
        - int - 1 if subscribable, 0 if not
    """
    try:
        result = sw.session.channel.software.isUserSubscribable(
            sw.key,
            channellabel,
            username
        )
    except Exception as e:
        raise e

    return result


def setGloballySubscribable(
    sw,
    channellabel
):
    """
    Description:
        - Set globally subscribable attribute for given channel.

    Parameters:
        - string sessionKey
        - string channelLabel - label of the channel
        - boolean subscribable - true if the channel is to be
                                globally subscribable. False otherwise.

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.channel.software.setGloballySubscribable(
            sw.key,
            channellabel
        )
    except Exception as e:
        raise e

    return result


def setUserManageable(
    sw,
    channellabel,
    login,
    action
):
    """
    Description:
    Set the manageable flag for a given channel and user.

    If value is set to 'true', this method will give the user
    manage permissions to the channel. Otherwise, that
    privilege is revoked.

    Parameters:
        - string sessionKey
        - string channelLabel - label of the channel
        - string login - login of the target user
        - boolean value - value of the flag to set

    Returns:
        int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.channel.software.setUserManageable(
            sw.key,
            channellabel,
            login,
            action
        )
    except Exception as e:
        raise e

    return result


def setUserSubscribable(
    sw,
    channellabel,
    username
):
    """
    Description:
    Set the subscribable flag for a given channel and user. If value is set to
    'true', this method will give the user subscribe permissions to the
    channel. Otherwise, that privilege is revoked.

    Parameters:
        - string sessionKey
        - string channelLabel - label of the channel
        - string login - login of the target user
        - boolean value - value of the flag to set

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.channel.software.setUserSubscribable(
            sw.key,
            channellabel,
            username
        )
    except Exception as e:
        raise e

    return result


def listAllPackages(
    sw,
    channellabel,
    start_date=None,
    end_date=None
):
    """
    Description:
    If start and end are giving:
        Lists all packages in the channel, regardless of package version,
        between the given dates.

    If start is given:
        Lists all packages in the channel, regardless of version
        whose last modified date is greater than given date.

    If only channelLabel is given:
        Lists all packages in the channel, regardless of the package version

    Parameters:
        - string sessionKey
        - string channelLabel - channel to query
        - dateTime.iso8601 startDate
        - dateTime.iso8601 endDate

    Returns:
        - array:
            - struct - package
                - string "name"
                - string "version"
                - string "release"
                - string "epoch"
                - string "checksum"
                - string "checksum_type"
                - int "id"
                - string "arch_label"
                - string "last_modified_date"
    """
    try:
        if start_date is None:
            result = sw.session.channel.software.listAllPackages(
                sw.key,
                channellabel
            )
        elif end_date is None:
            result = sw.session.channel.software.listAllPackages(
                sw.key,
                channellabel,
                start_date
            )
        else:
            result = sw.session.channel.software.listAllPackages(
                sw.key,
                channellabel,
                start_date,
                end_date
            )
    except Exception as e:
        raise e

    return result


def listArches(
    sw
):
    """
    Description:
    Lists the potential software channel architectures that can be created

    Parameters:
        - string sessionKey

    Returns:
        - array:
            - struct - channel arch
            - string "name"
            - string "label"
    """
    try:
        result = sw.session.channel.software.listArches(
            sw.key
        )
    except Exception as e:
        raise e

    return result


def listChannelRepos(
    sw,
    channellabel
):
    """
    Description:
    Lists associated repos with the given channel

    Parameters:
        - string sessionKey
        - string channelLabel - channel label

    Returns:
        - array:
            - struct - channel
                - int "id"
                - string "label"
                - string "sourceUrl"
                - string "type"
   """
    try:
        result = sw.session.channel.software.listChannelRepos(
            sw.key,
            channellabel
        )
    except Exception as e:
        raise e

    return result


def listChildren(
    sw,
    channellabel
):
    """
    Description:
    List the children of a channel

    Parameters:
    string sessionKey
    string channelLabel - the label of the channel

    Returns:
        array:
            - struct - channel
                - int "id"
                - string "name"
                - string "label"
                - string "arch_name"
                - string "summary"
                - string "description"
                - string "checksum_label"
                - dateTime.iso8601 "last_modified"
                - string "maintainer_name"
                - string "maintainer_email"
                - string "maintainer_phone"
                - string "support_policy"
                - string "gpg_key_url"
                - string "gpg_key_id"
                - string "gpg_key_fp"
                - dateTime.iso8601 "yumrepo_last_sync" - (optional)
                - string "end_of_life"
                - string "parent_channel_label"
                - string "clone_original"
                - array:
                    - struct - contentSources
                        - int "id"
                        - string "label"
                        - string "sourceUrl"
                        - string "type"
    """
    try:
        result = sw.session.channel.software.listChildren(
            sw.key,
            channellabel
        )
    except Exception as e:
        raise e

    return result


def listErrata(
    sw,
    channellabel,
    start_date=None,
    end_date=None
):
    """
    Description:
    List the errata applicable to a channel between startDate and endDate.

    If start and end are giving:
        List the errata applicable to a channel between startDate and endDate.

    If start is given:
        List the errata applicable to a channel after given startDate

    If only channelLabel is given:
        List the errata applicable to a channel

    Parameters:
        - string sessionKey
        - string channelLabel - channel to query
        - dateTime.iso8601 startDate
        - dateTime.iso8601 endDate

    Returns:
        - array:
            - struct - errata
                - int "id" - Errata ID.
                - string "date" - Date erratum was created.
                - string "update_date" - Date erratum was updated.
                - string "advisory_synopsis" - Summary of the erratum.
                - string "advisory_type" - Type label such as Security,
                                          Bug Fix
                - string "advisory_name" - Name such as RHSA, etc
    """
    try:
        if start_date is None:
            result = sw.session.channel.software.listErrata(
                sw.key,
                channellabel
            )
        elif end_date is None:
            result = sw.session.channel.software.listErrata(
                sw.key,
                channellabel,
                start_date
            )
        else:
            result = sw.session.channel.software.listErrata(
                sw.key,
                channellabel,
                start_date,
                end_date
            )
    except Exception as e:
        raise e

    return result


def listErrataByType(
    sw,
    channellabel,
    errtype
):
    """
    Description:
    List the errata of a specific type that are applicable to a channel

    Parameters:
        - string sessionKey
        - string channelLabel - channel to query
        - string advisoryType - type of advisory (one of of the following:
                                'Security Advisory',
                                'Product Enhancement Advisory',
                                'Bug Fix Advisory'

    Returns:
        - array:
            - struct - errata
                - string "advisory" - name of the advisory
                - string "issue_date" - date format follows
                                        YYYY-MM-DD HH24:MI:SS
                - string "update_date" - date format follows
                                        YYYY-MM-DD HH24:MI:SS
                - string "synopsis"
                - string "advisory_type"
                - string "last_modified_date" - date format follows
                                                YYYY-MM-DD HH24:MI:SS
    """
    try:
        result = sw.session.channel.software.listErrataByType(
            sw.key,
            channellabel,
            errtype
        )
    except Exception as e:
        raise e

    return result


def listLatestPackages(
    sw,
    channellabel
):
    """
    Description:
    Lists the packages with the latest version (including release and epoch)
    for the given channel

    Parameters:
        - string sessionKey
        - string channelLabel - channel to query

    Returns:
        - array:
            - struct - package
                - string "name"
                - string "version"
                - string "release"
                - string "epoch"
                - int "id"
                - string "arch_label"
    """
    try:
        result = sw.session.channel.software.listLatestPackages(
            sw.key,
            channellabel
        )
    except Exception as e:
        raise e

    return result


def listPackagesWithoutChannel(sw):
    """
    Description:
    Lists all packages that are not associated with a channel. Typically
    these are custom packages.

    Parameters:
        - string sessionKey

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
                                        determined by the gpg key it was
                                        signed with.
                - dateTime.iso8601 "last_modified"
    """
    try:
        result = sw.session.channel.software.listPackagesWithoutChannel(
            sw.key)
    except Exception as e:
        raise e

    return result


def listRepoFilters(
    sw,
    repolabel
):
    """
    Description:
    Lists the filters for a repo

    Parameters:
        - string sessionKey
        - string label - repository label

    Returns:
        - array:
            - struct - filter
                - int "sortOrder"
                - string "filter"
                - string "flag"
    """
    try:
        result = sw.session.channel.software.listRepoFilters(
            sw.key,
            repolabel
        )
    except Exception as e:
        raise e

    return result


def listSubscribedSystems(
    sw,
    channellabel
):
    """
    Description:
    Returns list of subscribed systems for the given channel label

    Parameters:
        - string sessionKey
        - string channelLabel - channel to query

    Returns:
        - array:
            - struct - system
                - int "id"
                - string "name"
    """
    try:
        result = sw.session.channel.software.listSubscribedSystems(
            sw.key,
            channellabel
        )
    except Exception as e:
        raise e

    return result


def listSystemChannels(
    sw,
    systemid
):
    """
    Description:
    Returns a list of channels that a system is subscribed to for
    the given system id

    Parameters:
        - string sessionKey
        - int serverId

    Returns:
        - array:
            - struct - channel
                - string "label"
                - string "name"
    """
    try:
        result = sw.session.channel.software.listSystemChannels(
            sw.key,
            systemid
        )
    except Exception as e:
        raise e

    return result


def setSystemChannels(
    sw,
    systemid,
    chanlist
):
    """
    Description:
    Returns a list of ContentSource (repos) that the
    user can see

    Parameters:
        - string sessionKey

    Returns:
        - array:
            - struct - map
                - long "id" - ID of the repo
                - string "label" - label of the repo
                - string "sourceUrl" - URL of the repo
    """
    try:
        result = sw.session.channel.software.setSystemChannels(
            sw.key,
            systemid,
            chanlist
        )
    except Exception as e:
        raise e

    return result


def listUserRepos(
    sw
):
    """
    Description:
    Returns a list of ContentSource (repos) that the user can see

    Parameters:
    string sessionKey

    Returns:
        - array:
            - struct - map
                - long "id" - ID of the repo
                - string "label" - label of the repo
                - string "sourceUrl" - URL of the repo
    """
    try:
        result = sw.session.channel.software.listUserRepos(
            sw.key
        )
    except Exception as e:
        raise e

    return result


def mergeErrata(
    sw,
    sourcechan,
    destchan,
    start_date=None,
    end_date=None
):
    """
    Description:
    Merges all errata from one channel into another

    Parameters:
        - string sessionKey
        - string mergeFromLabel - the label of the channel to pull errata from
        - string mergeToLabel - the label to push the errata into
        - string startDate (Not Required)
        - string endDate   (Not Required)

    Returns:
        - array:
            - struct - errata
            - int "id" - Errata Id
            - string "date" - Date erratum was created.
            - string "advisory_type" - Type of the advisory.
            - string "advisory_name" - Name of the advisory.
            - string "advisory_synopsis" - Summary of the erratum.
    """
    if end_date is None:
        end_date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

    if start_date is None:

        start_date = time.strftime(
            '%Y-%m-%d %H:%M:%S',
            (1980, 1, 1, 0, 0, 0, 0, 0, 0)
        )

    try:
        result = sw.session.channel.software.mergeErrata(
            sw.key,
            sourcechan,
            destchan,
            start_date,
            end_date
        )
    except Exception as e:
        raise e

    return result


def mergePackages(
    sw,
    sourcechan,
    destchan
):
    """
    Description:
    Merges all packages from one channel into another

    Parameters:
        - string sessionKey
        - string mergeFromLabel - the label of the channel to pull
                                    packages from
        - string mergeToLabel - the label to push the packages into

    Returns:
        - array:
            - struct - package
                - string "name"
                - string "version"
                - string "release"
                - string "epoch"
                - int "id"
                - string "arch_label"
                - string "path" - The path on that file system that
                                the package resides
                - string "provider" - The provider of the package, determined
                                      by the gpg key it was signed with.
                - dateTime.iso8601 "last_modified"
    """
    try:
        result = sw.session.channel.software.mergePackages(
            sw.key,
            sourcechan,
            destchan
        )
    except Exception as e:
        raise e

    return result


def regenerateNeededCache(
    sw,
    channellabel=None
):
    """
    Description:
    Completely clear and regenerate the needed Errata and Package cache
    or all systems subscribed to the specified channel. This should be
    used only if you believe your cache is incorrect for all the systems
    in a given channel.

    Parameters:
        - string sessionKey
        - string channelLabel - the label of the channel

    Returns:

        - int - 1 on success, exception thrown otherwise.
    """
    try:
        if channellabel is not None:
            result = sw.session.channel.software.regenerateNeededCache(
                sw.key,
                channellabel
            )
        else:
            result = sw.session.channel.software.regenerateNeededCache(
                sw.key
            )
    except Exception as e:
        raise e

    return result


def regenerateYumCache(
    sw,
    channellabel
):
    """
    Description:
    Regenerate yum cache for the specified channel.

    Parameters:
        - string sessionKey
        - string channelLabel - the label of the channel

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.channel.software.regenerateYumCache(
            sw.key,
            channellabel
        )
    except Exception as e:
        raise e

    return result


def removePackages(
    sw,
    channellabel,
    package_ids
):
    """
    Description:
    Removes a given list of packages from the given channel.

    Parameters:
        - string sessionKey
        - string channelLabel - target channel.
        - array:
            - int - packageId - id of a package to remove from the channel.

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.channel.software.removePackages(
            sw.key,
            channellabel,
            package_ids
        )
    except Exception as e:
        raise e

    return result


def removeRepo(
    sw,
    repository
):
    """
    Description:
    Removes a repository

    Parameters:
        - string sessionKey
        - long id - ID of repo to be removed or repo label (string)

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.channel.software.removeRepo(
            sw.key,
            repository
        )
    except Exception as e:
        raise e

    return result


def setContactDetails(
    sw,
    channellabel,
    name,
    email,
    phone,
    policy
):
    """
    Description:
    Set contact/support information for given channel.

    Parameters:
        - string sessionKey
        - string channelLabel - label of the channel
        - string maintainerName - name of the channel maintainer
        - string maintainerEmail - email of the channel maintainer
        - string maintainerPhone - phone number of the channel maintainer
        - string supportPolicy - channel support policy

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.channel.software.setContactDetails(
            sw.key,
            channellabel,
            name,
            email,
            phone,
            policy
        )
    except Exception as e:
        raise e

    return result


def setDetails(
    sw,
    channel_id,
    channel_map
):
    """
    Description:
    Allows to modify channel attributes

    Parameters:
        - string sessionKey
        - int channelDd - channel id
        - struct - channel_map
            - string "checksum_label" - new channel repository checksum label
                                        (optional)
            - string "name" - new channel name (optional)
            - string "summary" - new channel summary (optional)
            - string "description" - new channel description (optional)
            - string "maintainer_name" - new channel maintainer name (optional)
            - string "maintainer_email" - new channel email address (optional)
            - string "maintainer_phone" - new channel phone number (optional)
            - string "gpg_key_url" - new channel gpg key url (optional)
            - string "gpg_key_id" - new channel gpg key id (optional)
            - string "gpg_key_fp" - new channel gpg key fingerprint (optional)

    Returns:
        - int - 1 on success, exception thrown otherwise.

    """
    try:
        result = sw.session.channel.software.setDetails(
            sw.key,
            channel_id,
            channel_map
        )
    except Exception as e:
        raise e

    return result

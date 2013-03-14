"""
``Namespace: system``
======================

Provides methods to access and modify registered system.

- :func:`addEntitlements`
- :func:`addNote`
- :func:`comparePackageProfile`
- :func:`comparePackages`
- :func:`convertToFlexEntitlement`
- :func:`createPackageProfile`
- :func:`createSystemRecord`
- :func:`deleteCustomValues`
- :func:`deleteGuestProfiles`
- :func:`deleteNote`
- :func:`deleteNotes`
- :func:`deletePackageProfile`
- :func:`deleteSystem`
- :func:`deleteSystems`
- :func:`deleteTagFromSnapshot`
- :func:`downloadSystemId`
- :func:`getConnectionPath`
- :func:`getCpu`
- :func:`getCustomValues`
- :func:`getDetails`
- :func:`getDevices`
- :func:`getDmi`
- :func:`getEntitlements`
- :func:`getEventHistory`
- :func:`getId`
- :func:`getMemory`
- :func:`getName`
- :func:`getNetwork`
- :func:`getNetworkDevices`
- :func:`getRegistrationDate`
- :func:`getRelevantErrata`
- :func:`getRelevantErrataByType`
- :func:`getRunningKernel`
- :func:`getScriptActionDetails`
- :func:`getScriptResults`
- :func:`getSubscribedBaseChannel`
- :func:`getSystemCurrencyMultipliers`
- :func:`getSystemCurrencyScores`
- :func:`getUnscheduledErrata`
- :func:`getUuid`
- :func:`getVariables`
- :func:`isNvreInstalled`
- :func:`listActivationKeys`
- :func:`listActiveSystems`
- :func:`listActiveSystemsDetails`
- :func:`listAdministrators`
- :func:`listBaseChannels`
- :func:`listChildChannels`
- :func:`listDuplicatesByHostname`
- :func:`listDuplicatesByIp`
- :func:`listDuplicatesByMac`
- :func:`listEligibleFlexGuests`
- :func:`listExtraPackages`
- :func:`listFlexGuests`
- :func:`listGroups`
- :func:`listInactiveSystems`
- :func:`listLatestAvailablePackage`
- :func:`listLatestInstallablePackages`
- :func:`listLatestUpgradablePackages`
- :func:`listNewerInstalledPackages`
- :func:`listNotes`
- :func:`listOlderInstalledPackages`
- :func:`listOutOfDateSystems`
- :func:`listPackageProfiles`
- :func:`listPackages`
- :func:`listPackagesFromChannel`
- :func:`listSubscribableBaseChannels`
- :func:`listSubscribableChildChannels`
- :func:`listSubscribedChildChannels`
- :func:`listSystemEvents`
- :func:`listSystems`
- :func:`listSystemsWithExtraPackages`
- :func:`listSystemsWithPackage`
- :func:`listUngroupedSystems`
- :func:`listUserSystems`
- :func:`listVirtualGuests`
- :func:`listVirtualHosts`
- :func:`obtainReactivationKey`
- :func:`provisionSystem`
- :func:`provisionVirtualGuest`
- :func:`removeEntitlements`
- :func:`scheduleApplyErrata`
- :func:`scheduleGuestAction`
- :func:`scheduleHardwareRefresh`
- :func:`schedulePackageInstall`
- :func:`schedulePackageRefresh`
- :func:`schedulePackageRemove`
- :func:`scheduleReboot`
- :func:`scheduleScriptRun`
- :func:`scheduleSyncPackagesWithSystem`
- :func:`searchByName`
- :func:`setBaseChannel`
- :func:`setChildChannels`
- :func:`setCustomValues`
- :func:`setDetails`
- :func:`setGroupMembership`
- :func:`setGuestCpus`
- :func:`setGuestMemory`
- :func:`setLockStatus`
- :func:`setProfileName`
- :func:`setVariables`
- :func:`tagLatestSnapshot`
- :func:`upgradeEntitlement`
- :func:`whoRegistered`
"""


def addEntitlements(
    sw,
    server_id,
    entitlement_label
):
    """
    Description:
    Add addon entitlements to a server. Entitlements a server already has are
    quietly ignored.

    Parameters:
        - session object
        - int serverId
        - array:
            - string - entitlement_label

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.system.addEntitlements(
            sw.key,
            server_id,
            entitlement_label
        )
    except Exception as e:
        raise e

    return result


def addNote(
    sw,
    server_id,
    subject,
    body
):
    """
    Description:
    Add a new note to the given server.

    Parameters:
        - session object
        - int server_id
        - string subject - What the note is about.
        - string body - Content of the note.

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.system.addNote(
            sw.key,
            server_id,
            subject,
            body
        )
    except Exception as e:
        raise e

    return result


def comparePackageProfile(
    sw,
    server_id,
    profile_label
):
    """
    Description:
    Compare a system's packages against a package profile. In the result
    returned, 'this_system' represents the server provided as an input and
    'other_system' represents the profile provided as an input.

    Parameters:
        - session object
        - int server_id
        - string profile_label

    Returns:
        - array:
            - struct - Package Metadata
                - int "package_name_id"
                - string "package_name"
                - string "package_arch"
                - string "this_system" - Version of package on this system.
                - string "other_system" - Version of package on the other
                                        system.
                - int "comparison"
                    - 0 - No difference.
                    - 1 - Package on this system only.
                    - 2 - Newer package version on this system.
                    - 3 - Package on other system only.
                    - 4 - Newer package version on other system.
    """
    try:
        result = sw.session.system.comparePackageProfile(
            sw.key,
            server_id,
            profile_label
        )
    except Exception as e:
        raise e

    return result


def comparePackages(
    sw,
    this_server_id,
    other_server_id
):
    """
    Description:
    Compares the packages installed on two systems.

    Parameters:
        - session object
        - int this_server_id
        - int other_server_id

    Returns:
        - array:
            - struct - Package Metadata
                - int "package_name_id"
                - string "package_name"
                - string "package_arch"
                - string "this_system" - Version of package on this system.
                - string "other_system" - Version of package on the other
                                          system.
                - int "comparison"
                    - 0 - No difference.
                    - 1 - Package on this system only.
                    - 2 - Newer package version on this system.
                    - 3 - Package on other system only.
                    - 4 - Newer package version on other system.
    """
    try:
        result = sw.session.system.comparePackages(
            sw.key,
            this_server_id,
            other_server_id
        )
    except Exception as e:
        raise e

    return result


def convertToFlexEntitlement(
    sw,
    server_id,
    channel_family_label
):
    """
    Description:
    Converts the given list of systems for a given channel family to use the
    flex entitlement.

    Parameters:
        - object session
            - array:
                - int - serverId
            - string channel_family_label

    Returns:
        - int - the total the number of systems that were converted to use
                flex entitlement
    """
    try:
        result = sw.session.system.convertToFlexEntitlement(
            sw.key,
            server_id,
            channel_family_label
        )
    except Exception as e:
        raise e

    return result


def createPackageProfile(
    sw,
    server_id,
    profile_label,
    description
):
    """
    Description:
    Create a new stored Package Profile from a systems installed package list.

    Parameters:
        - object session
        - int server_id
        - string profile_label
        - string description

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.system.createPackageProfile(
            sw.key,
            server_id,
            profile_label,
            description
        )
    except Exception as e:
        raise e

    return result


def createSystemRecord(
    sw,
    server_id,
    kslabel
):
    """
    Description:
    Creates a cobbler system record with the specified kickstart label

    Parameters:
        - object session
        - int server_id
        - string kslabel

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.system.createSystemRecord(
            sw.key,
            server_id,
            kslabel
        )
    except Exception as e:
        raise e

    return result


def deleteCustomValues(
    sw,
    server_id,
    custominfolabel
):
    """
    Description:
    Delete the custom values defined for the custom system information keys
    provided from the given system.

    Parameters:
        - object session
        - int server_id
        - array:
            - string - custominfolabel

    Returns:
    int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.system.deleteCustomValues(
            sw.key,
            server_id,
            custominfolabel
        )
    except Exception as e:
        raise e

    return result


def deleteGuestProfiles(
    sw,
    hostid,
    guestnames
):
    """
    Description:
    Delete the specified list of guest profiles for a given host

    Parameters:
        - object session
        - int hostid
        - array:
            - string - guestnames

    Returns:
    int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.system.deleteGuestProfiles(
            sw.key,
            hostid,
            guestnames
        )
    except Exception as e:
        raise e

    return result


def deleteNote(
    sw,
    server_id,
    note_id
):
    """
    Description:
    Deletes the given note from the server.

    Parameters:
        - object session
        - int server_id
        - int note_id

    Returns:
    int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.system.deleteNote(
            sw.key,
            server_id,
            note_id
        )
    except Exception as e:
        raise e

    return result


def deleteNotes(
    sw,
    server_id
):
    """
    Description:
    Deletes all notes from the server.

    Parameters:
        - object session
        - int server_id

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.system.deleteNotes(
            sw.key,
            server_id
        )
    except Exception as e:
        raise e

    return result


def deletePackageProfile(
    sw,
    profile_id
):
    """
    Description:
    Delete a package profile

    Parameters:
        - object session
        - int profile_id

    Returns:
    int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.system.deletePackageProfile(
            sw.key,
            profile_id
        )
    except Exception as e:
        raise e

    return result


def deleteSystem(
    sw,
    system_id
):
    """
    Description:
    Delete a system given its cilent certificate.

    Parameters:
        - object session
        - string system_id - systemid file

    Returns:
        - int - 1 on success, exception thrown otherwise.

    Available since: 10.10
    """
    try:
        result = sw.session.system.deleteSystem(
            sw.key,
            system_id
        )
    except Exception as e:
        raise e

    return result


def deleteSystems(
    sw,
    server_ids
):
    """
    Description:
    Delete systems given a list of system ids.

    Parameters:
        - object session
        - array:
            - int - serverId

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.system.deleteSystems(
            sw.key,
            server_ids
        )
    except Exception as e:
        raise e

    return result


def deleteTagFromSnapshot(
    sw,
    server_id,
    tagname
):
    """
    Description:
    Deletes tag from system snapshot

    Parameters:
        - object session
        - int server_id
        - string tagname

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.system.deleteTagFromSnapshot(
            sw.key,
            server_id,
            tagname
        )
    except Exception as e:
        raise e

    return result


def downloadSystemId(
    sw,
    server_id
):
    """
    Description:
    Get the system ID file for a given server.

    Parameters:
        - object session
        - int server_id

    Returns:
        - string systemID
    """
    try:
        result = sw.session.system.downloadSystemId(
            sw.key,
            server_id
        )
    except Exception as e:
        raise e

    return result


def getConnectionPath(
    sw,
    server_id
):
    """
    Description:
    Get the list of proxies that the given system connects through in
    order to reach the server.

    Parameters:
        - object session
        - int server_id

    Returns:
        - array:
            - struct - proxy connection path details
                - int "position" - Position of proxy in chain.The proxy that
                                   the system connects directly to is listed
                                   in position 1.
                - int "id" - Proxy system id
                - string "hostname" - Proxy host name
    """
    try:
        result = sw.session.system.getConnectionPath(
            sw.key,
            server_id
        )
    except Exception as e:
        raise e

    return result


def getCpu(
    sw,
    server_id
):
    """
    Description:
    Gets the CPU information of a system.

    Parameters:
        - object session
        - int server_id

    Returns:
        - struct - CPU
            - string "cache"
            - string "family"
            - string "mhz"
            - string "flags"
            - string "model"
            - string "vendor"
            - string "arch"
            - string "stepping"
            - string "count"
    """
    try:
        result = sw.session.system.getCpu(
            sw.key,
            server_id
        )
    except Exception as e:
        raise e

    return result


def getCustomValues(
    sw,
    server_id
):
    """
    Description:
    Get the custom data values defined for the server.

    Parameters:
        - object session
        - int server_id

    Returns:
        - struct - custom value
            - string "custom info label"
    """
    try:
        result = sw.session.system.getCustomValues(
            sw.key,
            server_id
        )
    except Exception as e:
        raise e

    return result


def getDetails(
    sw,
    server_id
):
    """
    Description:
    Get system details.

    Parameters:
        - object session
        - int server_id

    Returns:
        - struct - server details
            - int "id" - System id
            - string "profile_name"
            - string "base_entitlement" - System's base entitlement label.
                                        (enterprise_entitled or sw_mgr_entitled
            - array "string"
                - addon_entitlements System's addon entitlements labels,
                  including:
                  - monitoring_entitled
                  - provisioning_entitled
                  - virtualization_host
                  - virtualization_host_platform
            - boolean "auto_update" - True if system has auto errata updates
                                      enabled.
            - string "release" - The Operating System release
                                (i.e. 4AS, 5Server)
            - string "address1"
            - string "address2"
            - string "city"
            - string "state"
            - string "country"
            - string "building"
            - string "room"
            - string "rack"
            - string "description"
            - string "hostname"
            - dateTime.iso8601 "last_boot"
            - string "osa_status" - Either 'unknown', 'offline', or 'online'.
            - boolean "lock_status" - True indicates that the system is locked.
                                    False indicates that the system is unlocked
    """
    try:
        result = sw.session.system.getDetails(
            sw.key,
            server_id
        )
    except Exception as e:
        raise e

    return result


def getDevices(
    sw,
    server_id
):
    """
    Description:
    Gets a list of devices for a system.

    Parameters:
        - object session
        - int server_id

    Returns:
        - array:
            - struct - device
                - string "device" - optional
                - string "device_class" - Includes CDROM, FIREWIRE, HD, USB,
                                           VIDEO, OTHER, etc.
                - string "driver"
                - string "description"
                - string "bus"
                - string "pcitype"
    """
    try:
        result = sw.session.system.getDevices(
            sw.key,
            server_id
        )
    except Exception as e:
        raise e

    return result


def getDmi(
    sw,
    server_id
):
    """
    Description:
    Gets the DMI information of a system.

    Parameters:
        - object session
        - int server_id

    Returns:
        - struct - DMI
            - string "vendor"
            - string "system"
            - string "product"
            - string "asset"
            - string "board"
            - string "bios_release" - (optional)
            - string "bios_vendor" - (optional)
            - string "bios_version" - (optional)
    """
    try:
        result = sw.session.system.getDmi(
            sw.key,
            server_id
        )
    except Exception as e:
        raise e

    return result


def getEntitlements(
    sw,
    server_id
):
    """
    Description:
    Gets the entitlements for a given server.

    Parameters:
        - object session
        - int server_id

    Returns:
        - array:
            - string - entitlement_label
    """
    try:
        result = sw.session.system.getEntitlements(
            sw.key,
            server_id
        )
    except Exception as e:
        raise e

    return result


def getEventHistory(
    sw,
    server_id
):
    """
    Description:
    Returns a list history items associated with the system, ordered from
    newest to oldest. Note that the details may be empty for events that were
    scheduled against the system (as compared to instant). For more
    information on such events, see the system.listSystemEvents operation.

    Parameters:
        - object session
        - int server_id

    Returns:
        - array:
            - struct - History Event
                - dateTime.iso8601 "completed" - Date that the event occurred
                  (optional)
                - string "summary" - Summary of the event
                - string "details" - Details of the event
    """
    try:
        result = sw.session.system.getEventHistory(
            sw.key,
            server_id
        )
    except Exception as e:
        raise e

    return result


def getId(
    sw,
    servername
):
    """
    Description:
    Get system IDs and last check in information for the given system name.

    Parameters:

        - sw session
        - string systemName

    Returns:

        - array:
            - struct - system
                - int "id"
                - string "name"
                - dateTime.iso8601 "last_checkin" - Last time server
                                                    successfully checked in
    """
    try:
        result = sw.session.system.getId(
            sw.key,
            servername
        )
    except Exception as e:
        raise e
    return result


def getMemory(
    sw,
    server_id
):
    """
    Description:
    Gets the memory information for a system.

    Parameters:
        - object session
        - int server_id

    Returns:
        - struct - memory
            - int "ram" - The amount of physical memory in MB.
            - int "swap" - The amount of swap space in MB.
    """
    try:
        result = sw.session.system.getMemory(
            sw.key,
            server_id
        )
    except Exception as e:
        raise e

    return result


def getName(
    sw,
    server_id
):
    """
    Description:
    Get system name and last check in information for the given system ID.

    Parameters:
        - object session
        - string server_id *(should this be int? docs say string...)

    Returns:
        - struct - name info
            - int "id" - Server id
            - string "name" - Server name
            - dateTime.iso8601 "last_checkin" - Last time server successfully
                                                checked in
    """
    try:
        result = sw.session.system.getName(
            sw.key,
            server_id
        )
    except Exception as e:
        raise e

    return result


def getNetwork(
    sw,
    server_id
):
    """
    Description:
    Get the addresses and hostname for a given server.

    Parameters:
        - object session
        - int server_id

    Returns:
        - struct - network info
            - string "ip" - IPv4 address of server
            - string "ip6" - IPv6 address of server
            - string "hostname" - Hostname of server
    """
    try:
        result = sw.session.system.getNetwork(
            sw.key,
            server_id
        )
    except Exception as e:
        raise e

    return result


def getNetworkDevices(
    sw,
    server_id
):
    """
    Description:
    Returns the network devices for the given server.

    Parameters:
        - object session
        - int server_id

    Returns:
        - array:
            - struct - network device
                - string "ip" - IP address assigned to this network device
                - string "interface" - Network interface assigned to device
                                      e.g. eth0
                - string "netmask" - Network mask assigned to device
                - string "hardware_address" - Hardware Address of device.
                - string "module" - Network driver used for this device.
                - string "broadcast" - Broadcast address for device.
                - array "ipv6" - List of IPv6 addresses
                - array:
                    - struct - ipv6 address
                        - string "address" - IPv6 address of this network dev
                        - string "netmask" - IPv6 netmask of this network dev
                        - string "scope" - IPv6 address scope
    """
    try:
        result = sw.session.system.getNetworkDevices(
            sw.key,
            server_id
        )
    except Exception as e:
        raise e

    return result


def getRegistrationDate(
    sw,
    server_id
):
    """
    Description:
    Returns the date the system was registered.

    Parameters:
        - object session
        - int server_id

    Returns:
        - dateTime.iso8601 - The date the system was registered, in local time.
    """
    try:
        result = sw.session.system.getRegistrationDate(
            sw.key,
            server_id
        )
    except Exception as e:
        raise e

    return result


def getRelevantErrata(
    sw,
    server_id
):
    """
    Description:
    Returns a list of all errata that are relevant to the system.

    Parameters:
        - object session
        - int server_id

    Returns:
        - array:
            - struct - errata
                - int "id" - Errata ID.
                - string "date" - Date erratum was created.
                - string "update_date" - Date erratum was updated.
                - string "advisory_synopsis" - Summary of the erratum.
                - string "advisory_type" - Type label such as Security, Bug Fix
                - string "advisory_name" - Name such as RHSA, etc
    """
    try:
        result = sw.session.system.getRelevantErrata(
            sw.key,
            server_id
        )
    except Exception as e:
        raise e

    return result


def getRelevantErrataByType(
    sw,
    server_id,
    advisory_type
):
    """
    Description:
    Returns a list of all errata of the specified type that are relevant to
    the system.

    Parameters:
        - object session
        - int server_id
        - string advisory_type - type of advisory (one of of the following:
                                'Security Advisory',
                                'Product Enhancement Advisory',
                                'Bug Fix Advisory'

    Returns:
        - array:
            - struct - errata
                - int "id" - Errata ID.
                - string "date" - Date erratum was created.
                - string "update_date" - Date erratum was updated.
    ;
    string "advisory_synopsis" - Summary of the erratum.
    string "advisory_type" - Type label such as Security, Bug Fix
    string "advisory_name" - Name such as RHSA, etc
    """
    try:
        result = sw.session.system.getRelevantErrataByType(
            sw.key,
            server_id,
            advisory_type
        )
    except Exception as e:
        raise e

    return result


def getRunningKernel(
    sw,
    server_id
):
    """
    Description:
    Returns the running kernel of the given system.

    Parameters:
        - object session
        - int server_id

    Returns:
    string
    """
    try:
        result = sw.session.system.getRunningKernel(
            sw.key,
            server_id
        )
    except Exception as e:
        raise e

    return result


def getScriptActionDetails(
    sw,
    action_id
):
    """
    Description:
    Returns script details for script run actions

    Parameters:

        - session object
        - int actionId - ID of the script run action.

    Returns:

        - struct - Script details
            - int "id" - action id
            - string "content" - script content
            - string "run_as_user" - Run as user
            - string "run_as_group" - Run as group
            - int "timeout" - Timeout in seconds
            - array:
                - struct - script result
                    - int "serverId" - ID of the server the script runs on.
                    - dateTime.iso8601 "startDate" - Time script began
                                                     execution.
                    - dateTime.iso8601 "stopDate" - Time script stopped
                                                    execution.
                    - int "returnCode" - Script execution return code.
                    - string "output" - Output of the script
                - result

    """
    try:
        result = sw.session.system.getScriptActionDetails(
            sw.key,
            action_id
        )
    except Exception as e:
        raise e

    return result


def getScriptResults(
    sw,
    action_id
):
    """
    Description:
    Fetch results from a script execution. Returns an empty array if no
    results are yet available.

    Parameters:

        - session object
        - int actionId - ID of the script run action.

    Returns:

        - array:
            - struct - script result
                - int "serverId" - ID of the server the script runs on.
                - dateTime.iso8601 "startDate" - Time script began execution.
                - dateTime.iso8601 "stopDate" - Time script stopped execution.
                - int "returnCode" - Script execution return code.
                - string "output" - Output of the script

    """
    try:
        result = sw.session.system.getScriptResults(
            sw.key,
            action_id
        )
    except Exception as e:
        raise e

    return result


def getSubscribedBaseChannel(
    sw,
    server_id
):
    """
    Description:
    Provides the base channel of a given system

    Parameters:
        - object session
        - int server_id

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
        result = sw.session.system.getSubscribedBaseChannel(
            sw.key,
            server_id
        )
    except Exception as e:
        raise e

    return result


def getSystemCurrencyMultipliers(
    sw
):
    """
    Description:
    Get the System Currency score multipliers

    Parameters:
        - object session

    Returns:
        - Map of score multipliers
    """
    try:
        result = sw.session.system.getSystemCurrencyMultipliers(
            sw.key
        )
    except Exception as e:
        raise e

    return result


def getSystemCurrencyScores(
    sw
):
    """
    Description:
    Get the System Currency scores for all servers the user has access to

    Parameters:
        - object session

    Returns:
        - array:
            - struct - system currency
                - int "sid"
                - int "critical security errata count"
                - int "important security errata count"
                - int "moderate security errata count"
                - int "low security errata count"
                - int "bug fix errata count"
                - int "enhancement errata count"
                - int "system currency score"
    """
    try:
        result = sw.session.system.getSystemCurrencyScores(
            sw.key
        )
    except Exception as e:
        raise e

    return result


def getUnscheduledErrata(
    sw,
    server_id
):
    """
    Description:
    Provides an array of errata that are applicable to a given system.

    Parameters:
        - object session
        - int server_id

    Returns:
        - array:
            - struct - errata
                - int "id" - Errata Id
                - string "date" - Date erratum was created.
                - string "advisory_type" - Type of the advisory.
                - string "advisory_name" - Name of the advisory.
                - string "advisory_synopsis" - Summary of the erratum.

    """
    try:
        result = sw.session.system.getUnscheduledErrata(
            sw.key,
            server_id
        )
    except Exception as e:
        raise e

    return result


def getUuid(
    sw,
    server_id
):
    """
    Description:
    Get the UUID from the given system ID.

    Parameters:
        - object session
        - int serverId

    Returns:
        - string
    """
    try:
        result = sw.session.system.getUuid(
            sw.key,
            server_id
        )
    except Exception as e:
        raise e

    return result


def getVariables(
    sw,
    server_id
):
    """
    Description:
    Lists kickstart variables set in the system record for the specified
    server. Note: This call assumes that a system record exists in cobbler for
    the given system and will raise an XMLRPC fault if that is not the case. To
    create a system record over xmlrpc use system.createSystemRecord To create
    a system record in the Web UI please go to System -> <Specified System> ->
    Provisioning -> Select a Kickstart profile -> Create Cobbler System Record.

    Parameters:
        - object session
        - int server_id

    Returns:
        - struct - System kickstart variables
            - boolean "netboot" - netboot enabled
            - array "kickstart variables"
                - struct - kickstart variable
                    - string "key"
                    - string or int "value"
    """
    try:
        result = sw.session.system.getVariables(
            sw.key,
            server_id
        )
    except Exception as e:
        raise e

    return result


def isNvreInstalled(
    sw,
    server_id,
    name,
    version,
    release,
    epoch=None
):
    """
    Description:
    Check if the package with the given NVRE is installed on given system.

    Parameters:
        - object session
        - int server_id
        - string name - Package name.
        - string version - Package version.
        - string release - Package release.
        - string epoch - Package epoch. (optional)

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        if epoch:
            result = sw.session.system.isNvreInstalled(
                sw.key,
                server_id,
                name,
                version,
                release,
                epoch
            )
        else:
            result = sw.session.system.isNvreInstalled(
                sw.key,
                server_id,
                name,
                version,
                release
            )
    except Exception as e:
        raise e

    return result


def listActivationKeys(
    sw,
    server_id
):
    """
    Description:
    List the activation keys the system was registered with. An empty list will
    be returned if an activation key was not used during registration.

    Parameters:
        - object session
        - int server_id

    Returns:
        - array:
            - string - key
    """
    try:
        result = sw.session.system.listActivationKeys(
            sw.key,
            server_id
        )
    except Exception as e:
        raise e

    return result


def listActiveSystems(
    sw
):
    """
    Description:
    Returns a list of active servers visible to the user.

    Parameters:
    object session

    Returns:
        - array:
            - struct - system
                - int "id"
                - string "name"
                - dateTime.iso8601 "last_checkin" - Last time server
                                                    successfully checked in
    """
    try:
        result = sw.session.system.listActiveSystems(
            sw.key
        )
    except Exception as e:
        raise e

    return result


def listActiveSystemsDetails(
    sw,
    server_ids
):
    """
    Description:
    Given a list of server ids, returns a list of active servers' details
    visible to the user.

    Parameters:
        - object session
        - array:
            - int - server_ids

    Returns:
        - array:
            - struct - server details
                - int "id" - The server's id
                - string "name" - The server's name
                - dateTime.iso8601 "last_checkin" - Last time server
                                                    successfully checked in
                                                    (in UTC)
                - int "ram" - The amount of physical memory in MB.
                - int "swap" - The amount of swap space in MB.
                - struct "network_devices" - The server's network devices
                - struct - network device
                    - string "ip" - IP address assigned to this network device
                    - string "interface" - Network interface assigned to device
                                           e.g. eth0
                    - string "netmask" - Network mask assigned to device
                    - string "hardware_address" - Hardware Address of device.
                    - string "module" - Network driver used for this device.
                    - string "broadcast" - Broadcast address for device.
                    - array "ipv6" - List of IPv6 addresses
                    - array:
                        - struct - ipv6 address
                            - string "address" - IPv6 address of network device
                            - string "netmask" - IPv6 netmask of network device
                            - string "scope" - IPv6 address scope
                - struct "dmi_info" - The server's dmi info
                - struct - DMI
                    - string "vendor"
                    - string "system"
                    - string "product"
                    - string "asset"
                    - string "board"
                    - string "bios_release" - (optional)
                    - string "bios_vendor" - (optional)
                    - string "bios_version" - (optional)
                - struct "cpu_info" - The server's cpu info
                - struct - CPU
                    - string "cache"
                    - string "family"
                    - string "mhz"
                    - string "flags"
                    - string "model"
                    - string "vendor"
                    - string "arch"
                    - string "stepping"
                    - string "count"
                - array "subscribed_channels" - List of subscribed channels
                - array:
                    - struct - channel
                        - int "channel_id" - The channel id.
                        - string "channel_label" - The channel label.
                - array "active_guest_system_ids" - List of virtual guest
                                                  system ids for active guests
                - array:
                    - int "guest_id" - The guest's system id.
    """
    try:
        result = sw.session.system.listActiveSystemsDetails(
            sw.key,
            server_ids
        )
    except Exception as e:
        raise e

    return result


def listAdministrators(
    sw,
    server_id
):
    """
    Description:
    Returns a list of users which can administer the system.

    Parameters:
        - object session
        - int server_id

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
        result = sw.session.system.listAdministrators(
            sw.key,
            server_id
        )
    except Exception as e:
        raise e

    return result


def listDuplicatesByHostname(
    sw
):
    """
    Description:
    List duplicate systems by Hostname.

    Parameters:
        - object session

    Returns:
        - array:
            - struct - Duplicate Group
                - string "hostname"
                - array "systems"
                    - struct - system
                    - int "systemId"
                    - string "systemName"
                    - dateTime.iso8601 "last_checkin" - Last time server
                                                        successfully checked in
    """
    try:
        result = sw.session.system.listDuplicatesByHostname(
            sw.key
        )
    except Exception as e:
        raise e

    return result


def listDuplicatesByIp(
    sw
):
    """
    Description:
    List duplicate systems by IP Address.

    Parameters:
    object session

    Returns:
        - array:
            - struct - Duplicate Group
                - string "ip"
                - array "systems"
                    - struct - system
                        - int "systemId"
                        - string "systemName"
                        - dateTime.iso8601 "last_checkin" - Last time server
                                                        successfully checked in
    """
    try:
        result = sw.session.system.listDuplicatesByIp(
            sw.key
        )
    except Exception as e:
        raise e

    return result


def listDuplicatesByMac(
    sw
):
    """
    Description:
    List duplicate systems by Mac Address.

    Parameters:
        - object session

    Returns:
        - array:
            - struct - Duplicate Group
                - string "mac"
                - array "systems"
                    - struct - system
                        - int "systemId"
                        - string "systemName"
                        - dateTime.iso8601 "last_checkin" - Last time server
                                                        successfully checked in
    """
    try:
        result = sw.session.system.listDuplicatesByMac(
            sw.key
        )
    except Exception as e:
        raise e

    return result


def listEligibleFlexGuests(
    sw
):
    """
    Description:
    List eligible flex guests accessible to the user

    Parameters:
        - object session

    Returns:
        - array:
            - struct - channel family system group
                - int "id"
                - string "label"
                - string "name"
                - array:
                    - int - systems
    """
    try:
        result = sw.session.system.listEligibleFlexGuests(
            sw.key
        )
    except Exception as e:
        raise e

    return result


def listExtraPackages(
    sw,
    server_id
):
    """
    Description:
    List extra packages for a system

    Parameters:
        - object session
        - int server_id

    Returns:
        - array:
            - struct - package
                - string "name"
                - string "version"
                - string "release"
                - string "epoch" - returned only if non-zero
                - string "arch"
                - date "installtime" - returned only if known
    """
    try:
        result = sw.session.system.listExtraPackages(
            sw.key,
            server_id
        )
    except Exception as e:
        raise e

    return result


def listFlexGuests(
    sw
):
    """
    Description:
    List flex guests accessible to the user

    Parameters:
        - object session

    Returns:
        - array:
            - struct - channel family system group
                - int "id"
                - string "label"
                - string "name"
                - array:
                    - int - systems
    """
    try:
        result = sw.session.system.listFlexGuests(
            sw.key
        )
    except Exception as e:
        raise e

    return result


def listGroups(
    sw,
    server_id
):
    """
    Description:
    List the available groups for a given system.

    Parameters:
        - object session
        - int server_id

    Returns:
        - array:
            - struct - system group
                - int "id" - server group id
                - int "subscribed" - 1 if the given server is subscribed to
                                     this server group, 0 otherwise
                - string "system_group_name" - Name of the server group
                - string "sgid" - server group id (Deprecated)
    """
    try:
        result = sw.session.system.listGroups(
            sw.key,
            server_id
        )
    except Exception as e:
        raise e

    return result


def listInactiveSystems(
    sw,
    days=None
):
    """
    Description:
    Lists systems that have been inactive for the default period of inactivity

    Parameters:
        - object session
        - int days (optional)
    Returns:
        - array:
            - struct - system
                - int "id"
                - string "name"
                - dateTime.iso8601 "last_checkin" - Last time server
                                                    successfully checked in
    """
    try:
        if days:
            result = sw.session.system.listInactiveSystems(
                sw.key,
                days
            )
        else:
            result = sw.session.system.listInactiveSystems(
                sw.key
            )
    except Exception as e:
        raise e

    return result


def listLatestAvailablePackage(
    sw,
    server_id,
    package_name
):
    """
    Description:
    Get the latest available version of a package for each system

    Parameters:
        - object session
        - array:
            - int - server_id
            - string package_name

    Returns:
        - array:
            - struct - system
                - int "id" - server ID
                - string "name" - server name
                - struct "package" - package structure
                - struct - package
                    - int "id"
                    - string "name"
                    - string "version"
                    - string "release"
                    - string "epoch"
                    - string "arch"
    """
    try:
        result = sw.session.system.listLatestAvailablePackage(
            sw.key,
            server_id,
            package_name
        )
    except Exception as e:
        raise e

    return result


def listLatestInstallablePackages(
    sw,
    server_id
):
    """
    Description:
    Get the list of latest installable packages for a given system.

    Parameters:
        - object session
        - int server_id

    Returns:
        - struct - package
            - string "name"
            - string "version"
            - string "release"
            - string "epoch"
            - int "id"
            - string "arch_label"
    """
    try:
        result = sw.session.system.listLatestInstallablePackages(
            sw.key,
            server_id
        )
    except Exception as e:
        raise e

    return result


def listLatestUpgradablePackages(
    sw,
    system_id
):
    """
    Description:
        - Get the list of latest upgradable packages for a given system.

        - Parameters:
            - session object
            - int serverId

        - Returns:
            - struct - package
                - string "name"
                - string "arch"
                - string "from_version"
                - string "from_release"
                - string "from_epoch"
                - string "to_version"
                - string "to_release"
                - string "to_epoch"
                - string "to_package_id"

    """
    try:
        result = sw.session.system.listLatestUpgradablePackages(
            sw.key,
            system_id
        )
    except Exception as e:
        raise e

    return result


def listNewerInstalledPackages(
    sw,
    server_id,
    package_name,
    package_version,
    package_release,
    package_epoch
):
    """
    Description:
    Given a package name, version, release, and epoch,
    returns the list of packages installed on the system w/
    the same name that are newer.

        - Parameters:
            - session object
            - int serverId
            - string name - Package name.
            - string version - Package version.
            - string release - Package release.
            - string epoch - Package epoch.

        - Returns:
            - array:
                - struct - package
                    - string "name"
                    - string "version"
                    - string "release"
                    - string "epoch"

    """
    try:
        result = sw.session.system.listNewerInstalledPackages(
            sw.key,
            server_id,
            package_name,
            package_version,
            package_release,
            package_epoch
        )
    except Exception as e:
        raise e

    return result


def listNotes(
    sw,
    server_id
):
    """
    Description:
    Provides a list of notes associated with a system.

    Parameters:
        - object session
        - int server_id

    Returns:
        - array:
            - struct - note details
                - int "id"
                - string "subject" - Subject of the note
                - string "note" - Contents of the note
                - int "system_id" - The id of the system associated with the
                                    note
                - string "creator" - Creator of the note
                - date "updated" - Date of the last note update
    """
    try:
        result = sw.session.system.listNotes(
            sw.key,
            server_id
        )
    except Exception as e:
        raise e

    return result


def listOlderInstalledPackages(
    sw,
    server_id,
    name,
    version,
    release,
    epoch
):
    """
    Description:
    Given a package name, version, release, and epoch, returns the list of
    packages installed on the system with the same name that are older.

    Parameters:
        - object session
        - int server_id
        - string name - Package name.
        - string version - Package version.
        - string release - Package release.
        - string epoch - Package epoch.

    Returns:
        - array:
            - struct - package
                - string "name"
                - string "version"
                - string "release"
                - string "epoch"
    """
    try:
        result = sw.session.system.listOlderInstalledPackages(
            sw.key,
            server_id,
            name,
            version,
            release,
            epoch
        )
    except Exception as e:
        raise e

    return result


def listOutOfDateSystems(
    sw
):
    """
    Description:
    Returns list of systems needing package updates.

    Parameters:
        - object session

    Returns:
        - array:
            - struct - system
                - int "id"
                - string "name"
                - dateTime.iso8601 "last_checkin" - Last time server
                                                successfully checked in
    """
    try:
        result = sw.session.system.listOutOfDateSystems(
            sw.key
        )
    except Exception as e:
        raise e

    return result


def listPackageProfiles(
    sw
):
    """
    Description:
    List the package profiles in this organization

    Parameters:
        - object session

    Returns:
        - array:
            - struct - package profile
                - int "id"
                - string "name"
                - string "channel"
    """
    try:
        result = sw.session.system.listPackageProfiles(
            sw.key
        )
    except Exception as e:
        raise e

    return result


def listPackages(
    sw,
    server_id
):
    """
    Description:
    List the installed packages for a given system. The attribute installtime
    is returned since API version 10.10.

    Parameters:
        - object session
        - int server_id

    Returns:
        - array:
            - struct - package
                - int "id"
                - string "name"
                - string "version"
                - string "release"
                - string "epoch"
                - string "arch"
                - date "installtime" - returned only if known
    """
    try:
        result = sw.session.system.listPackages(
            sw.key,
            server_id
        )
    except Exception as e:
        raise e

    return result


def listPackagesFromChannel(
    sw,
    server_id,
    channel_label
):
    """
    Description:
    Provides a list of packages installed on a system that are also contained
    in the given channel. The installed package list did not include arch
    information before RHEL 5, so it is arch unaware. RHEL 5 systems do upload
    the arch information, and thus are arch aware.

    Parameters:
        - object session
        - int server_id
        - string channel_label

    Returns:
        - array:
            - struct - package
                - string "name"
                - string "version"
                - string "release"
                - string "epoch"
                - int "id"
                - string "arch_label"
                - string "path" - The path on that file system that the package
                                resides
                - string "provider" - The provider of the package, determined
                                       by the gpg key it was signed with.
                - dateTime.iso8601 "last_modified"
    """
    try:
        result = sw.session.system.listPackagesFromChannel(
            sw.key,
            server_id,
            channel_label
        )
    except Exception as e:
        raise e

    return result


def listSubscribableBaseChannels(
    sw,
    server_id
):
    """
    Description:
    Returns a list of subscribable base channels.

    Parameters:
        - object session
        - int server_id

    Returns:
        - array:
            - struct - channel
                - int "id" - Base Channel ID.
                - string "name" - Name of channel.
                - string "label" - Label of Channel
                - int "current_base" - 1 indicates it is the current base
                                       channel
    """
    try:
        result = sw.session.system.listSubscribableBaseChannels(
            sw.key,
            server_id
        )
    except Exception as e:
        raise e

    return result


def listSubscribableChildChannels(
    sw,
    server_id
):
    """
    Description:
    Returns a list of subscribable child channels. This only shows channels the
    system is *not* currently subscribed to.

    Parameters:
        - object session
        - int server_id

    Returns:
        - array:
            - struct - child channel
                - int "id"
                - string "name"
                - string "label"
                - string "summary"
                - string "has_license"
                - string "gpg_key_url"
    """
    try:
        result = sw.session.system.listSubscribableChildChannels(
            sw.key,
            server_id
        )
    except Exception as e:
        raise e

    return result


def listSubscribedChildChannels(
    sw,
    server_id
):
    """
    Description:
    Returns a list of subscribed child channels.

    Parameters:
        - session object
        - int serverId

    Returns:
        - array:
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
        result = sw.session.system.listSubscribedChildChannels(
            sw.key,
            server_id
        )
    except Exception as e:
        raise e

    return result


def listSystemEvents(
    sw,
    server_id
):
    """
    Description:
    List all system events for given server. This includes *all* events for
    the server since it was registered. This may require the caller to filter
    the results to fetch the specific events they are looking for.

    Parameters:
        - object session
        - int server_id - ID of system.

    Returns:
        - array:
            - struct - action
                - int "failed_count" - Number of times action failed.
                - string "modified" - Date modified.
                    (Deprecated by modified_date)
                - dateTime.iso8601 "modified_date" - Date modified.
                - string "created" - Date created.
                                     (Deprecated by created_date)
                - dateTime.iso8601 "created_date" - Date created.
                - string "action_type"
                - int "successful_count" - Number of times action was
                    successful.
                - string "earliest_action" - Earliest date this action will
                                             occur.
                - int "archived" - If this action is archived. (1 or 0)
                - string "scheduler_user" - available only if concrete user has
                                            scheduled the action
                - string "prerequisite" - Pre-requisite action. (optional)
                - string "name" - Name of this action.
                - int "id" - Id of this action.
                - string "version" - Version of action.
                - string "completion_time" - The date/time the event was
                    completed.
                    Format ->YYYY-MM-dd hh:mm:ss.ms
                    Eg ->2007-06-04 13:58:13.0.(optional)
                    (Deprecated by completed_date)
                - dateTime.iso8601 "completed_date" - The date/time the event
                    was completed. (optional)
                - string "pickup_time" - The date/time the action was picked
                     up. Format ->YYYY-MM-dd hh:mm:ss.ms
                     Eg ->2007-06-04 13:58:13.0. (optional)
                     (Deprecated by pickup_date)
                - dateTime.iso8601 "pickup_date" - The date/time the action was
                    picked up. (optional)
                - string "result_msg" - The result string after the action
                                    executes at the client machine. (optional)
                - array "additional_info" - This array contains additional
                                        information for the event, if available
                    - struct - info
                        * string "detail" - The detail provided depends on the
                            specific event. For example, for a
                            package event, this will be the
                            package name, for an errata event,
                            this will be the advisory name and
                            synopsis, for a config file event,
                            this will be path and optional
                            revision information...etc.

                        * string "result" - The result (if included) depends on
                            the specific event. For example,
                            for a package or errata event, no
                            result is included, for a config
                            file event, the result might
                            include an error (if one occurred,
                            such as the file was missing) or in
                            the case of a config file
                            comparison it might include the
                            differenes found.

                Available since: 10.8
    """
    try:
        result = sw.session.system.listSystemEvents(
            sw.key,
            server_id
        )
    except Exception as e:
        raise e

    return result


def listSystems(
    sw
):
    """
    Description:
        - Returns a list of all servers visible to the user.

        - Parameters:
            - session object

        - Returns:
            - array:
                - struct - system
                    - int "id"
                    - string "name"
                    - dateTime.iso8601 "last_checkin" - Last time server
                                                        successfully checked in

    """
    try:
        result = sw.session.system.listSystems(
            sw.key
        )
    except Exception as e:
        raise e

    return result


def listSystemsWithExtraPackages(
    sw
):
    """
    Description:
    List systems with extra packages

    Parameters:
        - object session

    Returns:
        - array:
            - int "id" - System ID
            - string "name" - System profile name
            - int "extra_pkg_count" - Extra packages count
    """
    try:
        result = sw.session.system.listSystemsWithExtraPackages(
            sw.key
        )
    except Exception as e:
        raise e

    return result


def listSystemsWithPackage(
    sw,
    package_id=None,
    name=None,
    version=None,
    release=None
):
    """
    Description:
    Lists the systems that have the given installed package

    Parameters:
        - object session AND
        - int package_id OR
        - string name
        - string version
        - string release

    So either package_id here, or the NVR

    Returns:
        - array:
            - struct - system
                - int "id"
                - string "name"
                - dateTime.iso8601 "last_checkin" - Last time server
                    successfully checked in
    """
    try:
        if package_id:
            result = sw.session.system.listSystemsWithPackage(
                sw.key,
                package_id
            )
        else:
            result = sw.session.system.listSystemsWithPackage(
                sw.key,
                name,
                version,
                release
            )
    except Exception as e:
        raise e

    return result


def listUngroupedSystems(
    sw
):
    """
    Description:
    List systems that are not associated with any system groups.

    Parameters:
        - object session

    Returns:
        - array:
            - struct - system
                - int "id" - server id
                - string "name"
    """
    try:
        result = sw.session.system.listUngroupedSystems(
            sw.key
        )
    except Exception as e:
        raise e

    return result


def listUserSystems(
    sw,
    login=None
):
    """
    Description:
    List systems for a given user.

    Parameters:
        - object session
        - string login - User's login name.

    Returns:
        - array:
            - struct - system
                - int "id"
                - string "name"
                - dateTime.iso8601 "last_checkin" - Last time server
                                                    successfully checked in
    """
    try:
        if login:
            result = sw.session.system.listUserSystems(
                sw.key,
                login
            )
        else:
            result = sw.session.system.listUserSystems(
                sw.key
            )
    except Exception as e:
        raise e

    return result


def listVirtualGuests(
    sw,
    server_id
):
    """
    Description:
    Lists the virtual guests for agiven virtual host

    Parameters:
        - object session
        - int server_id - the virtual host's id

    Returns:
        - array:
            - struct - virtual system
                - int "id"
                - string "name"
                - string "guest_name" - The virtual guest name as provided by
                                        the virtual host
                - dateTime.iso8601 "last_checkin" - Last time server
                                                    successfully checked in.
    """
    try:
        result = sw.session.system.listVirtualGuests(
            sw.key,
            server_id
        )
    except Exception as e:
        raise e

    return result


def listVirtualHosts(
    sw
):
    """
    Description:
    Lists the virtual hosts visible to the user

    Parameters:
        - object session

    Returns:
        - array:
            - struct - system
                - int "id"
                - string "name"
                - dateTime.iso8601 "last_checkin" - Last time server
                                                    successfully checked in
    """
    try:
        result = sw.session.system.listVirtualHosts(
            sw.key
        )
    except Exception as e:
        raise e

    return result


def obtainReactivationKey(
    sw,
    server_id
):
    """
    Description:
    Obtains a reactivation key for this server.

    Parameters:
        - object session
        - int server_id

    Returns:
        - string
    """
    try:
        result = sw.session.system.obtainReactivationKey(
            sw.key,
            server_id
        )
    except Exception as e:
        raise e

    return result


def provisionSystem(
    sw,
    server_id,
    profile_name,
    date_time=None
):
    """
    Description:
    Provision a system using the specified kickstart profile.

    Parameters:
        - object session
        - int server_id - ID of the system to be provisioned.
        - string profile_name - Kickstart profile to use.

    Returns:
        - int - ID of the action scheduled, otherwise exception thrown on error
    """
    try:
        if date_time:
            result = sw.session.system.provisionSystem(
                sw.key,
                server_id,
                profile_name,
                date_time
            )
        else:
            result = sw.session.system.provisionSystem(
                sw.key,
                server_id,
                profile_name
            )
    except Exception as e:
        raise e

    return result


def provisionVirtualGuest(
    sw,
    server_id,
    guest_name,
    profile_name,
    memorymb=None,
    vcpus=None,
    storagegb=None,
    macaddress=None
):
    """
    Description:
    Provision a guest on the host specified. This schedules the guest for
    creation and will begin the provisioning process when the host checks in
    or if OSAD is enabled will begin immediately.

    Parameters:
        - object session
        - int serverId - ID of host to provision guest on.
        - string guest_name
        - string profile_name - Kickstart Profile to use.
        - int memorymb - Memory to allocate to the guest (optional)
        - int vcpus - Number of virtual CPUs to allocate to the guest(optional)
        - int storagegb - Size of the guests disk image. (optional)
        - string macaddress - macAddress to give the guest's virtual networking
                            hardware. (optional)

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        if macaddress:
            result = sw.session.system.provisionVirtualGuest(
                sw.key,
                server_id,
                guest_name,
                profile_name,
                memorymb,
                vcpus,
                storagegb,
                macaddress
            )
        elif memorymb and vcpus and storagegb:
            result = sw.session.system.provisionVirtualGuest(
                sw.key,
                server_id,
                guest_name,
                profile_name,
                memorymb,
                vcpus,
                storagegb
            )
        else:
            result = sw.session.system.provisionVirtualGuest(
                sw.key,
                server_id,
                guest_name,
                profile_name
            )
    except Exception as e:
        raise e

    return result


def removeEntitlements(
    sw,
    server_id,
    entitlement_labels
):
    """
    Description:
    Remove addon entitlements from a server. Entitlements a server does not
    have are quietly ignored.

    Parameters:
        - object session
        - int server_id
        - array:
            - string - entitlement_label

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.system.removeEntitlements(
            sw.key,
            server_id,
            entitlement_labels
        )
    except Exception as e:
        raise e

    return result


def scheduleApplyErrata(
    sw,
    server_ids,
    errata_ids,
    date_time=None
):
    """
    Description:
    Schedules an action to apply errata updates to multiple systems.

    Parameters:
        - object session
        - array:
            - int - server_id OR
        - int - server_id
        - array:
            - int - errataId (optional)
        - dateTime.iso8601 earliestOccurrence (optional)

    Returns:

    int - 1 on success, exception thrown otherwise.
    """
    try:
        if type(server_ids) is list:
            if date_time:
                result = sw.session.system.scheduleApplyErrata(
                    sw.key,
                    server_ids,
                    errata_ids,
                    date_time
                )
            else:
                result = sw.session.system.scheduleApplyErrata(
                    sw.key,
                    server_ids,
                    errata_ids
                )
        elif type(server_ids) is not list:
            if date_time:
                result = sw.session.system.scheduleApplyErrata(
                    sw.key,
                    server_ids,
                    errata_ids,
                    date_time
                )
            else:
                result = sw.session.system.scheduleApplyErrata(
                    sw.key,
                    server_ids,
                    errata_ids
                )
    except Exception as e:
        raise e

    return result


def scheduleGuestAction(
    sw,
    server_id,
    state,
    date_time=None
):
    """
    Description:
    Schedules a guest action for the specified virtual guest for a given
    date/time.

    Parameters:
        - object session
        - int server_id - the system Id of the guest
        - string state - One of the following actions 'start', 'suspend',
                        'resume', 'restart', 'shutdown'.
        - date_time - dateTime.iso8601 date - the time/date to schedule the
                    action

    Returns:
        - int actionId - The action id of the scheduled action
    """
    try:
        if date_time:
            result = sw.session.system.scheduleGuestAction(
                sw.key,
                server_id,
                state,
                date_time
            )
        else:
            result = sw.session.system.scheduleGuestAction(
                sw.key,
                server_id,
                state
            )
    except Exception as e:
        raise e

    return result


def scheduleHardwareRefresh(
    sw,
    server_id,
    date_time
):
    """
    Description:
    Schedule a hardware refresh for a system.

    Parameters:
        - object session
        - int server_id
        - dateTime.iso8601 earliestOccurrence

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.system.scheduleHardwareRefresh(
            sw.key,
            server_id,
            date_time
        )
    except Exception as e:
        raise e

    return result


def schedulePackageInstall(
    sw,
    server_id,
    packagelist,
    date_time
):
    """
    Description:
    Schedule package installation for a system.

    Parameters:

        - session object
        - int serverId
        - array:
            - int - packageId
        - dateTime.iso8601 earliestOccurrence

    Returns:

        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.system.schedulePackageInstall(
            sw.key,
            server_id,
            packagelist,
            date_time
        )
    except Exception as e:
        raise e

    return result


def schedulePackageRefresh(
    sw,
    server_id,
    date_time
):
    """
    Description:
        - Schedule a package list refresh for a system.

    Parameters:
        - session object
        - int serverId
        - dateTime.iso8601 earliestOccurrence

    Returns:
        - int - ID of the action scheduled, o
                therwise exception thrown on error
    """
    try:
        result = sw.session.system.schedulePackageRefresh(
            sw.key,
            server_id,
            date_time
        )
    except Exception as e:
        raise e

    return result


def schedulePackageRemove(
    sw,
    server_id,
    package_info,
    date_time
):
    """
    Description:
    Schedule package removal for a system.

    Parameters:
        - object session
        - int server_id
        - package_info - array:
            - int - packageId
        - dateTime.iso8601 earliestOccurrence

    Returns:
        - int - ID of the action scheduled, otherwise exception thrown on error
    """
    try:
        result = sw.session.system.schedulePackageRemove(
            sw.key,
            server_id,
            package_info,
            date_time
        )
    except Exception as e:
        raise e

    return result


def scheduleReboot(
    sw,
    server_id,
    date_time
):
    """
    Description:
    Schedule a reboot for a system.

    Parameters:

        - session object
        - int serverId
        - dateTime.iso860 earliestOccurrence

    Returns:

        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.system.scheduleReboot(
            sw.key,
            server_id,
            date_time
        )
    except Exception as e:
        raise e

    return result


def scheduleScriptRun(
    sw,
    servers,
    user,
    group,
    timeout,
    script,
    date_time
):
    """
    Description:
    Schedule a script to run.

    Parameters:
        - session object
        - [array: int | int ] - System ID(s) of the servers to run the script
                                on.
        - string username - User to run script as.
        - string groupname - Group to run script as.
        - int timeout - Seconds to allow the script to run before timing out.
        - string script - Contents of the script to run.
        - dateTime.iso8601 earliestOccurrence - Earliest the script can run.

    Returns:
        - int - ID of the script run action created. Can be used to fetch
                results with system.getScriptResults.
    """
    try:
        result = sw.session.system.scheduleScriptRun(
            sw.key,
            servers,
            user,
            group,
            timeout,
            script,
            date_time
        )
    except Exception as e:
        raise e

    return result


def scheduleSyncPackagesWithSystem(
    sw,
    target_server_id,
    source_server_id,
    package_info,
    date_time
):
    """
    Description:
    Sync packages from a source system to a target.

    Parameters:
        - object session
        - int target_server_id - Target system to apply package changes to.
        - int source_server_id - Source system to retrieve package state from.
        - package_info - array:
            - int - packageId - Package IDs to be synced.
        - dateTime.iso8601 date - Date to schedule action for

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.system.scheduleSyncPackagesWithSystem(
            sw.key,
            target_server_id,
            source_server_id,
            package_info,
            date_time
        )
    except Exception as e:
        raise e

    return result


def searchByName(
    sw,
    name
):
    """
    Description:
    Returns a list of system IDs whose name matches the supplied regular
    expression.

    Parameters:

        - session object
        - string regexp - A regular expression.

    Returns:

        - array:
            - struct - system
                - int "id"
                - string "name"
                - dateTime.iso8601 "last_checkin" - Last time server
                    successfully checked in

    http://java.sun.com/j2se/1.4.2/docs/api/java/util/regex/Pattern.html
    """
    try:
        result = sw.session.system.searchByName(
            sw.key,
            name
        )
    except Exception as e:
        raise e

    return result


def setBaseChannel(
    sw,
    server_id,
    channel_label
):
    """
    Description:
    Assigns the server to a new base channel. If the user provides an empty
    string for the channelLabel, the current base channel and all child
    channels will be removed from the system.

    Parameters:
        - object session
        - int server_id
        - string channel_label

    Returns:
    int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.system.setBaseChannel(
            sw.key,
            server_id,
            channel_label
        )
    except Exception as e:
        raise e

    return result


def setChildChannels(
    sw,
    server_id,
    channel_label
):
    """
    Description:
    Subscribe the given server to the child channels provided. This method
    will unsubscribe the server from any child channels that the server is
    currently subscribed to, but that are not included in the list. The user
    may provide either a list of channel ids (int) or a list of channel labels
    (string) as input.

    Parameters:
        - object session
        - int server_id
        - array:
            - string channel_label

    Returns:
    int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.system.setChildChannels(
            sw.key,
            server_id,
            channel_label
        )
    except Exception as e:
        raise e

    return result


def setCustomValues(
    sw,
    server_id,
    custom_labels
):
    """
    Description:
    Set custom values for the specified server.

    Parameters:
        - object session
        - int server_id
        - struct - Map of custom labels to custom values
            - string "custom info label"
            - string "value"

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.system.setCustomValues(
            sw.key,
            server_id,
            custom_labels
        )
    except Exception as e:
        raise e

    return result


def setDetails(
    sw,
    server_id,
    server_details
):
    """
    Description:
    Set server details. All arguments are optional and will only be modified
    if included in the struct.

    Parameters:
        - object session
        - int server_id - ID of server to lookup details for.
        - struct - server details
            - string "profile_name" - System's profile name
            - string "base_entitlement" - System's base entitlement label.
                                       (enterprise_entitled or sw_mgr_entitled)
            - boolean "auto_errata_update" - True if system has auto errata
                                             updates enabled
            - string "description" - System description
            - string "address1" - System's address line 1.
            - string "address2" - System's address line 2.
            - string "city"
            - string "state"
            - string "country"
            - string "building"
            - string "room"
            - string "rack"

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.system.setDetails(
            sw.key,
            server_id,
            server_details
        )
    except Exception as e:
        raise e

    return result


def setGroupMembership(
    sw,
    server_id,
    server_group_id,
    member
):
    """
    Description:
    Set a servers membership in a given group.

    Parameters:
        - object session
        - int server_id
        - int server_group_id
        - boolean member - '1' to assign the given server to the given server
                           group, '0' to remove the given server from the given
                           server group.

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.system.setGroupMembership(
            sw.key,
            server_id,
            server_group_id,
            member
        )
    except Exception as e:
        raise e

    return result


def setGuestCpus(
    sw,
    server_id,
    numofcpus
):
    """
    Description:
    Schedule an action of a guest's host, to set that guest's CPU allocation

    Parameters:
        - object session
        - int server_id - The guest's system id
        - int numofcpus - The number of virtual cpus to allocate to the guest

    Returns:
    int actionID - the action Id for the schedule action on the host system
    """
    try:
        result = sw.session.system.setGuestCpus(
            sw.key,
            server_id,
            numofcpus
        )
    except Exception as e:
        raise e

    return result


def setGuestMemory(
    sw,
    server_id,
    memory
):
    """
    Description:
    Schedule an action of a guest's host, to set that guest's memory allocation

    Parameters:
        - object session
        - int server_id - The guest's system id
        - int memory - The amount of memory to allocate to the guest

    Returns:
        - int actionID - the action Id for the schedule action on the host
                        system.
    """
    try:
        result = sw.session.system.setGuestMemory(
            sw.key,
            server_id,
            memory
        )
    except Exception as e:
        raise e

    return result


def setLockStatus(
    sw,
    server_id,
    lockstatus
):
    """
    Description:
    Set server lock status.

    Parameters:
        - object session
        - int server_id
        - boolean lockstatus - true to lock the system, false to unlock the
                                system.

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.system.setLockStatus(
            sw.key,
            server_id,
            lockstatus
        )
    except Exception as e:
        raise e

    return result


def setProfileName(
    sw,
    server_id,
    name
):
    """
    Description:
    Set the profile name for the server.

    Parameters:
        - object session
        - int server_id
        - string name - Name of the profile.

    Returns:
    int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.system.setProfileName(
            sw.key,
            server_id,
            name
        )
    except Exception as e:
        raise e

    return result


def setVariables(
    sw,
    server_id,
    netboot,
    kickstart_var

):
    """
    Description:
    Sets a list of kickstart variables in the cobbler system record for the
    specified server. Note: This call assumes that a system record exists in
    cobbler for the given system and will raise an XMLRPC fault if that is not
    the case. To create a system record over xmlrpc use
    system.createSystemRecord To create a system record in the Web UI please
    go to System -> <Specified System> -> Provisioning -> Select a Kickstart
    profile -> Create Cobbler System Record.

    Parameters:
        - object session
        - int server_id
        - boolean netboot
        - array:
            - struct - kickstart variable
                - string "key"
                - string or int "value"

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.system.setVariables(
            sw.key,
            server_id,
            netboot,
            kickstart_var
        )
    except Exception as e:
        raise e

    return result


def tagLatestSnapshot(
    sw,
    server_id,
    tagname
):
    """
    Description:
    Tags latest system snapshot

    Parameters:
        - object session
        - int server_id
        - string tagname

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.system.tagLatestSnapshot(
            sw.key,
            server_id,
            tagname
        )
    except Exception as e:
        raise e

    return result


def upgradeEntitlement(
    sw,
    server_id,
    entitlementname
):
    """
    Description:
    Adds an entitlement to a given server.

    Parameters:
        - object session
        - int server_id
        - string entitlementname - ONE OF:
            - 'enterprise_entitled',
            - 'provisioning_entitled',
            - 'monitoring_entitled',
            - 'nonlinux_entitled',
            - 'virtualization_host',
            - 'virtualization_host_platform'.

    Returns:
    int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.system.upgradeEntitlement(
            sw.key,
            server_id,
            entitlementname
        )
    except Exception as e:
        raise e

    return result


def whoRegistered(
    sw,
    server_id
):
    """
    Description:
    Returns information about the user who registered the system

    Parameters:
        - object session
        - int server_id - Id of the system in question

    Returns:
        - struct - user
            - int "id"
            - string "login"
            - string "login_uc" - upper case version of the login
            - boolean "enabled" - true if user is enabled, false if the user
                is disabled
    """
    try:
        result = sw.session.system.whoRegistered(
            sw.key,
            server_id
        )
    except Exception as e:
        raise e

    return result

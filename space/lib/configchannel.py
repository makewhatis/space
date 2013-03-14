"""
``Namespace: configchannel``
============================

Provides methods to access and
modify many aspects of configuration channels.

- :func:`channelExists`
- :func:`create`
- :func:`createOrUpdatePath`
- :func:`createOrUpdateSymlink`
- :func:`deleteChannels`
- :func:`deleteFileRevisions`
- :func:`deleteFiles`
- :func:`deployAllSystems`
- :func:`getDetails`
- :func:`getEncodedFileRevision`
- :func:`getFileRevision`
- :func:`getFileRevisions`
- :func:`listFiles`
- :func:`listGlobals`
- :func:`listSubscribedSystems`
- :func:`lookupChannelInfo`
- :func:`lookupFileInfo`
- :func:`scheduleFileComparisons`
- :func:`update`
"""


def channelExists(
    sw,
    channellabel
):
    """
    Description:
    Check for the existence of the config channel provided.

    Parameters:
        - string sessionKey
        - string channelLabel - Channel to check for.

    Returns:
        - 1 if exists, 0 otherwise.
    """
    try:
        result = sw.session.configchannel.channelExists(
            sw.key,
            channellabel
        )
    except Exception as e:
        raise e
    return result


def create(
    sw,
    channellabel,
    channelname,
    channeldescription
):
    """
    Description:
    Create a new global config channel. Caller must be at least a
    config admin or an organization admin.

    Parameters:
        - string sessionKey
        - string channelLabel
        - string channelName
        - string channelDescription

    Returns:
        - struct - Configuration Channel information
            - int "id"
            - int "orgId"
            - string "label"
            - string "name"
            - string "description"
            - struct "configChannelType"
            - struct - Configuration Channel Type information
                - int "id"
                - string "label"
                - string "name"
                - int "priority"
    """
    try:
        result = sw.session.configchannel.create(
            sw.key,
            channellabel,
            channelname,
            channeldescription,
        )
    except Exception as e:
        raise e
    return result


def createOrUpdatePath(
    sw,
    configlabel,
    path,
    isdir,
    path_info
):
    """
    Description:
    Create a new file or directory with the given path, or update
    an existing path.

    Parameters:
        - string sessionKey
        - string configChannelLabel
        - string path
        - boolean isDir
        - struct - path info
            - string "contents" - Contents of the file
            - boolean "contents_enc64" - Identifies base64 encoded content
                                         (default: disabled,
                                          only for non-directories)
            - string "owner" - Owner of the file/directory.
            - string "group" - Group name of the file/directory.
            - string "permissions" - Octal file/directory permissions (eg: 644)
            - string "selinux_ctx" - SELinux Security context (optional)
            - string "macro-start-delimiter" - Config file macro start
                                               delimiter. Use null or empty
                                               string to accept the default.
                                               (only for non-directories)
            - string "macro-end-delimiter" - Config file macro end delimiter.
                                             Use null or empty string to accept
                                             the default.
                                             (only for non-directories)
            - int "revision" - next revision number, auto increment for null
            - boolean "binary" - mark the binary content, if True,
                                 base64 encoded content is expected
                                 (only for non-directories)

    Returns:
        - struct - Configuration Revision information
        - string "type"
            - file
            - directory
            - symlink
        - string "path" - File Path
        - string "target_path" - Symbolic link Target File Path.
        - string "channel" - Channel Name
        - string "contents" - File contents (base64 encoded according to
                                            the contents_enc64 attribute)
        - boolean "contents_enc64" - Identifies base64 encoded content
        - int "revision" - File Revision
        - dateTime.iso8601 "creation" - Creation Date
        - dateTime.iso8601 "modified" - Last Modified Date
        - string "owner" - File Owner.
        - string "group" - File Group.
        - int "permissions" - File Permissions (Deprecated). Present for
                              files or directories only.
        - string "permissions_mode" - File Permissions. Present for files
                                      or directories only.
        - string "selinux_ctx" - SELinux Context (optional).
        - boolean "binary" - true/false , Present for files only.
        - string "md5" - File's md5 signature. Present for files only.
        - string "macro-start-delimiter" - Macro start delimiter for a
                                            config file.
    """
    try:
        result = sw.session.configchannel.createOrUpdatePath(
            sw.key,
            configlabel,
            path,
            isdir,
            path_info
        )
    except Exception as e:
        raise e
    return result


def createOrUpdateSymlink(
    sw,
    configlabel,
    path,
    isdir,
    path_info
):
    """
    Description:
    Create a new symbolic link with the given path, or update an existing path

    Parameters:
        - string sessionKey
        - string configChannelLabel
        - string path
        - struct - path info
            - string "target_path" - The target path for the symbolic link
            - string "selinux_ctx" - SELinux Security context (optional)
            - int "revision" - next revision number, skip this field
                            for automatic revision number assignment

    Returns:
        - struct - Configuration Revision information
            - string "type"
                - file
                - directory
                - symlink
            - string "path" - File Path
            - string "target_path" - Symbolic link Target File Path.
            - string "channel" - Channel Name
            - string "contents" - File contents (base64 encoded according
                                to the contents_enc64 attribute)
            - boolean "contents_enc64" - Identifies base64 encoded content
            - int "revision" - File Revision
            - dateTime.iso8601 "creation" - Creation Date
            - dateTime.iso8601 "modified" - Last Modified Date
            - string "owner" - File Owner.
            - string "group" - File Group.
            - int "permissions" - File Permissions (Deprecated).
            - string "permissions_mode" - File Permissions.
            - string "selinux_ctx" - SELinux Context (optional).
            - boolean "binary" - true/false , Present for files only.
            - string "md5" - File's md5 signature. Present for files only.
            - string "macro-start-delimiter" - Macro start delimiter for
                                            a config file.
            - string "macro-end-delimiter" - Macro end delimiter for a config
                                            file. Present for text files only.

    """
    try:
        result = sw.session.configchannel.createOrUpdateSymlink(
            sw.key,
            configlabel,
            path,
            isdir,
            path_info
        )
    except Exception as e:
        raise e
    return result


def deleteChannels(
    sw,
    channellabels
):
    """
    Description:
    Delete a list of global config channels. Caller must be a config admin.

    Parameters:
        - string sessionKey
        - array:
            - string - configuration channel labels to delete.

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.configchannel.deleteChannels(
            sw.key,
            channellabels
        )
    except Exception as e:
        raise e
    return result


def deleteFileRevisions(
    sw,
    channellabel,
    filepath,
    revisions
):
    """
    Description:
    Delete specified revisions of a given configuration file

    Parameters:
        - string sessionKey
        - string channelLabel - Label of config channel to lookup on.
        - string filePath - Configuration file path.
        - array:
            - int - List of revisions to delete

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.configchannel.deleteFileRevisions(
            sw.key,
            channellabel,
            filepath,
            revisions
        )
    except Exception as e:
        raise e
    return result


def deleteFiles(
    sw,
    channellabel,
    filepaths
):
    """
    Description:
        - Remove file paths from a global channel.

    Parameters:
        - string sessionKey
        - string channelLabel - Channel to remove the files from.
        - array:
            - string - file paths to remove.

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.configchannel.deleteFiles(
            sw.key,
            channellabel,
            filepaths
        )
    except Exception as e:
        raise e
    return result


def deployAllSystems(
    sw,
    channellabel,
    date_time
):
    """
    Description:
    Schedule an immediate configuration deployment for all
    systems subscribed to a particular configuration channel.

    Parameters:
        - string sessionKey
        - string channelLabel - The configuration channel's label.
        - dateTime.iso8601 date - The date to schedule the action (OPTIONAL)

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.configchannel.deployAllSystems(
            sw.key,
            channellabel,
            date_time
        )
    except Exception as e:
        raise e
    return result


def getDetails(
    sw,
    channellabel
):
    """
    Description:
    Lookup config channel details.

    Parameters:
        - string sessionKey
        - string channelLabel or int channelid

    Returns:
        - struct - Configuration Channel information
        - int "id"
        - int "orgId"
        - string "label"
        - string "name"
        - string "description"
        - struct "configChannelType"
        - struct - Configuration Channel Type information
            - int "id"
            - string "label"
            - string "name"
            - int "priority"
    """
    try:
        result = sw.session.configchannel.getDetails(
            sw.key,
            channellabel
        )
    except Exception as e:
        raise e
    return result


def getEncodedFileRevision(
    sw,
    configchan,
    filepath,
    revision
):
    """
    Description:
    Get revision of the specified config file

    Parameters:
        - string sessionKey
        - string configChannelLabel - label of config channel to lookup on
        - string filePath - config file path to examine
        - int revision - config file revision to examine

    Returns:
        - struct - Configuration Revision information
            - string "type"
                - file
                - directory
                - symlink
    - string "path" - File Path
    - string "target_path" - Symbolic link Target File Path.
    - string "channel" - Channel Name
    - string "contents" - File contents
                       (base64 encoded according to the
                        contents_enc64 attribute)
    - boolean "contents_enc64" - Identifies base64 encoded content
    - int "revision" - File Revision
    - dateTime.iso8601 "creation" - Creation Date
    - dateTime.iso8601 "modified" - Last Modified Date
    - string "owner" - File Owner.
    - string "group" - File Group.
    - int "permissions" - File Permissions (Deprecated). Present for files
                        or directories only.
    - string "permissions_mode" - File Permissions. Present for files
                                or directories only.
    - string "selinux_ctx" - SELinux Context (optional).
    - boolean "binary" - true/false , Present for files only.
    - string "md5" - File's md5 signature. Present for files only.
    - string "macro-start-delimiter" - Macro start delimiter for a config file.
                                    Present for text files only.
    - string "macro-end-delimiter" - Macro end delimiter for a config file.
                                   Present for text files only.
    """
    try:
        result = sw.session.configchannel.getEncodedFileRevision(
            sw.key,
            configchan,
            filepath,
            revision
        )
    except Exception as e:
        raise e
    return result


def getFileRevision(
    sw,
    configchan,
    filepath,
    revision
):
    """
    Description:
    Get revision of the specified config file

    Parameters:
        - string sessionKey
        - string configChannelLabel - label of config channel to lookup on
        - string filePath - config file path to examine
        - int revision - config file revision to examine

    Returns:
        - struct - Configuration Revision information
            - string "type"
                - file
                - directory
                - symlink
            - string "path" - File Path
            - string "target_path" - Symbolic link Target File Path.
            - string "channel" - Channel Name
            - string "contents" - File contents (base64 encoded according
                                to the contents_enc64 attribute)
            - boolean "contents_enc64" - Identifies base64 encoded content
            - int "revision" - File Revision
            - dateTime.iso8601 "creation" - Creation Date
            - dateTime.iso8601 "modified" - Last Modified Date
            - string "owner" - File Owner.
            - string "group" - File Group.
            - int "permissions" - File Permissions (Deprecated).
            - string "permissions_mode" - File Permissions.
            - string "selinux_ctx" - SELinux Context (optional).
            - boolean "binary" - true/false , Present for files only.
            - string "md5" - File's md5 signature. Present for files only.
            - string "macro-start-delimiter" - Macro start delimiter for
                                               a config file.
            - string "macro-end-delimiter" - Macro end delimiter for
                                               a config file.
    """
    try:
        result = sw.session.configchannel.getFileRevision(
            sw.key,
            configchan,
            filepath,
            revision
        )
    except Exception as e:
        raise e
    return result


def getFileRevisions(
    sw,
    channellabel,
    filepath
):
    """
    Description:
    Get list of revisions for specified config file

    Parameters:
        - string sessionKey
        - string channelLabel - label of config channel to lookup on
        - string filePath - config file path to examine

    Returns:
        - array:
    struct - Configuration Revision information
        - string "type"
            - file
            - directory
            - symlink
        - string "path" - File Path
        - string "target_path" - Symbolic link Target File Path.
        - string "channel" - Channel Name
        - string "contents" - File contents (base64 encoded according
                                     to the contents_enc64 attribute)
        - boolean "contents_enc64" - Identifies base64 encoded content
        - int "revision" - File Revision
        - dateTime.iso8601 "creation" - Creation Date
        - dateTime.iso8601 "modified" - Last Modified Date
        - string "owner" - File Owner.
        - string "group" - File Group.
        - int "permissions" - File Permissions (Deprecated).
        - string "permissions_mode" - File Permissions.
        - string "selinux_ctx" - SELinux Context (optional).
        - boolean "binary" - true/false , Present for files only.
        - string "md5" - File's md5 signature. Present for files only.
        - string "macro-start-delimiter" - Macro start delimiter for a config
                                            file.
        - string "macro-end-delimiter" - Macro end delimiter for a config file
    """
    try:
        result = sw.session.configchannel.getFileRevisions(
            sw.key,
            channellabel,
            filepath
        )
    except Exception as e:
        raise e
    return result


def listFiles(
    sw,
    channellabel
):
    """
    Description:
    Return a list of files in a channel.

    Parameters:
        - string sessionKey
        - string channelLabel - label of config channel to list files on.

    Returns:
        - array:
            - struct - Configuration File information
                - string "type"
                    - file
                    - directory
                    - symlink
                - string "path" - File Path
                - dateTime.iso8601 "last_modified" - Last Modified Date

    """
    try:
        result = sw.session.configchannel.listFiles(
            sw.key,
            channellabel
        )
    except Exception as e:
        raise e
    return result


def listGlobals(
    sw
):
    """
    Description:
    List all the global config channels accessible to the logged-in user.

    Parameters:
        - string sessionKey

    Returns:
        - array:
            - struct - Configuration Channel information
                - int "id"
                - int "orgId"
                - string "label"
                - string "name"
                - string "description"
                - string "type"
                - struct "configChannelType"
                - struct - Configuration Channel Type information
                    - int "id"
                    - string "label"
                    - string "name"
                    - int "priority"
    """
    try:
        result = sw.session.configchannel.listGlobals(
            sw.key
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
    Return a list of systems subscribed to a configuration channel

    Parameters:
        - string sessionKey
        - string channelLabel - label of config channel to list subscribed
          systems.

    Returns:
        - array:
            - struct - system
                - int "id"
                - string "name"
    """
    try:
        result = sw.session.configchannel.listSubscribedSystems(
            sw.key,
            channellabel
        )
    except Exception as e:
        raise e
    return result


def lookupChannelInfo(
    sw,
    configchannel
):
    """
    Description:
    Lists details on a list channels given their channel labels.

    Parameters:
        - string sessionKey
        - array:
            - string - configuration channel label

    Returns:
        - array:
            - struct - Configuration Channel information
                - int "id"
                - int "orgId"
                - string "label"
                - string "name"
                - string "description"
                - struct "configChannelType"
                - struct - Configuration Channel Type information
                    - int "id"
                    - string "label"
                    - string "name"
                    - int "priority"
    """
    try:
        result = sw.session.configchannel.lookupChannelInfo(
            sw.key,
            configchannel
        )
    except Exception as e:
        raise e
    return result


def lookupFileInfo(
    sw,
    channellabel,
    filepaths
):
    """
    Description:
    Given a list of paths and a channel, returns details about the latest
    revisions of the paths.

    Parameters:
        - string sessionKey
        - string channelLabel - label of config channel to lookup on
        - array:
            - string - List of paths to examine.

    Returns:
        - array:
            - struct - Configuration Revision information
                - string "type"
                    - file
                    - directory
                    - symlink
                - string "path" - File Path
                - string "target_path" - Symbolic link Target File Path.
                - string "channel" - Channel Name
                - string "contents" - File contents (base64 encoded according
                                            to the contents_enc64 attribute)
                - boolean "contents_enc64" - Identifies base64 encoded content
                - int "revision" - File Revision
                - dateTime.iso8601 "creation" - Creation Date
                - dateTime.iso8601 "modified" - Last Modified Date
                - string "owner" - File Owner.
                - string "group" - File Group.
                - int "permissions" - File Permissions (Deprecated).
                - string "permissions_mode" - File Permissions.
                - string "selinux_ctx" - SELinux Context (optional).
                - boolean "binary" - true/false , Present for files only.
                - string "md5" - File's md5 signature. Present for files only.
                - string "macro-start-delimiter" - Macro start delimiter for a
                                                   config file.
                - string "macro-end-delimiter" - Macro end delimiter for a
                                                 config file.

    """
    try:
        result = sw.session.configchannel.lookupFileInfo(
            sw.key,
            channellabel,
            filepaths
        )
    except Exception as e:
        raise e
    return result


def scheduleFileComparisons(
    sw,
    channellabel,
    filepath,
    serverids
):
    """
    Description:
    Schedule a comparison of the latest revision of a file against the version
    deployed on a list of systems.

    Parameters:
        - string sessionKey
        - string channelLabel - Label of config channel
        - string path - File path
        - array:
            - long - The list of server id that the comparison will be
                    performed on

    Returns:
        - int actionId - The action id of the scheduled action
    """
    try:
        result = sw.session.configchannel.scheduleFileComparisons(
            sw.key,
            channellabel,
            filepath,
            serverids
        )
    except Exception as e:
        raise e
    return result


def update(
    sw,
    channellabel,
    channelname,
    description
):
    """
    Description:
    Update a global config channel. Caller must be at least a config admin or
    an organization admin, or have access to a system containing this config
    channel.

    Parameters:
        - string sessionKey
        - string channelLabel
        - string channelName
        - string description

    Returns:
        - struct - Configuration Channel information
            - int "id"
            - int "orgId"
            - string "label"
            - string "name"
            - string "description"
            - struct "configChannelType"
            - struct - Configuration Channel Type information
                - int "id"
                - string "label"
                - string "name"
                - int "priority"
    """
    try:
        result = sw.session.configchannel.update(
            sw.key,
            channellabel,
            channelname,
            description
        )
    except Exception as e:
        raise e
    return result

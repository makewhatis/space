"""
``Namespace: system.config``
============================

Provides methods to access and modify many aspects of configuration channels
and server association. basically system.config name space

- :func:`addChannels`
- :func:`createOrUpdatePath`
- :func:`createOrUpdateSymlink`
- :func:`deleteFiles`
- :func:`deployAll`
- :func:`listChannels`
- :func:`listFiles`
- :func:`lookupFileInfo`
- :func:`removeChannels`
- :func:`setChannels`
"""


def addChannels(
    sw,
    system_ids,
    configuration_channels,
    addtotop
):
    """
    Description:
    Given a list of servers and configuration channels, this method appends
    the configuration channels to either the top or the bottom (whichever you
    specify) of a system's subscribed configuration channels list. The
    ordering of the configuration channels provided in the add list is
    maintained while adding. If one of the configuration channels in the 'add'
    list has been previously subscribed by a server, the subscribed channel
    will be re-ranked to the appropriate place.

    Parameters:
        - object session
        - array:
            - int - IDs of the systems to add the channels to.
        - array:
            - string - List of configuration channel labels in the ranked order
        - boolean addToTop
            - true - to prepend the given channels list to the top of the
                     configuration channels list of a server
            - false - to append the given channels list to the bottom of the
                      configuration channels list of a server

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.system.config.addChannels(
            sw.key,
            system_ids,
            configuration_channels,
            addtotop
        )
    except Exception as e:
        raise e

    return result


def createOrUpdatePath(
    sw,
    server_id,
    path,
    isdir,
    path_info,
    committolocal
):
    """
    Description:
    Create a new file (text or binary) or directory with the given path, or
    update an existing path on a server.

    Parameters:
        - object session
        - int server_id
        - string path - the configuration file/directory path
        - boolean isDir
            - True - if the path is a directory
            - False - if the path is a file
        - struct - path info
            - string "contents" - Contents of the file (text or base64 encoded
                                if binary) ((only for non-directories)
            - boolean "contents_enc64" - Identifies base64 encoded content
                                 (default: disabled, only for non-directories).
            - string "owner" - Owner of the file/directory.
            - string "group" - Group name of the file/directory.
            - string "permissions" - Octal file/directory permissions (eg: 644)
            - string "macro-start-delimiter" - Config file macro end delimiter.
                                Use null or empty string to accept the default.
                                (only for non-directories)
            - string "macro-end-delimiter" - Config file macro end delimiter.
                                 Use null or empty string to accept the default
                                 (only for non-directories)
            - string "selinux_ctx" - SeLinux context (optional)
            - int "revision" - next revision number, auto increment for null
            - boolean "binary" - mark the binary content, if True, base64
                                 encoded content is expected
                                 (only for non-directories)
        - int commitToLocal
            - 1 - to commit configuration files to the system's local
                  override configuration channel
            - 0 - to commit configuration files to the system's sandbox
                   configuration channel

    Returns:
        - struct - Configuration Revision information
            - string "type"
                - file
                - directory
                - symlink
            - string "path" - File Path
            - string "target_path" - Symbolic link Target File Path. Present
                                   for Symbolic links only.
            - string "channel" - Channel Name
            - string "contents" - File contents (base64 encoded according to
                                 the contents_enc64 attribute)
            - boolean "contents_enc64" - Identifies base64 encoded content
            - int "revision" - File Revision
            - dateTime.iso8601 "creation" - Creation Date
            - dateTime.iso8601 "modified" - Last Modified Date
            - string "owner" - File Owner. Present for files or directories
                                only.
            - string "group" - File Group. Present for files or directories
                                only.
            - int "permissions" - File Permissions (Deprecated). Present for
                                 files or directories only.
            - string "permissions_mode" - File Permissions. Present for files
                                         or directories only.
            - string "selinux_ctx" - SELinux Context (optional).
            - boolean "binary" - true/false , Present for files only.
            - string "md5" - File's md5 signature. Present for files only.
            - string "macro-start-delimiter" - Macro start delimiter for a
                                     config file. Present for text files only.
            - string "macro-end-delimiter" - Macro end delimiter for a config
                                     file. Present for text files only.

    Available since: 10.2
    """
    try:
        result = sw.session.system.config.createOrUpdatePath(
            sw.key,
            server_id,
            path,
            isdir,
            path_info,
            committolocal
        )
    except Exception as e:
        raise e

    return result


def createOrUpdateSymlink(
    sw,
    server_id,
    path,
    path_info,
    committolocal
):
    """
    Description:
    Create a new symbolic link with the given path, or update an existing path.

    Parameters:
        - object session
        - int server_id
        - string path - the configuration file/directory path
        - struct - path info
            - string "target_path" - The target path for the symbolic link
            - string "selinux_ctx" - SELinux Security context (optional)
            - int "revision" - next revision number, auto increment for null
        - int commitToLocal
            - 1 - to commit configuration files to the system's local override
                configuration channel
            - 0 - to commit configuration files to the system's sandbox
                configuration channel

    Returns:
        - struct - Configuration Revision information
            - string "type"
                - file
                - directory
                - symlink
            - string "path" - File Path
            - string "target_path" - Symbolic link Target File Path. Present
                                    for Symbolic links only.
            - string "channel" - Channel Name
            - string "contents" - File contents (base64 encoded according to
                                    the contents_enc64 attribute)
            - boolean "contents_enc64" - Identifies base64 encoded content
            - int "revision" - File Revision
            - dateTime.iso8601 "creation" - Creation Date
            - dateTime.iso8601 "modified" - Last Modified Date
            - string "owner" - File Owner. Present for files or directories
                                    only.
            - string "group" - File Group. Present for files or directories
                                    only.
            - int "permissions" - File Permissions (Deprecated). Present for
                                    files or directories only.
            - string "permissions_mode" - File Permissions. Present for files
                                    or directories only.
            - string "selinux_ctx" - SELinux Context (optional).
            - boolean "binary" - true/false , Present for files only.
            - string "md5" - File's md5 signature. Present for files only.
            - string "macro-start-delimiter" - Macro start delimiter for a
                                    config file. Present for text files only.
            - string "macro-end-delimiter" - Macro end delimiter for a
                                    config file. Present for text files only.

        Available since: 10.2
    """
    try:
        result = sw.session.system.config.createOrUpdateSymlink(
            sw.key,
            server_id,
            path,
            path_info,
            committolocal
        )
    except Exception as e:
        raise e

    return result


def deleteFiles(
    sw,
    server_id,
    paths,
    deletefromlocal
):
    """
    Description:
    Removes file paths from a local or sandbox channel of a server.

    Parameters:
        - object session
        - int server_id
        - array:
            - string - paths to remove.
        - boolean deletefromlocal
            - True - to delete configuration file paths from the system's
                    local override configuration channel
            - False - to delete configuration file paths from the system's
                    sandbox configuration channel

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.system.config.deleteFiles(
            sw.key,
            server_id,
            paths,
            deletefromlocal
        )
    except Exception as e:
        raise e

    return result


def deployAll(
    sw,
    system_ids
):
    """
    Description:
    Schedules a deploy action for all the configuration files on the given list
    of systems.

    Parameters:
        - object session
        - array system_ids:
            - int - id of the systems to schedule configuration files
                    deployment
            - dateTime.iso8601 date - Earliest date for the deploy action.

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.system.config.deployAll(
            sw.key,
            system_ids
        )
    except Exception as e:
        raise e

    return result


def listChannels(
    sw,
    system_id
):
    """
    Description:
    List all global configuration channels associated to a system in the order
    of their ranking.

    Parameters:
        - object session
        - int system_id

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
        result = sw.session.system.config.listChannels(
            sw.key,
            system_id
        )
    except Exception as e:
        raise e

    return result


def listFiles(
    sw,
    server_id,
    listlocal
):
    """
    Description:
    Return the list of files in a given channel.

    Parameters:
        - object session
        - int server_id
        - int listlocal
            - 1 - to return configuration files in the system's local override
                configuration channel
            - 0 - to return configuration files in the system's sandbox
                configuration channel

    Returns:
        - array:
            - struct - Configuration File information
                - string "type"
                    - file
                    - directory
                    - symlink
                - string "path" - File Path
                - string "channel_label" - the label of the central
                                    configuration channel that has this file.
                                    Note this entry only shows up if the file
                                    has not been overridden by a central
                                    channel.
                - struct "channel_type"
                - struct - Configuration Channel Type information
                    - int "id"
                    - string "label"
                    - string "name"
                    - int "priority"
                - dateTime.iso8601 "last_modified" - Last Modified Date
    """
    try:
        result = sw.session.system.config.listFiles(
            sw.key,
            server_id,
            listlocal
        )
    except Exception as e:
        raise e

    return result


def lookupFileInfo(
    sw,
    server_id,
    paths,
    searchlocal
):
    """
    Description:
    Given a list of paths and a server, returns details about the latest
    revisions of the paths.

    Parameters:
        - object session
        - int server_id
        - array:
            - string - paths to lookup on.
        - int searchlocal
            - 1 to search configuration file paths in the system's local
                override configuration or systems subscribed central channels
            - 0 to search configuration file paths in the system's sandbox
                configuration channel

    Returns:
        - array:
            - struct - Configuration Revision information
               - string "type"
                    * file
                    * directory
                    * symlink

                - string "path" - File Path
                - string "target_path" - Symbolic link Target File Path.
                    Present for Symbolic links only.
                - string "channel" - Channel Name
                - string "contents" - File contents (base64 encoded according
                    to the contents_enc64 attribute)
                - boolean "contents_enc64" - Identifies base64 encoded content
                - int "revision" - File Revision
                - dateTime.iso8601 "creation" - Creation Date
                - dateTime.iso8601 "modified" - Last Modified Date
                - string "owner" - File Owner. Present for files or directories
                    only.
                - string "group" - File Group. Present for files or directories
                    only.
                - int "permissions" - File Permissions (Deprecated). Present
                                    for files or directories only.
                - string "permissions_mode" - File Permissions. Present for
                                    files or directories only.
                - string "selinux_ctx" - SELinux Context (optional).
                - boolean "binary" - true/false , Present for files only.
                - string "md5" - File's md5 signature. Present for files only.
                - string "macro-start-delimiter" - Macro start delimiter for a
                                config file. Present for text files only.
                - string "macro-end-delimiter" - Macro end delimiter for a
                                config file. Present for text files only.

    Available since: 10.2
    """
    try:
        result = sw.session.system.config.lookupFileInfo(
            sw.key,
            server_id,
            paths,
            searchlocal
        )
    except Exception as e:
        raise e

    return result


def removeChannels(
    sw,
    system_ids,
    channel_labels
):
    """
    Description:
    Remove config channels from the given servers.

    Parameters:
        - object session
        - system_ids - array:
            - int - the IDs of the systems from which you would like to remove
                    configuration channels..
        - channel_labels - array:
            - string - List of configuration channel labels to remove.

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.system.config.removeChannels(
            sw.key,
            system_ids,
            channel_labels
        )
    except Exception as e:
        raise e

    return result


def setChannels(
    sw,
    system_ids,
    channel_labels
):
    """
    Description:
    Replace the existing set of config channels on the given servers.
    Channels are ranked according to their order in the configChannelLabels
    array.

    Parameters:
        - object session
        - system_ids - array:
            - int - IDs of the systems to set the channels on.
        - channel_labels - array:
            - string - List of configuration channel labels in the ranked order

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.system.config.setChannels(
            sw.key,
            system_ids,
            channel_labels
        )
    except Exception as e:
        raise e

    return result

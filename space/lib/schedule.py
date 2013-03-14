"""
``Namespace: schedule``
=======================

Methods to retrieve information about scheduled actions.

- :func:`archiveActions`
- :func:`cancelActions`
- :func:`deleteActions`
- :func:`listAllActions`
- :func:`listArchivedActions`
- :func:`listCompletedActions`
- :func:`listCompletedSystems`
- :func:`listFailedActions`
- :func:`listFailedSystems`
- :func:`listInProgressActions`
- :func:`listInProgressSystems`
- :func:`rescheduleActions`
"""


def archiveActions(
    sw,
    action_ids
):
    """
    Description:
    Archive all actions in the given list.

    Parameters:
        - session object
        - array:
            - int - action id

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.schedule.archiveActions(
            sw.key,
            action_ids
        )
    except Exception as e:
        raise e

    return result


def cancelActions(
    sw,
    action_ids
):
    """
    Description:
    Cancel all actions in given list. If an invalid action is provided,
    none of the actions given will canceled.

    Parameters:
        - session object
        - array:
            - int - action id

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.schedule.cancelActions(
            sw.key,
            action_ids
        )
    except Exception as e:
        raise e

    return result


def deleteActions(
    sw,
    action_ids
):
    """
    Description:
    Delete all archived actions in the given list.

    Parameters:
        - session object
        - array:
            - int - action id

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.schedule.deleteActions(
            sw.key,
            action_ids
        )
    except Exception as e:
        raise e

    return result


def listAllActions(
    sw
):
    """
    Description:
    Returns a list of all actions. This includes completed, in progress,
    failed and archived actions.

    Parameters:
    session object

    Returns:
        array:
            struct - action
                int "id" - Action Id.
                string "name" - Action name.
                string "type" - Action type.
                string "scheduler" - The user that scheduled the action.
                                    (optional)
                dateTime.iso8601 "earliest" - The earliest date and time the
                                              action will be performed
                int "completedSystems" - Number of systems that completed the
                                        action.
                int "failedSystems" - Number of systems that failed the action.
                int "inProgressSystems" - Number of systems that are in
                                          progress.
    """
    try:
        result = sw.session.schedule.listAllActions(
            sw.key
        )
    except Exception as e:
        raise e

    return result


def listArchivedActions(
    sw
):
    """
    Description:
    Returns a list of actions that have been archived.

    Parameters:
        - session object

    Returns:
        - array:
            - struct - action
                int "id" - Action Id.
                string "name" - Action name.
                string "type" - Action type.
                string "scheduler" - The user that scheduled the action.
                                     (optional)
                dateTime.iso8601 "earliest" - The earliest date and time the
                                              action will be performed
                int "completedSystems" - Number of systems that completed the
                                         action.
                int "failedSystems" - Number of systems that failed the action.
                int "inProgressSystems" - Number of systems that are in
                                          progress.
    """
    try:
        result = sw.session.schedule.listArchivedActions(
            sw.key
        )
    except Exception as e:
        raise e

    return result


def listCompletedActions(
    sw
):
    """
    Description:
    Returns a list of actions that have completed successfully.

    Parameters:
        - session object

    Returns:
        - array:
            - struct - action
                - int "id" - Action Id.
                - string "name" - Action name.
                - string "type" - Action type.
                - string "scheduler" - The user that scheduled the action.
                                       (optional)
                - dateTime.iso8601 "earliest" - The earliest date and time the
                                                 action will be performed
                - int "completedSystems" - Number of systems that completed
                                           the action.
                - int "failedSystems" - Number of systems that failed the
                                        action.
                - int "inProgressSystems" - Number of systems that are in
                                            progress.
    """
    try:
        result = sw.session.schedule.listCompletedActions(
            sw.key
        )
    except Exception as e:
        raise e

    return result


def listCompletedSystems(
    sw,
    action_id
):
    """
    Description:
    Returns a list of systems that have completed a specific action.

    Parameters:
        - session object
        - string action_id

    Returns:
        - array:
           - struct - system
                - int "server_id"
                - string "server_name" - Server name.
                - string "base_channel" - Base channel used by the server.
                - dateTime.iso8601 "timestamp" - The time the action was
                                                 completed
                - string "message" - Optional message containing details on the
                                     execution of the action. For example, if
                                     the action failed, this will contain the
                                     failure text.
    """
    try:
        result = sw.session.schedule.listCompletedSystems(
            sw.key,
            action_id
        )
    except Exception as e:
        raise e

    return result


def listFailedActions(
    sw
):
    """
    Description:
    Returns a list of actions that have failed.

    Parameters:
        - session object

    Returns:
        - array:
            - struct - action
                - int "id" - Action Id.
                - string "name" - Action name.
                - string "type" - Action type.
                - string "scheduler" - The user that scheduled the action.
                                       (optional)
                - dateTime.iso8601 "earliest" - The earliest date and time
                                                the action will be performed
                - int "completedSystems" - Number of systems that completed
                                            the action.
                - int "failedSystems" - Number of systems that failed the
                                        action.
                - int "inProgressSystems" - Number of systems that are in
                                            progress.
    """
    try:
        result = sw.session.schedule.listFailedActions(
            sw.key
        )
    except Exception as e:
        raise e

    return result


def listFailedSystems(
    sw,
    action_id
):
    """
    Description:
    Returns a list of systems that have failed a specific action.

    Parameters:
        - session object
        - string action_id

    Returns:
        - array:
            - struct - system
                - int "server_id"
                - string "server_name" - Server name.
                - string "base_channel" - Base channel used by the server.
                - dateTime.iso8601 "timestamp" - The time the action was
                                               completed
                - string "message" - Optional message containing details on the
                                   execution of the action. For example, if the
                                   action failed, this will contain the failure
                                   text.
    """
    try:
        result = sw.session.schedule.listFailedSystems(
            sw.key,
            action_id
        )
    except Exception as e:
        raise e

    return result


def listInProgressActions(
    sw
):
    """
    Description:
    Returns a list of actions that are in progress.

    Parameters:
        - session object

    Returns:
        - array:
            - struct - action
                - int "id" - Action Id.
                - string "name" - Action name.
                - string "type" - Action type.
                - string "scheduler" - The user that scheduled the action.
                                       (optional)
                - dateTime.iso8601 "earliest" - The earliest date and time the
                                                 action will be performed
                - int "completedSystems" - Number of systems that completed the
                                           action.
                - int "failedSystems" - Number of systems that failed the
                                        action.
                - int "inProgressSystems" - Number of systems that are in
                                            progress.
    """
    try:
        result = sw.session.schedule.listInProgressActions(
            sw.key
        )
    except Exception as e:
        raise e

    return result


def listInProgressSystems(
    sw,
    action_id
):
    """
    Description:
    Returns a list of systems that have a specific action in progress.

    Parameters:
        - session object
        - string action_id

    Returns:
        - array:
            - struct - system
                - int "server_id"
                - string "server_name" - Server name.
                - string "base_channel" - Base channel used by the server.
                - dateTime.iso8601 "timestamp" - The time the action was
                                                 completed
                - string "message" - Optional message containing details on the
                                    execution of the action. For example, if
                                    the action failed, this will contain the
                                    failure text.
    """
    try:
        result = sw.session.schedule.listInProgressSystems(
            sw.key,
            action_id
        )
    except Exception as e:
        raise e

    return result


def rescheduleActions(
    sw,
    action_ids,
    only_failed
):
    """
    Description:
    Reschedule all actions in the given list.

    Parameters:
        - session object
        - array:
            - int - action id
        - boolean onlyFailed - True to only reschedule failed actions, False to
                               reschedule all

    Returns:
        - int - 1 on success, exception thrown otherwise.
    """
    try:
        result = sw.session.schedule.rescheduleActions(
            sw.key,
            action_ids,
            only_failed
        )
    except Exception as e:
        raise e

    return result

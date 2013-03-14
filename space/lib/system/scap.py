"""
``Namespace: system.scap``
======================

Provides methods to schedule SCAP scans and access the results.

- :func:`getXccdfScanDetails`
- :func:`getXccdfScanRuleResults`
- :func:`listXccdfScans`
- :func:`scheduleXccdfScan`
"""


def getXccdfScanDetails(
    sw,
    scan_id
):
    """
    Description:
    Get details of given OpenSCAP XCCDF scan.

    Parameters:
        - object - session
        - int scan_id of XCCDF scan (xid).

    Returns:
        - struct - OpenSCAP XCCDF Scan
            - int "xid" - XCCDF TestResult id
            - int "sid" - serverId
            - int "action_id" - Id of the parent action.
            - string "path" - Path to XCCDF document
            - string "oscap_parameters" - oscap command-line arguments.
            - string "test_result" - Identifier of XCCDF TestResult.
            - string "benchmark" - Identifier of XCCDF Benchmark.
            - string "benchmark_version" - Version of the Benchmark.
            - string "profile" - Identifier of XCCDF Profile.
            - string "profile_title" - Title of XCCDF Profile.
            - dateTime.iso8601 "start_time" - Client machine time of scan start
            - dateTime.iso8601 "end_time" - Client machine time of scan
                                            completion.
            - string "errors" - Stderr output of scan.
    """
    try:
        result = sw.session.system.scap.getXccdfScanDetails(
            sw.key,
            scan_id
        )
    except Exception as e:
        raise e

    return result


def getXccdfScanRuleResults(
    sw,
    scan_id
):
    """
    Description:
    Return a full list of RuleResults for given OpenSCAP XCCDF scan.

    Parameters:
        - object - session
        - int scan_id of XCCDF scan (xid).

    Returns:
        - array:
            - struct - OpenSCAP XCCDF RuleResult
                - string "idref" - idref from XCCDF document.
                - string "result" - Result of evaluation.
                - string "idents" - Comma separated list of XCCDF idents.
    """
    try:
        result = sw.session.system.scap.getXccdfScanRuleResults(
            sw.key,
            scan_id
        )
    except Exception as e:
        raise e

    return result


def listXccdfScans(
    sw,
    server_id
):
    """
    Description:
    Return a list of finished OpenSCAP scans for a given system.

    Parameters:
        - object - session
        - int server_id

    Returns:
        - array:
            - struct - OpenSCAP XCCDF Scan
                - int "xid" - XCCDF TestResult ID
                - string "profile" - XCCDF Profile
                - string "path" - Path to XCCDF document
                - dateTime.iso8601 "completed" - Scan completion time
    """
    try:
        result = sw.session.system.scap.listXccdfScans(
            sw.key,
            server_id
        )
    except Exception as e:
        raise e

    return result


def scheduleXccdfScan(
    sw,
    server_id,
    path,
    additional_params,
    date_time=None
):
    """
    Description:
    Schedule OpenSCAP scan.

    Parameters:
        - object - session
        - array: int - server_id || int - server_id
        - string Path to xccdf content on targeted systems.
        - string Additional parameters for oscap tool.
        - dateTime.iso8601 date - Date to schedule action (Optional)

    Returns:

    int - ID if SCAP action created.
    """
    try:
        if date_time:
            result = sw.session.system.scap.scheduleXccdfScan(
                sw.key,
                server_id,
                path,
                additional_params,
                date_time
            )
        else:
            result = sw.session.system.scap.scheduleXccdfScan(
                sw.key,
                server_id,
                path,
                additional_params
            )

    except Exception as e:
        raise e

    return result

# -*- coding: utf-8 *-*
import argparse
import space.lib.api as sapi

def list(sw, args):
    """
    Lists all available api calls grouped by namespace
    """
    parser = argparse.ArgumentParser(
        prog='space api list',
        description='Add child channels to an activation key add an ' +
        'activationkey for child channels.'
    )

    parser.parse_args(args)

    calls = sapi.getApiCallList(sw)

    if calls:
        for call in calls:
            for name, info in calls.items():
                #names.append(info)
                for i,k in info.items():
                    print("%s : %s - %s" % (name, k['name'], k['parameters']))
    
    else:
        print("No calls in api. Most likely lies")
    return calls

Modules
=======

Add more module functions
-------------------------

Module functions can be placed inside the module dir::

    space/modules

Each function that is not prepended with _ will be considered
a viable command. The functions take a session and an args list
(which is passed in from the cli) as arguments::

    def dosomething(sess, args):
        
        parser = argparse.ArgumentParser(
            prog='space systems list',
            epilog='For detailed help ' +
            'pass --help to a target',
            description=('This command will ' +
            'list all spacewalk systems.')
        )
        parser.add_argument(
            '-g', '--group',
            default=None,
            required=False,
            help="System Group Name"
        )

        ... logic


Rather than porting the entire library, there is a single function in the swSession class `space.swSession.call` that allows the api function to be called. 

::

    sw = space.swSession()
    sw.call('api.getApiNamespaceList', arg)



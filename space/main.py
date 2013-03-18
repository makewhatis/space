"""
`main` is the main entry point for the cli
"""

import datetime
import imp
import json
import os
import re
import sys
import argparse
from getpass import getpass
from getpass import getuser
import signal

if sys.version_info >= (3, 0):
    import xmlrpc.client
    xmlrpc = xmlrpc.client
    from configparser import SafeConfigParser

if sys.version_info <= (2, 8):
    import xmlrpclib
    xmlrpc = xmlrpclib
    from ConfigParser import SafeConfigParser

sys.path.insert(0, os.path.dirname(__file__))

MODULE_DIR = os.path.join(
    os.path.dirname(
        os.path.abspath(__file__)), 'modules'
)

CONFIG = os.path.join(
    os.environ['HOME'], '.space/config.ini'
)
APP_NAME = "space"


# handle ctrl+c
def signal_handler(signal, frame):
        print("")
        sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)


def main(config=None):
    """
    Main function. Entry point in which we will route any requests to modules
    or argparse.
    """

    args = sys.argv
    # remove the filename arg
    args.pop(0)

    functions = load_funcs(config)

    # pull all the switches and values
    args, flags = parse_flags(args)

    # clean up args so that cargs only contains non-switch args
    args, cargs = clean_args(args)

    # debug stuff
    #print("flags: %d" % len(flags))
    #print("commands: %d\n\n" % len(cargs))
    #print("commands: %s\n\n" % cargs)
    #print("args: %s" % args)

    # check to see if we only have space + top level command
    # if so we throw a list of avail funcs for that top level
    # then exit
    if len(cargs) == 1:
        print(
            "Usage: space [options] '<namespace>'" +
            " <command> [arguments]"
        )

        # declare variables
        namespace = None
        avail = []

        for f, inst in functions.items():
            m = re.match('([a-z]*)\.([a-z_]*)', f)
            if m.group(1) == cargs[0]:
                # set namespace variable
                namespace = m.group(1)
                avail.append(m.group(2))

        if namespace and len(avail) > 0:
            print(
                "\nAvailable commands in " +
                "\"%s\" namespace:" % namespace
            )
            for a in avail:
                print(" %s" % (a))

            print(
                "\n* For help on any individual command, " +
                "just use the --help flag after."
            )
            return

        return print_avail_namespace_help()

    # first we check version
    # then check for major flags
    # then for actual command args
    if 'version' in flags:
        # need to pull this dynamically
        return '1.1'

    if 'docs' in flags:
        print_help()
        return

    if 'user' in flags:
        user = flags['user']
    else:
        user = None

    # we already pass config as an arg to this def
    # the flag will trumph all though
    if 'config' in flags:
        config = flags['config']

    if 'host' in flags:
        host = flags['host']
    else:
        host = None

    if 'logout' in flags:
            _logout(
                user=user,
                config=config
            )
            return

    if len(cargs) < 1:
        return print_avail_namespace_help()

    # check initial arg to see if its in the modules
    if "%s.%s" % (cargs[0], cargs[1]) in functions.keys():
        # loop through loaded functions
        for f in functions.keys():
            m = re.match('([a-z]*)\.([a-z_]*)', f)
            if m:
                top = m.group(1)
                sub = m.group(2)

            # check to see if a top level command has been called
            if top in args:

                # there should be at least one more, as we dont have top level
                # commands without sub commands yet
                if sub in args:

                    # second level command is found. Start prepping that.
                    module_path = "%s.%s" % (top, sub)

                    # need to pop off the two commands we already know about
                    args.pop(0)
                    args.pop(0)

                    # if the compiled module is in our function dict, as a key,
                    # then lets feed it args and call it
                    if module_path in functions.keys():
                        sw = _session(
                            user=user,
                            url=host,
                            config=config
                        )
                        functions[module_path](sw, args)
                        return True


def clean_args(args):
    result = []
    for arg in args:
        if not re.match('^--.*', arg):
            result.append(arg)
    return args, result


def parse_flags(args):
    """
    Parse options before commands. Once a non flag switch
    is found args are passed back with the pre switches
    split out.
    """
    result = {}
    end = False
    # this is needed because we are altering the list
    # so its necessary to return a list copy
    # http://stackoverflow.com/a/14465613/145851
    for arg in list(args):
        if end:
            return args, result

        if re.match('.*=.*', arg):
            m = re.match('^-+(.*)=(.*)', arg)
            result[m.group(1)] = m.group(2)
            index = args.index(m.group(0))
            args.pop(index)

        elif re.match('^-+(?!=).*', arg):
            m = re.match('^-+(.*)', arg)
            result[m.group(1)] = None
            index = args.index(m.group(0))
            args.pop(index)

        elif re.match('[a-zA-Z].*', arg):
            end = True
    return args, result


def load_funcs(config=None):

    modules = list()
    modules_dict = dict()
    functions = dict()
    module_dir = None

    if not config:
        module_dir = os.path.join(
            os.path.dirname(
                os.path.abspath(__file__)),
            'modules'
        )
    else:
        conffile = os.path.expanduser(config)
        confparse = SafeConfigParser()
        # does the file exist, if so, read from it...
        if os.path.isfile(conffile):

            confparse.read(conffile)
            if confparse.has_section('main'):
                module_dir = confparse.get('main', 'module_dir')
            else:
                print("main section not found!")
                return False
        else:
            print("Conf file not found!")
            return False

    # loop through files in the module dir
    for mod_ in os.listdir(module_dir):
        if mod_.startswith('_'):
            continue
        bare_ = mod_.rfind('.')
        if bare_ > 0:
            naked_ = mod_[:bare_]
        modules_dict[naked_] = mod_

    # loop through dict and load modules. Using the imp module here
    # to programatically load these modules
    for m, k in modules_dict.items():
        mod_, path, desc = imp.find_module(m, [module_dir])
        module = imp.load_module(m, mod_, path, desc)
        modules.append(module)

    # ripping out the name and functions of each module
    for mod in modules:
        module_name = mod.__name__.rsplit('.', 1)[-1]
        # listing attributes to find actual functions
        for attr in dir(mod):
            attr_name = '{0}.{1}'.format(module_name, attr)
            if attr.startswith('_'):
                continue
            if callable(getattr(mod, attr)):
                func = getattr(mod, attr)

                if isinstance(func, type):
                    # Ignore exception functions
                    if any(['Error' in func.__name__,
                            'Exception' in func.__name__]):
                        continue
                # add callable function to our loaded lib
                functions[attr_name] = func

    # Loop through and inject some sweetness into here.
    for mod in modules:
        if not hasattr(mod, '__sweet__'):
            mod.__sweet__ = functions

    return functions


def _session(
    user=None,
    password=None,
    now=None,
    url=None,
    session_dir=None,
    session_file=None,
    config=None
):
    """
    Will try and handle the session management here
    """

    # checking for keyword params. This is mostly to make testing possible.
    if not user:
        if not config:
            config = CONFIG
        if os.path.exists(config):
            confparse = SafeConfigParser()
            confparse.read(config)
            login = None
            if confparse.has_section('spacewalk'):
                if confparse.has_option('spacewalk', 'login'):
                    login = confparse.get('spacewalk', 'login')
                if login is None:
                    user = getuser()
                else:
                    user = login
        else:
            user = getuser()
            # need to implement logging
            #print("Config not present, using system login: %s" % user)

    if not url:
        if not config:
            config = CONFIG
        if os.path.exists(config):
            confparse = SafeConfigParser()
            confparse.read(config)
            if confparse.has_section('spacewalk'):
                if confparse.has_option('spacewalk', 'hostname'):
                    url = confparse.get('spacewalk', 'hostname')

    if not now:
        now = datetime.datetime.now().strftime('%s')

    if not session_dir:
        session_dir = '%s/.swsession' % (os.environ['HOME'])

    if not session_file:
        session_file = "%s/%s.session" % (session_dir, user)

    if user is None:
        sys.exit("Could not get username, is your config present?")
    session_data = {'%s' % user: 0, 'time': '%s' % int(now)}

    # handle initial creation of session dir
    if not os.path.exists(session_dir):
        os.makedirs(session_dir)

    # load session data if file exists for user else create
    if os.path.exists(session_file):

        with open(session_file, 'r') as f:
            s = json.load(f)

        # if session time is not 0
        if s['time'] is not 0:
            # calculate time session was last validated/init
            c = int(now) - int(s['time'])
            if c > 3600:
                print("expired. please login again")
                sw = swSession(
                    login=user,
                    config=config,
                    password=password
                )
                s[user] = str(sw.key)
                s['hostname'] = str(sw.hostname)
                s['time'] = int(now)
                d = json.dumps(s, session_file)
                _write_session(session_file, d)
                return sw
            else:
                # just refresh the time in the session file
                s['time'] = int(now)
                j = json.dumps(s, session_file)
                _write_session(session_file, j)
                return swSession(
                    login=user,
                    password=password,
                    config=config,
                    key=s.get(user),
                    url=s['hostname']
                )
        else:
            sw = swSession(
                login=user,
                password=password,
                config=config,
                url=url
            )
            session_data[user] = str(sw.key)
            session_data['hostname'] = str(sw.hostname)
            s = json.dumps(session_data, session_file)
            _write_session(session_file, s)
            return sw

    else:
        sw = swSession(
            login=user,
            password=password,
            config=config,
            url=url
        )
        session_data[user] = str(sw.key)
        session_data['hostname'] = str(sw.hostname)
        s = json.dumps(session_data, session_file)
        _write_session(session_file, s)
        return sw


def _logout(
    user=None,
    config=None
):
    """
    Will try and handle the session logout here
    """
    if config:
        if os.path.exists(config):
            confparse = SafeConfigParser()
            confparse.read(config)
            user = None
            if confparse.has_section('spacewalk'):
                if confparse.has_option('spacewalk', 'login'):
                    user = confparse.get('spacewalk', 'login')

    # check for current session file
    if not user:
        user = getuser()

    session_dir = '%s/.swsession' % (os.environ['HOME'])
    session_file = "%s/%s.session" % (session_dir, user)

    if os.path.exists(session_file):
        os.remove(session_file)
        print("Logged out.")
    else:
        print("No active sessions.")
    return


def _write_session(filename, data):
    with open(filename, 'w+') as f:
        f.write(data)


def get_user(user=None):
    """
    asks user for username.
    """
    # hack to deal with py2/py3
    try:
        inputs = raw_input
    except:
        inputs = input
        pass
    if user:
        inputs = user

    user = str(inputs('Please enter your spacewalk login: ')).strip()
    return user


def get_hostname(hostname=None):
    """
    asks user for username.
    """
    # hack to deal with py2/py3
    try:
        inputs = raw_input
    except:
        inputs = input
        pass
    if hostname:
        inputs = hostname

    hostname = str(inputs('Please enter a spacewalk host: ')).strip()
    return hostname


def get_pass(username='', getpass=getpass):
    """
    prompts for a password for an existing user
    """
    # we only need the getpass stuff if prompting for passwords.
    # This only happens on session init.

    passwd = getpass(
        'Please enter the spacewalk creds for user %s: ' % username)
    return passwd.strip()


def getauth(conffile, hostname):
    """
    config format:
    [hostname]
    login = username
    password = pass

    returns:
    tuple: (username, password)

    parameters:
    filename(str)           - configuration file path
    hostname(str)         - spacewalk hostname
    """

    login = None
    passwd = None

    # create
    srcfile = os.path.expanduser(conffile)

    confparse = SafeConfigParser()
    # does the file exist, if so, read from it...
    if os.path.isfile(srcfile):
        confparse.read(srcfile)
        if confparse.has_section(hostname):
            login = confparse.get(hostname, 'login')
            passwd = confparse.get(hostname, 'password')

    return str(login).strip(), str(passwd).strip()


class swSession(object):
    """
    Spacewalk Class that will be handing us a session object back.

    If the config is not present, we prompt for values needed
    to authenticate our Spacewalk session.
    """

    def __init__(
            self,
            url=None,
            login=None,
            password=None,
            config=None,
            key=None
    ):
        """
        returns swsession
        """
        if not config:
            config = CONFIG
        if os.path.isfile(config):
            confparse = SafeConfigParser()
            confparse.read(config)
        else:
            confparse = None
            #sys.exit("Cannot find config! ex. ~/.space/config.ini")

        if url:
            self.hostname = url
        else:
            self.hostname = None
            if confparse:
                if confparse.has_section('spacewalk'):
                    if confparse.has_option('spacewalk', 'hostname'):
                        self.hostname = confparse.get('spacewalk', 'hostname')
            else:
                self.hostname = get_hostname()

        if login:
            self.login = login
        else:
            self.login = None
            if confparse:
                try:
                    if confparse.has_section('spacewalk'):
                        if confparse.has_option('spacewalk', 'login'):
                            self.login = confparse.get('spacewalk', 'login')
                            if len(self.login) == 0:
                                self.login = None

                except:
                    sys.exit("config file in wrong format")
            else:
                login = get_user()

        self.server_api = "https://%s/rpc/api" % self.hostname
        self.server_push = "https://%s/APP" % self.hostname
        # passwords are private variables. Cached, but not exposed

        if password:
            self._password = password
        else:
            self._password = None
            if confparse:
                try:
                    if confparse.has_section('spacewalk'):
                        if confparse.has_option('spacewalk', 'password'):
                            self._password = confparse.get(
                                'spacewalk', 'password')
                except:
                    sys.exit("config file in wrong format")

        self.config = config

        # authentication config (order of precedence)
        # 1. login and password as args
        # 2. login and password from config file
        # 3. prompt for missing information

        # If login and/or password are specified explicitly they override
        # the config file
        if self.login is None \
            and self._password is None \
            and self.config is not None\
                and not key:

            self.login, self._password = getauth(self.config, self.hostname)

        # see what we got back and prompt if required:
        if str(self.login) == 'None' and not key:
            self.login = get_user()

        if str(self._password) == 'None' and not key:
            self._password = get_pass(self.login)

        try:

            self.session = xmlrpc.Server(self.server_api, verbose=0)

            if key:
                self.key = key
            else:
                try:
                    # actually login
                    self.key = self.session.auth.login(
                        self.login, self._password
                    )
                except Exception as e:
                    sys.exit("Login to %s Failed." % self.server_api)

        except xmlrpc.Fault as e:
            sys.exit("Login Failed: %s" % e)

    def call(self, ns, args):
        func = getattr(self.session, ns)

        try:
            results = func(self.key, *args)
        except Exception as e:
            raise

        return results


def print_help():
    functions = load_funcs()
    print("Help Docs\n")
    for func, inst in functions.items():
        print("space %s %s" % (
            func.split(".")[0], func.split(".")[1])
        )
        print(inst.__doc__)
    return functions


def print_short_help():
    functions = load_funcs()
    print(
        "Usage: space [options] '<namespace>' <command> [arguments]" +
        "\nFor detailed help on " +
        "any one command: [command] --help \n" +
        "\nAvailable Commands\n" +
        "------------------"
    )
    for func, inst in functions.items():
        print("space %s %s" % (
              func.split(".")[0], func.split(".")[1])
              )
    return functions


def print_avail_namespace_help():
    functions = load_funcs()
    print(
        "Usage: space [options] '<namespace>' <command> [arguments]\n" +
        "Options:\n" +
        "    --user         Spacewalk login name\n" +
        "    --password     Spacewalk password\n" +
        "    --host         Spacewalk host\n" +
        "    --config       optional config file to pass user/pass/host\n" +
        "                   info\n" +
        "    --docs         Print full docs to the terminal\n"
        "\nFor detailed help on \n" +
        "any one command: [command] --help \n" +
        "\nAvailable Namespaces\n" +
        "------------------"
    )
    funcs = []
    for func, inst in functions.items():
        f = func.split(".")[0]
        if f not in funcs:
            funcs.append(f)

    for top in funcs:
        print(" %s" % (top))

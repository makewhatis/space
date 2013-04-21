.. _quickstart:

Quick Start
===========

Getting start is easy. Make sure you have a couple prereqs though:

 * space module is installed
 * a working Spacewalk Server
 * python 2.6+ or 3.2+

Installation
------------

::

    pip install python-space
    

Authenticating
--------------

Authenticating can be done one of three ways:

 * Auth credentials stored in a config file
 * Command-line Flags
 * Command-line prompt

Space will check in the above order for credentials and config
info. If it doesn't find a valid config, and no flags are given
with the needed info, then it will prompt for info.

The prompt is going to be the easiest one-off method of interfacing
with spacewalk. Simply run a command, and it will prompt you for 
your:

 * host
 * username
 * password

You can also throw your info in flags::

    ~]$ space --username=me --hostname=example.spacewalk.server --password=blah

Once autheticated, there will be a session activated, and until expired,
will serve as a means for space to get session, and hostname info for your instance.

Note: you will still need to give auth info right now, the session was put there
to alleviate the amount of sessions getting created in spacewalk on big loops.

To logout or kill your session, run::

    space --logout

For sake of automating all the things, there may be a need for using a config
file to store auth credentials. By default space looks in $HOME/.space/config.ini

::

    mkdir ~/.space
    vim ~/.space/config.ini
    chmod 600 ~/.space/config.ini

add::

    [spacewalk]
    hostname= <HOSTNAME> eg. spacewalk.example.com
    username = <LOGIN>
    password = <PASSWORD>
    module_dir = <CUSTOM MODULE DIRECTORY>

This config can also be placed at /etc/space/config.ini

A config file can also be specified as a command line option::

    space --config=/path/to/config.ini systems list

The order that space checks for configs is:

    1. --config flag
    2. $HOME/.space/config.ini
    3. /etc/space/config.ini

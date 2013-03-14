.. _quickstart:

Quick Start
===========

Getting start is easy. Make sure you have a couple prereqs though:

 * space module is installed
 * a working Spacewalk Server

Authenticating
--------------

Authenticating can be done one of two ways:

 * CLI prompt
 * Auth credentials stored in a config file

CLI prompt is going to be the easiest one-off method of interfacing
with spacewalk. Simply run a command, and it will prompt you for 
your:

 * host
 * username
 * password

Once autheticated, there will be a session activated, and until expired,
will serve as authentication. 

To logout or kill your session, run::

    space --logout

For sake of automating all the things, there may be a need for using a config
file to store auth credentials. 

::

    [spacewalk]
    hostname = localhost 
    login = testuser
    password = letmein

The default location for this will be $HOME/.space , although a config file
can be specified as a command line option::

    space --config=/path/to/config.cfg systems listsystems


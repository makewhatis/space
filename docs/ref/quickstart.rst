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

    git clone git://github.com/makewhatis/spacewalk-cli.git
    cd spacewalk-cli
    python setup.py


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

A config file can also be specified as a command line option::

    space --config=/path/to/config.cfg systems listsystems


Working with the API to create new modules
------------------------------------------

Rather than porting the entire library, there is a single function in the swSession class `space.swSession.call` that allows the api function to be called. 

::

    sw = space.swSession()
    sw.call('api.getApiNamespaceList', [arg])

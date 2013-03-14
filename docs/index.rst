.. Space documentation master file, created by
   sphinx-quickstart on Thu Feb 28 12:56:59 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Space: A Spacewalk CLI
======================

Space is a command line interface python wrapper aimed at exposing the Spacewalk/RHN api to a easy to use command line interface. 

Some of the tasks and queries performed via Spacewalk UI be cumbersome, and time consuming, especially if you work with a fairly large implementation. Space helps ease the walk. 

Commands are grouped via the API namespaces for easy reference, and basic sessions make running multiple commands painless. 

::
    
    ~]$ space systems listsystems -g test_group

If you don't wish to use the CLI, then all methods are available as imports, taking at least an authenticated session object as a parameter.



User Guide
----------

This section will cover basic usage of this tool.

.. toctree::
   :maxdepth: 2

   ref/quickstart.rst



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


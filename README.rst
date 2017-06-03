============
simple-geoip
============
.. image:: https://travis-ci.org/Tethik/simplegeoip.png?branch=master
    :target: https://travis-ci.org/Tethik/simplegeoip
    :alt: Travis-CI

.. image:: https://codecov.io/gh/Tethik/simplegeoip/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/Tethik/simplegeoip
    :alt: codecov

.. image:: https://img.shields.io/pypi/v/nine.svg   
    :target: https://pypi.python.org/pypi/simplegeoip
    :alt: Latest version    

.. image:: https://img.shields.io/pypi/pyversions/simplegeoip.svg
    :target: https://pypi.python.org/pypi/simplegeoip/
    :alt: Supported python versions
    
.. image:: https://img.shields.io/github/license/Tethik/simplegeoip.svg   
    :target: https://github.com/Tethik/simplegeoip/blob/master/LICENSE
    

Dead simple geoip package. Pretty much just a wrapper around `maxminddb <https://github.com/maxmind/MaxMind-DB-Reader-python/>`_ 
that automatically downloads the geolite database for you. You can either do this manually using the 'download_latest_database' function 
or let the script do it automatically when it detects no database is installed.

Can be used as a package or standalone script.

Install
-------

.. code-block:: bash

    pip install simplegeoip


Usage
-----
As a python package.

.. code-block:: python

    import simplegeoip

    # Gets a dict with country/city information, if there is no database it will be downloaded automatically 
    simplegeoip.lookup('127.0.0.1')
    # Downloads an updated database into simplegeoip's application directory
    simplegeoip.download_latest_database()
    # Tells you when the database was last updated by maxmind
    simplegeoip.last_updated()
    # Returns a maxminddb reader object, if there is no database it will be downloaded automatically 
    simplegeoip.reader()
    

The same as above but as a standalone script

.. code-block:: bash

    simplegeoip 8.8.8.8
    simplegeoip update
    simplegeoip info 


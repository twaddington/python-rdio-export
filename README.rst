python-rdio-export
==================

.. image:: https://img.shields.io/pypi/dm/python-rdio-export.svg
    :target: https://pypi.python.org/pypi/python-rdio-export

This exporter can be used to backup the collection of an Rdio user. It
includes a command-line utility script and a library for bundling into
your own applications. The command-line utility will output results
to stdout by default.

If you like this library and it's saved you some time, please consider
supporting further development with a `Gittip donation`_!

Requirements
------------

- requests
- requests_oauthlib

Installing
----------

::

    $ pip install python-rdio-export

Authentication
--------------

You'll need to acquire API credentials from the `Rdio developer site`_.

When using the command-line utility you can authenticate with Rdio
one of three ways.

First, by providing your credentials to the command-line utility
directly:

::
    
    $ rdio-export --user twaddington --key your_api_key --secret your_api_secret

You can also (optionally) provide your Rdio credentials via two environment
variables:

::

    $ export RDIO_CONSUMER_KEY=your_api_key
    $ export RDIO_CONSUMER_SECRET=your_api_secret
    
You can also (optionally) provide your Rdio credentials via a global config
file located in :code:`~/.rdioconfig` with the format:

::

    [Rdio]
    rdioConsumerKey=your_api_key
    rdioConsumerSecret=your_api_secret

..

    Note: Credentials are parsed in the order listed above. For example, the
    script will first attempt to use credentials provided via the
    :code:`--key` and :code:`--secret` arguments. Next, credentials will be
    loaded from the environment variables. Finally, the config file will be
    examined for credentials.

Examples
--------

    Note: Results will be printed to stdout by default.

Export by username:

::

    $ rdio-export --user twaddington

Export by email:

::

    $ rdio-export --email tristan.waddington@gmail.com

Export to a file:

::

    $ rdio-export --user twaddington > rdio-backup.txt

Bug reports
-----------

If you encounter any issues, please open a new issue on the project's
`GitHub page`_.

License
-------

See the LICENSE_ file.

.. _Gittip donation: https://www.gittip.com/twaddington/
.. _LICENSE: https://github.com/twaddington/python-rdio-export/blob/master/LICENSE 
.. _GitHub page: https://github.com/twaddington/python-rdio-export
.. _Rdio developer site: http://www.rdio.com/developers/

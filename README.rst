python-rdio-export
==================

This exporter can be used to backup the collection of an Rdio user. It
includes a command-line utility script and a library for bundling into
your own applications.

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

Examples
--------

Export by username:

::

    $ rdio-export --user twaddington

Export by email:

::

    $ rdio-export --email tristan.waddington@gmail.com

Publishing
----------

::

    # Register with pypi (only done once)
    $ python setup.py register

    # Upload a new source distribution to pypi
    $ python setup.py sdist upload

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

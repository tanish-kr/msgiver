msgiver
=======

|Build Status|

msgiver will deliver the text to Messenger.

It is currently available for delivery to the following messenger.

-  Slack
-  Gitter
-  RocketChat

Install
-------

::

    $ git clone https://github.com/kitaro-tn/msgiver.git
    $ cd msgiver
    $ make install

Useage
------

::

    usage: msgiver [-h] {slack,gitter,setting} ...

    msgiver will deliver the text to Messenger.

    positional arguments:
      {slack,gitter,setting}
                            sub-command help
        slack               msgiver for Slack
        gitter              msgiver for Gitter
        setting             msgiver setting

    optional arguments:
      -h, --help            show this help message and exit

Setting msgiver
~~~~~~~~~~~~~~~

Generate msgiver setting file.

::

    $ msgiver setting

::

    usage: msgiver setting [-h]

    optional arguments:
      -h, --help  show this help message and exit

Post Slack
~~~~~~~~~~

::

    $ msgiver slack <message>

::

    usage: msgiver slack [-h] [-i ICON] [-c CHANNEL] [-s] message

    positional arguments:
      message               Slack post message

    optional arguments:
      -h, --help            show this help message and exit
      -i ICON, --icon ICON  Slack api icon url
      -c CHANNEL, --channel CHANNEL
                            Slack post channel
      -s, --syntax          Syntax highlight message

Development
-----------

::

    $ make develop

Test
~~~~

::

    $ make test

or

::

    $ python -m unittest tests

PEP8
~~~~

::

    $ pep8 msgiver

Watcher
~~~~~~~

::

    $ make watcher

Issues
------

-  https://github.com/kitaro-tn/msgiver/issues

.. |Build Status| image:: https://travis-ci.org/kitaro-tn/msgiver.svg?branch=master
   :target: https://travis-ci.org/kitaro-tn/msgiver

sra_py Documentation
====================

sra_py is a python wrapper for
`some-random-api <https://some-random-api.ml/>`__

Requirements
------------

1. `Python 3.6 or more <https://python.org/>`__
2. pip

Installation
------------

Versions of sra_py on PyPI are outdated. v2.0 is currently being
developed and can be installed using git.

Note: this requires git.

.. code:: shell

   pip install git+https://github.com/Atidipt123/sra_py.git

Quick start
-----------

First we need to define a client.

.. code:: py

   from sra_py import Client

   client = Client()

Now lets fetch a cat image using our client.

.. code:: py

   import os

   img = client.animal.get_image('cat')
   img.save('some-cat-image-file.png')
   os.startfile('some-cat-image-file.png')

Clients
-------
**Docs for Clients** - :doc:`client`

.. toctree::
   :maxdepth: 2

   client
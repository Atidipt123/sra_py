*class* **Pokemon**
===================

Properties
----------

    | **json**
    (`dict <https://docs.python.org/3/library/stdtypes.html#dict>`__) -
    The json data returned by the website
    | **stats**
    (`dict <https://docs.python.org/3/library/stdtypes.html#dict>`__) -
    Stats of the pokemon as a dictionary
    | **family**
    (`dict <https://docs.python.org/3/library/stdtypes.html#dict>`__) -
    Evolution stage of the pokemon as a dictionary
    | **name** , **id\_** , **description** , **image\_url** ,
    **gif\_url** , **type** , **species** , **height** , **weight** ,
    **gender** , **evolution\_stage** , **evolution\_line** ,
    **egg\_group** , **hp** , **attack** , **defence** , **sp\_attack**
    , **sp\_defence** , **total** , **speed** , **base\_experience** ,
    **abilities** , **generation**

*class* **Meme**
================

Properties
----------

    | **image\_url**
    (`str <https://docs.python.org/3/library/stdtypes.html#str>`__) -
    Image url of the meme
    | **category**
    (`str <https://docs.python.org/3/library/stdtypes.html#str>`__) -
    Category of the meme
    | **caption**
    (`str <https://docs.python.org/3/library/stdtypes.html#str>`__) -
    Caption of the meme
    | **id\_**
    (`str <https://docs.python.org/3/library/stdtypes.html#str>`__) - ID
    of the meme

Functions
---------

save()
~~~~~~

Parameters
^^^^^^^^^^

**None**

Returns
^^^^^^^

Saves the meme and returns true if it was a success

Return Type
^^^^^^^^^^^

`Bool <https://docs.python.org/3/library/stdtypes.html#boolean>`__

*class* **GIF**
===============

Properties
----------

    **gif\_url**
    `str <https://docs.python.org/3/library/stdtypes.html#str>`__ - URL
    of the gif

Functions
---------

save()
~~~~~~

Parameters
^^^^^^^^^^

**None**

Returns
^^^^^^^

Saves the gif and returns true if it was a success

Return Type
^^^^^^^^^^^

`Bool <https://docs.python.org/3/library/stdtypes.html#boolean>`__

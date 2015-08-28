===================
Maya Dynamic Import
===================

I was tired of constantly having to manage my paths when creating directory
structures for my scripts. This frustration inspired *mdynaimport*.

mdynaimport dynamically import all paths it finds from given starting
point. It support both python and mel paths.


Installation
------------

Put **mdynaimport.py** in a script directory already on mayas PYTHONPATH. For
convenience I place it in: ``c:\users\<username>\Documents\maya\script``.
This ensures that it will just work for all different maya versions.

Then you just place the **userSetup.py** in the directory you want to
dynamically import. If you already have a userSetup in place just add the
below code to it:

.. code:: python

    import mdynaimport
    mdynaimport.parse_paths()


Usage
-----

I prefer not to mix mel and python scripts, to keep it clear and easy to
find I use a file structure as bellow:

::

    scripts\
        MEL\
        PYTHON\
        userSetup.py
        mdynaimport.py


This will let mdynaimport separate the mel paths from the python paths.

This is **optional**, mdynaimport will determine what kind of path it is by
looking at available extensions in a directory. This is just how I prefer to
have it setup.


Custom Paths, Ignore patterns and Icons
---------------------------------------

Close to the top in the **mdynaimport.py** file you will find these variables:

.. code:: python

    # Custom paths
    PYENV = 'PYROOT'
    MELENV = 'MELROOT'

    # Include patterns to ignore here.
    EXCLUDE_PATTERNS = ('__', '.')
    ICONS = ('icon', 'icons')

To add custom paths you will need to have created an environment variable with
your paths added to it. Then replace PYENV and MELENV values with your
own environment names.

EXCLUDE_PATTERNS patterns is a tuple containing directory name patterns to
ignore. ICONS represents directory names that contains icons to be placed
in Mayas XBMLANGPATH.


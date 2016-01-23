Maya Dynamic Import
===================

I was tired of constantly having to manage my paths when creating directory
structures for my scripts. This frustration inspired *dynaimport*.

dynaimport dynamically import all paths it finds from given starting
point. It support both python and mel paths.


Installation
------------

Put **dynaimport.py** in a script directory already on mayas PYTHONPATH. For
convenience I place it in: ``c:\users\<username>\Documents\maya\script``.
This ensures that it will just work for all different maya versions.

Then place the **userSetup.py** provided in the directory you want to
dynamically import. There can be several of the same *userSetup.py* at
different location. As long as the path you put it in is in the *PYTHONPATH*
maya will try to execute the *userSetup*.

If you already have a *userSetup* in place then paste the following at the
top of userSetup.

```python
    import dynaimport
    dynaimport.parse_paths()
```

**This is important**, if you try to dynamically import
a path and launch a script but this happens before dynaimport the script
will not execute until you try to launch it again inside of maya.


Usage
-----

I prefer not to mix mel and python scripts, to keep it clear and easy to
find I use a file structure as bellow:

    scripts\
        MEL\
        PYTHON\
        userSetup.py
        dynaimport.py


This will let dynaimport separate the mel paths from the python paths.

This is **optional**, dynaimport will determine what kind of path it is by
looking at available extensions in a directory. This is just how I prefer to
have it setup.


Custom Paths, Ignore patterns and Icons
---------------------------------------

Close to the top in the **dynaimport.py** file you will find these variables:

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


Maya Dynamic Import
===================

mdynaimport is a Maya dynamic importer.

Most third party scripts comes with it's own separate folder structure, I
was tired of constantly having to check that my paths were in order. This
motivated me to create a script that updates search paths dynamically.

mdynaimport allows you to drag and drop your scripts into your script
structure and it should just work.


Installation
------------

To install mdynaimport, simply put mdynaimport.py in a folder on your mayas
PYTHONPATH... Any default script directory will do. Then simply put this block
of code into a userSetup.py in the folders you wish to dynamically import:

..code-block:: python

    import mdynaimport
    mdynaimport.parse_paths()
    ...

For convenience I place mdynaimport.py into the topmost scriptfolder in the
default maya preference path. usually:

..code-block:: bash

    c:\users\<username>\Documents\maya\script
    ...

This is the preferred way the folder structure should look where you want
mdynaimport to operate.

..code-block:: bash

    script/
        MEL/
        PYTHON/
        userSetup.py
        mdynaimport.py
    ...

That allows me to just drag and drop scripts/script-dir straight into
the folders without additional setup.

If you spread out your scripts over several folders just have a
userSetup.py in each and add the above lines. The mdynaimport.py only
needs to exist in one of the folders for you to have access to it.

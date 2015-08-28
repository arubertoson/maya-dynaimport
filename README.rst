===================
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

Put mdynaimport.py and userSetup.py in the topmost folder you want to
dynamically import. I use the topmost script folder in Maya's default
pref folder:

    c:\users\<username>\Documents\maya\script


If you already have a userSetup.py in use just add these lines:

.. code:: python

    import mdynaimport
    mdynaimport.parse_paths()


Usage
-----

To get the most out of mdynaimport its preferred that you have a directory
named "mel" in the same directory as the userSetup.py is:


    \\scripts
        \\MEL
        \\PYTHON
        userSetup.py
        mdynaimport.py


This will let mdynaimport look through the MEL directory and add all found
folders to the MAYA_SCRIPT_PATH environment. The rest of the found directories
will be added to sys.path in maya.

Now you can create your own folder structure without having to manage path
control. Just add a userSetup.py that runs mdynaimport in the topmost
directory.


Custom Paths
------------

To add custom paths you will need to have an environment variable with your
custom paths added to. At the top of mdynaimport you will see two variables:

..code-block:: python
PYENV = 'PYROOT'
MELENV = 'MELROOT'

Just change the values to your custom path, or create an environment with the
variable names and your are good to go.

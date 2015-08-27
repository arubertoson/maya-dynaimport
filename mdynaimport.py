# -*- coding: utf-8 -*-
"""
    mdynaimport.py
    ~~~~~~~~~~~~~~

    Was tired of constantly having to check my paths, so created a script
    that places search paths in maya specific environments.

    Place mdynaimport and userSetup.py in your script rootfolder, for
    convenience I use:

        "c:\users\<username>\Documents\maya\script"

    which should be on the same level as the normal preference (2015-x64/2015)
    folder. If you already have a userSetup.py just add the lines:

        import mdynaimport
        mdynaimport.parse_paths()

    I've structured my folder to contain one MEL and one PYTHON directory.

        script/
            MEL/
            PYTHON/
            userSetup.py
            mdynaimport.py

    That allows me to just drag and drop scripts/script-dir straight into
    the folders without additional setup.

    If you spread out your scripts over several folders just have a
    userSetup.py in each and add the above lines. The mdynaimport.py only
    needs to exist in one of the folders for you to have access to it.

    USAGE::

        >>> import mdynaimport
        >>> mdynaimport.parse_paths()

"""
import os
import site
import collections


__title__ = 'mdynaimport'
__author__ = 'Marcus Albertsson'
__email__ = 'marcus.arubertoson@gmail.com'
__url__ = "PATH/TO/GIT"
__version__ = '0.1.0'
__license__ = 'MIT'
__description__ = 'Dynamically import script paths to maya.'


PYENV = 'PYROOT'
MELENV = 'MELROOT'

# Include patterns to ignore here.
EXCLUDE_PATTERNS = ('__', '.')
ICONS = ('icon', 'icons')


def parse_paths():
    """
    Walks the source paths and place them in appropriate environment
    variables.
    """
    sources = get_source_paths()
    results = collections.defaultdict(list)
    for source_type, paths in sources.iteritems():

        for p in paths:
            subdirs = walkdirs(p)
            for dir in subdirs:
                print(dir)
                # Add paths to environments
                if os.path.basename(dir).lower().startswith(ICONS):
                    results['XBMLANGPATH'].append(dir)
                    os.environ['XBMLANGPATH'] += os.pathsep + dir

                if source_type == 'MEL':
                    results['MAYA_SCRIPT_PATH'].append(dir)
                    os.environ['MAYA_SCRIPT_PATH'] += os.pathsep + dir
                else:
                    results['PYTHONPATH'].append(dir)
                    site.addsitedir(dir)
    return results


def walkdirs(root):
    """
    Returns generator with all subdirs excluding given patterns and python
    packages.
    """
    for root, subdirs, files in os.walk(root):
        subdirs[:] = [
            d for d in subdirs
            if not d.startswith(EXCLUDE_PATTERNS)
            if '__init__.py' not in os.listdir(os.path.join(root, d))
        ]
        yield root


def get_source_paths():
    """
    Return valid paths from __file__ dir, PYENV and MELENV.
    """
    script_paths = collections.defaultdict(set)

    pyenv = filter(None, os.environ.get(PYENV).split(os.pathsep))
    melenv = filter(None, os.environ.get('PYROOT').split(os.pathsep))
    script_paths['python'].update(pyenv)
    script_paths['mel'].update(melenv)

    cwd = os.path.dirname(os.path.abspath(__file__))
    for p in os.listdir(cwd):
        if not os.path.isdir(p):
            continue

        if os.path.basename(p).lower().startswith('mel'):
            script_paths['mel'].append(p)
        else:
            script_paths['python'].append(p)
    return script_paths

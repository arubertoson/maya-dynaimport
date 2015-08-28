# -*- coding: utf-8 -*-

"""
    mdynaimport.py
    ~~~~~~~~~~~~~~

    Was tired of not being able to create a custom directory structure
    without having to constantly fiddle with paths.

    With mdynaimport in a maya PYTHONPATH just run through a userSetup.py
    to have the dir dynamically import paths.


    USAGE::

        >>> import mdynaimport
        >>> mdynaimport.parse_paths()

"""
import os
import site
import logging
import collections

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


__title__ = 'mdynaimport'
__author__ = 'Marcus Albertsson'
__email__ = 'marcus.arubertoson@gmail.com'
__url__ = 'http://github.com/arubertoson/maya-mdynaimport'
__version__ = '0.1.0'
__license__ = 'MIT'
__description__ = 'Dynamically import script paths to maya.'


# Custom paths
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
    for root_dir in sources:

        for script_type, dirs in walkdirs(root_dir).iteritems():

            for d in dirs:
                logger.debug(d)

                # Add paths to environments
                if os.path.basename(d).lower().startswith(ICONS):
                    results['XBMLANGPATH'].append(d)
                    os.environ['XBMLANGPATH'] += os.pathsep + d

                if script_type == 'mel':
                    results['MAYA_SCRIPT_PATH'].append(d)
                    os.environ['MAYA_SCRIPT_PATH'] += os.pathsep + d
                else:
                    results['PYTHONPATH'].append(d)
                    site.addsitedir(d)
    return results


def walkdirs(root):
    """
    Returns defaultdict with script type / paths mapping, excluding given
    patterns and python packages.
    """
    scriptype_paths = collections.defaultdict(list)
    for root, subdirs, files in os.walk(root):
        subdirs[:] = [
            d for d in subdirs
            if not d.startswith(EXCLUDE_PATTERNS)
            if '__init__.py' not in os.listdir(os.path.join(root, d))
        ]

        if [f for f in files if f.endswith('.py')]:
            scriptype_paths['python'].append(root)
        if [f for f in files if f.endswith('.mel')]:
            scriptype_paths['mel'].append(root)
    return scriptype_paths


def get_source_paths():
    """
    Return valid paths from __file__ dir, PYENV and MELENV.
    """
    script_paths = set()
    script_paths.update(filter(None, os.environ.get(PYENV).split(os.pathsep)))
    script_paths.update(None, os.environ.get('PYROOT').split(os.pathsep))

    cwd = os.path.dirname(os.path.abspath(__file__))
    for each in os.listdir(cwd):
        path = os.path.join(cwd, each)
        if not os.path.isdir(path) or each.startswith(EXCLUDE_PATTERNS):
            continue
        script_paths.add(path)

    return script_paths

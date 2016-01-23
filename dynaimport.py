"""
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
logger.setLevel(logging.INFO)


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

# Include search patterns here.
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
    scriptype_paths = collections.defaultdict(set)
    for root, subdirs, files in os.walk(root):

        # Filter subdirs
        tmpdir = []
        for i in subdirs:
            if i.startswith(EXCLUDE_PATTERNS):
                continue
            if '__init__.py' in os.listdir(os.path.join(root, i)):
                scriptype_paths['python'].add(root)
                continue
            tmpdir.append(i)
        subdirs[:] = tmpdir

        # If files with extension exists add to right source type.
        if ext_exists('.py', files):
            scriptype_paths['python'].add(root)
        if ext_exists('.mel', files):
            scriptype_paths['mel'].add(root)
    return scriptype_paths


def ext_exists(ext, files):
    for f in files:
        if f.endswith(ext):
            return True
    else:
        return False


def get_source_paths():
    """
    Return valid paths from __file__ dir, PYENV and MELENV.
    """
    script_paths = set()
    try:
        script_paths.update(filter(None, os.environ.get(PYENV).split(os.pathsep)))
        script_paths.update(filter(None, os.environ.get(MELENV).split(os.pathsep)))
    except AttributeError:
        logger.debug('No custom environ variables set.')

    cwd = os.path.dirname(os.path.abspath(__file__))
    for each in os.listdir(cwd):
        path = os.path.join(cwd, each)
        if not os.path.isdir(path) or each.startswith(EXCLUDE_PATTERNS):
            continue
        script_paths.add(path)

    return script_paths

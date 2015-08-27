#! C:\Program Files\Autodesk\Maya2015\bin\mayapy
# -*- coding: utf-8 -*-

"""Tests for mdynaimport."""

import os
import sys
import unittest
import itertools


import mdynaimport
import maya.standalone


class MDynaImportTest(unittest.TestCase):

    def setUp(self):
        maya.standalone.initialize(name='python')

    def test_get_source_paths(self):
        result = mdynaimport.get_source_paths()
        self.assertIsInstance(result, dict)
        self.assertIsInstance(result.values()[0], set)

        for p in itertools.chain.from_iterable(result.itervalues()):
            self.assertIsInstance(p, basestring)
            self.assertTrue(os.path.isdir(p), True)

    def test_parse_paths(self):
        result = mdynaimport.parse_paths()
        for key, values in result.iteritems():
            self.assertIn(key,
                          ['XBMLANGPATH', 'MAYA_SCRIPT_PATH', 'PYTHONPATH'])
            if key == 'PYTHONPATH':
                env = sys.path
            else:
                env = [
                    os.path.abspath(p)
                    for p in os.environ[key].split(os.pathsep)
                ]
            for p in values:
                self.assertIn(os.path.abspath(p), env)


if __name__ == '__main__':
    unittest.main()

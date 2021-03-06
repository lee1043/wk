#!/usr/bin/env python
from distutils.core import setup

setup (name = "WK",
       version='8.0',
       description = "Package to compute and draw the Wheeler-Kiladis figures",
       url = "http://cdat.sf.net, see WK 99",
       packages = ['WK'],
       package_dir = {'WK': 'lib'},
       data_files = [("share/wk",["share/test_data_files.txt"])],
       
      )

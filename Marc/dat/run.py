#!/usr/bin/env python
# run this module using runpy
import os
import runpy
import importlib


os.chdir("D:/Vigneswaranwork/Interface_development/Marc/dat")
current_work_dir = os.getcwd()
print(current_work_dir)


importlib.import_module('scan_file')
runpy.run_module(mod_name='scan_file', init_globals=None,
                 run_name='__main__', alter_sys=False)

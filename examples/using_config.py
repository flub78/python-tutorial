#!/usr/bin/python
# -*- coding:utf8 -*

import os
import importlib.util
# from package.config import *

conf_file = "config.py"  # This can be set dynamically at runtime
spec = importlib.util.spec_from_file_location("config", f"examples\package\{conf_file}")
config = importlib.util.module_from_spec(spec)
spec.loader.exec_module(config)
# from package.config import *

print ("verbose = ", config.verbose)
print ("user = ", config.user)
print ("password = ", config.password)
print ("host = ", config.host)
print ("database = ", config.database)
print ("list_of_users = ", config.list_of_users)
print ("dict_of_users = ", config.dict_of_users)

print ("bye")

os.system("pause")




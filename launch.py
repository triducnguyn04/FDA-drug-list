'''
Basic functions of launch.py 
1) Initialize graphics and settings
2) Update database
'''
import cache
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/database')
from database import database_update

# database_update
if cache.Settings.update_database == True:
    database_update.update()

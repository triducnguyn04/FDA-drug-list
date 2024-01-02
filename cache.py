# this script includes all cache data and settings for the application
import os
import sys
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/database')
from database import database_update
from database import analysis 

class Data:
    def __init__(self):
        self.data = analysis.product_analysis()

class Settings:
    def __init__(self):
        self.update_database = False



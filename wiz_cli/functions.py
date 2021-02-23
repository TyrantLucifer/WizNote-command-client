"""
@author: tyrantlucifer
@contact: tyrantlucifer@gmail.com
@blog: https://tyrantlucifer.com
@file: functions.py
@time: 2021/2/23 14:42
@desc: 
"""
from wiz_cli.common import *

class UpdateConfigurations(object):

    def __init__(self):
        pass

    @staticmethod
    def update_username(username):
        Setting.set_value("username", username)
        logger.info("Update username to {0}".format(username))

    @staticmethod
    def update_password(password):
        Setting.set_value("password", password)
        logger.info("Update password to {0}".format(password))




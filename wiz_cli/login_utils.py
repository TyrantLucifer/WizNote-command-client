"""
@author: tyrantlucifer
@contact: tyrantlucifer@gmail.com
@blog: https://tyrantlucifer.com
@file: login_utils.py
@time: 2021/2/23 13:16
@desc: 
"""
import requests
from wiz_cli.setting_utils import *


class UserLogin(object):

    def __init__(self):
        pass

    @is_init_username(Setting.get_value("username"))
    def get_token(self):
        username = Setting.get_value("username")
        password = Setting.get_value("password")
        user_login_url = "{0}/as/user/login".format(init_config.wiz_server)
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {
            "userId": username,
            "password": password
        }
        result = requests.post(user_login_url, headers=headers, data=data)
        result_dict = result.json()
        if result_dict['returnCode'] == 200:
            token = result_dict['result']['token']
            kb_server = result_dict['result']['kbServer']
            kb_guid = result_dict['result']['kbGuid']
            Setting.set_value("token", token)
            Setting.set_value("kb_server", kb_server)
            Setting.set_value("kb_guid", kb_guid)
            logger.info("Get user token successfully.")
            logger.info("Login wiz note successfully.")
        else:
            logger.error("Get user token failed.")
            logger.error("Login wiz note failed.")
            logger.error("Filed reason: {0}".format(result_dict['returnMessage']))
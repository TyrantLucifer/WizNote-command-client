"""
@author: tyrantlucifer
@contact: tyrantlucifer@gmail.com
@blog: https://tyrantlucifer.com
@file: init_utils.py
@time: 2021/2/23 12:50
@desc: 初始化配置工具类
"""
import os
import configparser


class InitConfig(object):
    """初始化工具类

    属性:
        version 版本号
        home_dir 家目录
        config_dir 配置目录
        config_file 配置文件
        log_file 日志文件
        kb_server 笔记存储服务器地址
        kb_guid 用户唯一标识号
        token api认证票据
        token token生成时间
        wiz_server 为知笔记用户登录服务器
    """

    def __init__(self):
        self.version = "0.0.3"
        self.username = "admin"
        self.password = "admin"
        self.kb_server = ""
        self.kb_guid = ""
        self.token = ""
        self.token_time = ""
        self.wiz_server = "https://as.wiz.cn"
        self.home_dir = os.path.expanduser('~')
        self.config_dir = os.path.join(self.home_dir,
                                       '.wiz-command-client')
        self.config_file = os.path.join(self.config_dir,
                                        'config.ini')
        self.log_file = os.path.join(self.config_dir,
                                     'wiz-cli.log')

        if not self.__is_exist_config_dir():
            self.__create_config_dir()

    def __is_exist_config_dir(self):
        if os.path.exists(self.config_dir):
            return True
        else:
            return False

    def __init_config_file(self):
        config = configparser.ConfigParser()
        config.add_section('default')
        config.set('default', 'username', self.username)
        config.set('default', 'password', self.password)
        config.set('default', 'kb_server', self.kb_server)
        config.set('default', 'kb_guid', self.kb_guid)
        config.set('default', 'wiz_server', self.wiz_server)
        config.set('default', 'token_time', "1990-01-01 00:00:00")
        with open(self.config_file, 'w+') as file:
            config.write(file)

    def __create_config_dir(self):
        os.mkdir(self.config_dir)
        with open(self.config_file, 'w') as file:
            file.write('')
        self.__init_config_file()

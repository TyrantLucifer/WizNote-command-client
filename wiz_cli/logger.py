"""
@author: tyrantlucifer
@contact: tyrantlucifer@gmail.com
@blog: https://tyrantlucifer.com
@file: logger.py
@time: 2021/2/23 13:09
@desc: 
"""
import time
import sys
import logging
from wiz_cli.init_utils import *

# 初始化工具类init_utils.InitConfig
init_config = InitConfig()

# 初始化全局logger记录格式及级别
logger = logging.getLogger("wiz-cli")
logger.setLevel(logging.DEBUG)

# 初始化全局logger控制台终端记录格式及级别
stream_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - [%(funcName)s] - %(levelname)s: %('
                              'message)s')
stream_handler.setLevel(logging.INFO)
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

# 初始化全局logger文件记录格式及级别
log_file_handler = logging.FileHandler(init_config.log_file)
log_file_handler.setLevel(logging.DEBUG)
log_file_handler.setFormatter(formatter)
logger.addHandler(log_file_handler)


# 定义计算函数运行时间装饰器
def calculate(func):
    def main(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        logger.info("Func - {0} Total time: {1}s".format(func.__name__,
                                                         round(time.time() - start, 2)))

    return main


# 定义判断用户名是否初始化装饰器
def is_init_username(username):
    def wrapper(func):
        def judge(*args, **kwargs):
            if username == "admin":
                logger.error('Username is not initialized. Please initialize username use --set-username option.')
                sys.exit(1)
            else:
                func(*args, **kwargs)

        return judge

    return wrapper

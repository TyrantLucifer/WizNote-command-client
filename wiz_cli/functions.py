"""
@author: tyrantlucifer
@contact: tyrantlucifer@gmail.com
@blog: https://tyrantlucifer.com
@file: functions.py
@time: 2021/2/23 14:42
@desc: 为主函数main提供功能封装
"""
from wiz_cli.upload_utils import *
from wiz_cli.print_utils import *


class UpdateConfigurations(object):
    """更新配置工具类

    方法:
        update_username 更新用户名
        update_password 更新密码
    """
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


class Upload(object):
    """提供上传功能封装工具类

    """
    def __init__(self):
        pass

    @staticmethod
    @calculate
    def upload(file, category):
        upload_note = UploadNote(file, category=category)
        upload_note.upload()

    @staticmethod
    @calculate
    def update(file, doc_guid):
        upload_note = UploadNote(file)
        upload_note.update(doc_guid)


class Display(object):
    """显示信息工具类

    属性:
        get_info 获取信息工具类
    方法:
        display_version 显示版本号
        display_categories 显示笔记目录列表
    """
    get_info = GetInfo()
    category_list_table = DrawCategoryListTable()
    note_list_table = DrawNoteListTable()

    def __init__(self):
        pass

    @staticmethod
    def display_categories():
        category_list = Display.get_info.get_all_categories()
        for category in category_list:
            Display.category_list_table.append(name=category)
        Display.category_list_table.print()

    @staticmethod
    def display_version():
        print(init_config.version)

    @staticmethod
    def display_notes(category):
        note_list = Display.get_info.get_all_notes(category)
        for note in note_list:
            Display.note_list_table.append(title=note["title"],
                                           doc_guid=note["doc_guid"])
        Display.note_list_table.print()



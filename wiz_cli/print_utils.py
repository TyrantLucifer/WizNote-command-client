"""
@author: tyrantlucifer
@contact: tyrantlucifer@gmail.com
@blog: https://tyrantlucifer.com
@file: print_utils.py
@time: 2021/2/25 19:32
@desc: 提供打印工具类
"""
from prettytable import PrettyTable


class DrawCategoryListTable(object):
    """打印目录列表

    属性:
        None
    """
    def __init__(self):
        self.table = []
        header = [
            "name"
        ]
        self.x = PrettyTable(header)
        self.x.reversesort = True

    def append(self, **kwargs):
        if kwargs:
            content = [
                kwargs['name']
            ]
            self.x.add_row(content)

    def str(self):
        return str(self.x)

    def print(self):
        print(self.str())


class DrawNoteListTable(object):
    """打印笔记列表

    属性:
        None
    """
    def __init__(self):
        self.table = []
        header = [
            "title",
            "doc_guid"
        ]
        self.x = PrettyTable(header)
        self.x.reversesort = True

    def append(self, **kwargs):
        if kwargs:
            content = [
                kwargs["title"],
                kwargs["doc_guid"]
            ]
            self.x.add_row(content)

    def str(self):
        return str(self.x)

    def print(self):
        print(self.str())
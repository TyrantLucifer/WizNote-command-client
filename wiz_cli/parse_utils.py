"""
@author: tyrantlucifer
@contact: tyrantlucifer@gmail.com
@blog: https://tyrantlucifer.com
@file: parse_utils.py
@time: 2021/2/23 15:12
@desc: 
"""
import re


class ParseMarkdown(object):
    """提供解析markdown文件功能

    使用正则匹配笔记中所有的图片地址，并将markdown内容加入html头包裹
    """
    def __init__(self, file):
        with open(file, "r", encoding='utf-8') as f:
            self.content = f.read()
        self.content = "<html><body><pre>" + self.content + "</pre></body></html>"

    def get_all_resources(self):
        resources = re.findall(r'!\[.*?\]\((.*?)\)', self.content, re.S)
        return resources



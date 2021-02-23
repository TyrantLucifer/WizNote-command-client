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

    def __init__(self, file):
        with open(file, "r", encoding='utf-8') as f:
            self.content = f.read()
        self.content = "<html><body><pre>" + self.content + "</pre></body></html>"

    def get_all_resources(self):
        resources = re.findall(r'!\[.*?\]\((.*?)\)', self.content, re.S)
        return resources



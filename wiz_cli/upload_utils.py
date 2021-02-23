"""
@author: tyrantlucifer
@contact: tyrantlucifer@gmail.com
@blog: https://tyrantlucifer.com
@file: upload_utils.py
@time: 2021/2/23 16:34
@desc: 
"""
import json
from requests_toolbelt.multipart.encoder import MultipartEncoder
from wiz_cli.login_utils import *
from wiz_cli.parse_utils import *


class UploadNote(object):
    """提供笔记上传功能工具类

    参数:
        file 笔记
        category 为知笔记目录

    笔记上传流程： 创建空笔记 -> 上传笔记图片资源至为知服务器 -> 笔记替换资源url -> 更新笔记
    """
    def __init__(self, file, category):
        UserLogin.get_token()
        self.file = file
        self.category = category
        self.upload_url = "{0}/ks/note/create/{1}".format(Setting.get_value("kb_server"),
                                                          Setting.get_value("kb_guid"))
        self.headers = {
            "X-Wiz-Token": Setting.get_value("token")
        }
        self.doc_guid = ""

    def upload_empty_note(self):
        html = "<html><head></head><body></body></html>"
        data = {
            "kbGuid": Setting.get_value("kb_guid"),
            "html": html,
            "title": self.file,
            "category": self.category
        }
        self.headers["Content-Type"] = "application/json"
        result = requests.post(self.upload_url, headers=self.headers, data=json.dumps(data))
        result_dict = result.json()
        if result_dict['returnCode'] == 200:
            self.doc_guid = result_dict['result']['docGuid']
            logger.info("Create empty note: {0} successfully.".format(self.file))
        else:
            logger.error("Create empty note: {0} failed.".format(self.file))
            logger.error("Failed reason: {0}".format(result_dict['returnMessage']))

    def upload_resource(self, resource):
        upload_url = "{0}/ks/resource/upload/{1}/{2}".format(Setting.get_value("kb_server"),
                                                             Setting.get_value("kb_guid"),
                                                             self.doc_guid)
        if sys.platform.find("win") >= 0:
            resource_name = resource.split("\\")[-1]
        else:
            resource_name = resource.split("/")[-1]
        resource_type = resource_name.split(".")[-1]
        multipart_encoder = MultipartEncoder(
            fields={
                "kbGuid": Setting.get_value("kb_guid"),
                "docGuid": self.doc_guid,
                'data': (resource_name, open(resource, 'rb'), 'image/{0}'.format(resource_type))
            }
        )
        self.headers['Content-Type'] = multipart_encoder.content_type
        result = requests.post(upload_url, headers=self.headers, data=multipart_encoder)
        result_dict = result.json()
        if result_dict['returnCode'] == 200:
            name = result_dict['name']
            url = result_dict['url']
            logger.info("Upload resource: {0} successfully.".format(resource))
            logger.debug("Resource information, name: {0}, url: {1}".format(name, url))
            return name, url
        else:
            logger.error("Upload resource: {0} failed.".format(resource))

    def upload_note(self):
        resources_list = list()
        parse_markdown = ParseMarkdown(self.file)
        resources = parse_markdown.get_all_resources()
        for resource in resources:
            name, url = self.upload_resource(resource)
            resources_list.append(name)
            parse_markdown.content = parse_markdown.content.replace(resource, url)
        data = {
            "html": parse_markdown.content,
            "resources": resources_list,
            "docGuid": self.doc_guid,
            "kbGuid": Setting.get_value("kb_guid")
        }

        self.headers['Content-Type'] = "application/json"

        upload_url = "{0}/ks/note/save/{1}/{2}".format(Setting.get_value("kb_server"),
                                                       Setting.get_value("kb_guid"),
                                                       self.doc_guid)
        result = requests.put(upload_url, headers=self.headers, data=json.dumps(data))
        result_dict = result.json()
        if result_dict['returnCode'] == 200:
            logger.info("Upload note: {0} successfully.".format(self.file))
        else:
            logger.error("Upload note: {0} failed.".format(self.file))
            logger.error("Failed reason: {0}".format(result_dict['returnMessage']))

    def upload(self):
        self.upload_empty_note()
        self.upload_note()


class GetInfo(object):

    def __init__(self):
        UserLogin.get_token()
        self.headers = {
            "X-Wiz-Token": Setting.get_value("token")
        }

    def get_all_categories(self):
        request_url = "{0}/ks/category/all/{1}".format(Setting.get_value("kb_server"),
                                                       Setting.get_value("kb_guid"))
        result = requests.get(request_url, headers=self.headers)
        result_dict = result.json()
        if result_dict["returnCode"] == 200:
            logger.info("Get all list of categories successfully.")
            return result_dict['result']
        else:
            logger.error("Get all list of categories failed.")
            logger.error("Failed reason: {0}".format(result_dict['returnMessage']))
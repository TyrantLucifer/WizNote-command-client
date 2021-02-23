"""
@author: tyrantlucifer
@contact: tyrantlucifer@gmail.com
@blog: https://tyrantlucifer.com
@file: upload_utils.py
@time: 2021/2/23 16:34
@desc: 
"""
from requests_toolbelt.multipart.encoder import MultipartEncoder
from wiz_cli.login_utils import *
from wiz_cli.parse_utils import *


class Upload(object):

    def __init__(self, file):
        self.user_login = UserLogin()
        self.user_login.get_token()
        self.file = file
        self.upload_url = "{0}/ks/note/create/{1}".format(Setting.get_value("kb_server"),
                                                          Setting.get_value("kb_guid"))
        self.headers = {
            "X-Wiz-Token": Setting.get_value("token")
        }
        self.doc_guid = ""

    def upload_empty_note(self, category):
        html = "<html><head></head><body></body></html>"
        data = {
            "kbGuid": Setting.get_value("kb_guid"),
            "html": html,
            "title": self.file,
            "category": category
        }
        self.headers["Content-Type"] = "application/json"
        result = requests.post(self.upload_url, headers=self.headers, data=data)
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
            parse_markdown.content = re.sub(repr(resource),
                                            url,
                                            parse_markdown.content,
                                            re.S)


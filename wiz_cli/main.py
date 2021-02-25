"""
@author: tyrantlucifer
@contact: tyrantlucifer@gmail.com
@blog: https://tyrantlucifer.com
@file: main.py
@time: 2021/2/23 13:02
@desc: main入口
"""
import argparse
from wiz_cli.functions import *


def get_parser():
    parser = argparse.ArgumentParser(description="The wiz note command client based python.",
                                     epilog='Powered by tyrantlucifer. If you have any questions, you can send e-mail '
                                            'to tyrantlucifer@gmail.com')

    parser.add_argument("--set-username", metavar="username", help="set wiz username")
    parser.add_argument("--set-password", metavar="password", help="set wiz password")
    parser.add_argument("--category", metavar="category", help="assign note category")
    parser.add_argument("--upload", metavar="file", help="assign note file")
    parser.add_argument("--update", metavar="file", help="update note")
    parser.add_argument("--doc-guid", metavar="doc_guid", help="the doc guid of note")
    parser.add_argument("--list-category", action="store_true", help="list all valid category")
    parser.add_argument("--list-note", metavar="category", help="list all notes in category")
    parser.add_argument("-v", "--version", action="store_true", help="display version")
    return parser


def main():
    parser = get_parser()
    args = parser.parse_args()
    if args.set_username:
        UpdateConfigurations.update_username(args.set_username)
    elif args.set_password:
        UpdateConfigurations.update_password(args.set_password)
    elif args.upload and args.category:
        print(1)
        Upload.upload(args.upload, args.category)
    elif args.update and args.doc_guid:
        Upload.update(args.update, args.doc_guid)
    elif args.list_category:
        Display.display_categories()
    elif args.list_note:
        Display.display_notes(args.list_note)
    elif args.version:
        Display.display_version()
    else:
        parser.print_help()


if __name__ == '__main__':
    main()

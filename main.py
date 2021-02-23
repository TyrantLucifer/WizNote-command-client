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
    parser.add_argument("--login", action="store_true", help="login wiz note")
    parser.add_argument("-v", "--version", action="store_true", help="display version")
    return parser


def main():
    parser = get_parser()
    args = parser.parse_args()
    if args.set_username:
        UpdateConfigurations.update_username(args.set_username)
    elif args.set_password:
        UpdateConfigurations.update_password(args.set_password)
    elif args.login:
        Upload.login()
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
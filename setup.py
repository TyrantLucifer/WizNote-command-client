"""
@author: tyrantlucifer
@contact: tyrantlucifer@gmail.com
@blog: https://tyrantlucifer.com
@file: setup.py.py
@time: 2021/2/23 20:33
@desc: 安装入口文件
"""

import codecs
from setuptools import setup

with codecs.open('README.rst', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="wiznote-cli",
    version="0.0.3",
    author="tyrantlucifer",
    author_email="tyrantlucifer@gmail.com",
    description="The command client of WizNote",
    url="https://github.com/tyrantlucifer/WizNote-command-client",
    packages=[
        "wiz_cli"
    ],
    entry_points={
        'console_scripts': [
            'wiznote-cli = wiz_cli.main:main'
        ]
    },
    install_requires=[
        "requests",
        "requests_toolbelt",
        "prettytable"
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Internet :: Proxy Servers',
    ],
    long_description=long_description,
)

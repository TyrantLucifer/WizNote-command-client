================
WizNote-cli
================

**WizNote-cli** is a client of WizNote based on python.

Features
--------

- Support upload markdown file from local to wiz server
- Support list all categories of wiz note
- Support list all notes in one category

How to install
--------------

- Use source code

::

    git clone https://github.com/TyrantLucifer/WizNote-command-client.git
    cd WizNote-command-client
    python(python3) setup.py install

- Use pip

::

    pip(pip3) install wiznote-cli

Usage
-----

::

    usage: wiznote-cli [-h] [--set-username username] [--set-password password]
                   [--category category] [--upload file] [--update file]
                   [--doc-guid doc_guid] [--list-category]
                   [--list-note category] [-v]

The wiz note command client based python.

optional arguments:
  -h, --help            show this help message and exit
  --set-username username
                        set wiz username
  --set-password password
                        set wiz password
  --category category   assign note category
  --upload file         assign note file
  --update file         update note
  --doc-guid doc_guid   the doc guid of note
  --list-category       list all valid category
  --list-note category  list all notes in category
  -v, --version         display version

Powered by tyrantlucifer. If you have any questions, you can send e-mail to
tyrantlucifer@gmail.com


Documentation
-------------

You can find all the documentation in the
`Readme <https://github.com/TyrantLucifer/WizNote-command-client>`__.

License
-------

MIT License

Copyright (c) 2021 **TyrantLucifer**

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


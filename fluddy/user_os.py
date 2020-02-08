#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module initialises fluddy dir paths for Dawrin (MacOS), Win32 (Windows) and Linux.
Safer than Path('/path/to/') (varying python versions).
"""
import os
import sys
import logging

logger = logging.getLogger(__name__)


class SetOS(object):

    def __init__(self):
        if sys.platform == 'darwin':
            self.path_var = '/'
            self.env_ext = '.command'
            self.set_user = os.path.expanduser("~")
            self.os_loc = self.set_user + self.path_var + 'fluddy' + self.path_var
            buddy_loc = os.path.expanduser("~")
            self.env_file_loc = buddy_loc + self.path_var + 'fluddy' + self.path_var + 'buds' + self.path_var
        elif sys.platform == 'win32':
            self.path_var = r'"\"'.strip('""')
            self.env_ext = '.bat'
            self.set_user = os.path.expanduser("~")
            self.os_loc = self.set_user + self.path_var + 'fluddy' + self.path_var
            buddy_loc = os.path.expanduser("~")
            self.env_file_loc = buddy_loc + self.path_var + 'fluddy' + self.path_var + 'buds' + self.path_var
        elif sys.platform == 'linux' or sys.platform == 'linux2':
            self.path_var = '/'
            self.env_ext = '.sh'
            self.set_user = os.path.expanduser("~")
            self.os_loc = self.set_user + '/fluddy/'
            buddy_loc = os.path.expanduser("~")
            self.env_file_loc = buddy_loc + '/fluddy' + '/buds/'
        else:
            print("fluddy error: Unsupported OS.")
            sys.exit()




#!/usr/bin/python3
"""
initialise fluddy dir, buds dir and fbin.py.
buds dir stores .command / .bat / .sh files.
fbin.py is dictionary of Flask Apps added by user.
"""
import os
import stat
import logging

logger = logging.getLogger(__name__)


def initialize_flask_buddy():
    from fluddy import SetOS
    global env_command_dir
    save_dir = os.path.expanduser("~")
    env_command_dir = os.path.join(save_dir + SetOS().path_var + 'fluddy', 'buds' + SetOS().path_var)
    fbin_loc = os.path.join(save_dir + SetOS().path_var + 'fluddy' + SetOS().path_var)
    if not os.path.exists(env_command_dir):
        os.makedirs(env_command_dir)
    if not os.path.exists(fbin_loc + 'fbin.py'):
        file_name = 'fbin.py'
        fbin_file = open(fbin_loc + file_name, 'w+')
        fbin_file.write("flask_bin = {}")
        st = os.stat(fbin_loc + file_name)
        os.chmod(fbin_loc + file_name, st.st_mode | stat.S_IEXEC)
        fbin_file.close()
    if not os.path.exists(fbin_loc + '__init__.py'):
        file_name = '__init__.py'
        init_bin = open(fbin_loc + file_name, 'w+')
        init_bin.close()


if __name__ == '__main__':
    initialize_flask_buddy()

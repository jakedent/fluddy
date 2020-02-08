#!/usr/bin/python3
# -*- coding: utf-8 -*-
# noreorder
"""
Prepares .command / .bat files for launch.
Checks and updates port on each launch.
flask_bin = dict of Flask Apps.
No reorder of imports.
"""
from os import path
import sys, os
u_loc = os.path.expanduser("~")
if sys.platform == 'darwin' or sys.platform == 'linux' or sys.platform == 'linux2':
    usr_buds_path_var = '/'
elif sys.platform == 'win32':
    usr_buds_path_var = r'"\"'.strip('""')
else:
    print("Unsupported OS.")
    sys.exit()
sys.path.append(path.abspath(u_loc + usr_buds_path_var + 'fluddy' + usr_buds_path_var))
try:
    from fbin import flask_bin
except ImportError:
    print("Importing after setup.")
from fluddy import SetOS
from fluddy import FlaskPort
from fluddy import __ascii__, __windows_ascii__
import subprocess
import stat
import logging

logger = logging.getLogger(__name__)


def initialise_project(*args):
    # get Flask App name to launch and start launch process.
    global user_input_name
    user_input_name = str([args[0]]).strip('[]').strip("''")
    generate_launch_file()  # start launch process


def generate_launch_file():
    global env, start_venv
    print("fluddy: Configuring launch file...")
    env_file = user_input_name + SetOS().env_ext  # set .command or .bat

    try:
        env = open(SetOS().env_file_loc + env_file, 'w+')  # make launch file (.command/.bat/.sh)
    except IOError:
        env = open(SetOS().env_file_loc + env_file, 'w+')  # make launch file (.command/.bat/.sh)

    if os.path.exists(SetOS().env_file_loc + user_input_name + SetOS().env_ext):  # check for Fluddy dirs
        # set by MacOS
        if sys.platform == 'darwin':
            start_venv = 'source ' + '{}'.format(flask_bin[user_input_name]) + SetOS().path_var + 'venv' + \
                         SetOS().path_var + 'bin' + SetOS().path_var + 'activate'
            mac_launch()
            print("fluddy: Launch file configured with permissions.")
            # launch on MacOS
            try:
                print("fluddy: Launching Flask App...")
                subprocess.call(['open', env.name])   # Launch Flask App via .command file.
                print("fluddy: Flask App launched!")
            except Exception as E:
                print("fluddy error: {0}".format(E))

        # set by Linux
        elif sys.platform == 'linux' or sys.platform == 'linux2':
            start_venv = '. ' + '{}'.format(flask_bin[user_input_name]) + SetOS().path_var + 'venv' + \
                         SetOS().path_var + 'bin' + SetOS().path_var + 'activate'
            lin_launch()
            print("fluddy: Launch file configured with permissions.")
            # launch on Linux
            try:
                print("fluddy: Launching Flask App...")
                subprocess.call([SetOS().env_file_loc + user_input_name + SetOS().env_ext], shell=True)  # Launch .sh
                print("fluddy: Flask App launched!")
            except Exception as E:
                print("fluddy error: {0}".format(E))

        # set by Windows
        elif sys.platform == 'win32' or sys.platform == 'win64':
            start_venv = '{}'.format(flask_bin[user_input_name]) + SetOS().path_var + 'venv' + SetOS().path_var + 'Scripts' + \
                         SetOS().path_var + 'activate'
            win_launch()
            print("fluddy: Launch file configured.")
            # launch on Windows
            try:
                print("fluddy: Launching Flask App in new window...")
                subprocess.call(env.name, shell=True)  # Launch Flask App via .bat file.
                print("fluddy: Flask App launch successful.")
            except Exception as E:
                print("fluddy error: {0}".format(E))

        #  Fail safe
        else:
            print("fluddy error: Unsupported OS.")
    #  Fail safe
    else:
        print("fluddy error: Error configuring launch file.")

    logger.info('Created launch file (.command / .bat).')


# write .command files and set permissions.
def mac_launch():
    #  update .command
    env.write('echo "{}"'.format(__ascii__) + '\n' + 'cd ' + '{}\n'.format(flask_bin[user_input_name]) +
              start_venv + "\nflask run --port " '{}\n'.format(FlaskPort().port))
    #  Set permissions
    st = os.stat(SetOS().env_file_loc + user_input_name + SetOS().env_ext)
    os.chmod(SetOS().env_file_loc + user_input_name + SetOS().env_ext, st.st_mode | stat.S_IEXEC)
    #  Set permissions
    env.close()


# write .bat files.
def win_launch():
    env.write('echo {}'.format(__windows_ascii__) + '\n' +
              'cd ' + '{}\n'.format(flask_bin[user_input_name]) +
              'call ' + start_venv + "\nflask run --port " '{}\n'.format(FlaskPort().port) + '\n' +
              'pause>null')
    env.close()


# write .sh files and set permissions.
def lin_launch():
    #  update .command or file
    env.write('echo "{}"'.format(__ascii__) + '\n' + 'cd ' + '{}\n'.format(flask_bin[user_input_name]) +
              start_venv + "\nflask run --port " '{}\n'.format(FlaskPort().port))
    #  Set permissions
    subprocess.call('chmod +x {}'.format(SetOS().env_file_loc + user_input_name + SetOS().env_ext), shell=True)
    #  Set permissions
    env.close()


if __name__ == '__main__':
    initialise_project()
    mac_launch()
    win_launch()
    lin_launch()


#!/usr/bin/python3
# -*- coding: utf-8 -*-
# noreorder
"""
Implementation of the main CLI interface for fluddy.
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
from fluddy import __version__
from fluddy import SetOS
from fluddy import create_flask_app
from fluddy import initialise_project
import subprocess
import argparse
import logging

logger = logging.getLogger(__name__)


def main():
    global pargs
    parser = argparse.ArgumentParser(prog='fluddy',
                                     usage='%(prog)s [projectName] [--add] [--create] [--update] [--list] [--remove] '
                                           '[--version] ' '[-h]',
                                     description='Flask Buddy - simple Flask management.',
                                     epilog='https://github.com/jakedent/fluddy')

    parser.add_argument('-a', '--add',
                        metavar='',
                        type=str,
                        nargs=2,
                        help='Add Flask App. fluddy --add [name] [path]')
    parser.add_argument('-c', '--create',
                        metavar='',
                        type=str,
                        nargs=2,
                        help='Create Flask App. fluddy --create [name] [path]')
    parser.add_argument('-u',
                        '--update',
                        metavar='',
                        type=str,
                        nargs=1,
                        help='Update Flask App: fluddy --update [name]')
    parser.add_argument('-r',
                        '--remove',
                        metavar='',
                        type=str,
                        nargs=1,
                        help='Remove Flask App (from fluddy): fluddy --remove [name]')
    parser.add_argument('-ls', '--list',
                        action='store_true',
                        help='List Flask Apps and exit')
    parser.add_argument('-v', '--version',
                        action='version',
                        version='%(prog)s ' + __version__)
    parser.add_argument('input',
                        nargs='?',
                        metavar='projectName',
                        type=str,
                        help='Launch App. fluddy [projectName]')

    if len(sys.argv[1:]) == 0:
        parser.print_help()
        parser.exit()

    pargs = parser.parse_args()
    logging.getLogger().setLevel(max(3, 0))

    if pargs.list:
        for list in flask_bin:
            print('{}'.format(list))
        sys.exit()

    if pargs.create:
        create_flask_app(str(pargs.create[0]), str(pargs.create[1]))

    if pargs.input:
        try:
            initialise_project(str([pargs.input]).strip('[]').strip("''"))
        except KeyError:
            print(str([pargs.input]))
            print("fluddy error: You have not added that project yet.")

    if pargs.update:
        if pargs.update[0] in flask_bin:
            subprocess.call('{}'.format(flask_bin[(pargs.update[0])]) + SetOS().path_var + 'venv'
                            + SetOS().path_var + 'bin' + SetOS().path_var + 'pip '
                            'install -r ' + flask_bin[(pargs.update[0])] + SetOS().path_var + 'requirements.txt',
                            shell=True)
            print("fluddy: Successfully updated {}!".format(pargs.update[0]))
        else:
            print("fluddy error: Could not find Flask App to update.")

    if pargs.remove:
        if pargs.remove[0] in flask_bin:
            flask_bin.pop(pargs.remove[0], None)
            print("fluddy: Removed {}!".format(pargs.remove[0]))
            try:
                upd_conf = open(SetOS().os_loc + 'fbin.py', 'w+')
            except IOError:
                upd_conf = open(SetOS().os_loc + 'fbin.py', 'w+')
            upd_conf.write("flask_bin = " + str(flask_bin))  # update (write) dict
            upd_conf.close()
        else:
            print("fluddy error: Could not find Flask App name to remove.")

    if pargs.add:
        # update flask_bin in fbin.py
        try:
            key = str(pargs.add[0])  # Flask App Name
            value = str(pargs.add[1])  # Flask App Path
            flask_bin.update({key: value})
        except Exception as e:
            print('Error: {}'.format(e))
            parser.print_help()
            sys.exit(1)
        try:
            upd_conf = open(SetOS().os_loc + 'fbin.py', 'w+')
        except IOError:
            upd_conf = open(SetOS().os_loc + 'fbin.py', 'w+')
        upd_conf.write("flask_bin = " + str(flask_bin))  # update (write) dict
        upd_conf.close()
        print("fluddy: Added {}!".format(key), "...now ready to launch.")


if __name__ == '__main__':
    main()

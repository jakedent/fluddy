#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Creates a launch-able Flask App:
(dirs, __init__.py, routes.py, index.html, etc.)
Uses standard Flask App dir structure.
Creates virtual env, installs Flask and dotenv.
"""
from fluddy import SetOS
from fluddy import __flask_version__
from fluddy import __dot_env_version__
import os
import sys
import subprocess
import logging

logger = logging.getLogger(__name__)


def create_flask_app(*args):
    # create flask app dir structure and req.txt
    flask_app_sto = os.path.join(
        str([args[1]]).strip('[]').strip("''"), str([args[0]]).strip('[]').strip("''"))  # join path
    app_folder = r'app'  # Flask app dir
    tmp_folder = r'templates'  # Flask templates dir
    stc_folder = r'static'  # Flask static dir
    if not os.path.exists(flask_app_sto):
        os.makedirs(flask_app_sto)  # create Flask App path
        os.makedirs(os.path.join(flask_app_sto, app_folder))  # create app dir in Flask app
        os.makedirs(os.path.join(flask_app_sto, app_folder, tmp_folder))  # create templates dir
        os.makedirs(os.path.join(flask_app_sto, app_folder, tmp_folder, stc_folder))  # create static dir
    req_file = open(flask_app_sto + SetOS().path_var + 'requirements.txt', 'w+')  # create req.txt
    #  write Flask and dotenv to requirements.txt for install
    req_file.write('# Flask Framework\n' 'Flask == {}\n'.format(__flask_version__) + 'python-dotenv == {}\n'.format(
        __dot_env_version__) +
                   '\n# Flask Packages\n'
                   '# Insert Flask packages here during development '
                   '(delete this comment and update flask version when needed).')
    req_file.close()
    # create app instance (appName.py)
    instance_file = open(flask_app_sto + SetOS().path_var + '{}'.format(str([args[0]]).strip('[]').strip("''")) + '.py',
                         'w+')
    # write to appName.py file
    instance_file.write("from app import app")
    instance_file.close()
    if sys.platform == 'darwin' or sys.platform == 'linux' or sys.platform == 'linux2':
        # create venv MacOS
        subprocess.call('python3 -m venv {}'.format(flask_app_sto + SetOS().path_var + 'venv'), shell=True)
        print("fluddy: Created virtual environment (venv).")
        # install Flask and dotenv to venv MacOS
        subprocess.call('{}'.format(flask_app_sto) + SetOS().path_var + 'venv' + SetOS().path_var + 'bin' +
                        SetOS().path_var + 'pip install -r '  + flask_app_sto + SetOS().path_var + 'requirements.txt',
                        shell=True)
    elif sys.platform == 'win32':
        # create venv Windows
        subprocess.call('virtualenv {}'.format(os.path.join(flask_app_sto, 'venv')).replace(r'\\', r'"\"'.strip('""')), shell=True)
        print("fluddy: Created virtual environment (venv).")
        # install Flask and dotenv to venv Windows
        subprocess.call('{}'.format(os.path.join(flask_app_sto, 'venv', 'Scripts', 'pip ') + 'install -r ' + '{}'.format(os.path.join(flask_app_sto, 'requirements.txt')).replace(r'\\', r'"\"'.strip('""'))).replace(r'\\', r'"\"'.strip('""')), shell=True)
    else:
        print("fluddy error: You should'nt have seen this error.")

    print("fluddy: Installed Flask & dotenv to {} venv via pip.".format([args[0]]))

    # create __init__.py
    init_file = open(flask_app_sto + SetOS().path_var + app_folder + SetOS().path_var + '__init__.py', 'w+')
    # create routes.py
    route_file = open(flask_app_sto + SetOS().path_var + app_folder + SetOS().path_var + 'routes.py', 'w+')
    # create .flaskenv
    flask_env_file = open(flask_app_sto + SetOS().path_var + '.flaskenv', 'w+')
    # create index.html
    index_file = open(flask_app_sto + SetOS().path_var + app_folder + SetOS().path_var +
                      tmp_folder + SetOS().path_var + 'index.html', 'w+')
    # write __init__.py
    init_file.write("from flask import Flask\n" "\napp = Flask(__name__)\n" "\nfrom app import routes")
    init_file.close()
    # write routes.py
    route_file.write("from flask import render_template\n" "from app import app\n" "\n\n@app.route('/')\n"
                     "@app.route('/index')\n" "def index():\n" "\treturn render_template('index.html')")
    route_file.close()
    # write .flaskenv
    flask_env_file.write("FLASK_APP=" "{}".format(str([args[0]]).strip('[]').strip("''")) + ".py")
    flask_env_file.close()
    # write index.html
    index_file.write('<!DOCTYPE html>\n' '<html lang="en">\n' '<head>\n' '\t<meta charset="UTF-8">\n'
                     '\t<title>Fluddy</title>' '</head>\n' '<body>\n'
                     '\t<h3 style="text-align: center; margin-top: 10%; color: #262626;">Hello, from Fluddy.</h3>\n'
                     '</body>\n' '</html>')
    init_file.close()


if __name__ == '__main__':
    create_flask_app()

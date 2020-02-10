# Monolithic create Flask and Venv
import subprocess
import os
import stat
from sys import platform
import sys


def create_flask():
    global flask_app_name, flask_app_loc, flask_app_sto, path_var, req_file
    flask_app_name = input("Project: ")
    flask_app_loc = input("Exact path to (Desktop, Documents, etc): ")
    if platform == "darwin":
        flask_app_sto = os.path.join(flask_app_loc + '/' + flask_app_name)
        path_var = '/'
    elif platform == "win32" or platform == "win64":
        flask_app_sto = os.path.join(flask_app_loc + r'\'' + flask_app_name)
        path_var = r'\''
    else:
        print("Unsupported platform.")
        sys.exit()
    if not os.path.exists(flask_app_sto):
        os.makedirs(flask_app_sto)
    try:
        req_file = open(flask_app_sto + path_var + 'requirements.txt', 'w+')
    except EnvironmentError:
        req_file = open(flask_app_sto + path_var + 'requirements.txt', 'w+')
    req_file.write('# Flask Framework\n' 'Flask == 1.1.1\n' 'python-dotenv == 0.10.5\n' '\n# Flask Packages\n'
                   '# Insert Flask packages here during development (delete this comment and update flask version when needed).')
    req_file.close()
    continue_setup()


def continue_setup():
    global app_folder, tmp_folder, stc_folder
    app_folder = 'app'
    tmp_folder = 'templates'
    stc_folder = 'static'
    try:
        instance_file = open(flask_app_sto + path_var + '{}'.format(flask_app_name) + '.py', 'w+')
    except EnvironmentError:
        instance_file = open(flask_app_sto + path_var + '{}'.format(flask_app_name) + '.py', 'w+')
    instance_file.write("from app import app")
    instance_file.close()
    try:
        subprocess.call('python3 -m venv {}'.format(flask_app_sto + path_var + 'venv'), shell=True)
        print("Created venv MACOS.")
        subprocess.call('{}'.format(flask_app_sto) + path_var + 'venv' + path_var + 'bin' + path_var + 'pip '
                        'install -r ' + flask_app_sto + path_var + 'requirements.txt', shell=True)
    except EnvironmentError:
        subprocess.call('virtual venv {}'.format(flask_app_sto + path_var + 'venv'), shell=True)
        print("Created venv WIN.")
        subprocess.call('{}'.format(flask_app_sto) + path_var + 'venv' + path_var + 'bin' + path_var + 'pip '
                        'install -r ' + flask_app_sto + path_var + 'requirements.txt', shell=True)
    print("Installed Flask to {} venv via pip.".format(flask_app_name))
    subprocess.call(['mkdir ' + flask_app_sto + path_var + app_folder], shell=True)
    finish_setup()


def finish_setup():
    subprocess.call(['mkdir ' + flask_app_sto + path_var + app_folder + path_var + tmp_folder], shell=True)
    subprocess.call(['mkdir ' + flask_app_sto + path_var + app_folder + path_var + tmp_folder + path_var + stc_folder],
                    shell=True)
    try:
        init_file = open(flask_app_sto + path_var + app_folder + path_var + '__init__.py', 'w+')
        route_file = open(flask_app_sto + path_var + app_folder + path_var + 'routes.py', 'w+')
        flask_env_file = open(flask_app_sto + path_var + '.flaskenv', 'w+')
        index_file = open(flask_app_sto + path_var + app_folder + path_var + tmp_folder + path_var + 'index.html', 'w+')
    except EnvironmentError:
        init_file = open(flask_app_sto + path_var + app_folder + path_var + '__init__.py', 'w+')
        route_file = open(flask_app_sto + path_var + app_folder + path_var + 'routes.py', 'w+')
        flask_env_file = open(flask_app_sto + path_var + '.flaskenv', 'w+')
        index_file = open(flask_app_sto + path_var + app_folder + path_var + tmp_folder + path_var + 'index.html', 'w+')
    init_file.write("from flask import Flask\n" "\napp = Flask(__name__)\n" "\nfrom app import routes")
    init_file.close()
    route_file.write("from flask import render_template\n" "from app import app\n" "\n\n@app.route('/')\n" 
                     "@app.route('/index')\n" "def index():\n" "\treturn render_template('index.html')")
    route_file.close()
    flask_env_file.write("FLASK_APP=" "{}".format(flask_app_name) + ".py")
    flask_env_file.close()
    index_file.write('<!DOCTYPE html>\n' '<html lang="en">\n' '<head>\n' '\t<meta charset="UTF-8">\n'
                     '\t<title>Fluddy</title>' '</head>\n' '<body>\n'
                     '\t<h3 style="text-align: center; margin-top: 10%; color: #262626;">Hello, from Fluddy.</h3>\n'
                     '</body>\n' '</html>')
    init_file.close()


if __name__ == '__main__':
    create_flask()

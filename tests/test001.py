# create .command file
import subprocess
from config import flask_bin
import os
import stat


x = flask_bin["tleConverter"]
# print(x)


def venv_instance():
    print("Locate project, launch env, run Flask.")
    fn = 'flask-env.command'
    try:
        env = open(fn, 'w+')
    except IOError:
        env = open(fn, 'w+')
    if os.path.exists('flask-env.command'):
        env.write("cd " '{}\n'.format(x) + "\nsource venv/bin/activate\n" "\nflask run\n")
        st = os.stat('flask-env.command')
        os.chmod('flask-env.command', st.st_mode | stat.S_IEXEC)
        print("Written with perms.")
    else:
        print("Error writing env file.")
    try:
        print("Opening term window...")
        subprocess.call(['open', env.name])
        print("Term Window Opened.")
    except Exception as E:
        print("FAIL: {0}".format(E))


if __name__ == '__main__':
    venv_instance()

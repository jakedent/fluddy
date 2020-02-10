# Monolithic launch
import subprocess
from config import flask_bin
import os
import stat
import socket, errno


def initialize_flask_buddy():
    global env_command_dir
    current_directory = os.getcwd()
    env_command_dir = os.path.join(current_directory, r'buds')
    if not os.path.exists(env_command_dir):
        os.makedirs(env_command_dir)


def check_flask_port():
    global port
    for port in range(5000, 6000):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.bind(("127.0.0.1", port))
            print("Connected : {}".format(port))
            break
        except socket.error as e:
            if e.errno == errno.EADDRINUSE:
                print("{}".format(port), " in use.")
            else:
                # something else raised the socket.error exception
                print(e)

        s.close()


def get_project():
    global user_input_name
    while True:
        user_input_name = input("Key: ")
        if user_input_name in flask_bin:
            print(flask_bin[user_input_name])
            check_flask_port()
            venv_instance()
        if user_input_name not in flask_bin:
            print ("Flask app not found.")
            continue
        break


def venv_instance():
    print("Generating command file...")
    env_file = user_input_name + '.command'
    buddy_loc = os.getcwd()
    env_file_loc = buddy_loc + "/buds/"
    try:
        env = open(env_file_loc + env_file, 'w+')
    except IOError:
        env = open(env_file_loc + env_file, 'w+')
    if os.path.exists(env_file_loc + user_input_name + '.command'):
        env.write("cd " '{}\n'.format(flask_bin[user_input_name]) + "\nsource venv/bin/activate\n" "\nflask run --port " '{}\n'.format(port))
        st = os.stat(env_file_loc + user_input_name + '.command')
        os.chmod(env_file_loc + user_input_name + '.command', st.st_mode | stat.S_IEXEC)
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
    get_project()

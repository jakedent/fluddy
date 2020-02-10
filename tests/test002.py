# get Flask project from user input
from config import flask_bin


def get_project(project):
    try:
        if project in flask_bin:
            print(flask_bin[project])
        elif project not in flask_bin:
            print("Could not find project.")
            x = input("Name: ")
            get_project(x)
        else:
            print("Input Fail.")
    except Exception as TF:
        print("TOTAL FAIL: {0}".format(TF))


if __name__ == '__main__':
    x = input("Name: ")
    get_project(x)


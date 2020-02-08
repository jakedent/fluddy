#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
launcher.py checks default Flask port (5000) on every launch.
self.port is used to write port number to launch files (.command, .bat, .sh).
Sets new port by increment of 1 starting at 5000, if in use.
"""
import socket, errno
import logging

logger = logging.getLogger(__name__)


class FlaskPort(object):

    def __init__(self):
        self.port = None
        for self.port in range(5000, 6000):  # check between default Flask Port and 6000.
            set_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                set_socket.bind(("127.0.0.1", self.port))
                print("fluddy: Launching Flask App on port {}".format(self.port))
                break
            except socket.error as e:
                if e.errno == errno.EADDRINUSE:
                    print("fluddy: port {}".format(self.port), " is already running.")
                else:
                    print(e)

            set_socket.close()

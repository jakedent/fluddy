# connect to next available port after 5000 (if 5000 is not free)
import socket, errno


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


if __name__ == '__main__':
    check_flask_port()

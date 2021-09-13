#!/bin/python3
import socket


def give_me_free_ports():
    ports = []

    try:
        user_input = int(input("How many ports do you need?\n"))
        # Ceiling number 10 is arbitrary.
        assert 0 < user_input <= 10
        
        for i in range(0, user_input):
            skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            skt.bind(("", 0))
            local = skt.getsockname()
            ports.append(local[1])
            skt.close()

        print(f"Available ports:\n{ports}")

    except ValueError:
        print("This doesn't seem to be an integer!")
    except AssertionError:
        print("I only accept integers between 1 and 10 :)")


if __name__ == "__main__":
    give_me_free_ports()

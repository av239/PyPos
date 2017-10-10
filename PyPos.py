import argparse
import logging
import socket

import coloredlogs

VERSION = 0.2


def setup_args():
    parser = argparse.ArgumentParser(
        description="PyPoS v" + str(VERSION)
    )
    parser.add_argument('-host',
                        help='Host to scan',
                        type=str,
                        required=True)
    parser.add_argument('-start',
                        help='Starting port',
                        type=int)
    parser.add_argument('-end',
                        help='Ending port',
                        type=int)
    args = parser.parse_args()
    return args


def scan_port(host, port, print_closed=False):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)
    try:
        result = sock.connect_ex((host, port))
        if result == 0:
            logging.info("Port {0:0d} is open".format(port))
        else:
            if print_closed:
                logging.warning("port {0:1d} is closed.".format(port))
    except socket.error as err:
        logging.warning(err)


def main():
    args = setup_args()
    coloredlogs.install()
    logging.info("Starting...")
    for i in range(args.start, args.end):
        scan_port(args.host, i)
    logging.info("Finished.")


if __name__ == "__main__":
    main()

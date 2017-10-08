import requests
import logging
import coloredlogs
import argparse

VERSION = 0.1


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
    uri = str(host) + ":" + str(port)
    try:
        result = requests.get(uri)
        logging.info("Port {0:0d} is open.".format(port))
    except requests.exceptions.RequestException:
        if print_closed:
            logging.warning("port {0:1d} is closed.".format(port))


def main():
    args = setup_args()
    coloredlogs.install()
    logging.info("Starting...")
    for i in range(args.start, args.end):
        scan_port(args.host, i)
    logging.info("Finished.")


if __name__ == "__main__":
    main()

import signal
import sys
import argparse
import os

from . import observer
from . import config


def parse_args():
    parser = argparse.ArgumentParser(description='Manage displays')
    parser.add_argument('--create-config', action='store_true')
    parser.add_argument('--daemon', action='store_true')
    return parser.parse_args()


def signal_handler(sig, frame):
    sys.exit(0)


def main():
    args = parse_args()
    if args.create_config:
        print(f'{config.create()} created')
        return
    elif args.daemon:
        pid = os.fork()
        if pid > 0:
            sys.exit()
    # first start
    config.load()
    observer.start_observer(config.load)
    signal.signal(signal.SIGINT, signal_handler)
    signal.pause()


main()

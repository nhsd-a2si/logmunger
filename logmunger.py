#!/usr/bin/env python3
import sys


def parse_args(args):
    import argparse
    parser = argparse.ArgumentParser(
        description='Munger for Service Finder + DoS logs')
    return parser.parse_args(args)


if __name__ == '__main__':
    parse_args(sys.argv[1:])

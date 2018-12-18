#!/usr/bin/env python3
import sys


def parse_args(args):
    import argparse
    parser = argparse.ArgumentParser(
        description='Munger for Service Finder + DoS logs')
    parser.add_argument('--sfslog',
                        help='path to text file containing SFS logs',
                        required=True)
    parser.add_argument('--doslog',
                        help='path to CSV file containing DoS logs',
                        required=True)
    return parser.parse_args(args)


if __name__ == '__main__':
    parse_args(sys.argv[1:])

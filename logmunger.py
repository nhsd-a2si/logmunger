#!/usr/bin/env python3
import datetime
import json
import re
import sys

RE_PARSE_SFS_LINE = re.compile(
    '(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})'
    '.*'
    'payload=(?P<payload>\{.*\})[^}]+'  # Match up to the last closing brace
)


def parse_args(args):
    import argparse
    parser = argparse.ArgumentParser(
        description='Munger for Service Finder + DoS logs')
    parser.add_argument('--sfslog',
                        type=argparse.FileType('r'),
                        help='path to text file containing SFS logs',
                        required=True)
    parser.add_argument('--doslog',
                        type=argparse.FileType('r'),
                        help='path to CSV file containing DoS logs',
                        required=True)
    return parser.parse_args(args)


def parse_sfs_line(sfs_line):
    log_event = dict()
    match = RE_PARSE_SFS_LINE.search(sfs_line)
    if match:
        log_event['timestamp'] = datetime.datetime.strptime(
            match.group('timestamp'), '%Y-%m-%d %H:%M:%S')
        payload = json.loads(match.group('payload'))
        log_event.update(payload)
    return log_event


if __name__ == '__main__':
    parse_args(sys.argv[1:])

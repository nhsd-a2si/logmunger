#!/usr/bin/env python3
import copy
import csv
import datetime
import json
import re
import sys

OUTPUT_FIELDNAMES = (
    'timestamp', 'postcode', 'searchDistance', 'gpPracticeId',
    'whenServiceNeeded', 'ageGroup', 'gender', 'serviceTypes',
    'pilot_id', 'role', 'result_count', 'status', 'dos_region_name'
)

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


def write_merged_data_dict_csv(merged_data_dict, output_file):
    writer = csv.DictWriter(output_file, OUTPUT_FIELDNAMES)
    writer.writeheader()
    for (timestamp, event) in merged_data_dict.items():
        output_row = copy.copy(event)
        output_row['timestamp'] = timestamp
        service_types = '{data_source} ({source_id})'.format(
            data_source=output_row['serviceTypes'][0]['dataSource'],
            source_id=output_row['serviceTypes'][0]['sourceId']
        )
        output_row['serviceTypes'] = service_types
        writer.writerow(output_row)


def process_sfs_file(sfs_file):
    sfs_data_dict = dict()
    for sfs_line in sfs_file:
        log_event = parse_sfs_line(sfs_line)
        if log_event:
            timestamp = log_event.pop('timestamp')
            sfs_data_dict[timestamp] = log_event
    return sfs_data_dict


def parse_sfs_line(sfs_line):
    log_event = dict()
    match = RE_PARSE_SFS_LINE.search(sfs_line)
    if match:
        log_event['timestamp'] = datetime.datetime.strptime(
            match.group('timestamp'), '%Y-%m-%d %H:%M:%S')
        payload = json.loads(match.group('payload'))
        log_event.update(payload)
    return log_event


def process_dos_file(dos_file):
    dos_data_dict = dict()
    reader = csv.DictReader(dos_file)
    for dos_row_dict in reader:
        log_event = parse_dos_row_dict(dos_row_dict)
        timestamp = log_event.pop('timestamp')
        dos_data_dict[timestamp] = log_event
    return dos_data_dict


def parse_dos_row_dict(dos_row_dict):
    log_event = dict()
    log_event['timestamp'] = datetime.datetime.strptime(
        dos_row_dict['Date & Time'][:19], '%Y/%m/%d %H:%M:%S')
    log_event['pilot_id'] = dos_row_dict['Pilot ID']
    log_event['role'] = dos_row_dict['Role']
    log_event['result_count'] = dos_row_dict['result_count']
    log_event['status'] = dos_row_dict['status']
    log_event['dos_region_name'] = dos_row_dict['dosRegionName']
    return log_event


def merge_logs(sfs_log, dos_log):
    result = copy.deepcopy(sfs_log)
    for (timestamp, payload) in result.items():
        if timestamp in dos_log:
            payload.update(dos_log[timestamp])
    return result

if __name__ == '__main__':
    parse_args(sys.argv[1:])

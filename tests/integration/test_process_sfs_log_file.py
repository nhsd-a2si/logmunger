import datetime
import unittest

from ..context import logmunger


class ProcessSFSLogFileTestCase(unittest.TestCase):
    def test_fixture_file_processed_correctly(self):
        with open('tests/fixtures/good_sfs_log.txt', 'r') as sfs_file:
            sfs_data_dict = logmunger.process_sfs_file(sfs_file)

        record1_timestamp = datetime.datetime(
            year=2018,
            month=11,
            day=13,
            hour=11,
            minute=42,
            second=5
        )
        record2_timestamp = datetime.datetime(
            year=2018,
            month=11,
            day=13,
            hour=11,
            minute=42,
            second=9
        )
        self.assertEqual(
            {
                'postcode': 'PR8 1TN',
                'searchDistance': '60',
                'gpPracticeId': {
                    'sourceId': 155695
                },
                'whenServiceNeeded': '24',
                'ageGroup': '18-99',
                'gender': 'm',
                'serviceTypes': [
                    {
                        'dataSource': 'DIRECTORY_OF_SERVICES',
                        'sourceId': 14004
                    }
                ]
            },
            sfs_data_dict[record1_timestamp]
        )
        self.assertEqual(
            {
                'postcode': 'N15 0JE',
                'searchDistance': '60',
                'gpPracticeId': None,
                'whenServiceNeeded': '24',
                'ageGroup': None,
                'gender': None,
                'serviceTypes': [
                    {
                        'dataSource': 'DIRECTORY_OF_SERVICES',
                        'sourceId': 14024
                    }
                ]
            },
            sfs_data_dict[record2_timestamp]
        )

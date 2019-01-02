import datetime
import unittest

from ..context import logmunger


class ProcessDoSLogFileTestCase(unittest.TestCase):
    def test_fixture_file_processed_correctly(self):
        with open('tests/fixtures/good_dos_log.csv', 'r') as dos_file:
            dos_data_dict = logmunger.process_dos_file(dos_file)

        record1_timestamp = datetime.datetime(
            year=2018,
            month=11,
            day=1,
            hour=2,
            minute=33,
            second=9
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
                'pilot_id': '12345',
                'role': 'Admin',
                'result_count': '15',
                'status': 'success',
                'dos_region_name': 'London'
            },
            dos_data_dict[record1_timestamp]
        )
        self.assertEqual(
            {
                'pilot_id': '99007',
                'role': 'Admin',
                'result_count': '5',
                'status': 'success',
                'dos_region_name': 'North West'
            },
            dos_data_dict[record2_timestamp]
        )

    def test_space_only_lines_ignored(self):
        with open('tests/fixtures/bad_dos_log_space_lines.csv', 'r')\
                as dos_file:
            try:
                logmunger.process_dos_file(dos_file)
            except TypeError:
                self.fail('TypeError raised unexpectedly!')

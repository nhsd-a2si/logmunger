import unittest

from .context import logmunger

EXAMPLE_DOS_ROW_DICT = {
    '_raw': 'foo|bar|baz|bang',
    'Date & Time': '2018/11/13 12:42:05.000000+0000',
    'cmsgender': 'x',
    'Pilot ID': 99999,
    'Role': 'Admin',
    'result_count': 9,
    'status': 'success',
    'dosRegionName': 'North West'
}


class ParseDoSRowTestCase(unittest.TestCase):
    def test_row_datetime_extracted(self):
        dos_log_row = logmunger.parse_dos_row_dict(EXAMPLE_DOS_ROW_DICT)
        timestamp = dos_log_row['timestamp']
        self.assertEqual(2018, timestamp.year)
        self.assertEqual(11, timestamp.month)
        self.assertEqual(13, timestamp.day)
        self.assertEqual(12, timestamp.hour)
        self.assertEqual(42, timestamp.minute)
        self.assertEqual(5, timestamp.second)

    def test_row_datetime_microseconds_removed(self):
        dos_log_row = logmunger.parse_dos_row_dict(EXAMPLE_DOS_ROW_DICT)
        timestamp = dos_log_row['timestamp']
        self.assertEqual(0, timestamp.microsecond)

    def test_row_desired_values_extracted(self):
        dos_log_row = logmunger.parse_dos_row_dict(EXAMPLE_DOS_ROW_DICT)
        self.assertEqual(99999, dos_log_row['pilot_id'])
        self.assertEqual('Admin', dos_log_row['role'])
        self.assertEqual(9, dos_log_row['result_count'])
        self.assertEqual('success', dos_log_row['status'])
        self.assertEqual('North West', dos_log_row['dos_region_name'])

    def test_row_unwanted_values_discarded(self):
        dos_log_row = logmunger.parse_dos_row_dict(EXAMPLE_DOS_ROW_DICT)
        self.assertFalse('_raw' in dos_log_row)
        self.assertFalse('cmsgender' in dos_log_row)

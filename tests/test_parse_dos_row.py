import unittest

from .context import logmunger

EXAMPLE_DOS_ROW_DICT = {
    'Date & Time': '2018/11/13 12:42:05.000000+0000'
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

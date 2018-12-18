import unittest

from .context import logmunger

EXAMPLE_SFS_LINE = (
    '| 2018-11-13 12:40:42.902 | 2018-11-13 12:40:42.902 [32m INFO[m '
    '[nio-8080-exec-8] 582b307b4f5 [36mu.n.d.a.s.a.RequestContextLoggingFilte'
    'r [m : Completed API request: uri=/api/aggregatedSearch;payload={"postco'
    'de":"W1A 1AA","searchDistance":"60","gpPracticeId":null,"whenServiceNeede'
    'd":"24","ageGroup":null,"gender":null,"serviceTypes":[{"dataSource":"DIRE'
    'CTORY_OF_SERVICES","sourceId":14011},{"dataSource":"DIRECTORY_OF_SERVICES'
    '","sourceId":14012}]}]'
)


class ParseSFSLineTestCase(unittest.TestCase):
    def test_line_datetime_extracted(self):
        sfs_log_event = logmunger.parse_sfs_line(EXAMPLE_SFS_LINE)
        timestamp = sfs_log_event['timestamp']
        self.assertEqual(2018, timestamp.year)
        self.assertEqual(11, timestamp.month)
        self.assertEqual(13, timestamp.day)
        self.assertEqual(12, timestamp.hour)
        self.assertEqual(40, timestamp.minute)
        self.assertEqual(42, timestamp.second)

    def test_line_datetime_microseconds_removed(self):
        sfs_log_event = logmunger.parse_sfs_line(EXAMPLE_SFS_LINE)
        timestamp = sfs_log_event['timestamp']
        self.assertEqual(0, timestamp.microsecond)

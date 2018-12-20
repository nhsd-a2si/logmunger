import datetime
import unittest

from .context import logmunger


class MergeLogsTestCase(unittest.TestCase):
    def test_empty_logs_return_empty_merge(self):
        result = logmunger.merge_logs(sfs_log={}, dos_log={})
        self.assertEqual({}, result)

    def test_empty_dos_log_yields_unchanged_sfs_log(self):
        sfs_log = {datetime.datetime(year=2018, month=12, day=7,
                                     hour=12, minute=3, second=3):
                       {'postcode': 'W1A 1AA'}}
        result = logmunger.merge_logs(sfs_log=sfs_log, dos_log={})
        self.assertEqual(sfs_log, result)

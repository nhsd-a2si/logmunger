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

    def test_matching_dos_records_augment_sfs_log(self):
        sfs_log = {datetime.datetime(year=2018, month=12, day=7,
                                     hour=12, minute=3, second=3):
                       {'postcode': 'W1A 1AA'},
                   datetime.datetime(year=2018, month=12, day=7,
                                     hour=12, minute=5, second=9):
                       {'postcode': 'W1B 1BB'}
                   }
        dos_log = {
            datetime.datetime(year=2018, month=12, day=7,
                              hour=12, minute=5, second=9):
                {'pilot_id': '12345',
                 'role': 'Admin',
                 'result_count': 22,
                 'status': 'active',
                 'dos_region_name': 'A Region'}
        }
        result = logmunger.merge_logs(sfs_log=sfs_log, dos_log=dos_log)
        self.assertEqual(
            {
                datetime.datetime(year=2018, month=12, day=7,
                                  hour=12, minute=3, second=3):
                    {'postcode': 'W1A 1AA'},
                datetime.datetime(year=2018, month=12, day=7,
                                  hour=12, minute=5, second=9):
                    {'postcode': 'W1B 1BB', 'pilot_id': '12345',
                     'role': 'Admin',
                     'result_count': 22,
                     'status': 'active',
                     'dos_region_name': 'A Region'}
            },
            result
        )

    def test_source_dicts_unaltered(self):
        sfs_log = {datetime.datetime(year=2018, month=12, day=7,
                                     hour=12, minute=3, second=3):
                       {'postcode': 'W1A 1AA'},
                   datetime.datetime(year=2018, month=12, day=7,
                                     hour=12, minute=5, second=9):
                       {'postcode': 'W1B 1BB'}
                   }
        dos_log = {
            datetime.datetime(year=2018, month=12, day=7,
                              hour=12, minute=5, second=9):
                {'pilot_id': '12345',
                 'role': 'Admin',
                 'result_count': 22,
                 'status': 'active',
                 'dos_region_name': 'A Region'}
        }
        logmunger.merge_logs(sfs_log=sfs_log, dos_log=dos_log)
        self.assertEqual(
            {
                datetime.datetime(year=2018, month=12, day=7,
                                  hour=12, minute=3, second=3):
                    {'postcode': 'W1A 1AA'},
                datetime.datetime(year=2018, month=12, day=7,
                                  hour=12, minute=5, second=9):
                    {'postcode': 'W1B 1BB'}
            },
            sfs_log
        )
        self.assertEqual(
            {
                datetime.datetime(year=2018, month=12, day=7,
                                  hour=12, minute=5, second=9):
                    {'pilot_id': '12345',
                     'role': 'Admin',
                     'result_count': 22,
                     'status': 'active',
                     'dos_region_name': 'A Region'}
            },
            dos_log
        )

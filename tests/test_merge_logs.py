import unittest

from .context import logmunger


class MergeLogsTestCase(unittest.TestCase):
    def test_empty_logs_return_empty_merge(self):
        result = logmunger.merge_logs(sfs_log={}, dos_log={})
        self.assertEqual({}, result)

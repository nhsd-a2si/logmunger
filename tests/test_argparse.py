import unittest

from .context import logmunger


class ArgParseTestCase(unittest.TestCase):
    def test_exit_with_no_args(self):
        with self.assertRaises(SystemExit):
            logmunger.parse_args([])

    def test_exit_with_just_sfslog_arg(self):
        with self.assertRaises(SystemExit):
            logmunger.parse_args(
                ['--sfslog', 'tests/fixtures/good_sfs_log.txt'])

    def test_exit_with_just_doslog_arg(self):
        with self.assertRaises(SystemExit):
            logmunger.parse_args(
                ['--doslog', 'tests/fixtures/good_dos_log.csv'])

    def test_no_exit_with_sfslog_and_doslog_args(self):
        try:
            logmunger.parse_args(
                ['--sfslog', 'tests/fixtures/good_sfs_log.txt',
                 '--doslog', 'tests/fixtures/good_dos_log.csv'])
        except SystemExit:
            self.fail('SystemExit raised unexpectedly!')

    def test_both_filename_argument_parsed(self):
        parser = logmunger.parse_args(
                    ['--sfslog', 'tests/fixtures/good_sfs_log.txt',
                     '--doslog', 'tests/fixtures/good_dos_log.csv'])
        self.assertEqual('tests/fixtures/good_sfs_log.txt', parser.sfslog.name)
        self.assertEqual('tests/fixtures/good_dos_log.csv', parser.doslog.name)

import unittest

from .context import logmunger


class ArgParseTestCase(unittest.TestCase):
    def test_exit_with_no_args(self):
        with self.assertRaises(SystemExit):
            logmunger.parse_args([])

    def test_exit_with_just_sfslog_arg(self):
        with self.assertRaises(SystemExit):
            logmunger.parse_args(['--sfslog', 'somefile.txt'])

    def test_exit_with_just_doslog_arg(self):
        with self.assertRaises(SystemExit):
            logmunger.parse_args(['--doslog', 'somefile.txt'])

    def test_no_exit_with_sfslog_and_doslog_args(self):
        try:
            logmunger.parse_args(
                ['--sfslog', 'somefile.txt',
                 '--doslog', 'somefile.txt'])
        except SystemExit:
            self.fail('SystemExit raised unexpectedly!')

    def test_both_filename_argument_parsed(self):
        parser = logmunger.parse_args(
                    ['--sfslog', 'sfslog.txt',
                     '--doslog', 'doslog.csv'])
        self.assertEqual('sfslog.txt', parser.sfslog)
        self.assertEqual('doslog.csv', parser.doslog)

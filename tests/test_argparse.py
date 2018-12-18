import unittest

from .context import logmunger


class ArgParseTestCase(unittest.TestCase):
    def test_exit_with_no_args(self):
        with self.assertRaises(SystemExit):
            logmunger.parse_args([])

    def test_no_exit_with_sfslog_arg(self):
        try:
            logmunger.parse_args(['--sfslog', 'somefile.txt'])
        except SystemExit:
            self.fail('SystemExit raised unexpectedly!')

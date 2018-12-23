import io
import unittest

from ..context import logmunger


class LogMungerTestCase(unittest.TestCase):
    def test_logmunger_main(self):
        """
        This reads data from the fixture files named as args below.
        """
        output_file = io.StringIO()
        logmunger.main(
            output_file,
            'logmunger.py',
            '--sfslog',
            'tests/fixtures/good_sfs_log.txt',
            '--doslog',
            'tests/fixtures/good_dos_log.csv'
        )
        output = output_file.getvalue()
        self.assertIn(
            'timestamp,postcode,searchDistance,gpPracticeId,whenServiceNeeded,'
            'ageGroup,gender,serviceTypes,serviceTypesCount,pilot_id,role,'
            'result_count,status,dos_region_name\r\n',
            output
        )
        self.assertIn(
            '2018-11-13 11:42:05,PR8 1TN,60,12312,24,18-99,m,DIRECTORY_OF_'
            'SERVICES (14004),1,,,,',
            output
        )
        self.assertIn(
            '2018-11-13 11:42:09,N15 0JE,60,,24,,,DIRECTORY_OF_'
            'SERVICES (14024),1,99007,Admin,5,success,North West',
            output
        )

import io
import unittest

from ..context import logmunger


EXPECTED_CSV_HEADER = (
    'timestamp,postcode,searchDistance,gpPracticeId,whenServiceNeeded,'
    'ageGroup,gender,pilot_id,role,result_count,status,dos_region_name'
    '\r\n'
)


class WriteMergedDataDictCSVTestCase(unittest.TestCase):
    def test_csv_headers_correct(self):
        output_file = io.StringIO()
        logmunger.write_merged_data_dict_csv({}, output_file)
        self.assertEqual(
            EXPECTED_CSV_HEADER,
            output_file.getvalue()
        )

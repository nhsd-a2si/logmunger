import datetime
import io
import unittest

from ..context import logmunger


EXPECTED_CSV_HEADER = (
    'timestamp,postcode,searchDistance,gpPracticeId,whenServiceNeeded,'
    'ageGroup,gender,serviceTypes,serviceTypesCount,pilot_id,role,'
    'result_count,status,dos_region_name\r\n'
)


class WriteMergedDataDictCSVTestCase(unittest.TestCase):
    def test_csv_headers_correct(self):
        output_file = io.StringIO()
        logmunger.write_merged_data_dict_csv({}, output_file)
        self.assertEqual(
            EXPECTED_CSV_HEADER,
            output_file.getvalue()
        )

    def test_csv_is_correct(self):
        merged_data_dict = {
            datetime.datetime(
                    year=2018, month=8, day=4, hour=2, minute=3,
                    second=1): {
                'postcode': 'PR8 1TN',
                'searchDistance': '60',
                'gpPracticeId': 12312,
                'whenServiceNeeded': '24',
                'ageGroup': '18-99',
                'gender': 'm',
                'serviceTypes': [
                    {
                        'dataSource': 'DIRECTORY_OF_SERVICES',
                        'sourceId': 14004
                    }
                ],
                'pilot_id': '12345',
                'role': 'User',
                'result_count': '125',
                'status': 'failure',
                'dos_region_name': 'Midlands'
            },
            datetime.datetime(
                    year=2018, month=8, day=5, hour=6, minute=7,
                    second=9): {
                'postcode': 'W1A 1AA',
                'searchDistance': '10',
                'gpPracticeId': 87656,
                'whenServiceNeeded': '24',
                'ageGroup': '10-12',
                'gender': 'f',
                'serviceTypes': [
                    {
                        'dataSource': 'DIRECTORY_OF_SERVICES',
                        'sourceId': 14222
                    },
                    {
                        'dataSource': 'NHS SOURCE 2',
                        'sourceId': 99
                    }
                ],
                'pilot_id': '66625',
                'role': 'Admin',
                'result_count': '25',
                'status': 'success',
                'dos_region_name': 'South West'
            }
        }
        output_file = io.StringIO()
        logmunger.write_merged_data_dict_csv(
            merged_data_dict, output_file)
        data_rows = output_file.getvalue().split('\r\n')[1:]
        self.assertIn(
            '2018-08-04 02:03:01,PR8 1TN,60,12312,24,18-99,m,DIRECTORY_OF_'
            'SERVICES (14004),1,12345,User,125,'
            'failure,Midlands',
            data_rows
        )
        self.assertIn(
            '2018-08-05 06:07:09,W1A 1AA,10,87656,24,10-12,f,DIRECTORY_OF_'
            'SERVICES (14222);NHS SOURCE 2 (99),2,66625,Admin,'
            '25,success,South West',
            data_rows
        )

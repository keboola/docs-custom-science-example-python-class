import sample_application
import os
import csv
from keboola import docker


class TestSampleApplication:
    def test_sample_application(self):
        cfg = docker.Config()
        app = sample_application.SampleApplication()
        app.run()

        sample_data = [
            {"someText": "aaa", "number": "10", "double_number": "20"},
            {"someText": "bbb", "number": "20", "double_number": "40"},
            {"someText": "ccc", "number": "30", "double_number": "60"},
            {"someText": "ddd", "number": "40", "double_number": "80"}
        ]

        result_data = []
        assert(os.path.isfile(cfg.get_data_dir() + 'out/tables/destination.csv'))
        with open(cfg.get_data_dir() + 'out/tables/destination.csv', 'rt') as sample:
            csv_reader = csv.DictReader(sample, delimiter=',', quotechar='"')
            for row in csv_reader:
                result_data.append(row)

        assert(sample_data == result_data)

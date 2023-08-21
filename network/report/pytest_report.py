import os
from dataclasses import dataclass

import time


@dataclass
class PytestReportConfig:
    """
    [https://github.com/christiansandberg/pytest-reporter-html1]
    """
    dir_name = 'result'
    report_name = 'pytest_report.html'
    template = 'html1/index.html'

    @staticmethod
    def get_report_path(project_root_dir: str) -> str:
        return os.path.join(project_root_dir, PytestReportConfig.dir_name, PytestReportConfig.report_name)


def publish_pytest_report(project_root_dir: str) -> None:
    pytest_report_path: str = PytestReportConfig.get_report_path(project_root_dir)

    while not os.path.exists(pytest_report_path):
        time.sleep(0.1)

    if os.path.isfile(pytest_report_path):
        # TODO: Publish test report to the QA related bucket (e.g. GCS, S3)
        print('\n[TODO] Report has been published to [GCS_PATH] bucket within [GCP_PROJECT]\n')
        pass
    else:
        raise FileNotFoundError(f'[{pytest_report_path}] is not a valid file path')

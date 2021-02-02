import pandas as pd
import os

import src.constants.files as files

import logging


REAL_DATA_PATH = files.create_folder(os.path.join(files.PROJECT_ROOT_PATH, "data"))
REAL_RAW_DATA_PATH = files.create_folder(os.path.join(REAL_DATA_PATH, "raw"))
TEST_RAW_DATA_PATH = os.path.join(files.PROJECT_ROOT_PATH, "tests", "free_integration_test", "data_test", "raw")


def prepare_raw_test_data(force_recompute=False):
    real_raw_csv_files = [file for file in os.listdir(REAL_RAW_DATA_PATH) if file.endswith(".csv")]
    test_raw_csv_files = [file for file in os.listdir(TEST_RAW_DATA_PATH) if file.endswith(".csv")]

    files_to_copy_in_test = [file for file in real_raw_csv_files if file not in test_raw_csv_files]

    if force_recompute:
        files_to_copy_in_test = real_raw_csv_files

    for file in files_to_copy_in_test:
        logging.info(f"Truncating {file} and writing truncated version into test raw data folder")
        df = pd.read_csv(os.path.join(REAL_RAW_DATA_PATH, file))

        # Keep only a sub amount of data.
        df_trunc = df.iloc[:100]

        df_trunc.to_csv(os.path.join(TEST_RAW_DATA_PATH, file), index=False)

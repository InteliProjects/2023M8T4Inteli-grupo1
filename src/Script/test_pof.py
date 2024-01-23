import pytest
import pandas as pd
from pof import S3Uploader  # Substitua 'pof' pelo nome do seu script, se diferente
from unittest.mock import MagicMock
from io import StringIO

class MockS3Client:
    def __init__(self):
        self.uploaded_files = {}

    def put_object(self, Bucket, Key, Body):
        self.uploaded_files[Key] = Body

def test_read_and_prepare_data():
    uploader = S3Uploader("mock_bucket", "mock_key", "mock_secret", "mock_token")
    test_df = pd.DataFrame({
        "col1": [1, 2, None],
        "col2": [None, 3, 4]
    })
    test_df.to_csv("test.csv", index=False)

    result_df = uploader.read_and_prepare_data("test.csv")
    expected_df = pd.DataFrame({
        "col1": [1.0, 2.0, 0.0],
        "col2": [0.0, 3.0, 4.0]
    })
    assert result_df.equals(expected_df)

def test_upload_file(monkeypatch):
    mock_s3 = MockS3Client()
    monkeypatch.setattr("boto3.client", lambda *args, **kwargs: mock_s3)

    uploader = S3Uploader("mock_bucket", "mock_key", "mock_secret", "mock_token")
    uploader.upload_file("test.csv", "test_s3.csv")

    expected_df = pd.read_csv("test.csv")
    generated_csv = mock_s3.uploaded_files["test_s3.csv"]
    generated_df = pd.read_csv(StringIO(generated_csv))

    expected_df.fillna(0, inplace=True)

    pd.testing.assert_frame_equal(expected_df, generated_df, check_dtype=False, atol=1e-5)

def teardown_module(module):
    import os
    os.remove("test.csv")

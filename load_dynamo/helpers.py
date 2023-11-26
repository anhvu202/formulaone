from pathlib import Path
from dotenv import dotenv_values
import boto3
import os

def get_path_to_data():
    """Return path to data."""
    return Path('Data/')

def get_raw_data_path():
    """Return path to raw data."""
    return get_path_to_data() / 'RawData'

def get_tidy_data_path():


def get_dynamo_resource():
    load_dotenv()

    session = boto3.Session(
        aws_access_key_id = os.getenv("aws_access_key_id"),
        aws_secret_access_key = os.getenv("aws_secret_access_key"),
    )

    dynamo_resource = session.resource("dynamodb", region_name = "eu-west-1")
    return dynamo_resource
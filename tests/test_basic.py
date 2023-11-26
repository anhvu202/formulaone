# content of test_sample.py

from load_dynamo.helpers import get_tidy_data_path
from load_dynamo.helpers import get_dynamo_resource
import pandas as pd

def test_table_exist():
    dynamo_resource = get_dynamo_resource()
    tables = []
    for table in dynamo_resource.tables.all():
        tables.append(table.name)
    assert "doc-example-table-movies" in tables

# def test_check_dataframe_size():
#     df = pd.read_parquet(get_tidy_data_path() / 'current_race.parquet')
#     assert df.shape[1] == 26

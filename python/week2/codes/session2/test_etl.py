from etl import ETL
def test_read_json_file():
    path_json = "../../data/json_sample.json"
    e = ETL(input_path=path_json)
    e.read_json()
    assert type(e.data)==dict
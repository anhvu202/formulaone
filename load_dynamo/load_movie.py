import simplejson as json
from helpers import get_path_to_data
from helpers import get_dynamo_resource
from boto3.dynamodb.conditions import Key

dynamo_resource = get_dynamo_resource()

movies = dynamo_resource.Table("doc-example-table-movies")

data = movies.query(KeyConditionExpression = Key("year").eq(2013))

with open(get_path_to_data()/ "rawdata.json", "w") as f:
    json.dump(data, f)
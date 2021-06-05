import ijson
from itertools import islice

def json_processor(json):
    objects = ijson.items(f, 'item')
    objects = islice(objects, 200)
    print(objects)
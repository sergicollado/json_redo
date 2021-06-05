import ijson
from message_client import MessageClient

def json_processor(json):
    for entry_log in ijson.items(json, 'item'):
        process_post(entry_log)

def process_post(data: dict):
    if data['type'] != 'post':
        return
    MessageClient.send_post(data['url'], data)
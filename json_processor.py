import ijson
from message_client import MessageClient

def json_processor(json):
    for entry_log in ijson.items(json, 'item'):
        process_post(entry_log)
        process_sms(entry_log)
        process_email(entry_log)

def process_post(data: dict):
    if data['type'] != 'post':
        return
    MessageClient.send_post(data['url'], data)

def process_sms(data: dict):
    if data['type'] != 'sms':
        return
    MessageClient.send_sms(data['phone'], data)

def process_email(data: dict):
    if data['type'] != 'email':
        return
    MessageClient.send_email(data['email'], data)
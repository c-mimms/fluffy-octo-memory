import requests
from xml.dom import minidom
import json
from datetime import datetime as date

def lambda_handler(event, context):
    r = requests.get('http://api.sr.se/api/v2/podfiles?programid=493&format=json')
    result = json.loads(r.text)
    podfile = result['podfiles'][0]
    pod = dict()
    pod['uid'] = podfile['url']
    pod['updateDate'] = date.utcfromtimestamp(int(podfile['publishdateutc'][6:-5])).isoformat() + '.0Z'
    pod['titleText'] = podfile['title']
    pod['mainText'] = ''
    pod['streamUrl'] = podfile['url'].replace('http','https')
    return {
        'statusCode': '200',
        'body': json.dumps(pod),
        'headers': {
        'Content-Type': 'application/json',
        },
    }
# {
#   "uid": "urn:uuid:1335c695-cfb8-4ebb-abbd-80da344efa6b",
#   "updateDate": "2016-05-23T22:34:51.0Z",
#   "titleText": "Amazon Developer Blog, week in review May 23rd",
#   "mainText": "",
#   "streamUrl": "https://developer.amazon.com/public/community/blog/myaudiofile.mp3",
#   "redirectionUrl": "https://developer.amazon.com/public/community/blog"
# }
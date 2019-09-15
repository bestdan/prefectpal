import yaml
import os
from pushbullet import Pushbullet

file_path = os.path.join('/Users/danielegan/src/pb_creds.yaml')

with open(file_path, 'r') as stream:
    try:
        creds = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

token = creds['pushbullet']

pb = Pushbullet('{}'.format(token['token']))

push = pb.push_note("Hi Bird", "This is working 🔥")

import sys
import random
from workflow import Workflow
import utils
wf = Workflow()

config = {
        'length': 16,
        'digits':{
            'letters':'0123456789',
            'count':2,
            },
        'symbols':{
            'letters':'!@#$%^&*()_+-=`~{}[]\|:;<>,.?/',
            'count':2,
            },
        'upper':{
            'letters':'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
            'count':2,
            },
        'lower':{
            'letters':'abcdefghijklmnopqrstuvwxyz',
            'count':2,
            },
        }

argc = len(sys.argv)
if argc >= 5:
    config['upper']['count'] = int(sys.argv[4])
if argc >= 4:
    config['digits']['count'] = int(sys.argv[3])
if argc >=3:
    config['symbols']['count'] = int(sys.argv[2])
if argc >=2:
    config['length'] = int(sys.argv[1])

config['lower']['count'] = config['length'] \
                               - config['symbols']['count'] \
                               - config['upper']['count'] \
                               - config['digits']['count']

subtitle = "pass [length] [symbols] [digits] [uppers], press 'Enter' to copy to clipboard."
if config['lower']['count'] < 0:
    title = 'length {} is too small'.format(config['length'])
    wf.add_item(title,subtitle,valid=False)
    exit()

selected_letters = []
for t in ['upper','digits','symbols','lower']:
    selected_letters.extend(random.sample(config[t]['letters'], config[t]['count']))

random.shuffle(selected_letters)

uid = arg = title = ''.join(selected_letters)
wf.add_item(title,subtitle,arg=arg,valid=True)

data = utils.load_passwords()
for idx,d in enumerate(data):
    uid = arg = title = d['password']
    subtitle = "created at {}".format(d['create_time'])
    wf.add_item(title,subtitle,arg=arg,valid=True)

wf.send_feedback()

import sys
import utils
import datetime

password = sys.argv[1]
create_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

data = utils.load_passwords()
password_exists = False
for d in data:
    if d['password'] == password:
        password_exists = True
        break

if not password_exists:
    data.insert(0,{
        'password': password,
        'create_time': create_time,
        })
    utils.save_passwords(data)

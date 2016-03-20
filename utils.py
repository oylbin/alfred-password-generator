import pickle
import os
filename = os.path.join(os.path.dirname(__file__), 'data.json')

def load_passwords():
    if os.path.exists(filename):
        data = pickle.load(open(filename))
    else:
        data = []
    return data

def save_passwords(data):
    data = data[:10]
    f = open(filename,'w')
    pickle.dump(data,f)
    f.close()


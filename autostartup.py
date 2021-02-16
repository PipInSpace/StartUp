import os
import pickle
import datetime

def load_obj():
    with open('apps.pkl', 'rb') as f:
        return pickle.load(f)

apps = load_obj()

time = datetime.datetime.now()
time = time.strftime("%H")
print(time)

for element in apps.get(time):
    os.startfile(element)

import os
import pandas as pd
import random
import signal

data = pd.read_csv('./userDataAfter.csv')

l = len(data)
status = True

def signal_handler(signum, frame):
    if signum == 15:
        global status
        status = False

while status:
    signal.signal(signal.SIGTERM, signal_handler)
    os.system('clear')
    print (data.loc[int(random.random() * l), 'username'])

import os 
DIR_PATH = os.path.dirname(os.path.realpath(__file__))

import matplotlib.pyplot as plt

# https://github.com/MIT-LCP/wfdb-python
# pip install wfdb
import wfdb

record = wfdb.rdrecord(os.path.join(DIR_PATH, 'Subject10_AccTempEDA'))
print(record.__dict__)

wfdb.plot_wfdb(record=record, title='Subject10_AccTempEDA')

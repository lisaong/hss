import matplotlib.pyplot as plt

# https://github.com/MIT-LCP/wfdb-python
# pip install wfdb
import wfdb

record = wfdb.rdrecord('./data/physionet/Subject10_AccTempEDA')
wfdb.plot_wfdb(record=record, title='Subject10_AccTempEDA')
display(record.__dict__)

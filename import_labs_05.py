# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 15:12:29 2015

@author: David
"""

itr = '05'

WORKINGDIR = r'E:\Data\WrangledData\LabReports\Python'
TARGETDIR = r'../Data'
OUTPUTDIR = r'../Output'

import os, time
start = time.time()
os.chdir(WORKINGDIR)
print(os.getcwd())
import lineprocess_05 as lp

file_out = open(OUTPUTDIR + r'/python_text_' + itr + r'.txt', 'w', encoding='latin-1')
file_out.write('name|dob|sex|zip|ssn|d_coll|ticket|d_perf|face|gluc|fruct|a1c|bun|creat|alkp|bil_t|ast|alt|ggt|prot|albu|glob|chol|hdl|tch_r|trigs|u_pro|u_cre|u_pcr|bmi|pulse|bpsys|bpdias\n')

llb = lp.LabLineBuffer(file_out)

for filename in os.listdir(TARGETDIR):
    file_in = open(TARGETDIR + '/' + filename, 'r', encoding='latin-1')
    llb.process(file_in)
    file_in.close()

file_out.close()

end = time.time()
print('elapsed time: {x:.2f} seconds'.format(x=end - start))


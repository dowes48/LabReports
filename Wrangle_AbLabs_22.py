# -*- coding: utf-8 -*-
"""
Created on Tue Jan 20 06:04:04 2026

@author: dowes
"""

WORKINGDIR = r'C:\Users\dowes\OneDrive\Projects\LabReports'
TARGETDIR = r'./AbLab_Rpts/AbLab_2021'
#TARGETDIR = r'./AbLab_Rpts'
OUTPUTDIR = r'C:\Users\dowes\OneDrive\Projects\LabReports\Output'

import os
import copy
from datetime import datetime
from time import time

itr = '22'

start = time()
os.chdir(WORKINGDIR)

clean_ID_dict = {'ticket':"", 'd_coll':"", 'name':"",'dob':"", 'sex':"", 'ssn':"",'zip':""}
ID_file_out = open(OUTPUTDIR + r'/ID_output_' + itr + r'.csv', 'w')
ID_file_out.write('ticket,d_coll,name,dob,sex,ssn,zip\n')

clean_lab_dict = {'ticket':"", 'd_coll':"", 'age':"", 'sex':"", 'd_perf':"", 'face':"",
              'gluc':"", 'fruct':"", 'a1c':"", 'bun':"",'creat':"", 'alkp':"",
              'bil_t':"", 'ast':"", 'alt':"", 'ggt':"", 'prot':"", 'albu':"",
              'glob':"", 'chol':"", 'hdl':"", 'tch_r':"", 'trigs':"", 'u_pro':"",
              'u_cre':"", 'u_pcr':"", 'bmi':"", 'pulse':"", 'bpsys':"", 'bpdias':""}
lab_file_out = open(OUTPUTDIR + r'/labs_output_' + itr + r'.csv', 'w')
lab_file_out.write('ticket,d_coll,age,sex,d_perf,face,gluc,fruct,a1c,bun,creat,alkp,bil_t,' +
                   'ast,alt,ggt,prot,albu,glob,chol,hdl,tch_r,trigs,u_pro,u_cre,u_pcr,bmi,' +
                   'pulse,bpsys,bpdias\n')

def fixMV(valStr):
    if valStr =="NVG":
        return "9998"
    if valStr=="NVH":
        return "9999"
    return valStr

def process_reports(f_in):
    lab_dict = copy.deepcopy(clean_lab_dict)
    lab_lst = []
    ID_dict = copy.deepcopy(clean_ID_dict)
    ID_lst = []

    for line in f_in:
        if "\f" not in line:
            if 'NAME:'          in line:
                ID_dict['name'] = line[6:].strip()
            if 'DOB/SEX:'       in line:
                ID_dict['dob'] = line[9:19].strip()
                ID_dict['sex'] = line[21]
                lab_dict['sex'] = line[21]
                ID_dict['zip'] = line[60:].strip()
                date_dob = datetime.strptime(line[9:19].strip(), "%m/%d/%Y")
            if 'SOC SEC NO:'    in line:
                ID_dict['ssn'] = line[12:21]
                ID_dict['d_coll'] = line[55:].strip()
                lab_dict['d_coll'] = line[55:].strip()
                date_coll = datetime.strptime(lab_dict['d_coll'],"%m/%d/%Y")
                age_days = (date_coll - date_dob).days
                lab_dict['age'] = str(int(age_days/365.25))
            if 'TICKET NUMBER:' in line:
                lab_dict['ticket'] = line[15:25]
                ID_dict['ticket'] = line[15:25]
                lab_dict['d_perf'] = line[55:].strip()
            if 'TYPE/AMT:'      in line:
                lab_dict['face'] =  line[22:].strip().replace(r',', '')
            if 'GLUCOSE (MG/DL' in line:
                lab_dict['gluc'] = fixMV(line[30:40].strip())
            if 'FRUCTOSAMINE  ' in line:
                lab_dict['fruct'] = fixMV(line[30:40].strip())
            if 'HB A1C (%)    ' in line:
                lab_dict['a1c'] = fixMV(line[30:40].strip())
            if 'BUN (MG/DL)   ' in line:
                lab_dict['bun'] = fixMV(line[30:40].strip())
            if line.find('CREATININE (MG')==0:
                lab_dict['creat'] = fixMV(line[30:40].strip())
            if 'ALK. PHOS. (U/' in line:
                lab_dict['alkp'] = fixMV(line[30:40].strip())
            if 'BILI. TOT. (MG' in line:
                lab_dict['bil_t'] = fixMV(line[30:40].strip())
            if 'AST(SGOT) (U/L' in line:
                lab_dict['ast'] =  fixMV(line[30:40].strip())
            if 'ALT(SGPT) (U/L' in line:
                lab_dict['alt'] =  fixMV(line[30:40].strip())
            if 'GGT(GGTP) (U/L' in line:
                lab_dict['ggt'] =  fixMV(line[30:40].strip())
            if 'TOT. PROTEIN (' in line:
                lab_dict['prot'] = fixMV(line[30:40].strip())
            if 'ALBUMIN (G/DL)' in line:
                lab_dict['albu'] = fixMV(line[30:40].strip())
            if 'GLOBULIN (G/DL' in line:
                lab_dict['glob'] = fixMV(line[30:40].strip())
            if line.find('CHOLESTEROL (M')==0:
                lab_dict['chol'] = fixMV(line[30:40].strip())
            if 'HDL CHOLESTERO' in line:
                lab_dict['hdl'] =  fixMV(line[30:40].strip())
            if 'CHOL/HDL CHOL ' in line:
                lab_dict['tch_r'] = fixMV(line[30:40].strip())
            if 'TRIGLYCERIDES ' in line:
                lab_dict['trigs'] = fixMV(line[30:40].strip())
            if 'URINE PROTEIN ' in line:
                lab_dict['u_pro'] = fixMV(line[30:40].strip())
            if 'URINE CREATINI' in line:
                lab_dict['u_cre'] = fixMV(line[30:40].strip())
            if 'PROT/CREAT RAT' in line:
                lab_dict['u_pcr'] = fixMV(line[30:40].strip())
            if 'BMI           ' in line:
                lab_dict['bmi'] =  fixMV(line[30:40].strip())
            if 'PULSE         ' in line:
                lab_dict['pulse'] = fixMV(line[30:40].strip())
            if 'BLOOD PRESSURE' in line:
                t_str = line[30:40].strip()
                bp_list = t_str.split('/')
                lab_dict['bpsys']  = bp_list[0]
                lab_dict['bpdias'] = bp_list[1]
        else:
            for k, v in lab_dict.items():
                lab_lst.append(v)
            lab_file_out.write(",".join(lab_lst) + '\n')
            lab_dict = copy.deepcopy(clean_lab_dict)
            lab_lst = []

            for k, v in ID_dict.items():
                ID_lst.append(v)
            ID_file_out.write(",".join(ID_lst) + '\n')
            ID_dict = copy.deepcopy(clean_ID_dict)
            ID_lst = []


for dirpath, dirnames, filenames in os.walk(TARGETDIR):
    # Iterate over files in the current directory
    for filename in filenames:
        # Construct and print the full path of each file
        full_file_path = os.path.join(dirpath, filename)
        file_in = open(full_file_path, 'r')
        process_reports(file_in)
        file_in.close()

lab_file_out.close()
ID_file_out.close()

end = time()
print('elapsed time: {x:.2f} seconds'.format(x = end - start))




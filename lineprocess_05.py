# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 15:36:06 2015

@author: David
"""
from datetime import datetime

STATA_DATE_ZERO = datetime.strptime('1960-01-01', '%Y-%m-%d')

def statadays(datestr):
    if datestr == '':
        return '.'
    else:
        mon_s, day_s, year_s = datestr.split(r'/')
        return str((datetime(int(year_s), int(mon_s), int(day_s)) - STATA_DATE_ZERO).days)
# end statadays function definition


class LabLineBuffer():
  
  def clear(self):
    self.name  =self.dob   =self.sex   =self.zip  =self.ssn=""
    self.d_coll=self.ticket=self.d_perf=self.face =self.gluc=""
    self.fruct =self.a1c   =self.bun   =self.creat=self.alkp=""
    self.bil_t =self.ast   =self.alt   =self.ggt  =self.prot=""
    self.albu  =self.glob  =self.chol  =self.hdl  =self.tch_r=""
    self.trigs =self.u_pro =self.u_cre =self.u_pcr=self.bmi=""
    self.pulse =self.bpsys =self.bpdias= ""
   
  def __init__(self, file_out):
    self.fout = file_out
    self.clear()
  
  def flush(self):
    self.fout.write('|'.join([self.name, self.dob, self.sex, self.zip, self.ssn, self.d_coll, self.ticket, self.d_perf, self.face, self.gluc, self.fruct, self.a1c, self.bun, self.creat, self.alkp, self.bil_t, self.ast, self.alt, self.ggt, self.prot, self.albu, self.glob, self.chol, self.hdl, self.tch_r, self.trigs, self.u_pro, self.u_cre, self.u_pcr, self.bmi, self.pulse, self.bpsys, self.bpdias]) + '\n')
    self.clear()
  
  def fixMV(self, valStr):
    if valStr =="NVG":
      return ".a"
    if valStr=="NVH":
      return ".b"
    return valStr
  
  def processLines(self, line):
    if 'NAME:' in line: 
      self.name = line[6:].strip()
      return
    if 'DOB/SEX:' in line:
      self.dob = statadays(line[9:19])
      self.sex = line[21]
      self.zip = line[60:].strip()
      return
    if 'SOC SEC NO:' in line:
      self.ssn = line[12:21]
      self.d_coll = statadays(line[55:].strip())
      return
    if 'TICKET NUMBER:' in line:
      self.ticket = line[15:25]
      self.d_perf = statadays(line[55:].strip())
      return
    if 'TYPE/AMT:'      in line: 
      self.face =  line[22:].strip().replace(r',', '')
      return
    if 'GLUCOSE (MG/DL' in line: 
      self.gluc =  self.fixMV(line[30:40].strip())
      return
    if 'FRUCTOSAMINE  ' in line: 
      self.fruct = self.fixMV(line[30:40].strip())
      return
    if 'HB A1C (%)    ' in line: 
      self.a1c =   self.fixMV(line[30:40].strip())
      return
    if 'BUN (MG/DL)   ' in line: 
      self.bun =   self.fixMV(line[30:40].strip())
      return
    if 'CREATININE (MG' in line: 
      self.creat = self.fixMV(line[30:40].strip())
      return
    if 'ALK. PHOS. (U/' in line: 
      self.alkp =  self.fixMV(line[30:40].strip())
      return
    if 'BILI. TOT. (MG' in line: 
      self.bil_t = self.fixMV(line[30:40].strip())
      return
    if 'AST(SGOT) (U/L' in line: 
      self.ast =   self.fixMV(line[30:40].strip())
      return
    if 'ALT(SGPT) (U/L' in line: 
      self.alt =   self.fixMV(line[30:40].strip())
      return
    if 'GGT(GGTP) (U/L' in line: 
      self.ggt =   self.fixMV(line[30:40].strip())
      return
    if 'TOT. PROTEIN (' in line: 
      self.prot =  self.fixMV(line[30:40].strip())
      return
    if 'ALBUMIN (G/DL)' in line: 
      self.albu =  self.fixMV(line[30:40].strip())
      return
    if 'GLOBULIN (G/DL' in line: 
      self.glob =  self.fixMV(line[30:40].strip())
      return
    if 'CHOLESTEROL (M' in line: 
      self.chol =  self.fixMV(line[30:40].strip())
      return
    if 'HDL CHOLESTERO' in line: 
      self.hdl =   self.fixMV(line[30:40].strip())
      return
    if 'CHOL/HDL CHOL ' in line: 
      self.tch_r = self.fixMV(line[30:40].strip())
      return
    if 'TRIGLYCERIDES ' in line: 
      self.trigs = self.fixMV(line[30:40].strip())
      return
    if 'URINE PROTEIN ' in line: 
      self.u_pro = self.fixMV(line[30:40].strip())
      return
    if 'URINE CREATINI' in line: 
      self.u_cre = self.fixMV(line[30:40].strip())
      return
    if 'PROT/CREAT RAT' in line: 
      self.u_pcr = self.fixMV(line[30:40].strip())
      return
    if 'BMI           ' in line: 
      self.bmi =   self.fixMV(line[30:40].strip())
      return
    if 'PULSE         ' in line: 
      self.pulse = self.fixMV(line[30:40].strip())
      return
    if 'BLOOD PRESSURE' in line: 
      t_str = line[30:40].strip()
      bp_list = t_str.split('/')
      self.bpsys  = bp_list[0]
      self.bpdias = bp_list[1]
      return
  
  def process(self, fin):
    if self.name!='':
      self.flush()
    for line in fin:
      if '<FF>' not in line: 
        self.processLines(line)
      else:
        self.flush()
# end class LabLineBuffer declaration










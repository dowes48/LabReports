# -*- coding: utf-8 -*-
"""
Created on Fri Dec 19 06:51:35 2025

@author: dowes
"""
import copy

clean_dict = {'name':"",'dob':"", 'sex':"",'zip':""}

lab_dct = copy.deepcopy(clean_dict)

lab_dct['name'] = "Blaine S Hunter"
lab_dct['dob'] = "03/03/1970"
lab_dct['sex'] = "M"
lab_dct['zip'] = "03306"

lab_lst = []

for k, v in lab_dct.items():
    lab_lst.append(v)

print("|".join(lab_lst))

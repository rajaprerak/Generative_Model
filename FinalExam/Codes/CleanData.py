from bs4 import BeautifulSoup as BS import magic import json import os import time
from pprint import pprint
from glob import glob import io import re import unicodedata as ud
from numpy import * import numpy as np
import merge_ids_duplicates as mid



def merge_duplicates():
    files_ = glob('Candidate Profile Data/*')
    file_data = {}
    count = 0
    total = 0

    for j,i in enumerate(files_):
        with io.open(i, 'r', encoding='us-ascii') as f:
            data = f.read().lower()
            data = data.replace('\\n','') 
            data = re.sub(r'\\u[0-9a-f]{,4}','',data) 
            file_data[j] = json.loads(data)
            total += len(file_data[j])
    for i in range(len(files_)-1):
        list_i = {}
        for j in range(i+1,len(files_)):
            print files_[i],files_[j]
            #print i,j
            one = file_data[i]
            two = file_data[j]
            list_j = {}
            for k in range(len(one)):
                for l in range(len(two)):
                    if one[k]['skills'] == two[l]['skills']:
                        list_i[k] = True
                        list_j[k] = True
                        count += 1

                        file_data[j][l]['candidateid'] = one[k]['candidateid']
                        for z in range(l+1,len(two)):
                            file_data[j][z]['candidateid'] = unicode(int(two[z]['candidateid'])+1)
                        
    
    for j,i in enumerate(files_):
        with io.open(i, 'w', encoding='utf8') as f:
            f.write(unicode(json.dumps(file_data[j])))
            f.truncate()
files = glob('Candidate Profile Data/*')
data = dict()
skillset = dict()
skillsetjob = dict()
candidate = 1

for file_ in files:
    with io.open(file_, 'r+', encoding='utf-8') as json_file:
        json_data = json_file.read().lower()

        json_data = ud.normalize('NFKC',json_data)
        filename = "".join(file_.split('.')[:-1]).split('/')[1]
        
        json_data = json_data.replace('\\n','') 
        json_data = re.sub(r'\\u[0-9a-f]{,4}','',json_data) 
        json_file.seek(0)
        
        json_data = json.loads(json_data)

        j = 0
        m = 0
        for i in range(len(json_data)):
            skills_data = json_data[i]['skills']
            skills = skills_data.split(',')
            json_data[i]['candidateid'] = unicode(candidate)
           
            skill_experience_years = re.findall(r'((\d\d(?=\+ years\)))|(\d(?= (years|year)\))))',skills_data)
            for l in skill_experience_years:
                j += 1
            extracted, respectively:

            skills = re.sub(r'\s\(((\d\d(\+ years))|(\d (years|year))|(less than 1 year))\)', 'token', skills_data)
            skills = re.sub(r'(token\,\s)','token',skills)
            skills = skills.split('token')
            skills = skills[:][:-1] 
            for index,skl in enumerate(skills):
                m += 1
                if skl in skillset.keys():
                    skillset[skl] += 1
                    skillsetjob[skl] += [filename]
                else:
                    skillset[skl] = 1
                    skillsetjob[skl] = [filename]
            candidate += 1
        
        if j!=m:
            
        else:
            
            pass
        json_file.write(unicode(json.dumps(json_data)))
        json_file.truncate()

print (skillset.keys())
mid.merge_duplicates()


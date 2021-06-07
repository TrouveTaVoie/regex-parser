    
    
import re
import os
from datetime import date



import pandas as pd

import phonenumbers


import logging



import sys
import operator
import string

    

def find_phone(text):
        try:
            return list(iter(phonenumbers.PhoneNumberMatcher(text, None)))[0].raw_string
        except:
            try:
                return re.search(
                    r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})',
                    text).group()
            except:
                return ""

def extract_email(text):
        email = re.findall(r"([^@|\s]+@[^@]+\.[^@|\s]+)", text)
        if email:
            try:
                return email[0].split()[0].strip(';')
            except IndexError:
                return None

def extract_name(resume_text):
        nlp_text = nlp(resume_text)

        # First name and Last name are always Proper Nouns
        # pattern_FML = [{'POS': 'PROPN', 'ENT_TYPE': 'PERSON', 'OP': '+'}]

        pattern = [{'POS': 'PROPN'}, {'POS': 'PROPN'}]
        matcher.add('NAME', None, pattern)

        matches = matcher(nlp_text)

        for match_id, start, end in matches:
            span = nlp_text[start:end]
            return span.text
        return ""

# def extract_university(text, file):
#         df = pd.read_csv(file, header=None)
#         universities = [i.lower() for i in df[1]]
#         college_name = []
#         listex = universities
#         listsearch = [text.lower()]

#         for i in range(len(listex)):
#             for ii in range(len(listsearch)):
                
#                 if re.findall(listex[i], re.sub(' +', ' ', listsearch[ii])):
                
#                     college_name.append(listex[i])
        
#         return college_name

# def job_designition(text):
#         job_titles = []
        
#         __nlp = nlp(text.lower())
        
#         matches = designitionmatcher(__nlp)
#         for match_id, start, end in matches:
#             span = __nlp[start:end]
#             job_titles.append(span.text)
#         return job_titles

# def get_degree(text):
#         doc = custom_nlp2(text)
#         degree = []

#         degree = [ent.text.replace("\n", " ") for ent in list(doc.ents) if ent.label_ == 'Degree']
#         return list(dict.fromkeys(degree).keys())

# def get_company_working(text):
#         doc = custom_nlp3(text)
#         degree = []

#         degree = [ent.text.replace("\n", " ") for ent in list(doc.ents)]
#         return list(dict.fromkeys(degree).keys())
    
# def extract_skills(text):

#         skills = []

#         __nlp = nlp(text.lower())
#         # Only run nlp.make_doc to speed things up

#         matches = skillsmatcher(__nlp)
#         for match_id, start, end in matches:
#             span = __nlp[start:end]
#             skills.append(span.text)
#         skills = list(set(skills))
#         return skills

#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

#print enron_data.keys()

print enron_data['SKILLING JEFFREY K']

count = 0

for i in enron_data.values():
    if i['poi'] == True:
        count = count + 1

print count

with open('../final_project/poi_names.txt') as f:
    f.readline()
    f.readline()
    names = f.readlines()
    
print len(names)



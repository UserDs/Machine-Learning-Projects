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



# print len(enron_data)

# print len(enron_data["SKILLING JEFFREY K"])

# count = 0
# for key, value in enron_data.iteritems():
#     if enron_data[key]['poi'] == 1:
#         count = count + 1
# print count 

# print enron_data["PRENTICE JAMES"]["total_stock_value"]

# print enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]

# print enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]


# print enron_data["SKILLING JEFFREY K"]["total_payments"]

count = 0
for key in enron_data:
    if enron_data[key]["salary"] != 'NaN':
        count = count + 1
print count 

count = 0
for key in enron_data:
    if enron_data[key]["email_address"] != 'NaN':
        count = count + 1
print count
#!/usr/bin/python3
import  xlrd
import  os
import argparse
import pymongo
import subprocess
import email_sender

parser = argparse.ArgumentParser(formatter_class = argparse.RawTextHelpFormatter)
parser.add_argument("--filename", help = "Absolute/Relative path to excel file to populate event handlers in database")
parser.add_argument("--email", help = "yes/no to send api_token to the respective co-ordinators")
args = parser.parse_args()



if not os.path.isfile( args.filename ):
    print('please provide a path to excel file')
    sys.exit()




myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["event_management_backend"]



collection_list = mydb.list_collection_names()
if "faculty_coordinators" in collection_list:

          print("Dropping previous collection 'faculty_coordinators'")
          collection = mydb['faculty_coordinators']
          collection.drop()






xl_object = xlrd.open_workbook(args.filename)
sheet = xl_object.sheet_by_index(0)


email_list = []
collection_records = []
for i in range(sheet.nrows):

      email_list.append( sheet.cell_value(i,3) )
      dictionary = {  'coordinator_id'  :  sheet.cell_value(i,0),
             'name': sheet.cell_value(i,1),
             'type': sheet.cell_value(i,2),
             'email':  sheet.cell_value(i,3),
             'api_token' : str(abs(hash(sheet.cell_value(i,3).strip())))
             }
      collection_records.append(dictionary)

mydb.faculty_coordinators.insert_many(collection_records)




if args.email == 'yes':

    print('sending email')
    email_sender.send(email_list)






import sys
import  xlrd
import  os
import argparse
import argparse
import pymongo
import subprocess
#import email_sender

parser = argparse.ArgumentParser(formatter_class = argparse.RawTextHelpFormatter)
parser.add_argument("--filename", help = "Absolute/Relative path to excel file to populate event handlers in database")

args = parser.parse_args()


if not os.path.isfile( args.filename ):
    print('please provide a path to excel file')
    sys.exit()




myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient["event_management_backend"]



collection_list = mydb.list_collection_names()
if "students_data" in collection_list:

          print("Dropping previous collection 'students_data'")
          collection = mydb['students_data']
          collection.drop()






xl_object = xlrd.open_workbook(args.filename)
sheet = xl_object.sheet_by_index(0)


#email_list = []
collection_records = []
for i in range(1,sheet.nrows):

      #email_list.append( sheet.cell_value(i,3) )
      dictionary = {  'email' : sheet.cell_value(i,1),
   		      'name': sheet.cell_value(i,2),
			'StudentID'  :  sheet.cell_value(i,3),
          
             'branch': sheet.cell_value(i,4),
             'year':  sheet.cell_value(i,5),
             'cgpa' : sheet.cell_value(i,6),
             'attendence' : sheet.cell_value(i,7),
             
             }
      collection_records.append(dictionary)

mydb.students_data.insert_many(collection_records)


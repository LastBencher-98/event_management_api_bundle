
import time
import datetime
import pymongo 
from mongoconfig import MongoDB
from flask import Flask, jsonify, request, render_template
from flask_restful import Api, Resource 
import json
import helper





mydb = MongoDB( database = 'event_management_backend', host='localhost', port=27017)
app = Flask(__name__)
helper_obj = helper.helper(mydb)






@app.route('/api/v0.1/listeventcords', methods=['GET'])
def send_event_coordinators():
   
     """ 
     
     sends all  co-ordinators in json response 
     
     """          

     data = list(mydb.faculty_coordinators.find({},{"_id":0, "api_token":0}))
     response =  jsonify(data)
     return response, 200


@app.route('/api/v0.1/addevents', methods=['POST'])
def add_event():
     """

     Adds events to events collections, auth_token required

     TODO : better designing for assigning eid

     """
          
     data = json.loads(request.data)

     if 'auth_token' in data.keys() :


          if not helper_obj.validate_token(data['auth_token']) :
               return '', 401


       
          for event in data['events']:
               event['eid'] = str(sum(ord(i) for i in event['ename']) % 10**6 )
               event['co_ordinator'] =  helper_obj.get_user_from_token( data['auth_token'] )
               event['date'] =  repr(datetime.datetime.strptime(event['date'], '%d/%m/%Y'))
               event['vacancy'] = event['nos']
               event['registered_students'] = []
               mydb.events.insert_one(event)
               
          response = jsonify({'message':'success'})
          return response
     else :

          return '', 206


@app.route('/api/v0.1/liststudents', methods=['GET'])
def list_students():
     """

     sends all students in students_data collection

     """
     if not request.args:
          data = list(mydb.students_data.find({},{'_id':0}))
          return jsonify(data), 200
     else:
          return '', 406


@app.route('/api/v0.1/listevents', methods=['GET'])
def list_event():
     """

     sends all the events in events collection if no arguments supplied

     send all eligible  events for a student if usn is passed in arguments

     """  

     if not request.args:
          data = list(mydb.events.find({},{'_id':0}))
          return jsonify(data), 200

     elif 'usn' in request.args and len(request.args) == 1:

          if helper_obj.validate_usn(request.args['usn']):
               data = helper_obj.get_events_for_usn(request.args['usn'])
               return jsonify(data), 200
          else:
               return '', 404
 
     else :
          return  '', 400 


@app.route('/api/v0.1/attendevent', methods=['POST'])
def attend_event():

     """

     validates a student token, 
     and adds to attendance collection if token is valid
     return appropriate message

     """  

     if  len(request.args) != 3 or \
          ('usn' not in request.args and 'eid' not in request.args and 'token' not in request.args) :
          return '', 400
     else :
          usn = request.args['usn']
          eid = request.args['eid']
          token = request.args['token']
          if helper_obj.validate_reg_token(usn, eid, token):
               data = { 'message' : 'Valid token'}
               mydb.attendance_collection.insert_one( {  'token' : token, 'usn' : usn, 'eid' : eid })
               return jsonify(data), 200
          else:
               data = { 'message' : 'Invalid token'}
               return jsonify(data), 401


@app.route('/api/v0.1/registerevent', methods=['POST'])
def register_event():

@app.route('/api/v0.1/mailattendees', methods=['POST'])
def mail_attendance():



@app.route('/api/v0.1/sendinvitation', methods=['POST'])
def send_invitation():



@app.route('/api/v0.1/rmevent', methods=['POST'])
def remove_event():





# TODO : add watchdog, removes  events which are inactive

# TODO : handle status codes

# TODO : validate structure of json, while adding events, and rest

# TODO : proper PEP8 compatibles

'''
@app.errorhandler(400)
def bad_request(e):

     message = {
          
          'err' :
          
          { 'message' : 'Please refer API documentation.'}

     }

     resp = jsonify(message)

     resp.status_code = 200

     return resp


'''


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5555, ssl_context=('cert.pem', 'key.pem'))


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


@app.route('/api/v0.1/addevents', methods=['POST'])
def add_event():


@app.route('/api/v0.1/liststudents', methods=['GET'])
def list_students():


@app.route('/api/v0.1/listevents', methods=['GET'])
def list_event():


@app.route('/api/v0.1/attendevent', methods=['POST'])
def attend_event():



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

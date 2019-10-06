import email_sender


class helper(object):

    def __init__(self, dbobject):
        self.mydb = dbobject


    def validate_token(self, auth_token):
        return len(list(self.mydb.faculty_coordinators.find({'api_token':  auth_token.strip()  }))) > 0 



    def get_user_from_token(self,  auth_token):

        user =  list(self.mydb.faculty_coordinators.find({'api_token':  auth_token.strip()  }))
        return  user[0]['coordinator_id']


    def constraint_check(self,  usn, eid):
        student_data = list(self.mydb.students_data.find({'StudentID':  usn.strip()  }))[0]
        
        event_data = list(self.mydb.events.find({'eid':  eid  }))[0]

        if event_data['vacancy'] > 0:
            if   'OPEN' in event_data['branch'] or student_data['branch'] in event_data['branch']:
            
    
                if -1 in event_data['Year'] or student_data['year'] in event_data['Year']  :

                        if event_data['cgpa'] == -1 or student_data['cgpa'] >= event_data['cgpa']:
                            if student_data['attendence'] >= 75.0:
                                return True, 'eligible'
                            else:
                                return  False, 'attendence shortage'
                        else:
                            return  False, 'cgpa constraint'
                else:
                        return  False, 'year constraint'
            else:
                return  False, 'branch constraint'
        else:
            return  False, 'no vacancy'




    def get_events_for_usn(self,  usn):
        data = []
        
        for event in list(self.mydb.events.find({},{'_id':0})) :
            
            constraint, _reason = self.constraint_check( usn, event['eid'] )
            
            if constraint:
                data.append(event)
                
        return data


    def validate_reg_token(self,  usn, eid, token):
        
        if self.validate_usn( usn) and self.validate_event( eid):
            reglist = list(self.mydb.events.find({'eid' : eid.strip() }))[0]['registered_students']
            if [usn,token] in reglist:
                return True
        return False 

    def validate_usn(self,  usn):
        
        return len(list(self.mydb.students_data.find({'StudentID':  usn.strip()  }))) > 0 


    def validate_event(self,  eid):
        
    
        return len(list(self.mydb.events.find({'eid': eid.strip()  }))) > 0 




    def update_event( self, usn, eid):
        """

        TODO : better token implementation
        """

        event = list(self.mydb.events.find({'eid': eid  }))[0]
    
        token = str(abs(hash(str(eid)+str(usn))))     # token implementation
        
        old_list =  list(self.mydb.events.find({'eid': eid.strip()  }))[0]['registered_students']
        
        if usn  not in [ i[0] for i in old_list] : 

            old_list.append(  [usn, token] )
            self.mydb.events.update(  {  "eid" : eid  },  {   "$set"  :   { "registered_students" : old_list  } } )
            self.mydb.events.update(  {  "eid" : eid  },  {   "$inc"  :   { "vacancy" : -1  } } )
        
            email =   list(self.mydb.students_data.find({'StudentID': usn.strip() }))[0]['email']
            email_sender.send_token(email, token, event)
            print('sending invitation')
        
        return token


    def get_email( self,  auth_token):

        return list(self.mydb.faculty_coordinators.find({'api_token' : auth_token}))[0]['email']


    def get_name(self, usn):

        return list(self.mydb.students_data.find({'StudentID': usn}))[0]['name']  


    def get_event_name(self,  eid):

        return list(self.mydb.events.find({'eid': eid }))[0]['ename'] 


    def get_attendees(self,  eid, email):
        data = list(self.mydb.attendance_collection.find({'eid' : eid.strip() },{'_id':0}))
        student_list = { x['usn']: self.get_name(  x['usn'])   for x in data }
        event_name = self.get_event_name(eid)
        print(email, event_name)
        email_sender.send_list(sorted(student_list.items()), email, event_name)
        print('sending email')
        return data


    def invite_eligible_students(self,  eid):

        usns = [ (x['StudentID'], x['email'], x['name']) for x in list(self.mydb.students_data.find({})) ]
        event = list(self.mydb.events.find({'eid': eid  }))[0]
        
        for usn, email, name in usns:
            constraint, _reason = self.constraint_check(usn, eid)
            if constraint :
                email_sender.send_invite(email, name, event )
        print('email invites sent')
        return usns

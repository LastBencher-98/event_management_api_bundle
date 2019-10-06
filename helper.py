import email_sender


class helper(object):

    def __init__(self, dbobject):
        self.mydb = dbobject

    def validate_token(self, auth_token):
         pass


    def get_user_from_token(self,  auth_token):

         pass


    def constraint_check(self,  usn, eid):

         pass


    def get_events_for_usn(self,  usn):

         pass


    def validate_reg_token(self,  usn, eid, token):

         pass

    def validate_usn(self,  usn):

         pass

    def validate_event(self,  eid):
        
         pass




    def update_event( self, usn, eid):

         pass


    def get_email( self,  auth_token):

         pass


    def get_name(self, usn):

         pass


    def get_event_name(self,  eid):

         pass


    def get_attendees(self,  eid, email):

         pass

    def invite_eligible_students(self,  eid):

         pass

try : 
    import ezgmail

except :
        print("check https://pypi.org/project/EZGmail/ for configuring initially")

import datetime



def  send( data):
    for i in data:
        body_string = f'''
You are assigned as an event co-ordinator, your authentication token is given below
Your token : "{hash(i)} "
please do not share it publically'''
        ezgmail.send( i.strip(), 'Assigned as event coordinator', body_string)


def send_token(email, token, event ):
        date_obj = eval( event['date'])
        body_string = f'''
You have been successfully registered  to the event {event['ename']},  {event['caption']}
which will be held  on  { date_obj.strftime("%m/%d/%Y") }
Your  registration token : "{token} ".
Please carry it on the day of event '''
        subject = f"Registration for {event['ename'].upper()} successful"
        ezgmail.send( email, subject, body_string)



def  send_list(data, email, event_name):

        slist = [ "\n\nUSN\t\t\t\tNAME"]
        for i in data:
                slist.append(f'{i[0]}\t\t{i[1]}')
        
        subject = f'{event_name} attendees list'
        body = '\n'.join(slist) + '\n\n Please consider the attendance for the above students'

        ezgmail.send( email, subject, body)


def send_invite(email, recipient,  event ):

        subject = f"Invitation for the event {event['ename']}"
        date_obj = eval( event['date'])
        body = f"""Hello, {recipient} 
You are cordially invited to {event['ename']},  {event['caption']}


Event Details :
        
Date:  { date_obj.strftime("%m/%d/%Y") }.
Location : {event['location'].capitalize()} .
Capacity : {event['nos']}. 

Please register if interested. 
Attendance will be provided.
        """
        ezgmail.send(email, subject, body)
try : 
    import ezgmail

except :
        print("check https://pypi.org/project/EZGmail/ for configuring initially")




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

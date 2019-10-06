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



try : 
    import ezgmail

except :
        print("check https://pypi.org/project/EZGmail/ for configuring initially")




def send(email, subject, body):
    ezgmail.send(email, subject, body)

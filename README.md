# Event Management API Bundle

The API bundle that manages event records and resolves attendance issues for the events


## API Documentation (POSTMAN)

(Link)[https://documenter.getpostman.com/view/9043780/SVtR3rAM?version=latest]


## Usage


### Clone the repository


    git clone https://github.com/LastBencher-98/event_management_api_bundle.git




### Build Docker (optional because not yet tested)

Run the image, binding associated ports, and mounting the present working
directory:

 build `event_mgmt/api_container` from source:
 
    cd event_management_api_bundle
    docker run -p 5555:5555 event_mgmt/api_container 


### Config Gmail API
A Pythonic interface to the Gmail API that actually works as of June 2019.

The Gmail API quickstart doesn't actually seem to work on Python 3 without some adjustments, and the entire documentation is a bit much for someone who just wants to read and send emails from their Gmail account. EZGmail just works.

The Gmail API documentation by Google is available at https://developers.google.com/gmail/api/

You will need to download a credentials-gmail.json file by going to https://developers.google.com/gmail/api/quickstart/python and clicking the Enable the Gmail API button (after logging in to your Gmail account). You will need to rename the downloaded credentials.json file to credentials-gmail.json.


###  Install Requirements

    pip3 install -r requirements.txt


### Install and Configure MongoDB 

Please visit here [Getting_started_MongoDB](https://docs.mongodb.com/manual/tutorial/getting-started/)
Pass the right host domain/ip and port in flask_server.py


### Populate Students to DB

    python3 populate_students.py --help
    python3 populate_students.py --filename students.xlsx 


### Populate Co-ordinators to DB

Pass yes/no for notifying the co-oridinators via email

    python3 populate_cords.py --help
    python3 populate_cords.py --filename students.xlsx --email yes


### Run the Documentaion server

    python3 flask_document_server.py


### Generate self-signed digital certificates (optional) 


    chmod +x self_signed_key_gen.sh
    ./self_signed_key_gen.sh

Replace if you have CA certificates, replace cert.pem and key.pem respectively


### Run  the API server 

For running over http

    python3 flask_server.py nossl


For running over https

    python3 flask_server.py ssl


## Contributors

    [Vishal_Nayak](https://github.com/LastBencher-98/)
    [Ravish](https://github.com/ravish0007/)
    [Divyashree](https://github.com/DivyashreeNaik)
    [Sumana_Rehaman](https://github.com/nismiya)




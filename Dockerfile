FROM ubuntu:16.04

MAINTANER Your Name "ravish@gmail.com"

RUN apt-get update -y && \
    apt-get install -y python3 python-pip3 python-dev3 openssl wget

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

CMD ["wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | sudo apt-key add - "]

RUN echo "deb [ arch=amd64 ] https://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/4.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.2.list

CMD ["apt-get update"]

CMD ["sudo apt-get install -y mongodb-org"]

CMD ["service mongod start"]


CMD ["chmod +x self_signed_key_gen.sh ; ./self_signed_key_gen.sh"]

CMD ["chmod +x populate_cord.py"]

CMD ["./populate_cord.py  --filename cords.xlsx --email yes"]


CMD ["chmod +x populate_students.py"]

CMD ["./populate_students.py  --filename students.xlsx --email yes"]

ENTRYPOINT [ "python" ]

CMD [ "flask_server.py" ]
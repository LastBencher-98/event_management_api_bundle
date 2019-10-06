from flask import Flask, redirect
from flask_restful import Api, Resource 


app = Flask(__name__)



@app.route('/')
def hello():
    return redirect("https://documenter.getpostman.com/view/9043780/SVtR3rAM?version=latest", code=302)





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

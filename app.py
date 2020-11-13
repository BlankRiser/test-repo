import os
from flask_sqlalchemy import SQLAlchemy

# os.environ["DJANGO_SETTINGS_MODULE"] = "proj.settings"

# import django  # noqa: E402 module level import not at top of file

# django.setup()

from flask import Flask, request, json
# from hello.models import GithubData
app = Flask(__name__)

# app.config.from_object(os.environ['APP_SETTINGS'])


app.config['SQLALCHEMY_DATABASE_URI']='postgres://mdbtssfxfrfmbt:85e19ba21e968ac1f3b04a6da1fa2cbe629fed7ab4851f143e85b3728fd16b89@ec2-34-200-106-49.compute-1.amazonaws.com:5432/d9o5stbu9dopan'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import *

# any method
# any URL
@app.route('/')
def received():

    print(request.method)
    headers = request.headers

    body = request.json
    body = str(body)
    method =request.method
    url = request.url
    print("Url: ", url)
    print("\nheaders: ", headers)
    
    body = request.json
    body = str(body) 

    # GithubData.objects.create(path=url, method=method, headers=headers, body=body)
    
    webhook_data = Webhook_data(path =url,method = method,headers = headers,body = body)
    db.session.add(webhook_data)
    db.session.commit()

    return "ok"


@app.route('/<path:path>', methods=['GET', 'POST', 'PUT','HEAD','DELETE']) 
def receivedParams(path):

    print(request.method)
    headers = request.headers

    body = request.json
    body = str(body)

    method =request.method
    url = request.url

    print("Url: ", url)
    print("\nheaders: ", headers)
    
    body = request.json
    body = str(body) 

    # GithubData.objects.create(path=url, method=method, headers=headers, body=body)
    
    webhook_data = Webhook_data(path =url,method = method,headers = headers,body = body)
    db.session.add(webhook_data)
    db.session.commit()

    return "ok"

if __name__ =='__main__':
    app.run(debug=True)
import os
from flask_sqlalchemy import SQLAlchemy
from models import *


from flask import Flask, request, json
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='postgres://mdbtssfxfrfmbt:85e19ba21e968ac1f3b04a6da1fa2cbe629fed7ab4851f143e85b3728fd16b89@ec2-34-200-106-49.compute-1.amazonaws.com:5432/d9o5stbu9dopan'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/', methods=['GET', 'POST', 'PUT','HEAD','DELETE'])
def retrieveData():
    # parameters = request.args #returns ImmutableMultiDict([])
    # print("parameters: ", parameters)

    method =request.method
    print(request.method)

    headers = request.headers
    headers = str(headers)
    print("\nheaders: ", headers)

    url = request.url
    print("Path: ", url)

    # body = request.json 
    # json can be easier to parse later but make sure request.headers['Content-type'] is 'application/json'
    body = request.data
    body = str(body)

    webhook_data = Webhook_data(path =url,method = method,headers = headers,body = body)
    db.session.add(webhook_data)
    db.session.commit()
    
    return "ok"
    
    # if request.headers['Content-type'] == 'application/json':
    #    with open('data.json', 'w', encoding='utf-8') as f:
    #        json.dump(request.json, f, ensure_ascii=False, indent=4)
    #    return json.dumps(request.json) 

@app.route('/<path:path>', methods=['GET', 'POST', 'PUT','HEAD','DELETE']) 
def retrieveDataParam(path):

    method =request.method
    print(request.method)

    headers = request.headers
    headers = str(headers)
    print("\nheaders: ", headers)

    url = request.url
    print("Path: ", url)

    # body = request.json 
    # json can be easier to parse later but make sure request.headers['Content-type'] is 'application/json'
    body = request.data
    body = str(body)

    webhook_data = Webhook_data(path =url,method = method,headers = headers,body = body)
    db.session.add(webhook_data)
    db.session.commit()
    
    # GithubData.objects.create(path=url, method=method, headers=headers, body=body)
    return "ok"

if __name__ =='__main__':
    app.run(debug=True)
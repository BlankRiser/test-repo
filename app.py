import os

os.environ["DJANGO_SETTINGS_MODULE"] = "proj.settings"

import django  # noqa: E402 module level import not at top of file

django.setup()

from flask import Flask, request, json
from hello.models import GithubData
app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])


# any method
# any URL
# @app.route('/')
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT','HEAD','DELETE']) 
def api_gh_msg(path):
    """
    Flask lets you get all the methods only when mentioned explicitly 
    or by the default would be GET method
    WebHook connector that get gets the details which GitHub posts.
    (Still working on it)
    Returns:
        dictionary: JSON that is sent to the above route by GitHub to subscribed events.
    """
    print(request.method)
    headers = request.headers
    # parameters = request.args #returns ImmutableMultiDict([])
    # print("parameters: ", parameters)
    body = request.json
    body = str(body)
    method =request.method
    url = request.url
    print("Url: ", url)
    print("\nheaders: ", headers)
    
    # body = request.json 
    # json can be easier to parse later but make sure request.headers['Content-type'] is 'application/json'
    body = request.data 
    GithubData.objects.create(path=url, method=method, headers=headers, body=body)

    return "ok"



    # if request.headers['Content-type'] == 'application/json':
    #    with open('data.json', 'w', encoding='utf-8') as f:
    #        json.dump(request.json, f, ensure_ascii=False, indent=4)
    #    return json.dumps(request.json) 

if __name__ =='__main__':
    app.run(debug=True)
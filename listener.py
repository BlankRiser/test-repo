from flask import Flask, request, json
import json


app = Flask(__name__)


@app.route('/', methods=['POST'])
def api_gh_msg():
    """
    WebHook connector that get gets the details which GitHub posts.
    (Still working on it)
    Returns:
        dictionary: JSON that is sent to the above route by GitHub to subscribed events.
    """
    headers = request.headers
    print(headers)
    if request.headers['Content-type'] == 'application/json':
       with open('data.json', 'w', encoding='utf-8') as f:
           json.dump(request.json, f, ensure_ascii=False, indent=4)
       return json.dumps(request.json) 

if __name__ =='__main__':
    app.run(debug=True)
from json.decoder import JSONDecodeError
from flask import Flask,render_template
import requests,json

app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/virtual",methods=['GET'])
def hosts():
    # r = input("Select virtual hosts:")  
    response=requests.get("http://localhost:15672/api/vhosts/vh1")
    # response=requests.get("https://api.github.com")
    res = response.json() 
    # return dict(response.json())
    # res=dict(response)
    print(json.dumps(res ,indent= 4,))
    return json.dumps(res , indent= 4,)
    # return (res)

@app.route("/vhostq",methods=['GET'])
def queue():
    # vhost=input("select vhost:")
    # response=requests.get('http://localhost:15672/api/queues/{vhost}')    
    response=requests.get("http://localhost:15672/api/queues/vh1")
    # res1=dict(response.text)
    # res1=dict(response.headers)
    # print(json.dumps(res1 ,indent=4))
    # return json.dumps(res1 , indent=4)
    print(response)
    return str(response)

if __name__ == "__main__":  
    app.run(debug=True)    

from flask import Flask, request
from flask_restplus import Api, Resource, fields

app = Flask(__name__)

api = Api(app, version='1.0', title="My First API", description="Here's an API to try, there are several methods here you can ping")

@api.route('/sum')
@api.doc(params={"parma":"2","parmb":"3"})
class Sum(Resource):
    def get(self):
        return int(request.args.get("parma"))+int(request.args.get("parmb"))

@api.route('/compute/<string:action>')
@api.doc(params={"parma":"2","parmb":"3"})
class Compute(Resource):
    def get(self,action):
        a=int(request.args.get("parma"))
        b=int(request.args.get("parmb"))
        if action =="sum":
            return a+b
        elif action == "subtract":
            return a-b
        elif action == "multiply":
            return a*b
        elif action == "divide":
            return a/b
        else:
            return f"sorry, I don't know how to '{action}'"

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)

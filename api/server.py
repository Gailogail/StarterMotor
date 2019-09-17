from flask import Flask, request
from flask_restplus import Api, Resource, fields
import random
import string

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

@api.route('/evaluate')
@api.doc(params={"password":"hunter2"})
class Sum(Resource):
    def get(self):
        return "Of course not, you sent it as plaintext over an unsecured connection. You muppet."

def random_word(uppercase=False):
    with open("words.txt") as f:
        raw_words=f.read()
    split_words=raw_words.split()
    total_words=len(split_words)
    random_index=random.randint(0,total_words)
    word=split_words[random_index]
    if uppercase:
        word=word[0].upper()+word[1:]
    return word

post_fields = api.model('Model', {
         'length': fields.Integer(default=4),
         "special": fields.Boolean,
         "number": fields.Boolean,
         "separator": fields.String(default=""),
         "uppercase": fields.Boolean,
             })
@api.route('/generate')
class generatePassword(Resource):

     @api.expect(post_fields)
     def post(self):
         json_data = request.json
         password=""
         for i in range(json_data['length']):
             if password is not "":
                 password+=json_data['separator']
             uppercase = json_data['uppercase']
             password+=random_word(uppercase)
         if json_data['special']:
             password+=random.choice(string.punctuation)
         if json_data['number']:
             password+=random.choice(string.digits)
         return password


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)

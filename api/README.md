To run:

* (Optional) set up a virutal environment
* run `pip install -r requirements.txt`
* Run server with `python server.py`
* Check 127.0.0.1:5000 in your browser to see if it's running correctly
* Run client with `python client.py`

The server offers 4 APIs:
* GET /compute/<action>?first=a&second=b
    * if <action> is "sum" return a+b
    * if <action> is "multiply" return axb
    * if <action> is "divide" return a/b
    * if <action> is "subtract" return a-b
* GET /sum?first=a&second=b
* GET /evaluate?password=hunter2
        * tells the user they are an idiot
* POST /generate
        * takes a json of the form:
                {
                  "length": 4,
                  "special": true,
                  "number": true,
                  "separator": "-",
                  "uppercase": true
                }
        * returns a correct-horse-battery-staple password

The client goes through 3 steps:
* A basic GET request to /compute/
* Asks the user for their password, and then returns the response of /evaluate
* Asks for some configuration settings and then returns a Correct Horse Battery Stabple password

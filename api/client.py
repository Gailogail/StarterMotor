import requests  # We're using a library to simplify making API requests


print("1+1=")
# send a post request to our server to do this terribly complicated calculation for us
r = requests.get("http://127.0.0.1:5000/compute/sum?first=1&second=1")
# Throw an error if the get request didn't work
assert r.status_code == 200
print(r.text)
print()

print("Is your password secure?")
password = input("Enter your password:")
r = requests.get(f"http://127.0.0.1:5000/evaluate?password={password}")
assert r.status_code == 200
print(r.text)

print("How about we make a new one?")
config = {}
config["length"] = int(input("How many words?"))
config["separator"] = input("What should go between words? ('-','_','+')")
while True:
    response = input("Special characters? (y/n)")
    if response == "y":
        config["special"] = True
        break
    elif response == "n":
        config["special"] = False
        break
    else:
        print("Please type 'y' or 'n'")

while True:
    response = input("Include a number? (y/n)")
    if response == "y":
        config["number"] = True
        break
    elif response == "n":
        config["number"] = False
        break
    else:
        print("Please type 'y' or 'n'")

while True:
    response = input("Make the first letter of each word uppercase? (y/n)")
    if response == "y":
        config["uppercase"] = True
        break
    elif response == "n":
        config["uppercase"] = False
        break
    else:
        print("Please type 'y' or 'n'")

r = requests.post("http://127.0.0.1:5000/generate", json=config)
assert r.status_code == 200
print(r.text)

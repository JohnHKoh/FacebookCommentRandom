import requests
import json
import time
import random
import math

def comment(parameters, link):
    while True:
        r = requests.post(link, parameters)
        result = json.dumps(r.json(), indent=4, sort_keys=True)
        print result
        rand = random.randint(600, 3600)
        print "Sleeping for {} minutes".format(math.floor(rand/60))
        time.sleep(rand)


if __name__ == "__main__":
    # User customizable
    token = ""
    message = ""
    link = "" # Comment node, should look like https://graph.facebook.com/NUMBERS/comments

    # Don't touch below this line
    access_token = token

    parameters = {'access_token': access_token,
                  'message': message}


    comment(parameters, link)

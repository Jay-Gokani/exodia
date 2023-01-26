# import the Flask (web app) framework for Python
import time
import redis
from flask import Flask

# variable for assigning the script as a programme or module based on line 13
app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

# getting number of hits
def get_hits():
    retries = 3
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

# take the user to the URL '/' i.e. homepage and display text
@app.route('/')
def index():
    count = get_hits()
    return 'Hello there, Jay! This page has been viewed {} times.\n'.format(count)

# only execute code if run as a programme (opposed to as a module)
# if __name__ == "__main__":
#    app.run(debug=True)
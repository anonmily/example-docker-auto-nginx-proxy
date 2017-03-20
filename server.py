from flask import Flask
import os, uuid
app = Flask(__name__)

UNIQUE_IDENTIFIER = uuid.uuid1()

@app.route("/")
def hello():
    return "Hello World. I am %s" % UNIQUE_IDENTIFIER

if __name__ == "__main__":
	try:
		app.run(host="0.0.0.0", port=os.environ.get("PORT",5000))
	except KeyboardInterrupt:
		print("Exiting")

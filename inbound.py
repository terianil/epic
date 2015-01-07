from flask import *
import logging
 

app = Flask(__name__)

@app.route("/inbound", methods=['POST'])
def hello():
	app.logger.debug('I\'m working.')

	return request.data 

if __name__ == "__main__":
	app.logger.addHandler(logging.StreamHandler())
	app.logger.setLevel(logging.DEBUG)

	app.run()

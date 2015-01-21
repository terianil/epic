from flask import *  # @UnusedWildImport
import logging  # @Reimport
import json  # @Reimport
from InboundPort import InboundPort 
from Query import *  # @UnusedWildImport
from XMLParser import XMLParser
import sys


app = Flask(__name__)
port = InboundPort()
query = Query()

@app.route("/inbound", methods=['POST'])
def inbound():
	app.logger.debug('I\'m working.')

	data = json.dumps(request.get_json())
	port.receive(data)

	return port.printAll()

if __name__ == "__main__":
	query = XMLParser.printme(sys.argv[1])
	print("Field: " + query.field)
	print("Function: " + query.functionType.name)
	print("Time: " + query.time)
	print("ConditionType: " + query.conditionType.name)
	print("ConditionArument: " + query.conditionArgument)
	app.logger.addHandler(logging.StreamHandler())
	app.logger.setLevel(logging.DEBUG)

	app.run(port=50001)

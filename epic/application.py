from flask import *  # @UnusedWildImport
import logging  # @Reimport
import json  # @Reimport
import sys
from epic.InboundPort import InboundPort
from epic.QueryProcessorManager import QueryProcessorManager


app = Flask(__name__)
port = InboundPort()
queryManager = QueryProcessorManager()


@app.route("/inbound", methods=['POST'])
def inbound():
    app.logger.debug('I\'m working.')

    data = json.dumps(request.get_json())
    port.receive(data)

    return port.printAll()


if __name__ == "__main__":
    app.logger.addHandler(logging.StreamHandler())
    app.logger.setLevel(logging.DEBUG)

    app.run(port=50001)

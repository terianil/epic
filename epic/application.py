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
    queryManager.addTuple(request.get_json())

    port.receive(data)



    return port.printAll()

@app.route("/addquery", methods=['POST'])
def addQuery():
    try:
        queryManager.addQueryProcessor(str(request.form['query']))
        return redirect('/')
    except:
        return '<h3>Syntax error!</h3></br></br><a href="/addqueryform"> Back </a>'


@app.route("/addqueryform", methods=['GET'])
def addQueryForm():
    return render_template('newQueryForm.html')

@app.route("/", methods=['GET'])
def queries():
    response = '<html><head><meta http-equiv="refresh" content="1" >'

    response += '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">'
    response += '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap-theme.min.css">'
    response += '<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js"></script>'
    response += '<script src="//code.jquery.com/jquery-1.11.2.min.js"></script>'

    response += '</head><body>'

    response += '<a href="/addqueryform"><button>Add new query</button></a>'

    response += '<table class="table table-hover" style="margin-top: 50px">'
    response += '<thead><tr class="row">'
    response += '<th class="col-md-4">Query</td>'
    response += '<th class="col-md-4">Result</td>'
    response += '</tr></thead><tbody>'
    for queryProcessor in queryManager.getQueryProcessors():
        response += '<tr class="row">'
        response += '<td class="col-md-4">'+ queryProcessor.query.toString()+ '</td>'
        response += '<td class="col-md-4">' + str(queryProcessor.executeQuery()) + '</td>'
        response += '</tr>'

    response += '</tbody></table>'

    response += '</body></html>'

    return response

if __name__ == "__main__":
    app.logger.addHandler(logging.StreamHandler())
    app.logger.setLevel(logging.DEBUG)

    app.run(port=50001)

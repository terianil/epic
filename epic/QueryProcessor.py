from flask import json
from epic import Query


class QueryProcessor:
    query = None
    data = None

    def __init__(self, query):
        assert isinstance(query, Query)
        self.query = query

    def executeQuery(self):
        pass

    def insertNewTuple(self, tuple):
        assert isinstance(tuple, json)
        pass

    def getQueryData(self):
        pass
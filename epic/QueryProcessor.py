from collections import deque
import json
from epic.Query import Query


class QueryProcessor:
    query = Query()
    data = deque()

    def __init__(self, query):
        assert isinstance(query, Query)
        self.query = query

    def executeQuery(self):
        pass

    def insertNewTuple(self, tuple):
        self.data.append(5)
        pass

    def getQueryData(self):
        pass
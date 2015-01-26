from collections import deque
from epic.Query import Query
from epic.Tuple import Tuple
import datetime
from datetime import timedelta


class QueryProcessor:
    query = None
    data = deque()

    def __init__(self, query):
        assert isinstance(query, Query)
        self.query = query

    def executeQuery(self):
        pass

    def insertNewTuple(self, json):
        self.data.append(Tuple(json[self.query.field]))

    def getQueryData(self):
        return self.data

    def tick(self):
        self.data = [item for item in self.data if item.timestamp >= (datetime.datetime.now() - timedelta(seconds=self.query.time))]

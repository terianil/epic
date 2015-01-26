from collections import deque
from epic.QueryParserFromXml import QueryParserFromXml
from epic.QueryProcessor import QueryProcessor


class QueryProcessorManager:
    queryProcessors = deque

    def __init__(self):
        self.queryProcessors = deque()

    def addQueryProcessor(self, query):
        queryParser = QueryParserFromXml()
        self.queryProcessors.append(QueryProcessor(queryParser.parse(query)))


    def addTuple(self, tuple):
        for item in self.queryProcessors:
            item.insertNewTuple(tuple)
from collections import deque
from epic.AggregationFunctionType import AggregationFunctionType
from epic.ConditionType import ConditionType
from epic.Query import Query
from epic.Tuple import Tuple
import datetime
from datetime import timedelta


class QueryProcessor:
    query = None
    data = deque

    def __init__(self, query):
        #assert isinstance(query, Query)
        self.query = query
        self.data = deque()

    def executeQuery(self):
        self.tick()

        result = None

        if(self.query.functionType is AggregationFunctionType.Sum):
            result = self.executeSumQuery()
        elif(self.query.functionType is AggregationFunctionType.Avg):
            result = self.executeAvgQuery()

        print('result: ' + str(result))

        return self.checkQueryCondition(result)



    def executeSumQuery(self):
        return sum(item.data for item in self.data)

    def executeAvgQuery(self):
        if len(self.data) != 0:
            return sum(item.data for item in self.data) / len(self.data)

        return 0.0

    def checkQueryCondition(self, queryResultValue):
        if queryResultValue is None:
            return False

        return {
            ConditionType.GreaterThan: queryResultValue > self.query.conditionArgument,
            ConditionType.LessThan: queryResultValue < self.query.conditionArgument,
        }[self.query.conditionType]

    def insertNewTuple(self, json):
        self.data.append(Tuple(json[self.query.field]))
        print('pole:' + str(json[self.query.field]))

    def getQueryData(self):
        return self.data

    def tick(self):
        self.data = [item for item in self.data if item.timestamp >= (datetime.datetime.now() - timedelta(seconds=self.query.time))]

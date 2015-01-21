import json
from time import sleep
from unittest import TestCase, main
from epic.AggregationFunctionType import AggregationFunctionType
from epic.ConditionType import ConditionType
from epic.Query import Query
from epic.QueryProcessor import QueryProcessor

__author__ = 'terianil'


class TestQueryProcessor(TestCase):
    def test_QueryProcessorShouldStoreRightValuesFromInputJson(self):
        #Arrange
        query = Query("b", AggregationFunctionType.Avg, 5, ConditionType.GreaterThan, 5)
        queryProcessor = QueryProcessor(query)

        tuple1 = json.loads('{"a": 1, "b": 2, "c": 3}')
        tuple2 = json.loads('{"a": 4, "b": 5, "c": 6}')
        tuple3 = json.loads('{"a": 7, "b": 8, "c": 9}')

        #Act
        queryProcessor.insertNewTuple(tuple1)
        queryProcessor.insertNewTuple(tuple2)
        queryProcessor.insertNewTuple(tuple3)

        queryData = queryProcessor.getQueryData()

        #Assert
        self.assertEquals(queryData[0].data, 2)
        self.assertEquals(queryData[1].data, 5)
        self.assertEquals(queryData[2].data, 8)

    def test_QueryProcessorShouldRemoveDataOlderThanWindowSize(self):
        #Arrange
        query = Query("b", AggregationFunctionType.Avg, 1, ConditionType.GreaterThan, 5)
        queryProcessor = QueryProcessor(query)

        tuple1 = json.loads('{"a": 1, "b": 2, "c": 3}')
        tuple2 = json.loads('{"a": 4, "b": 5, "c": 6}')

        #Act
        queryProcessor.insertNewTuple(tuple1)
        queryProcessor.insertNewTuple(tuple2)

        sleep(2)

        queryData = queryProcessor.getQueryData()

        #Assert
        self.assertEquals(len(queryData), 0)


if __name__ == '__main__':
    main()
from xml.dom import minidom
from AggregationFunctionType import AggregationFunctionType
from ConditionType import ConditionType
from Query import Query
import sys

#otwieramy plik w parserze
class XMLParser:
    @staticmethod
    def printme (path):
        DOMTree = minidom.parse(path)

        name = DOMTree.getElementsByTagName("Field")[0]
        field = name.firstChild.data

        name = DOMTree.getElementsByTagName("Function")[0]
        aggregateFunctionType = name.firstChild.data
        if aggregateFunctionType == "sum":
            aggregateFunctionType = AggregationFunctionType.Sum
        elif aggregateFunctionType == "avg":
            aggregateFunctionType = AggregationFunctionType.Avg
    
        name = DOMTree.getElementsByTagName("Time")[0]
        time = name.firstChild.data

        name = DOMTree.getElementsByTagName("ConditionType")[0]
        conditionType = name.firstChild.data
        if conditionType == "GreaterThan":
            conditionType = ConditionType.GreaterThan
        elif conditionType == "LessThan":
            conditionType = ConditionType.LessThan
    
        name = DOMTree.getElementsByTagName("ConditionArgument")[0]
        conditionArgument = name.firstChild.data
    
        b = Query(field, aggregateFunctionType, time, conditionType, conditionArgument)

        print(field)
        print(aggregateFunctionType)
        print(time)
        print(conditionType)
        print(conditionArgument)
        print(sys.argv[1])
        
        return b
from xml.dom import minidom
from epic.AggregationFunctionType import AggregationFunctionType
from epic.ConditionType import ConditionType
from lxml import etree  # @UnresolvedImport
import sys

#otwieramy plik w parserze
from epic.Query import Query


class QueryParserFromXml:
    def parse (self, query):
        with open("schema.xsd", 'r') as f:
            schema_root = etree.XML(f.read())

        schema = etree.XMLSchema(schema_root)
        xmlparser = etree.XMLParser(schema=schema)
        
        try:
            etree.fromstring(query, xmlparser)
            print("XML OK")
        except:
            print("XML BAD")
        
        DOMTree = minidom.parseString(query)

        name = DOMTree.getElementsByTagName("Field")[0]
        field = name.firstChild.data

        name = DOMTree.getElementsByTagName("Function")[0]
        aggregateFunctionType = name.firstChild.data
        if aggregateFunctionType == "Sum":
            aggregateFunctionType = AggregationFunctionType.Sum
        elif aggregateFunctionType == "Avg":
            aggregateFunctionType = AggregationFunctionType.Avg
    
        name = DOMTree.getElementsByTagName("Time")[0]
        time = float(name.firstChild.data)

        name = DOMTree.getElementsByTagName("ConditionType")[0]
        conditionType = name.firstChild.data
        if conditionType == "GreaterThan":
            conditionType = ConditionType.GreaterThan
        elif conditionType == "LessThan":
            conditionType = ConditionType.LessThan

        print(str(type(conditionType)))
    
        name = DOMTree.getElementsByTagName("ConditionArgument")[0]
        conditionArgument = float(name.firstChild.data)
    
        query = Query(field, aggregateFunctionType, time, conditionType, conditionArgument)
        
        return query
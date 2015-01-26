from epic.AggregationFunctionType import AggregationFunctionType
from epic.ConditionType import ConditionType


class Query:
    functionType = None
    time = None
    field = None
    conditionType = None
    conditionArgument = None

    def __init__(self, field="field1", functionType=AggregationFunctionType.Sum, time=5,
                 conditionType=ConditionType.GreaterThan, conditionArgument=100):
        self.field = field
        self.functionType = functionType
        self.time = time
        self.conditionType = conditionType
        self.conditionArgument = conditionArgument

    def toString(self):
        return ' <b>funcion:</b> ' + str(self.functionType.name)+' <b>condition:</b> ' + str(self.conditionType.name)\
               +' ' + str(self.conditionArgument)  +' <b>time:</b>' + str(self.time)
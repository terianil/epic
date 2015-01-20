from ConditionType import *
from AggregationFunctionType import *

class Query:
	functionType = None
	time = None
	field = None
	conditionType = None
	conditionArgument = None

	def __init__(self, functionType=AggregationFunctionType.Sum, time=5, field="field1", conditionType=ConditionType.GreaterThan, conditionArgument=100):
		self.functionType = functionType
		self.time = time
		self.field = field
		self.conditionType = conditionType
		self.conditionArgument = conditionArgument

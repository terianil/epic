import datetime


class Tuple:
    data = None
    timestamp = None

    def __init__(self, data):
        self.timestamp = datetime.datetime.now()
        print('tuple:' + str(self.timestamp))
        self.data = data

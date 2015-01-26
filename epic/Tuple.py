import datetime


class Tuple:
    data = None
    timestamp = None

    def __init__(self, data):
        self.timestamp = datetime.datetime.now()
        self.data = data

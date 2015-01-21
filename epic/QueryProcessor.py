from epic import Query


class QueryProcessor:
    query = None
    def __init__(self, query):
        assert isinstance(query, Query)
        self.query = query
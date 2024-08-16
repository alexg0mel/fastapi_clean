from . import QueryStore


class TestQueryStory(QueryStore):

    def raw_query(self) -> str:
        return "select {foo} from {bar} where baz={baz}"

    async def execute(self, conn):
        pass


class TestQueryStore:
    def test(self):
        params = {'foo': 'FOO', 'bar': 'BAR', 'baz': 'BAZ'}
        test_query = TestQueryStory(**params)
        assert [param for param in test_query.params] == ['FOO', 'BAR', 'BAZ']
        assert test_query.query == 'select $1 from $2 where baz=$3'

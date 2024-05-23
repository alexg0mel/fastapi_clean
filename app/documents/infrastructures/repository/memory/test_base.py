from .base import InMemoryProvider

data1 = {'key1': 'value1', 'key2': 'value2', 'key3': [1, 2, 3]}
data2 = 1, 2, 3, (4, 5)


class TestBase:
    def test(self):
        provider = InMemoryProvider()
        value = provider.get_value(name='value')
        assert value is None
        provider.store(data=1, value=data1)
        provider.store(data=2, value=data2)
        expected_data1 = provider.get_value(data=1)
        expected_data2 = provider.get_value(data=2)
        assert expected_data1 == data1
        assert expected_data2 == data2

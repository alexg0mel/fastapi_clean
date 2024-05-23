from typing import Any


class InMemoryProvider:
    """
    key-value store
    """
    def __init__(self):
        self._items = {}

    @staticmethod
    def _build_key_by_attribute(**attribute) -> str:
        assert len(attribute) == 1
        name, value = attribute.popitem()
        return f'{name}::{value}'

    def get_value(self, *_, default=None, **attribute) -> Any | None:
        key = self._build_key_by_attribute(**attribute)
        return self._items.get(key, default)

    def store(self, *_, value: Any, **attribute):
        key = self._build_key_by_attribute(**attribute)
        self._items.update({key: value})

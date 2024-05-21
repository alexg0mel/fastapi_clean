from .base import BaseModel


class TestBaseModel:
    def test_to_dict(self):
        model = BaseModel()
        model.param1 = 1
        model.param2 = "2"
        result = model.to_dict()
        assert 'param1' in result
        assert result['param1'] == 1
        assert 'param2' in result
        assert result['param2'] == '2'

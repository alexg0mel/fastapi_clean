
from pydantic import BaseModel
from pydantic.main import Model


class Base(BaseModel):

    def to_dict(self, **kwargs) -> dict:
        return self.model_dump(**kwargs)

    @classmethod
    def from_dict(cls: type[Model], data: dict) -> Model:
        return cls.model_validate(data, from_attributes=True)

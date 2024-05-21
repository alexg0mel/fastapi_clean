
from pydantic import BaseModel
from pydantic.main import Model


class Base(BaseModel):

    def to_dict(self, **kwargs) -> dict:
        return self.model_dump(**kwargs)

    @classmethod
    def from_kwargs(cls: type[Model], **kwargs) -> Model:
        return cls(**kwargs)

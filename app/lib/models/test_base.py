from .base import Base


class Base2(Base):
    a: int
    b: int = 0
    c: str = 'test'


class Base3(Base2):
    d: int


class TestBase:
    def test(self):
        base2 = Base2(a=4, c='c4')
        base3 = Base3.from_kwargs(**base2.to_dict(), d=5)
        assert base2.a == base3.a
        assert base2.b == base3.b
        assert base2.c == base3.c
        assert base3.d == 5

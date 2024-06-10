from enum import Enum


class Stage(str, Enum):
    TradezoneOrder = "TO"
    ProformaInvoice = "PI"
    Invoice = "IN"
    CanceledDocument = "CD"


class TypeUser(str, Enum):
    Buyer = "buyer"
    Seller = "seller"


class DocumentStatus(str, Enum):
    Draft = "draft"
    Active = "active"
    Forming = "forming"


class AlphaGroup(str, Enum):
    Empty = "-"
    Alpha = "α"
    Beta = "β"
    Gamma = "γ"
    Delta = "δ"
    Epsilon = "ε"
    Zeta = "ζ"
    Eta = "η"
    Theta = "θ"
    Iota = "ι"
    Kappa = "κ"

    @classmethod
    def as_name(cls, value: str) -> str:
        try:
            name = cls(value).name.lower()
            if name == 'empty':
                name = ''
        except ValueError:
            name = ''
        return name

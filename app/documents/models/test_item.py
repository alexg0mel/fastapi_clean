from .item import (select_type_of_item,
                   ItemPO, ItemSO, ItemPI, ItemSI, ItemPIn, ItemSIn, ItemCD, Item)
from .enums import Stage, TypeUser


ANY = 'any'


# stage, type of user, type of Item
select_type_of_item_test_cases = (
    (Stage.TradezoneOrder, TypeUser.Seller, ItemSO),
    (Stage.TradezoneOrder, TypeUser.Buyer, ItemPO),
    (Stage.ProformaInvoice, TypeUser.Seller, ItemSI),
    (Stage.ProformaInvoice, TypeUser.Buyer, ItemPI),
    (Stage.Invoice, TypeUser.Seller, ItemSIn),
    (Stage.Invoice, TypeUser.Buyer, ItemPIn),
    (Stage.CanceledDocument, TypeUser.Seller, ItemCD),
    (Stage.CanceledDocument, TypeUser.Buyer, ItemCD),
    (Stage.CanceledDocument, ANY, ItemCD),
    (Stage.TradezoneOrder, ANY, Item),
    (ANY, TypeUser.Seller, Item),
    (ANY, ANY, Item),

)


class TestItem:
    def test_select_type_of_item(self):
        for test_case in select_type_of_item_test_cases:
            assert select_type_of_item(test_case[0], test_case[1]) == test_case[2]

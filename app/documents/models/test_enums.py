from .enums import AlphaGroup


class TestEnums:
    def test_alpha_group(self):
        assert AlphaGroup.Empty == "-"
        assert AlphaGroup.Alpha == "α"
        assert AlphaGroup.Beta == "β"
        assert AlphaGroup.Kappa == "κ"

        assert AlphaGroup.as_name("α") == "alpha"
        assert AlphaGroup.as_name("-") == ""
        assert AlphaGroup.as_name("+") == ""

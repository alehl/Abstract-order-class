"""This file should have our order classes in it."""

class AbstractMelonOrder(object):
    """ Abstract class for shared attributes/methods from domestic and international melon orders """

    shipped = False

    def __init__(self, species, qty, order_type, tax):
        """Initialize melon order attributes"""
        self.species = species
        self.qty = qty
        self.order_type = None
        self.tax = float()

    def get_total(self):
        """Calculate price."""

        base_price = 5
        christmas_price = base_price * 1.5
        flat_fee_under10 = 3

        if self.order_type == "international" and self.qty < 10:
            if self.species == "christmas":
                total = ((1 + self.tax) * self.qty * christmas_price) + flat_fee_under10
            else:
                total = ((1 + self.tax) * self.qty * base_price) + flat_fee_under10
        elif self.species == "christmas":
            total = ((1 + self.tax) * self.qty * christmas_price)
        else:
            total = (1 + self.tax) * self.qty * base_price
        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True

class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""
    def __init__(self, species, qty):
        super(DomesticMelonOrder, self).__init__(species, qty, "domestic", 0.08)

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    def __init__(self, species, qty, country_code):
        super(InternationalMelonOrder, self).__init__(species, qty, "international", 0.17)
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""
        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):
    def __init__(self, species, qty):
        super(DomesticMelonOrder, self).__init__(species, qty, "domestic", 0)
        self.passes_inspection = False

    def inspect_melons()



class Shoe:
    def __init__(self, brand, model, size, price):
        self.brand = brand
        self.model = model
        self.size = size
        self.price = price

    def display(self):
        return f"{self.brand} {self.model} - Size: {self.size}, Price: ฿{self.price}"


class TennisShoe(Shoe):
    def __init__(self, brand, model, size, court, price):
        super().__init__(brand, model, size, price)
        self.court = court

    def display(self):
        return f"{self.brand} {self.model} - Size: {self.size}, Court: {self.court}, Price: ${self.price}"


if __name__ == "__main__":
    # Example usage
    shoe1 = Shoe("Adidas", "SAMBA OG SHOES", 4.5, 3800)
    print(shoe1.display())  # Output: Nike Air Max - Size: 10, Price: $120

    ADIFOM_shoe1 = TennisShoe("Adidas", "ADIFOM STAN SMITH MULE SHOES", 7, "Hard", 2500)
    print(ADIFOM_shoe1.display())  # Output: Adidas Barricade - Size: 9.5, Court: Hard, Price: $150

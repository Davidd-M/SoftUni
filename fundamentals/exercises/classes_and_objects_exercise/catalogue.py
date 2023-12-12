class Catalogue:
    def __init__(self, name: str):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        return [s for s in self.products if s.startswith(f"{first_letter}")]

    def __repr__(self):
        self.products = sorted(list(self.products))
        return (f"Items in the {self.name} catalogue:\n" +
                f"\n".join(self.products))


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Zirror")
catalogue.add_product("Xesk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)



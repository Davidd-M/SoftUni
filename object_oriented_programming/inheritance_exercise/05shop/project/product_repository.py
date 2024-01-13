from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product) -> None:
        self.products.append(product)

    def find(self, product_name: str):
        try:
            return next(filter(lambda x: x.name == product_name, self.products))
        except StopIteration:
            pass

    def remove(self, product_name):
        cur_product = next((x for x in self.products if getattr(x, 'name', None) == product_name), None)
        if cur_product:
            self.products = [p for p in self.products if p != cur_product]
        return cur_product

    def __repr__(self):
        formatted_list = [f"{v.name}: {v.quantity}" for v in self.products]
        return '\n'.join(formatted_list)






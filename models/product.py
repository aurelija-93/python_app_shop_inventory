class Product:
    def __init__(
            self,
            name,
            description,
            stock,
            purchase_price,
            selling_price,
            supplier,
            id = None
            ):
        self.name = name
        self.description = description
        self.stock = stock
        self.purchase_price = purchase_price
        self.selling_price = selling_price
        self.margin = round((self.selling_price-self.purchase_price)/self.purchase_price*100)
        self.supplier = supplier
        self.id = id
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def __repr__(self):
        return f"Product(name={self.name}, price={self.price}, stock={self.stock})"

class ShoppingCart:
    def __init__(self):
        self.items = []  # Lista de tuplas (producto, cantidad)
        self.total = 0

    def add_item(self, product, quantity):
        """Agrega un producto al carrito."""
        if product.stock >= quantity:  # Verifica que haya suficiente stock
            self.items.append((product, quantity))
            self.total += product.price * quantity
            product.stock -= quantity  # Actualiza el stock
            return True
        return False

    def complete_purchase(self):
        """Finaliza la compra."""
        if not self.items:
            return False  # No se puede completar una compra sin productos
        return True

    def __repr__(self):
        return f"ShoppingCart(total={self.total}, items={self.items})"

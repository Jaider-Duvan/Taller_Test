import pytest
from SistemasDeCompras import Product
from SistemasDeCompras import ShoppingCart  
def test_shopping_cart_system():
    # Creación de productos
    laptop = Product("Laptop", 1000, 5)
    smartphone = Product("Smartphone", 700, 10)
    charger = Product("Charger", 50, 20)

    # Inicialización del carrito de compras
    cart = ShoppingCart()

    # Añadir productos al carrito
    assert cart.add_item(laptop, 2) == True  # Se añaden 2 laptops
    assert cart.add_item(smartphone, 1) == True  # Se añade 1 smartphone
    assert cart.add_item(charger, 5) == True  # Se añaden 5 cargadores

    # Verificar total calculado
    assert cart.total == 2900  # (2 * 1000) + (1 * 700) + (5 * 50)

    # Verificar que el stock se haya actualizado correctamente
    assert laptop.stock == 3  # 5 - 2
    assert smartphone.stock == 9  # 10 - 1
    assert charger.stock == 15  # 20 - 5

    # Finalizar la compra
    assert cart.complete_purchase() == True

    # Prueba para compra sin productos
    empty_cart = ShoppingCart()
    assert empty_cart.complete_purchase() == False

def test_shopping_cart_insufficient_stock():
    # Crear producto con stock limitado
    headphones = Product("Headphones", 100, 2)

    # Inicialización del carrito
    cart = ShoppingCart()

    # Intentar agregar más productos de los disponibles
    assert cart.add_item(headphones, 3) == False  # Stock insuficiente
    assert cart.total == 0  # Total no debería cambiar
    assert headphones.stock == 2  # Stock permanece igual

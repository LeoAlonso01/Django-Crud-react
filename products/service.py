from .models import salesCart, cartItem, Sales

def complete_sale(cliente):
    # Obtener todos los ítems del carrito del cliente
    cart_items = salesCart.objects.filter(cliente=cliente)
    
    if not cart_items.exists():
        raise ValueError('No hay ítems en el carrito para completar la venta.')

    # Crear una nueva venta
    total = sum(item.quantity * item.id_product.price for item in cart_items)
    sale = Sales.objects.create(total=total, cliente=cliente)

    # Crear ítems de la venta
    for item in cart_items:
        cart_item = cartItem.objects.create(
            id_product=item.id_product,
            sales=sale,
            quantity=item.quantity
        )
    
    # Limpiar el carrito si es necesario
    cart_items.delete()
    
    return sale

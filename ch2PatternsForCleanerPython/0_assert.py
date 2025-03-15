def apply_discount(product, discount):
    price = int(product['price'] * (1.0 - discount))
    assert 0 <= price <= product['price'], 'Discount is more than 100%.'
    return price

shoes = {'name': 'Fancy Shoes', 'price': 14900}

print(apply_discount(shoes, 0.25))

print(apply_discount(shoes, 2.0))
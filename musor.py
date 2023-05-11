from pprint import pprint

products = []

new_product = {
    "product_id": 12,
    "quantity": 12,
    "price": 23.99,
    "total": 12 * 23.99,
}

new_product2 = {
    "product_id": 75,
    "quantity": 2,
    "price": 4.49,
    "total": 4 * 4.49,
}

products.append(new_product)
products.append(new_product2)

pprint(products)

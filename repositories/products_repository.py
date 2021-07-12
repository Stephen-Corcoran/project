from db.run_sql import run_sql

from models.manufacturers import Manufacturer
from models.products import Product

import repositories.manufacturers_repository as manufacturers_repository

def save(product):
    sql = "INSERT INTO products (name, description, quantity, buy_price, sell_price) VALUES (%s, %s, %s, %s, %s) RETURNING"
    values = [product.name, product.description, product.quantity, product.buy_price, product.sell_price]
    results = run_sql(sql, values)
    id = results[0] ['id']
    product.id = id
    return product
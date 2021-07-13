from db.run_sql import run_sql
from models import products
from models import manufacturers

from models.manufacturers import Manufacturer
from models.products import Product

import repositories.manufacturers_repository as manufacturers_repository

def save(product):
    sql = "INSERT INTO products (name, description, quantity, buy_price, sell_price) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [product.name, product.description, product.quantity, product.buy_price, product.sell_price]
    results = run_sql(sql, values)
    id = results[0]['id']
    product.id = id
    return product

def select_all():
    products = []
    sql = "SELECT * FROM prodcuts"
    results = run_sql (sql)
    for row in results:
        product = Product(row ['name'], row ['id'])
        products.append(product)
    return products

def select(id):
    product = None
    sql = "SELECT * FROM products WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        product = Product(result['name'])
    return product

def delete_all():
    sql = "DELETE FROM products"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM products WHERE id=%s"
    values =[id]
    run_sql(sql, values)

def update(product):
    sql = "UPDATE products SET (name, description, quantity, buy_price, sell_price) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [product.name, product.description, product.quantity, product.buy_price, product.sell_price, ]
    print(values)
    run_sql(sql, values)

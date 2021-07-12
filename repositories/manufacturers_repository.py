from db.run_sql import run_sql

from models.manufacturers import Manufacturer
from models.products import Product

import repositories.products_repository as products_repository

def save(manufacturer):
    sql = "INSERT INTO manufacturers (name) VALUES (%s) RETURNING"
    values = [manufacturer.name]
    results = run_sql(sql, values)
    id = results[0] ['id']
    manufacturer.id = id
    return manufacturer
from db.run_sql import run_sql

from models.manufacturers import Manufacturer
from models.products import Product

import repositories.products_repository as products_repository

def save(manufacturer):
    sql = "INSERT INTO manufacturers (name) VALUES (%s) RETURNING *"
    values = [manufacturer.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    manufacturer.id = id
    return manufacturer

def delete_all():
    sql = "DELETE FROM manufacturers"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM manufacturers WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(manufacturer):
    sql = "UPDATE manufacturers SET (name) = (%s) WHERE id = %s"
    values = [manufacturer.name, manufacturer.id]
    run_sql(sql, values)
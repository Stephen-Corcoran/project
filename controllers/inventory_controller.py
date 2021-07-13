from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.manufacturers import Manufacturer
from models.products import Product

import repositories.manufacturers_repository as manufacturers_repository
import repositories.products_repository as products_repositories

manufacturers_blueprint = Blueprint("manufacturers", __name__)
products_blueprint = Blueprint("products", __name__)

@manufacturers_blueprint.route("/manufacturers")
def manufacturers():
    manufacturers = manufacturers_repository.select_all()
    return render_template("manufacturers/index.html", all_manufacturers = manufacturers)

@manufacturers_blueprint.route("/manufacturers/new")
def new_manufacturer():
    manufacturers = manufacturers_repository.select_all()
    return render_template("manufacturers/new.html", all_manufacturers = manufacturers)

@manufacturers_blueprint.route("/manufacturers", methods=['POST'])
def create_manufacturer():
    name = request.form ["name"]
    return redirect('/manufacturers')

@manufacturers_blueprint.route("/manufacturers/<id>", methods=['GET'])
def show_manufacturers(id):
    manufacturer = manufacturers_repository.select(id)
    return render_template("manufacturers/show.html", manufacturer = manufacturer)

@manufacturers_blueprint.route("/manufacturers/<id>", methods=['POST'])
def update_manufacturers(id):
    name = request.form['name']
    print(manufacturers.name)
    manufacturers_repository.update(manufacturers)
    return redirect('/manufacturers')

@manufacturers_blueprint.route("/manufacturers/<id>/delete", methods=["POST"])
def delete_manufacturers():
    manufacturers_repository.delete(id)
    return redirect('/manufacturers')


@products_blueprint.route("/products")
def products():
    products = products_repositories.select_all()
    return render_template("products/index.html", all_products = products)

@products_blueprint.route("/products/new")
def new_manufacturer():
    products = products_repositories.select_all()
    return render_template("products/new.html", all_products = products)

@products_blueprint.route("/products", methods=['POST'])
def create_manufacturer():
    name = request.form ["name"]
    return redirect('/products')

@products_blueprint.route("/products/<id>", methods=['GET'])
def show_products(id):
    manufacturer = products_repositories.select(id)
    return render_template("products/show.html", manufacturer = manufacturer)

@products_blueprint.route("/products/<id>", methods=['POST'])
def update_products(id):
    name = request.form['name']
    print(products.name)
    products_repositories.update(products)
    return redirect('/products')

@products_blueprint.route("/products/<id>/delete", methods=["POST"])
def delete_products():
    products_repositories.delete(id)
    return redirect('/products')



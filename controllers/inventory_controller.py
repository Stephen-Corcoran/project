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
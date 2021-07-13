from flask import Flask, render_template, request, redirect, Blueprint

from models.manufacturers import Manufacturer
from models.products import Product

import repositories.manufacturers_repository as manufacturers_repository
import repositories.products_repository as products_repositories


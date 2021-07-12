from flask import Flask, render_template, request, redirect, Blueprint

from models.manufacturers import manufacturers
from models.products import products

import repositories.manufacturers_repository as manufacturers_repository
import repositories.products_repositories as products_repositories
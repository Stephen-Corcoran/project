from flask import Flask, render_template, request, redirect, Blueprint

from models.manufacturers import manufacturer
from models.products import product

import repositories.manufacturers_repository as manufacturers_repository
import repositories.products_repositories as products_repositories
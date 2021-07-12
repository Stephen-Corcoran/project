import pdb

from models.manufacturers import Manufacturer, Manufacturers
from models.products import Product

import repositories.manufacturers_repository as manufacturers_repository 
import repositories.products_repositories as products_repositories

manufacturers_repository.delete_all()
products_repositories.delete_all()

manufacturer1 = Manufacturer ("we make stuff 1")
manufacturers_repository.save(manufacturer1)
manufacturer2 = Manufacturer ("we make stuff 2")
manufacturers_repository.save(manufacturer2)

product1 = Product ("name of product 1", "description of product 1", 100, 10, 15, manufacturer1)
products_repositories.save(product1)
product2 = Product ("name of product 2", "description of product 2", 200, 20, 40, manufacturer2)
products_repositories.save(product1)


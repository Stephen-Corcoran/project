import pdb

from models.manufacturers import Manufacturers
from models.products import Products

import repositories.manufacturers_repository as manufacturers_repository 
import repositories.products_repositories as products_repositories

manufacturers_repository.delete_all()
products_repositories.delete_all()
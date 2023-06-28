import pdb
from models.supplier import Supplier
from models.product import Product
import repositories.supplier_repository as supplier_repository
import repositories.product_repository as product_repository

product_repository.delete_all()
supplier_repository.delete_all()

supplier1 = Supplier("Madam Malkin's", "0200 1111", "muggles@malkins.co.uk")
supplier_repository.save(supplier1)

supplier2 = Supplier("Quality Quidditch Supplies", "0200 2222", "muggles@qqs.co.uk")
supplier_repository.save(supplier2)

supplier3 = Supplier("Scribbulus", "0200 3333", "muggles@scribbulus.co.uk")
supplier_repository.save(supplier3)

supplier4 = Supplier("Weasleys' Wizard Wheezes", "0200 4444", "muggles@weasleys.co.uk")
supplier_repository.save(supplier4)

product1 = Product(
    "Gryffindor Robes",
    "Changes size according to the wearer. Includes self-repairing seams.",
    4, 300, 600, supplier1
    )

product2 = Product(
    "Ravenclaw Robes",
    "Changes size according to the wearer. Includes self-repairing seams.",
    6, 300, 600, supplier1
    )

product3 = Product(
    "Hufflepuff Robes",
    "Changes size according to the wearer. Includes self-repairing seams.",
    10, 300, 600, supplier1
    )

product4 = Product(
    "Slytherin Robes",
    "Changes size according to the wearer. Includes self-repairing seams.",
    2, 300, 600, supplier1
    )
product5 = Product(
    "Nimbus 2000",
    "Produced by the Nimbus Racing Broom Company.",
    7, 2000, 2500, supplier2
    )
product6 = Product(
    "Broomstick Servicing Kit",
    "Includes a Handbook of Do-It-Yourself Broomcare.",
    15, 50, 75, supplier2
    )
product7 = Product(
    "Quidditch Gloves",
    "One size fits all. Provides extra grip in adverse weather conditions.",
    30, 30, 50, supplier2
    )
product8 = Product(
    "Golden Snitch",
    "Real goblin gold. Working Flesh Memory.",
    0, 100, 200, supplier2
    )
product9 = Product(
    "Plain Parchment",
    "Ten rolls of high-quality all-purpose parchment.",
    9, 20, 30, supplier3
    )
product10 = Product(
    "Colour-Change Ink",
    "Once used, the charm lasts for one month.",
    5, 15, 25, supplier3
    )
product11 = Product(
    "Set of Quills",
    "Five quills for all occasions. Charm-free.",
    6, 10, 15, supplier3
    )
product12 = Product(
    "Extendable Ears",
    "Original invention by Fred and George Weasley.",
    1, 20, 50, supplier4
    )
product13 = Product(
    "Peruvian Instant Darkness Powder",
    "Resistant to most muggle light sources.",
    12, 50, 150, supplier4
    )
product14 = Product(
    "Skiving Snackbox",
    "Original invention by Fred and George Weasley.",
    8, 40, 100, supplier4
    )
product15 = Product(
    "Spell-Checking Quill",
    "Spell-correcting charm reliable for three months.",
    4, 10, 25, supplier4
    )

products = [
    product1,
    product2,
    product3,
    product4,
    product5,
    product6,
    product7,
    product8,
    product9,
    product10,
    product11,
    product12,
    product13,
    product14,
    product15
    ]

for product in products:
    product_repository.save(product)

pdb.set_trace()
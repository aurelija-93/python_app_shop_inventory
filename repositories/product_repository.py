from db.run_sql import run_sql
from models.product import Product
import repositories.supplier_repository as supplier_repository

def save(product):
    sql = "INSERT INTO products (name, description, stock, purchase_price, selling_price, supplier_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id"
    values = [product.name, product.description, product.stock, product.purchase_price, product.selling_price, product.supplier.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    product.id = id

def select_all():
    products = []
    sql = "SELECT * FROM products"
    results = run_sql(sql)
    for row in results:
        supplier = supplier_repository.select(row['supplier_id'])
        product = Product(row['name'], row['description'], row['stock'], row['purchase_price'], row['selling_price'], supplier, row['id'])
        products.append(product)
    return products

def select(id):
    product = None
    sql = "SELECT * FROM products WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        supplier = supplier_repository.select(result['supplier_id'])
        product = Product(result['name'], result['description'], result['stock'], result['purchase_price'], result['selling_price'], supplier, result['id'])
    return product

def update(product):
    sql = "UPDATE products SET (name, description, stock, purchase_price, selling_price, supplier_id) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [product.name, product.description, product.stock, product.purchase_price, product.selling_price, product.supplier.id, product.id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM products"
    run_sql(sql)

def delete(id):
    sql = 'DELETE FROM products WHERE id = %s'
    values = [id]
    run_sql(sql, values)
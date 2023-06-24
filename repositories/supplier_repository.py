from db.run_sql import run_sql
from models.supplier import Supplier

def save(supplier):
    sql = "INSERT INTO suppliers (name, phone, email) VALUES (%s, %s, %s) RETURNING id"
    values = [supplier.name, supplier.phone, supplier.email]
    result = run_sql(sql, values)
    supplier.id = result[0]['id']
    return supplier

def select_all():
    suppliers = []
    sql = "SELECT * FROM suppliers"
    results = run_sql(sql)
    for row in results:
        supplier = Supplier(row['name'], row['phone'], row['email'], row['id'])
        suppliers.append(supplier)
    return suppliers

def select(id):
    supplier = None
    sql = "SELECT * FROM suppliers where id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        supplier = Supplier[result['name'], result['phone'], result['email'], result['id']]
    return supplier

def update(supplier):
    sql = "UPDATE suppliers SET (name, phone, email) = (%s, %s, %s) WHERE id = %s"
    values = [supplier.name, supplier.phone, supplier.email, supplier.id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM suppliers"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM suppliers WHERE id = %s"
    values = [id]
    run_sql(sql, values)
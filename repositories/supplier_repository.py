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
    pass

def update(supplier):
    pass

def delete_all():
    pass

def delete(id):
    pass
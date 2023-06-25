from flask import Flask, Blueprint, render_template, request, redirect
from models.product import Product
from repositories import product_repository
from repositories import supplier_repository

products_blueprint = Blueprint('products', __name__)

@products_blueprint.route('/products')
def index():
    products = product_repository.select_all()
    return render_template('/products/index.html', products=products)

@products_blueprint.route('/products/<id>')
def show(id):
    product = product_repository.select(id)
    return render_template('/products/show.html', product=product)

@products_blueprint.route('/products/new')
def new():
    suppliers = supplier_repository.select_all()
    return render_template('/products/new.html', suppliers=suppliers)

@products_blueprint.route('/products', methods=['POST'])
def create():
    name = request.form['name']
    description = request.form['description']
    stock = request.form['stock']
    purchase_price = request.form['purchase_price']
    selling_price = request.form['selling_price']
    supplier_id = request.form['supplier_id']
    supplier = supplier_repository.select(supplier_id)
    product = Product(name, description, stock, purchase_price, selling_price, supplier)
    product_repository.save(product)
    return redirect('/products')

@products_blueprint.route('/products/<id>/edit')
def edit():
    return render_template('/products/edit.html')

@products_blueprint.route('/products/<id>', methods=['POST'])
def update(id):
    name = request.form['name']
    description = request.form['description']
    stock = request.form['stock']
    purchase_price = request.form['purchase']
    selling_price = request.form['selling']
    supplier_id = request.form['supplier_id']
    supplier = supplier_repository.select(supplier_id)
    product = Product(name, description, stock, purchase_price, selling_price, supplier)
    product_repository.update(product)
    return redirect(f"/products/{id}")

@products_blueprint.route('/products/<id>/delete')
def delete(id):
    product_repository.delete(id)
    return redirect('/products')
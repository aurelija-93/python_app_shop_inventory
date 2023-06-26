from flask import Flask, Blueprint, render_template, redirect, request
from models.supplier import Supplier
from repositories import supplier_repository
from repositories import product_repository

suppliers_blueprint = Blueprint('suppliers', __name__)

@suppliers_blueprint.route('/suppliers')
def index():
    suppliers = supplier_repository.select_all()
    return render_template('/suppliers/index.html', suppliers=suppliers)

@suppliers_blueprint.route('/suppliers/<id>')
def show(id):
    supplier = supplier_repository.select(id)
    products = product_repository.products_for_supplier(id)
    return render_template('/suppliers/show.html', supplier=supplier, products=products)

@suppliers_blueprint.route('/suppliers/new')
def new():
    return render_template('/suppliers/new.html')

@suppliers_blueprint.route('/suppliers', methods=['POST'])
def create():
    name = request.form['name']
    phone = request.form['phone']
    email = request.form['email']
    supplier = Supplier(name, phone, email)
    supplier_repository.save(supplier)
    return redirect('/suppliers')

@suppliers_blueprint.route('/suppliers/<id>/edit')
def edit(id):
    supplier = supplier_repository.select(id)
    return render_template('suppliers/edit.html', supplier=supplier)

@suppliers_blueprint.route('/suppliers/<id>', methods=['POST'])
def update(id):
    name = request.form['name']
    phone = request.form['phone']
    email = request.form['email']
    supplier = Supplier(name, phone, email, id)
    supplier_repository.update(supplier)
    return redirect('/suppliers')

# @suppliers_blueprint.route('/suppliers/<id>/delete', methods=['POST'])
# def delete(id):
#     supplier_repository.delete(id)
#     return redirect('/suppliers')
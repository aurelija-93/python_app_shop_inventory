from flask import Flask, Blueprint, render_template, redirect, request
from models.supplier import Supplier
from repositories import supplier_repository

suppliers_blueprint = Blueprint('suppliers', __name__)

@suppliers_blueprint.route('/suppliers')
def index():
    suppliers = supplier_repository.select_all()
    return render_template('/suppliers/index.html', suppliers=suppliers)

@suppliers_blueprint.route('/suppliers/new')
def new():
    return render_template('/suppliers/form.html')

@suppliers_blueprint.route('/suppliers', methods=['POST'])
def create():
    name = request.form['name']
    phone = request.form['phone']
    email = request.form['email']
    supplier = Supplier(name, phone, email)
    supplier_repository.save(supplier)
    return redirect('/suppliers')

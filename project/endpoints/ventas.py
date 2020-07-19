from flask import request, jsonify, Blueprint
from project import db
from project.models import Productos
from project.schemas import productos_schema

blueprint = Blueprint('Productos', __name__)


@blueprint.route('/NewProduct', methods=['GET'])
def list():
    producto = Productos.query.filter_by(id_producto=1).all()

    return jsonify(productos_schema.dump(producto, many=True)), 200


@blueprint.route('/NewProduct', methods=['POST'])
def create():
    producto = productos_schema.load(request.json)

    db.session.add(producto)
    db.session.commit()

    return productos_schema.dump(producto), 201


@blueprint.route('/Change/<id_producto>', methods=['PATCH'])
def change(id_producto):
    producto = Productos.query.filter_by(id_producto=id_producto).first()
    datos = request.get_json()

    producto.id_producto = datos['id_producto']
    producto.nombre_producto = producto.nombre_producto
    producto.precio = producto.precio

    db.session.add(producto)
    db.session.commit()

    return {'id_producto': producto.id_producto, 'nombre_producto': producto.nombre_producto,
            'precio': producto.precio}, 201


@blueprint.route('/Change', methods=['GET'])
def show():
    producto = Productos.query.all()

    return jsonify(productos_schema.dump(producto, many=True)), 201

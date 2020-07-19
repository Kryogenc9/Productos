from project import db


class Productos(db.Model):
    id_producto = db.Column(db.Integer, primary_key=True, nullable=False)
    nombre_producto = db.Column(db.Text, nullable=False)
    precio = db.Column(db.Integer, nullable=False)

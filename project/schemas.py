from project import ma
from project.models import Productos


class ProductosSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Productos
        load_instance = True


productos_schema = ProductosSchema()

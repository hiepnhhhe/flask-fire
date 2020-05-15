from flask import Blueprint, jsonify, make_response

from ..extensions import db
from .models import PeriodicElement
from .serializers import ElementShema

blueprint = Blueprint('elemental', __name__)

@blueprint.route("/elements")
def getAllElement():
    try:
        elems = PeriodicElement.query.all()
        items = [
            {
                "position": item.position,
                "name": item.name,
                "weight": item.weight,
                "symbol": item.symbol,
                "image": item.image
            } for item in elems
        ]
        return jsonify(items)
    except Exception as e:
        return make_response(e, 500)
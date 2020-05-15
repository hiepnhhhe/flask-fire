from flask import Blueprint, request
from ..extensions import api

from .models import Account
from .serializers import user_schema
from .resources import UserLogin, UserLogoutAccess, UserLogoutRefresh, UserRegistration, TokenRefresh, AllUsers, SecretResource

blueprint = Blueprint('user', __name__)

api.add_resource(UserRegistration, 'registration')
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogoutAccess, '/logout/access')
api.add_resource(UserLogoutRefresh, '/logout/refresh')
api.add_resource(TokenRefresh, '/token/refresh')
api.add_resource(AllUsers, '/users')
api.add_resource(SecretResource, '/secret')

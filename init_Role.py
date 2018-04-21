from app.models import Role
from run import app

with app.app_context():
    Role.insert_roles()
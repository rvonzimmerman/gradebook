from .models import Role
from sqlalchemy.exc import IntegrityError

def create_user_roles(app, db):
    roles = [
        Role(name="teacher", description="K-5 Teacher"),
        Role(name="administrator", description="All access privileges"),
        Role(name="specialist", description="Access to Specialist reports")]

    with app.app_context():
        for role in roles:
            try:
                db.session.add(role)
                db.session.commit()
            except IntegrityError:
                db.session.rollback()

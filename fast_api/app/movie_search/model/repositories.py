from sqlalchemy.orm import Session
from .models import User
class MovieRepository:
    def __init__(self,db: Session):
        self.session = db

    def create_user(self,data):
        existing_user = self.session.query(User).filter(User.email == data.get("email")).first()
        if existing_user:
            return None
        new_user = User(**data)
        self.session.add(new_user)
        self.session.commit()
        self.session.refresh(new_user)
        return new_user

    def match_email_password(self,data):
        return self.session.query(User).filter(User.email == data.get("email"),
                                               User.password==data.get("password")).first()

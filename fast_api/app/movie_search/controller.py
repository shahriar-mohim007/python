from .schema import RegisterRequest,RegisterResponse,LoginRequest
from sqlalchemy.orm import Session
from .model.repositories import MovieRepository
from .token import encode


class UserController:
    def __init__(self):
        self.repository = None

    def create_user(self,dto: RegisterRequest,db: Session):
        self.repository = MovieRepository(db)
        user_data = self.repository.create_user(dto.model_dump())
        if not user_data:
            return {
                'error': 'User with this email already exists'
            }
        return RegisterResponse(**
            {
                "id": user_data.id,
                "fullname": user_data.fullname,
                "email": user_data.email,
            }
        )


class LoginController:
    def __init__(self):
        self.repository = None

    def create_token(self,dto: LoginRequest,db: Session):
        self.repository = MovieRepository(db)
        user_data = self.repository.match_email_password(dto.model_dump())
        if not user_data:
            return {"message": "User Not Found"}

        token = encode({
            "id": user_data.id,
            "fullname": user_data.fullname,
            "email": user_data.email,
        })

        return {"access_token": token}


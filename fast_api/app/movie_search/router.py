import logging
logger =logging.getLogger(__name__)

from fastapi import FastAPI, Request, Depends, APIRouter
from .schema import RegisterRequest,LoginRequest
from .controller import UserController,LoginController
from sqlalchemy.orm import Session
from core.database.session import get_db
from .token import auth_required
move_router = APIRouter()
app = FastAPI()

@move_router.post('/register')
def register(request:Request,dto: RegisterRequest,db: Session = Depends(get_db)):
    lang = request.headers.get('Accept-Language')
    logger.info(lang)
    data = UserController().create_user(dto, db)
    return data

@move_router.post('/login')
def login(request:Request,dto: LoginRequest,db: Session = Depends(get_db)):
    lang = request.headers.get('Accept-Language')
    logger.info(lang)
    data = LoginController().create_token(dto, db)
    return data

@auth_required
@move_router.get('/search')
def search(request:Request,db: Session = Depends(get_db)):
    pass

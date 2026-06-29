from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from backend.schemas.auth_schema import TokenSchema, LoginResponseSchema
from backend.schemas.user_schema import CreateUserSchema, UserSchema, LoginSchema
from backend.models.users import User
from backend.utils.security import get_password_hash, verify_password, create_access_token
from backend.utils.dependencies import get_db

router = APIRouter()

@router.post("/register", response_model=UserSchema)
def register(user: CreateUserSchema, db: Session = Depends(get_db)):
    existing = db.query(User).filter((User.username == user.username) | (User.email == user.email)).first()
    if existing:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username or email already registered")
    hashed_password = get_password_hash(user.password)
    db_user = User(username=user.username, email=user.email, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.post("/login", response_model=LoginResponseSchema)
def login(form: LoginSchema, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == form.username).first()
    if not user or not verify_password(form.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    access_token = create_access_token(data={"sub": str(user.id)})
    token = TokenSchema(access_token=access_token)
    return LoginResponseSchema(token=token, user=user)

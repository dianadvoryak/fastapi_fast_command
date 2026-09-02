from fastapi import APIRouter, Depends, HTTPException, Response
from authx import AuthX, AuthXConfig
from pydantic import BaseModel

auth_login = APIRouter(prefix="/login", tags=["login"])

config = AuthXConfig()
config.JWT_SECRET_KEY = "SECRET_KEY"
config.JWT_ACCESS_COOKIE_NAME = "my_access_token"
config.JWT_TOKEN_LOCATION = ["cookies"]

security = AuthX(config=config)

class UserLoginSchema(BaseModel):
    username: str
    password: str

@auth_login.post("/login")
def login(creds: UserLoginSchema, response: Response):
    if creds.username == 'test' and creds.password == 'test':
        token = security.create_access_token(uid = '12345')
        response.set_cookie(config.JWT_ACCESS_COOKIE_NAME, token)
        return {'access_token': token}
    raise HTTPException(status_code=401, detail="Incorrect username or password")


@auth_login.get("/protected", dependencies=[Depends(security.access_token_required)])
def protected():
    return {'data': 'TOP SECRET'}

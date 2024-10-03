from typing import Annotated

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
import jwt
from jwt.exceptions import InvalidTokenError

from app.utils.handler_exceptions import raise_http_exception
from config.config import ALGORITHM, SECRET_KEY

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth")


class AuthController():
    def __init__(self, auth_service, user_service):
        self.auth_service = auth_service
        self.user_service = user_service

    @raise_http_exception
    async def login(self, credentials):
        result = await self.auth_service.login(
            self.user_service, credentials.username, credentials.password
        )
        error = "Invalid Credentials" if not result else None
        return {"error": error, "response": result, "status_code": 401 if not result else 200}

    @raise_http_exception
    async def get_logged_user(self, access_token: Annotated[str, Depends(oauth2_scheme)]):
        credentials_exception = {"error": "Could not validate credentials", "status_code": 401}
        try:
            token_data = jwt.decode(access_token, SECRET_KEY, algorithms=[ALGORITHM])
        except InvalidTokenError:
            return credentials_exception
        user = await self.user_service.get_by_email(token_data.get("sub"))
        if user is None:
            return credentials_exception
        return {"error": None, "response": user.__dict__, "status_code": 200}

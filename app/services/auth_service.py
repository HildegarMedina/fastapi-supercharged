from datetime import datetime, timedelta, timezone

import jwt

from config.config import ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITHM, SECRET_KEY


class AuthService():
    def __init__(self, repo):
        self.repo = repo

    async def login(self, user_svc, email, password):
        user = await user_svc.get_by_email(email)
        if user and user.check_password(password):
            access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
            iat = datetime.now(timezone.utc)
            expire = iat + access_token_expires
            return {
                "access_token": self.create_access_token(user, iat, expire),
                "token_type": "bearer"
            }
        return False

    def create_access_token(self, user: dict, iat: datetime, expire: datetime):
        """Create access token."""
        to_encode = {
            "sub": user.email,
            "iat": iat,
            "exp": expire
        }
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

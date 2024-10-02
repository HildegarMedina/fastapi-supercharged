from datetime import datetime, timezone

import bcrypt
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base, declared_attr

Base = declarative_base()


class TimestampMixin:
    created_at = Column(DateTime, default=datetime.now(tz=timezone.utc))

    @declared_attr
    def created_by(cls):
        return Column(Integer, ForeignKey("users.id"), nullable=True)

    modified_at = Column(DateTime, default=datetime.now(tz=timezone.utc))

    @declared_attr
    def modified_by(cls):
        return Column(Integer, ForeignKey("users.id"), nullable=True)


class User(TimestampMixin, Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    _password = Column("password", String, nullable=False)
    last_login = Column(DateTime)

    @property
    def password(self):
        raise AttributeError("Password is not a readable attribute.")

    @password.setter
    def password(self, plain_password):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(plain_password.encode('utf-8'), salt)
        self._password = hashed_password.decode('utf-8')

    def verify_password(self, plain_password):
        return bcrypt.checkpw(plain_password.encode('utf-8'), self._password.encode('utf-8'))

from sqlalchemy.exc import IntegrityError

from app.utils.handler_exceptions import raise_http_exception


class UserController:
    def __init__(self, user_svc):
        """Initialize User Controller."""
        self.user_svc = user_svc

    @raise_http_exception
    async def get_user(self, user_id):
        result = await self.user_svc.get(user_id)
        message = "User not found." if not result else None
        return {"error": message, "response": result, "status_code": 404 if not result else 200}

    @raise_http_exception
    async def get_list_users(self):
        result = await self.user_svc.get_list()
        return {"error": False, "response": result}

    @raise_http_exception
    async def create_user(self, data):
        try:
            result = await self.user_svc.create(data)
            return {"error": False, "response": result}
        except IntegrityError:
            return {"error": "Email already exists.", "status_code": 400}

    @raise_http_exception
    async def update_user(self, user_id, data):
        try:
            await self.user_svc.update(user_id, data)
            return {"error": False, "response": None}
        except IntegrityError:
            return {"error": "Email already exists.", "status_code": 400}

    @raise_http_exception
    async def delete_user(self, user_id):
        result = await self.user_svc.get(user_id)
        if result:
            await self.user_svc.delete(result)
            return {"error": False, "response": None}
        return {"error": "User not found.", "response": None, "status_code": 404}

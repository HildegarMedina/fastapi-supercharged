from sqlalchemy import select

from app.domain.models import User


class UserService:
    def __init__(self, repo):
        """User Service."""
        self.repo = repo

    async def get(self, user_id):
        return await self.repo.get(User, user_id)

    async def get_list(self):
        result = await self.repo.execute(select(User))
        return result.scalars().all()

    async def create(self, data):
        data = User(**data.dict())
        self.repo.add(data)
        return await self.repo.save(data)

    async def update(self, user_id, data):
        object = await self.repo.get(User, user_id)
        object.first_name = data.first_name
        object.last_name = data.last_name
        object.email = data.email
        if data.password:
            object.password = data.password
        return await self.repo.save(object)

    async def delete(self, user):
        await self.repo.delete(user)
        await self.repo.commit()

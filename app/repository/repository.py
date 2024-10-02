from sqlalchemy.ext.asyncio import AsyncSession


class Repository(AsyncSession):

    def __init__(self, *args, **kwargs):
        """Initialize Repository."""
        super().__init__(*args, **kwargs)

    async def save(self, object):
        try:
            await self.commit()
            await self.refresh(object)
            return object
        except Exception:
            await self.rollback()
            raise

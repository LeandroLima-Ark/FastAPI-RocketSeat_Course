from sqlalchemy import insert, select
from src.models.entities.users import Users
from src.models.settings.database_connection_handler import DBConnectionHandler

# pylint:disable = W0212
class UsersRepository:
    async def insert_user(self, user_infos: dict) -> None:
        async with DBConnectionHandler() as db:
            query = insert(Users).values(**user_infos)
            await db.session.execute(query)
            await db.session.commit()

    async def get_users_by_name(self, name: str) -> list[dict]:
        async with DBConnectionHandler() as db:
            query =(
                select(Users)
                .where(Users.c.nome == name)
            )
            result = await db.session.execute(query)
            rows = result.fetchall()

            users_list = [dict(row._mapping) for row in rows]
            return users_list
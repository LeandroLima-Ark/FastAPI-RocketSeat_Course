import pytest
from src.models.repositories.users_repository import UsersRepository

@pytest.mark.asyncio
#@pytest.mark.skip(reason="already done")
async def test_insert_user():
    new_user = {
        "nome": "Salazar",
        "idade": 67,
    }

    repo = UsersRepository()
    await repo.insert_user(new_user)

@pytest.mark.asyncio
#@pytest.mark.skip(reason="already done")
async def test_get_user_by_name():
    repo = UsersRepository()
    response = await repo.get_users_by_name("Salazar")
    print(response)
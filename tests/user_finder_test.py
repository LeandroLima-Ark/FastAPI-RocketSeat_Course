import pytest
from src.controllers.user_finder import UserFinder

class UserRepositoryMock:
    def __init__(self):
        self.get_users_by_name_att = {}

    async def get_users_by_name(self, name: str) -> list[dict]:
        self.get_users_by_name_att["nome"] = name
        return [{"nome": "Raul"}, {"nome": "Amauri"}]

@pytest.mark.asyncio
async def test_find_user_by_name():
    user_repo = UserRepositoryMock()
    user_finder = UserFinder(user_repo)
    name = "Batista"

    response = await user_finder.find_user_by_name(name)

    assert user_repo.get_users_by_name_att["nome"] == name

    assert response["type"] == "USERS"
    assert response["count"] == 2
    assert "atributtes" in response
    assert isinstance(response["atributtes"], list)
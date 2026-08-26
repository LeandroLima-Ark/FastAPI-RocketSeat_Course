import pytest
from src.controllers.user_register import UserRegister

class UserRepositoryMock:
    def __init__(self):
        self.insert_users_att = {}

    async def insert_user(self, user_data: dict):
        self.insert_users_att["user_data"] = user_data

@pytest.mark.asyncio
@pytest.mark.skip()
async def test_register_user():
    user_repository =  UserRepositoryMock()
    user_register = UserRegister(user_repository)

    user_data = {
        "nome": "Leandro",
        "idade": 67
    }

    response = await user_register.register_user(user_data)
    print(response)

    assert response["type"] == "USERS"
    assert response["count"] == 1
    assert response["attributes"] == user_data

@pytest.mark.asyncio
async def test_register_user_error_name():
    user_repository = UserRepositoryMock()
    user_register = UserRegister(user_repository)

    invalid_user_data = {
        "nome": "Pedro",
        "idade": 100,
    }

    with pytest.raises(Exception) as excinfo:
        await user_register.register_user(invalid_user_data)

    assert str(excinfo.value) == "Nome não encontrado"
    assert user_repository.insert_users_att == {}

@pytest.mark.asyncio
async def test_register_user_error_age():
    user_repository = UserRepositoryMock()
    user_register = UserRegister(user_repository)

    invalid_user_data = {
        "nome": "Leandro",
        "idade": 300,
    }

    with pytest.raises(Exception) as excinfo:
        await user_register.register_user(invalid_user_data)

    assert str(excinfo.value) == "Idade invalida para cadastro"
    assert user_repository.insert_users_att == {}

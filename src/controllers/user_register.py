from src.models.repositories.interfaces.users_repository import UsersRepositoryInterface
from .interfaces.user_register import UserRegisterInterface

class UserRegister(UserRegisterInterface):
    def __init__(self, users_repository: UsersRepositoryInterface) -> None:
        self.users_repository = users_repository

    async def register_user(self, user_data: dict) -> dict:
        self.__validate_user_data(user_data)
        await self.__registry_user(user_data)
        return self.__form_response(user_data)

    def __validate_user_data(self, user_data: dict) -> None:
        age = user_data["idade"]
        name = user_data["nome"]

        if name not in ["Leandro", "Raul", "Amauri", "Yago", "Carlos"]:
            raise Exception("Nome não encontrado")

        if age < 0 or age > 200:
            raise Exception("Idade invalida para cadastro")

    async def __registry_user(self, user_data: dict) -> None:
        await self.users_repository.insert_user(user_data)

    def __form_response(self, user_data: dict) -> dict:
        return{
            "type": "USERS",
            "count": 1,
            "attributes": user_data
        }
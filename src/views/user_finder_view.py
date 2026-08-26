from src.controllers.interfaces.user_finder import UserFinderInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse

class UserFinderView:
    def __init__(self, controller: UserFinderInterface) -> None:
        self.__controller = controller

    async def handle_find_user_by_name(self, http_request: HttpRequest) -> HttpResponse:
        user_data = http_request.body
        response = await self.__controller.find_user_by_name(user_data)
        return HttpResponse(body=response, status_code=200)
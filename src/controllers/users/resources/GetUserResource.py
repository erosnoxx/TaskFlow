from flask import Response, current_app
from flask_restx import Resource
from src.controllers.users import namespace
from src.application.useCases.user.GetUserUseCase import GetUserUseCase
from src.controllers.schemas.common.ErrorSchemas import ErrorSchemas
from src.controllers.schemas.users.UserSchemas import UserSchemas
from src.domain.dto.user.input.GetUserInputDto import GetUserInputDto
from src.domain.dto.user.output.GetUserOutputDto import GetUserOutputDto


class GetUserResource(Resource):
    @namespace.doc("Busca um usuário por username.")
    @namespace.response(200, 'Ok', UserSchemas.get_user_output_schema())
    @namespace.response(400, 'Bad Request', ErrorSchemas.http_400())
    @namespace.response(401, 'Unauthorized', ErrorSchemas.http_401())
    @namespace.response(404, 'Not Found', ErrorSchemas.http_404())
    @namespace.response(409, 'Conflict', ErrorSchemas.http_409())
    @namespace.response(500, 'Internal Server Error', ErrorSchemas.http_500())
    @ErrorSchemas.handle_exceptions
    def get(self, username: str) -> Response:
        get_user_usecase: GetUserUseCase = current_app.usecases.get_user_usecase
        input_dto = GetUserInputDto(username=username)
        output_dto = get_user_usecase.execute(input_dto=input_dto)
        return UserSchemas.make_success_response(output_dto=output_dto)

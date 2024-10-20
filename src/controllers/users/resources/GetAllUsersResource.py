from flask import Response, current_app
from flask_restx import Resource
from src.controllers.schemas.common.ErrorSchemas import ErrorSchemas
from src.controllers.schemas.users.UserSchemas import UserSchemas
from src.controllers.users import namespace
from src.application.useCases.user.GetAllUsersUseCase import GetAllUsersUseCase


class GetAllUsersResource(Resource):
    @namespace.doc("Busca um usuário por username.")
    @namespace.response(200, 'Ok', UserSchemas.get_all_users_output_schema())
    @namespace.response(400, 'Bad Request', ErrorSchemas.http_400())
    @namespace.response(401, 'Unauthorized', ErrorSchemas.http_401())
    @namespace.response(404, 'Not Found', ErrorSchemas.http_404())
    @namespace.response(409, 'Conflict', ErrorSchemas.http_409())
    @namespace.response(500, 'Internal Server Error', ErrorSchemas.http_500())
    @ErrorSchemas.handle_exceptions
    def get(self) -> Response:
        get_all_users_usecase: GetAllUsersUseCase = current_app.usecases.get_all_users_usecase
        output_dto = get_all_users_usecase.execute()
        return UserSchemas.make_success_response_all_users(output_dto=output_dto)
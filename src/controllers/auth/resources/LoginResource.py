from flask import Response, current_app, request
from flask_login import login_user
from flask_restx import Resource
from src.application.useCases.user.AuthenticateUserUseCase import AuthenticateUserUseCase
from src.controllers.auth import namespace
from src.controllers.schemas.auth.LoginSchemas import LoginSchemas
from src.controllers.schemas.common.ErrorSchemas import ErrorSchemas
from src.domain.dto.user.input.AuthenticateUserInputDto import AuthenticateUserInputDto
from src.exceptions.users.InvalidFieldException import InvalidFieldException
from src.infra.utils.ValidatorsUtil import ValidatorsUtil


class LoginResource(Resource):
    @namespace.doc("Registra um usuário.")
    @namespace.expect(LoginSchemas.login_input_schema())
    @namespace.response(200, 'Ok', LoginSchemas.login_output_schema())
    @namespace.response(400, 'Bad Request', ErrorSchemas.http_400())
    @namespace.response(404, 'Not Found', ErrorSchemas.http_404())
    @namespace.response(401, 'Unauthorized', ErrorSchemas.http_401())
    @namespace.response(409, 'Conflict', ErrorSchemas.http_409())
    @namespace.response(500, 'Internal Server Error', ErrorSchemas.http_500())
    @ErrorSchemas.handle_exceptions
    def post(self) -> Response:
        data = request.json

        required_fields = AuthenticateUserInputDto.required_fields
        missing_fields = ValidatorsUtil.validate_input(
            data=data,
            required_fields=required_fields)
        if missing_fields:
            raise InvalidFieldException(f"Campos faltantes: {', '.join(missing_fields)}")
        
        authenticate_user_input_dto = AuthenticateUserInputDto()
        authenticate_user_input_dto.set_attributes(**data)

        authenticate_user_usecase: AuthenticateUserUseCase = current_app.usecases.authenticate_user_usecase
        authenticate_user_output_dto = authenticate_user_usecase.execute(
            input_dto=authenticate_user_input_dto)
        
        login_user(authenticate_user_output_dto.user_entity)
        
        return LoginSchemas.make_success_response(username=authenticate_user_output_dto.user_entity.username)

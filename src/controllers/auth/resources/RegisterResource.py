from flask import Response, current_app, request
from flask_restx import Resource
from src.controllers.auth import namespace
from src.application.useCases.user.CreatePersonUseCase import CreatePersonUseCase
from src.application.useCases.user.CreateUserUseCase import CreateUserUseCase
from src.controllers.schemas.auth.RegisterSchemas import RegisterSchemas
from src.controllers.schemas.common.ErrorSchemas import ErrorSchemas
from src.domain.dto.user.input.CreatePersonInputDto import CreatePersonInputDto
from src.domain.dto.user.input.CreateUserInputDto import CreateUserInputDto
from src.exceptions.users.InvalidFieldException import InvalidFieldException
from src.infra.utils.ValidatorsUtil import ValidatorsUtil


class RegisterResource(Resource):
        @namespace.doc("Registra um usuário.")
        @namespace.expect(RegisterSchemas.register_input_schema())
        @namespace.response(201, 'Created', RegisterSchemas.register_output_schema())
        @namespace.response(400, 'Bad Request', ErrorSchemas.http_400())
        @namespace.response(404, 'Not Found', ErrorSchemas.http_404())
        @namespace.response(409, 'Conflict', ErrorSchemas.http_409())
        @namespace.response(500, 'Internal Server Error', ErrorSchemas.http_500())
        @ErrorSchemas.handle_exceptions
        def post(self) -> Response:
            data = request.json

            person_required_fields = CreatePersonInputDto.required_fields
            user_required_fields = CreateUserInputDto.required_fields
            missing_fields = ValidatorsUtil.validate_input(
                data=data,
                required_fields=person_required_fields + user_required_fields)
            if missing_fields:
                raise InvalidFieldException(f"Campos faltantes: {', '.join(missing_fields)}")

            person_input_dto = CreatePersonInputDto()
            person_input_dto.set_attributes(**data)
            person_usecase: CreatePersonUseCase = current_app.usecases.create_person_usecase
            person_output_dto = person_usecase.execute(input_dto=person_input_dto)

            user_input_dto = CreateUserInputDto()
            user_input_dto.set_attributes(**data)
            user_usecase: CreateUserUseCase = current_app.usecases.create_user_usecase
            user_output_dto = user_usecase.execute(
                person_id=person_output_dto.person_entity.id,
                input_dto=user_input_dto)

            return RegisterSchemas.make_success_response(user_id=user_output_dto.user_entity.id)

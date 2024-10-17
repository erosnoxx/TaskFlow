from flask import current_app, request
from flask_restx import Resource
from src.application.useCases.user.CreatePersonUseCase import CreatePersonUseCase
from src.application.useCases.user.CreateUserUseCase import CreateUserUseCase
from src.controllers.auth import namespace
from src.controllers.schemas.AuthSchemas import AuthSchemas
from src.controllers.schemas.common.ErrorSchemas import ErrorSchemas
from src.domain.dto.user.input.CreatePersonInputDto import CreatePersonInputDto
from src.domain.dto.user.input.CreateUserInputDto import CreateUserInputDto
from src.exceptions.users.InvalidFieldException import InvalidFieldException
from src.exceptions.users.PersonNotExistsException import PersonNotExistsException
from src.exceptions.users.UserAlreadyExistsException import UserAlreadyExistsException
from src.infra.utils.ValidatorsUtil import ValidatorsUtil


class RegisterResource(Resource):
        @namespace.doc("Registra um usuário.")
        @namespace.expect(AuthSchemas.register_input_schema())
        @namespace.response(201, 'Created', AuthSchemas.register_output_schema())
        @namespace.response(400, 'Bad Request', ErrorSchemas.http_400())
        @namespace.response(404, 'Not Found', ErrorSchemas.http_404())
        @namespace.response(409, 'Conflict', ErrorSchemas.http_409())
        @namespace.response(500, 'Internal Server Error', ErrorSchemas.http_500())
        def post(self) -> tuple[dict, int]:
            data = request.json

            try:
                person_required_fields = CreatePersonInputDto.required_fields
                user_required_fields = CreateUserInputDto.required_fields
                missing_fields = ValidatorsUtil.validate_input(
                    data=data,
                    required_fields=person_required_fields + user_required_fields)
                if missing_fields:
                    return ({
                    'success': False,
                    'statuscode': 400,
                    'message': 'Campos obrigatórios estão faltando.',
                    'details': f"Campos faltantes: {', '.join(missing_fields)}"
                }, 400)

            except Exception as e:
                return ({
                    'success': False,
                    'statuscode': 500,
                    'message': 'Erro interno no servidor.',
                    'details': str(e)
                }, 500)

            try:
                person_input_dto = CreatePersonInputDto(
                    first_name=data.get('first_name'),
                    last_name=data.get('last_name'),
                    birthdate=data.get('birthdate'),
                    phone_number=data.get('phone_number'))
                person_usecase: CreatePersonUseCase = current_app.usecases.create_person_usecase
                person_output_dto = person_usecase.execute(input_dto=person_input_dto)

                user_input_dto = CreateUserInputDto(
                    username=data.get('username'),
                    email=data.get('email'),
                    password=data.get('password'))
                user_usecase: CreateUserUseCase = current_app.usecases.create_user_usecase
                user_output_dto = user_usecase.execute(
                    person_id=person_output_dto.person_entity.id,
                    input_dto=user_input_dto)

                return ({
                        'success': True,
                        'statuscode': 201,
                        'message': 'Usuário registrado com sucesso.',
                        'id': user_output_dto.user_entity.id
                    }, 201)

            except InvalidFieldException as ife:
                return ({
                    'success': False,
                    'statuscode': 400,
                    'message': 'Um ou mais campos fornecidos são inválidos.',
                    'details': str(ife)
                }, 400)

            except PersonNotExistsException as pne:
                    return ({
                        'success': False,
                        'statuscode': 404,
                        'message': 'Erro ao criar usuário.',
                        'details': str(pne)
                    }, 404)

            except UserAlreadyExistsException as uae:
                return ({
                    'success': False,
                    'statuscode': 409,
                    'message': 'Usuário já registrado com os dados fornecidos.',
                    'details': str(uae)
                }, 409)

            except Exception as e:
                return ({
                    'success': False,
                    'statuscode': 500,
                    'message': 'Erro interno no servidor.',
                    'details': str(e)
                }, 500)

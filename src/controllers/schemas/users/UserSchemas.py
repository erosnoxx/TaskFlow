import datetime
from src.controllers.schemas import *
from src.domain.dto.user.output.GetAllUsersOutputDto import GetAllUsersOutputDto
from src.domain.dto.user.output.GetUserOutputDto import GetUserOutputDto


class UserSchemas:
    @staticmethod
    def get_user_output_schema() -> Model:
        return api.model('Get User Output', {
            'full_name': fields.String(description='Nome completo do usuário.'),
            'birthdate': fields.String(description='Data de nascimento do usuário.', example='2000-01-01'),
            'age': fields.Integer(description='Idade do usuário.', min=1, max=3,),
            'username': fields.String(required=False, description='Nome de usuário para login.'),
            'email': fields.String(
                required=False,
                description='Endereço de e-mail do usuário.',
                default='example@email.com'),
            'phone_number': fields.String(description='Número de telefone do usuário.', example='11999999999')})
    
    @staticmethod
    def get_all_users_output_schema() -> Model:
        return api.model('Get All Users Output', {
            'users': fields.List(fields.Nested(UserSchemas.get_user_output_schema()), description='Lista de usuários.')
        })

    @staticmethod
    def make_success_response(output_dto: GetUserOutputDto) -> Response:
        birthdate = output_dto.user_entity.person.birthdate.strftime('%Y-%m-%d')
        response_data = {
            'full_name': output_dto.user_entity.person.full_name,
            'birthdate': birthdate,
            'age': output_dto.user_entity.person.age,
            'username': output_dto.user_entity.username,
            'email': output_dto.user_entity.email,
            'phone_number': output_dto.user_entity.person.phone_number
        }
        response = make_response(response_data, 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    
    @staticmethod
    def make_success_response_all_users(output_dto: GetAllUsersOutputDto) -> Response:
        users = []
        
        if output_dto.all_users:
            for user in output_dto.all_users:
                birthdate = user.person.birthdate.strftime('%Y-%m-%d')
                user_data = {
                    'full_name': user.person.full_name,
                    'birthdate': birthdate,
                    'age': user.person.age,
                    'username': user.username,
                    'email': user.email,
                    'phone_number': user.person.phone_number
                }
                users.append(user_data)

        response_data = {'users': users}
        response = make_response(response_data, 200)
        response.headers['Content-Type'] = 'application/json'
        return response

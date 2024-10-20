from src.controllers.schemas import *
from src.controllers.users import namespace as namespace_users


class RegisterSchemas:
    @staticmethod
    def register_input_schema() -> Model:
        return api.model('Register Person Input', {
            'first_name': fields.String(required=True, description='Primeiro nome do usuário.'),
            'last_name': fields.String(required=True, description='Sobrenome do usuário.'),
            'birthdate': fields.String(description='Data de nascimento do usuário.', example='2000-01-01'),
            'phone_number': fields.String(required=True, description='Número de telefone do usuário.'),
            'username': fields.String(required=True, description='Nome de usuário para login.'),
            'email': fields.String(
                required=True,
                description='Endereço de e-mail do usuário.',
                default='example@email.com'),
            'password': fields.String(required=True,
                                      description='Senha do usuário.', min_length=8, max_length=255,
                                      default='SenhaForte5@')})

    @staticmethod
    def register_output_schema() -> Model:
        return api.model('Register Person Output', {
            'success': fields.Boolean(description='Indica se o registro foi bem-sucedido.'),
            'statuscode': fields.Integer(default=201, description='Código de status HTTP do resultado da operação.'),
            'message': fields.String(description='Mensagem informativa sobre o resultado do registro.'),
            'id': fields.Integer(description='ID do usuário.')})

    @staticmethod
    def make_success_response(username: str) -> Response:
        response_data = {
                'success': True,
                'statuscode': 201,
                'message': 'Usuário registrado com sucesso.',
                'username': username}
        response = make_response(response_data, 201)
        response.headers['Location'] = f'{api.prefix}/{namespace_users.name}/{username}'
        response.headers['Content-Type'] = 'application/json'
        return response

from src.controllers.schemas import *


class LoginSchemas:
    @staticmethod
    def login_input_schema() -> Model:
        return api.model('Login User Input', {
            'username': fields.String(required=False, description='Nome de usuário para login.'),
            'email': fields.String(
                required=False,
                description='Endereço de e-mail do usuário.',
                default='example@email.com'),
            'password': fields.String(required=True,
                                      description='Senha do usuário.', min_length=8, max_length=255,
                                      default='SenhaForte5@')})

    @staticmethod
    def login_output_schema() -> Model:
        return api.model('Login User Output', {
            'success': fields.Boolean(description='Indica se o login foi bem-sucedido.'),
            'statuscode': fields.Integer(default=200, description='Código de status HTTP do resultado da operação.'),
            'message': fields.String(description='Mensagem informativa sobre o resultado do login.'),
            'id': fields.Integer(description='ID do usuário.')})

    @staticmethod
    def make_success_response(username: str) -> Response:
        response_data = {
                'success': True,
                'statuscode': 200,
                'message': 'Usuário logado com sucesso.',
                'username': username}
        response = make_response(response_data, 200)
        response.headers['Content-Type'] = 'application/json'
        return response

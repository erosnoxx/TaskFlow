from flask import make_response
from flask_login import logout_user, current_user
from flask_restx import Resource


class LogoutResource(Resource):
    def delete(self) -> None:
        if not current_user.is_authenticated:
            response_data = {
                'success': False,
                'statuscode': 401,
                'message': 'Usuário não está autenticado.'
            }
            response = make_response(response_data, 401)

            response.headers['Content-Type'] = 'application/json'
            return response

        username = current_user.username
        logout_user()
        
        response_data = {
            'success': True,
            'statuscode': 200,
            'message': 'Usuário deslogado com sucesso.',
            'username': username
        }
        response = make_response(response_data, 200)

        return response

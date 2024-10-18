from flask import make_response
from flask_restx import fields, Model
from src.application.extensions.Api import api
from src.exceptions.users.InvalidFieldException import InvalidFieldException
from src.exceptions.users.PersonNotExistsException import PersonNotExistsException
from src.exceptions.users.UserAlreadyExistsException import UserAlreadyExistsException


class ErrorSchemas:
    @staticmethod
    def http_400() -> Model:
        return api.model('Error 400', {
            'success': fields.Boolean(default=False),
            'message': fields.String,
            'details': fields.String,
            'statuscode': fields.Integer(default=400)
        })
    
    @staticmethod
    def http_404() -> Model:
        return api.model('Error 404', {
            'success': fields.Boolean(default=False),
            'message': fields.String,
            'details': fields.String,
            'statuscode': fields.Integer(default=404)
        })

    @staticmethod
    def http_500() -> Model:
        return api.model('Error 500', {
            'success': fields.Boolean(default=False),
            'message': fields.String,
            'details': fields.String,
            'statuscode': fields.Integer(default=500)
        })

    @staticmethod
    def http_409() -> Model:
        return api.model('Error 409', {
            'success': fields.Boolean(default=False),
            'message': fields.String,
            'details': fields.String,
            'statuscode': fields.Integer(default=409)
        })

    @staticmethod
    def make_error_response(status_code: int, message: str, details: str=None):
        response_data = {
            'success': False,
            'statuscode': status_code,
            'message': message,
            'details': details
        }
        response = make_response(response_data, status_code)
        response.headers['Content-Type'] = 'application/json'
        return response

    @staticmethod
    def handle_exceptions(f: callable):
        def wrapper(*args, **kwargs):
            try:
                return f(*args, **kwargs)
            except InvalidFieldException as ife:
                return ErrorSchemas.make_error_response(
                    status_code=400,
                    message='Um ou mais campos fornecidos são inválidos.',
                    details=str(ife))
            except PersonNotExistsException as pne:
                return ErrorSchemas.make_error_response(
                    status_code=404,
                    message='Erro ao criar usuário.',
                    details=str(pne))
            except UserAlreadyExistsException as uae:
                return ErrorSchemas.make_error_response(
                    status_code=409,
                    message='Usuário já registrado com os dados fornecidos.',
                    details=str(uae))
            except Exception as e:
                return ErrorSchemas.make_error_response(
                    status_code=500,
                    message='Erro interno no servidor',
                    details=str(e))
        return wrapper

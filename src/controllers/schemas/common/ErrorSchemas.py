from flask import make_response
from flask_restx import fields, Model
from src.application.extensions.Api import api
from src.exceptions.http.BadRequestException import BadRequestException
from src.exceptions.http.ConflictException import ConflictException
from src.exceptions.http.InternalServerException import InternalServerException
from src.exceptions.http.NotFoundException import NotFoundException
from src.exceptions.http.UnauthorizedException import UnauthorizedException


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
    def http_401() -> Model:
        return api.model('Error 401', {
            'success': fields.Boolean(default=False),
            'message': fields.String,
            'details': fields.String,
            'statuscode': fields.Integer(default=401)
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
            except BadRequestException as bre:
                return ErrorSchemas.make_error_response(
                    status_code=400,
                    message='Erro interno no servidor',
                    details=str(bre))
            except ConflictException as ce:
                return ErrorSchemas.make_error_response(
                    status_code=409,
                    message='Erro interno no servidor',
                    details=str(ce))
            except NotFoundException as nfe:
                return ErrorSchemas.make_error_response(
                    status_code=404,
                    message='Erro interno no servidor',
                    details=str(nfe))
            except UnauthorizedException as ue:
                return ErrorSchemas.make_error_response(
                    status_code=401,
                    message='Erro interno no servidor',
                    details=str(ue))
            except InternalServerException as ise:
                return ErrorSchemas.make_error_response(
                    status_code=500,
                    message='Erro interno no servidor',
                    details=str(ise))
            except Exception as e:
                return ErrorSchemas.make_error_response(
                    status_code=500,
                    message='Erro interno no servidor',
                    details=str(e))
        return wrapper

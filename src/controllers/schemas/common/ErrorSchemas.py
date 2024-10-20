from src.controllers.schemas import *
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
            'message': fields.String(default='Requisição inválida. Verifique os dados enviados.'),
            'details': fields.String,
            'statuscode': fields.Integer(default=400)
        })
    
    @staticmethod
    def http_404() -> Model:
        return api.model('Error 404', {
            'success': fields.Boolean(default=False),
            'message': fields.String(default='Recurso não encontrado.'),
            'details': fields.String,
            'statuscode': fields.Integer(default=404)
        })

    @staticmethod
    def http_500() -> Model:
        return api.model('Error 500', {
            'success': fields.Boolean(default=False),
            'message': fields.String(default='Erro interno no servidor.'),
            'details': fields.String,
            'statuscode': fields.Integer(default=500)
        })

    @staticmethod
    def http_409() -> Model:
        return api.model('Error 409', {
            'success': fields.Boolean(default=False),
            'message': fields.String(default='Conflito nos dados enviados.'),
            'details': fields.String,
            'statuscode': fields.Integer(default=409)
        })
    
    @staticmethod
    def http_401() -> Model:
        return api.model('Error 401', {
            'success': fields.Boolean(default=False),
            'message': fields.String(default='Acesso não autorizado.'),
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
                    message='Requisição inválida.',
                    details=str(bre))
            except ConflictException as ce:
                return ErrorSchemas.make_error_response(
                    status_code=409,
                    message='Conflito nos dados enviados.',
                    details=str(ce))
            except NotFoundException as nfe:
                return ErrorSchemas.make_error_response(
                    status_code=404,
                    message='Recurso não encontrado.',
                    details=str(nfe))
            except UnauthorizedException as ue:
                return ErrorSchemas.make_error_response(
                    status_code=401,
                    message='Acesso não autorizado.',
                    details=str(ue))
            except InternalServerException as ise:
                return ErrorSchemas.make_error_response(
                    status_code=500,
                    message='Erro interno no servidor.',
                    details=str(ise))
            except Exception as e:
                return ErrorSchemas.make_error_response(
                    status_code=500,
                    message='Erro desconhecido.',
                    details=str(e))
        return wrapper

from flask_restx import fields, Model
from src.application.extensions.Api import api


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
    def http_404() -> any:
        return api.model('Error 404', {
            'success': fields.Boolean(default=False),
            'message': fields.String,
            'details': fields.String,
            'statuscode': fields.Integer(default=404)
        })

    @staticmethod
    def http_500() -> any:
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

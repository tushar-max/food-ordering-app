from flask_restful import Resource

from bl.authorization.signup import signup_bl


class SignUp(Resource):
    def post(self):
        return signup_bl()
        
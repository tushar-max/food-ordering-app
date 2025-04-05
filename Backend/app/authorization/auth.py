from flask_restful import Resource

from bl.authorization.login import login_bl


class Authorization(Resource):
    def post(self):
        return login_bl()
        
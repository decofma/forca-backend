from crypt                                  import methods
from flask                                  import Flask, request
from flask_restplus                         import Resource
from flask_restplus.namespace               import Namespace

from view.api.api_model                     import MODEL_GET_LETTER
from ...model.facade.get_frontletter_facade import RecebeLetra

api = Namespace('RecebeLetra', path='/',
                description='Recebe a letra enviada pelo frontend')


model_api_get_letter = api.model('model_api_get_letter', MODEL_GET_LETTER)

app = Flask(__name__)

@app.route('/get_frontend_letter') 
class GetLetter(Resource):
    @api.expect(model_api_get_letter)

    def get(self):

        result = RecebeLetra().jogada(request.get_json())






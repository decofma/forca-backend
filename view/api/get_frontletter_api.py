from flask                                  import Flask, request,jsonify
from flask_restplus                         import Resource
from flask_restplus.namespace               import Namespace

from view.api.api_model                     import MODEL_GET_LETTER
from model.facade.get_frontletter_facade    import RecebeLetra

api = Namespace(name='RecebeLetra', path='/',
                description='Recebe a letra enviada pelo frontend')


model_api_get_letter = api.model('model_api_get_letter', MODEL_GET_LETTER)

# app = Flask(__name__)

@api.route('/get_frontend_letter/') 
class GetLetter(Resource):
    @api.expect(model_api_get_letter)

    def get(self):

        result = RecebeLetra().jogada(request.get_json())

        return jsonify(result)




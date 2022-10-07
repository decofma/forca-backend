from flask                                  import Flask, request, jsonify
from flask_restplus                         import Resource
from flask_restplus.namespace               import Namespace

from view.api.api_model                     import MODEL_GET_STATUS_GAME
from model.facade.status_facade          import RecebeStatusGame

api = Namespace(name='RecebeStatus', path='/',
                description='Recebe o status se o jogo inicou ou não')


model_api_get_status = api.model('model_api_get_status', MODEL_GET_STATUS_GAME)

# app = Flask(__name__)

@api.route('/get_status_game/') 
class GetStatusGame(Resource):
    @api.expect(model_api_get_status)

    def get(self):

        result = RecebeStatusGame().trata_status(request.get_json())
        
        return jsonify(result)

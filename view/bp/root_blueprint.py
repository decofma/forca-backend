from ..api.get_frontletter_api                          import api as get_frontletter
from ..api.status_facade_api                            import api as status
from flask                                              import Blueprint
from flask_restplus                                     import Api
from flask.helpers                                      import url_for
import os

# ---------------------------->>
# BLUE-PRINT - CONSTANTS
# ---------------------------->>
BLUE_PRINT_BASE_URL = '/'

BLUE_PRINT_NAME         = 'root-bp'
API_VERSION             = '1.0'
API_TITLE               = 'Jogo da forca'
API_DESCRIPTION         = 'API Jogo de forca desenvolvido para a matéria de Sistemas Derivados pelo aluno André Ferraz.'

# ---------------------------->>
# Registra os Blue Prints
# ---------------------------->>
bp = Blueprint(BLUE_PRINT_NAME, __name__)

@property
def specs_url(self):

    if os.environ.get("FLASK_ENV") == "production":
        _scheme = "https"
    else:
        _scheme = "http"
    return url_for(self.endpoint('specs'), _external=True, _scheme=_scheme)
Api.specs_url = specs_url


api = Api(
    bp,
    version=API_VERSION,
    doc='/',
    title=API_TITLE,
    description=API_DESCRIPTION
)

api.add_namespace(get_frontletter)
api.add_namespace(status)

# ---------------------------->>
# Inicializa a aplicação
# ---------------------------->>
def init_app(app):
    app.register_blueprint(bp)
    
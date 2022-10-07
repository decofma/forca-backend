from typing_extensions import Required
from flask_restplus import fields

MODEL_GET_LETTER = {
    "letra" : fields.String(required= True)
}

MODEL_GET_STATUS_GAME = {
    "status" : fields.Integer(required= True)
}
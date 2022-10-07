from flask_restplus import fields

MODEL_GET_LETTER = {
    "letter" : fields.String(required= True)
}

MODEL_GET_STATUS_GAME = {
    "status" : fields.Integer(required= True)
}
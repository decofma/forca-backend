from flask_restplus import fields

MODEL_GET_LETTER = {
    "letter" : fields.String(required= True),
    "hidden_word" : fields.String(required= True),
    "try": fields.Integer(required= True)
}

MODEL_GET_STATUS_GAME = {
    "status" : fields.Integer(required= True)
}
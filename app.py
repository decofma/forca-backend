from flask_cors                      import CORS
from flask                           import Flask,render_template,redirect,request
import view.bp.root_blueprint       as root 

app = Flask(__name__) 


@app.after_request
def set_response_headers(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response
  
def create_app():

    app = Flask(__name__)
    CORS(app)

    root.init_app(app)

    return app


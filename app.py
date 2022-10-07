from flask import Flask,render_template,redirect,request

import model.facade.functions as functions
  
app = Flask(__name__) 

secret_word = None
word_set = None
to_display = None
tries = None
blanks = None


@app.after_request
def set_response_headers(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response
  
@app.route('/') 
def hello_world(): 
    return ('home')


@app.route('/game_lost')
def game_lost_landing():
	return ('lose')

@app.route('/game_won')
def game_won_landing():
	return ('won')

if __name__ == '__main__': 
    app.run() 

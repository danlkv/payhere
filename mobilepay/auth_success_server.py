import pickle

import requests
from flask import Flask
from flask import request

import conf

app = Flask(__name__)

@app.route("/")
def initiate_browser_redirect():
    return '''
    <script>
        location.href = '/handle?' + location.hash.substring(1);
    </script>
    '''

@app.route("/handle")
def handle_successful_confirmation():

    r = requests.post('https://api.sandbox.mobilepay.dk' + '/merchant-authentication-openidconnect/connect/token',
                      data={'grant_type': 'authorization_code', 'code': request.args.get('code'),
                            'code_verifier': pickle.load(open('./challenge_verifier', 'rb')),
                            'client_id': conf.CLIENT_ID, 'client_secret': conf.get(conf.CLIENT_ID)['client_secret'],
                            'redirect_uri': conf.get(conf.CLIENT_ID)['redirect_uri']})
    # get and save  auth token
    return 'Success. We have been authentificated to proceed with payment. Choose a product.'




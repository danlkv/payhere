import base64
import pickle
from urllib.parse import urlencode, quote
import requests

from oic import rndstr
from hashlib import sha256

import conf

challenge_verifier = base64.urlsafe_b64encode(rndstr(64).encode('utf-8')).decode('utf-8')
challenge = sha256()
challenge.update(challenge_verifier.encode('utf-8'))
challenge = base64.urlsafe_b64encode(challenge.digest()).decode('utf-8')

#from now on pickle is used only for the sake of prototyping
pickle.dump(challenge_verifier, open('./challenge_verifier', 'wb'))

query_params = {
    'response_type': 'code id_token',
    'client_id': conf.CLIENT_ID,
    'redirect_uri': conf.get(conf.CLIENT_ID)['redirect_uri'],
    'scope': 'openid invoice offline_access',
    'state': rndstr(),
    'code_challenge': challenge,
    'code_challenge_method': 'S256',
    'nonce': rndstr()
}

r = requests.get(conf.API_HOST + '/account/connect/authorize/callback',
                 params=urlencode(query_params, quote_via=quote))
print(r.url)
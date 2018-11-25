API_HOST = 'https://sandprod-admin.mobilepay.dk'
CLIENT_ID = 'Hackathon01'

def get(client_id):
    return {
        'Hackathon01': {
            'merchant_id': '3bd92d61-0bf1-4ef4-aaa5-da580c5909a0',
            'invoice_issuer': '19656cbd-87bb-4d89-a3f4-868698e8ee93',
            'x-ibm-client-id': "83209b51-d263-4c80-b4e6-66e9fdc7b36e",
            'x-ibm-client-secret': "N4eJ4tB2dO2pL0fI1xR1eO2lT7eK1mI5gC5pR6fJ2pW5xP1hG5",
            'client_secret': 'zSoLbzM6Rz2VYrMgzq5fe9GqLpV4CipZNJ3yxG7NTr0',
            'redirect_uri': 'http://127.0.0.1:7890/',
        }
    }[client_id]

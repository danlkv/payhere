import pickle
import requests


from datetime import date

import conf

CLIENT_ID = 'Hackathon01'

user_auth = pickle.load(open('user_auth', 'rb'))


def incrementCurrentInvoiceId():
    with open('./invoice_id', 'r+') as invoiceF:
        invoiceId = int(invoiceF.readline()) + 1
        invoiceF.seek(0)
        invoiceF.write(str(invoiceId))
        return invoiceId

configs = conf.get(CLIENT_ID)

payload = {     "InvoiceIssuer": configs['invoice_issuer'], "ConsumerAlias":{"Alias":"+35812345678","AliasType":"Phone"},
                "ConsumerName":"Test name","TotalAmount":360,"TotalVATAmount":72,
                "CountryCode":"FI","CurrencyCode":"EUR","ConsumerAddressLines":[["Otaniemi 13"]],
                    "InvoiceNumber": str(incrementCurrentInvoiceId()),"IssueDate":"2018-05-03","DueDate":"2018-05-11",
                    "OrderDate": '{:%Y-%m-%d}'.format(date.today()), "Comment":
                    "Lorem ipsum dolor sit amet, eros faucibus aliqua erat aliquam odio vitae.",
                    "MerchantContactName":"Some Company","MerchantOrderNumber":"859","BuyerOrderNumber":"456",
                    "PaymentReference":"186","InvoiceArticles":[{
                        "ArticleNumber":"456","ArticleDescription":"Lorem ipsum dolor sit amet",
                        "VATRate":25,"TotalVATAmount":72,"TotalPriceIncludingVat":360,"Unit":"single",
                        "Quantity":6,"PricePerUnit":60,"PriceReduction":1.2,"PriceDiscount":2,"Bonus":5}]
                    }



headers = {
    'x-ibm-client-id': "83209b51-d263-4c80-b4e6-66e9fdc7b36e",
    'x-ibm-client-secret': "N4eJ4tB2dO2pL0fI1xR1eO2lT7eK1mI5gC5pR6fJ2pW5xP1hG5",
    'Authorization': 'Bearer ' + user_auth['id_token'],
    'accept': "application/json",
    'Content-Type': "application/json",
}



r = requests.get('https://api.sandbox.mobilepay.dk' + '/invoice-restapi/api/v1//merchants/%s/invoices' % configs['merchant_id'], headers=headers, json=payload)
#proceed with request handling...
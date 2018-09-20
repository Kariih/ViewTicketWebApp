from requests.auth import HTTPBasicAuth
import requests
import json

#Setting authentication details to api
token = 'TCl6givNOws8Te39GZS5uQFc8NApKS7AJtyxzqWw'
mail = 'kari.hdb@gmail.com/token'

#fetch list of 25 tickes from api
#Parameter - page number to request
def get_page_of_tickets(page):
        params = {
            'per_page': '25',
            'page': page
        }
        response = requests.get(
            'https://karihdb.zendesk.com/api/v2/tickets.json', params=params, auth=HTTPBasicAuth(
            mail, token))
        return json.loads(response.text)

#fetch single ticket from api
#Parameter - id of ticket to request
def get_single_ticket(id):
    url = 'https://karihdb.zendesk.com/api/v2/tickets/' + str(id) + '.json'
    response = requests.get(url, auth=HTTPBasicAuth(mail, token))
    return json.loads(response.text)

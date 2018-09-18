from flask import Flask, render_template
from requests.auth import HTTPBasicAuth
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

#@app.route('/tickets/<range>')
@app.route('/tickets/<int:page>')
def showTicketList(page):
    tickets_from_api = get_tickets_from_api(page)
    data = json.loads(tickets_from_api.text)
    prev = 0
    next = 0

    if data["previous_page"] is not None:
        prev = page - 1
        print("prev: " + str(prev))
    if data["next_page"] is not None:
        next = page + 1
        print("next data: " + str(data["next_page"]))
        print("next: " + str(next))

    return render_template("ticketlist.html", tickets=data["tickets"], prev=prev, next=next, page=page)

@app.route('/ticket/<page>/<id>')
def showSingleTicket(page, id):
    ticket_from_api = get_ticket_from_api(id)
    return render_template("ticket.html", ticket=json.loads(ticket_from_api.text)['ticket'], page=page)

def get_tickets_from_api(page):

    params = {
        'per_page': '25',
        'page': page
    }
    token = 'TCl6givNOws8Te39GZS5uQFc8NApKS7AJtyxzqWw'
    request = requests.get('https://karihdb.zendesk.com/api/v2/tickets.json', params=params, auth=HTTPBasicAuth('kari.hdb@gmail.com/token', token))
    print(json.loads(request.text))
    return request

def get_ticket_from_api(id):

    url = 'https://karihdb.zendesk.com/api/v2/tickets/' + str(id) + '.json'
    token = 'TCl6givNOws8Te39GZS5uQFc8NApKS7AJtyxzqWw'
    request = requests.get(url, auth=HTTPBasicAuth('kari.hdb@gmail.com/token', token))
    print(json.loads(request.text))
    return request

if __name__ == "__main__":
    app.run(debug=True, port=5000)


#------------------NOTES---------------------
#pip install Flask
#pip install requests

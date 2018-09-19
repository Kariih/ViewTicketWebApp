from flask import Flask, render_template
import api_requests

app = Flask(__name__)

#Route to index.html page
#Return - the HTML index page for application
@app.route('/')
def index():
    return render_template("index.html")

#Fetch ticket from api based on id and displayed on HTML page
#Parameter - current page number and id of cliked ticket
#Return - HTML page that is rendered by flask
@app.route('/ticket/<page>/<id>')
def showSingleTicket(page, id):
    return render_template(
        "ticket.html", ticket=api_requests.get_single_ticket(id)['ticket'], page=page)

#route to HTML page for showing list of tickets
#Parameter - current page number
#Return - HTML page that is rendered by flask
@app.route('/tickets/<int:page>')
def showTicketList(page):
    tickets_from_api = api_requests.get_page_of_tickets(page)

    #Checking of it exist a next or previous page of tickets,
    #if yes, assing the page number for next and previous page
    prev = 0
    next = 0

    if tickets_from_api["previous_page"] is not None:
        prev = page - 1
    if tickets_from_api["next_page"] is not None:
        next = page + 1

    return render_template(
        "ticketlist.html", tickets=tickets_from_api["tickets"], prev=prev, next=next, page=page)

#Starting the application
if __name__ == "__main__":
    app.run()


#------------------NOTES---------------------
#pip install Flask
#pip install requests

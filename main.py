from flask import Flask, render_template
import api_requests

app = Flask(__name__)

#Route to index.html page
@app.route('/')
def index():
    return render_template("index.html")

#Fetch ticket from api based on id and displayed on HTML page
#Parameter - current page number and id of cliked ticket
@app.route('/ticket/<page>/<id>')
def showSingleTicket(page, id):
    ticket_from_api = api_requests.get_single_ticket(id)

    #check if api response includes an error key
    if "error" in ticket_from_api:
        return render_template("error.html", error=ticket_from_api["error"])
    else:
        return render_template(
            "ticket.html", ticket=ticket_from_api['ticket'], page=page)

#route to HTML page for showing list of tickets
#Parameter - current page number
@app.route('/tickets/<int:page>')
def showTicketList(page):
    tickets_from_api = api_requests.get_page_of_tickets(page)

    #check if api response includes an error key
    if "error" in tickets_from_api:
        return render_template("error.html", error=tickets_from_api["error"])
    else:
        #Checking of it exist a next or previous page of tickets,
        #if yes, assing the page number for next and previous page
        prev = page - 1 if tickets_from_api["previous_page"] is not None else 0
        next = page + 1 if tickets_from_api["next_page"] is not None else 0

        return render_template(
            "ticketlist.html", tickets=tickets_from_api["tickets"], prev=prev, next=next, page=page)

#handle internal errors, if code/library "breaks"
@app.errorhandler(500)
def page_not_found(e):
    return render_template('error.html', error="500 - Something went wrong")

#handle error if route/page isn't found
@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', error="404 - Page not found")

#Starting the application
if __name__ == "__main__":
    app.run()

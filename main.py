from flask import Flask, render_template
#request

app = Flask(__name__)

#Setting folder root for the application
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/tickets/<range>')
def showTicketList(range):
    return "Showing tickets %s" %range

@app.route('/ticket/<int:ticket_number>')
def showSingleTicket(ticket_number):
    return "Showing ticket %s" %ticket_number

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask,render_template

from flask import *
from api.user_api import user
from api.booking_api import booking
from api.attraction_api import attraction
from api.order_api import orders

app = Flask(__name__)
app.config["JSON_AS_ASCII"]=False
app.config["TEMPLATES_AUTO_RELOAD"]=True
app.json.ensure_ascii = False

app.register_blueprint(attraction)
app.register_blueprint(user)
app.register_blueprint(booking)
app.register_blueprint(orders)

# Pages
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/attraction/<id>")
def attraction(id):
    return render_template("attraction.html")

@app.route("/booking")
def booking():
    return render_template("booking.html")

@app.route("/thankyou")
def thankyou():
    return render_template("thankyou.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000 )

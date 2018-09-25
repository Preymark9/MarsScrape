from flask import Flask, render_template
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)
print(app)
# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/scrape_mars"
mongo = PyMongo(app)


@app.route("/")
def index():
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars)
# remember! when building an HTML to define mars again so it knows how to call the db

@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scrapeweb.run
   return "print done"


if __name__ == "__main__":
    app.run()

#import necessary libraries
from flask import Flask, render_template, redirect
import scrape_mars.py
from flask_pymongo import PyMongo

# Import our pymongo library, which lets us connect our Flask app to our Mongo database.


#create instance of Flask app
app= Flask(__name__)

#Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"]= "mongodb://localhost:27017/mars_app"
mongo=PyMongo(app)



#create route that renders index.html template
@app.route("/")
def index():
    mars= mongo.db.mars.find_one()
    return render_template("Index.html", mars=mars)

# @app.scrape("/scrape")
# def scraper():
#     # mars=mongo.db.mars
#     # mars_data= scrape_mars.scrape_all()
#     # mars.replace_one({}, mars_data, upsert=True)
#     return "Scraping Successful"

if __name__ == "__main__":
    app.run()

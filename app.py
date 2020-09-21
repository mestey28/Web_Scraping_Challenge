#import necessary libraries
from flask import Flask, render_template, redirect
import pymongo
import scrape_mars


# Import our pymongo library, which lets us connect our Flask app to our Mongo database.


#create instance of Flask app
app= Flask(__name__)

#Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"]= "mongodb://localhost:27017/mars_app"
mongo=PyMongo(app)



## Use PyMongo to establish Mongo connection

@app.route("/")
def index():
    mars= mongo.db.mars.find_one()
    return render_template("Index.html", mars=mars)


## Route that will trigger the scrape function
@app.route("/scrape")
def scrape():
    mars_scrape = scrape_mars.scrape()
    # mars_data= scrape_mars.scrape_all()
    mongo.db.mars.update({}, mars_scrape, upsert=True)

    #redirect to home page
    return redirect("/"
    )

if __name__ == "__main__":
    app.run(debug=True)

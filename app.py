#import necessary libraries
from flask import flask, render_template

# Import our pymongo library, which lets us connect our Flask app to our Mongo database.
import pymongo

#create instance of Flask app
app= Flask(__name__)

# Create connection variable
conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn)

#create route that renders index.html template
@app.route("/")
def echo():
    return 'testing'
    # return render_template("index.html", text="Test")

if __name__ == "__main__":
    app.run(debug=True)

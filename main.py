import warnings
warnings.simplefilter(action='ignore', category=DeprecationWarning)
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask import Flask, render_template, jsonify, request
from database.menu import MainMenu
from database.table import getEnumTable

#TODO convert table functions to data frames and then make a convertToString taking the dataframe
#TODO populate the dataframe and string conversion into the html
#TODO make textbox the right size for all text
#TODO make textbox float as you scroll down page
#TODO fix coloring/CSS
#TODO fix tables that are currently placeholders
#TODO fix CSV files and figure out storage
#TODO change ENV variables instead of using postgres username/pin
#TODO containerize it to launch on docker
#TODO make it an executable that instantly launches to web page
#TODO make it open to local network
#TODO make it open on web
#TODO consider cloud refactor

app = Flask(__name__)

# ------------Start Program
db_username = os.environ.get("DB_USER")
db_password = os.environ.get("DB_PASS")
db_url = os.environ.get("DB_URL") #requires the last 13 characters to get the DB name
engine = create_engine(f"postgresql://{db_username}:{db_password}@localhost:5432/{db_url[-13::]}")
Session = sessionmaker(bind=engine)
session = Session()

@app.teardown_appcontext
def shutdown_session(exception=None):
    session.close()

@app.route("/")
def index():
    session = Session()
    menu = MainMenu(session)
    session.close()
    return render_template("index.html", menu=menu)

@app.route("/roll", methods=["POST"])
def roll():
    category_id = request.json.get("category_id")
    session = Session()
    result = getEnumTable(session, category_id)
    session.close()
    return jsonify({"result": result})

# console output for testing
"""
MainMenu(session)

while True:
    try:
        choice = input("---choose category to roll:\n")

        if choice.lower() == "exit":
            break
        else:
            getEnumTable(session, choice)

    except Exception as e:
        print(f"Invalid Selection: {e}\n")


"""


if __name__ == "__main__":
    app.run(debug=True)
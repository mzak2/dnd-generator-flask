import warnings
warnings.simplefilter(action='ignore', category=DeprecationWarning)
import pandas as pd
import os
import psycopg2 # for some reason isn't imported for SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask import Flask, render_template, jsonify, request
from database.menu import MainMenu
from database.table import getEnumDF
from database.string_templates import townEventString, magicItemString, potionsString, civilizationString, \
    wildernessString, characterString

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
db_url = os.environ.get("dnd_gen_url")
engine = create_engine(f"{db_url}")
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

    try:
        result_df = getEnumDF(session, category_id)

        if category_id == 4:
            result_str = townEventString(result_df)
        elif category_id == 29:
            result_str = magicItemString(result_df)
        elif category_id == 30:
            result_str = potionsString(result_df)
        elif category_id > 0 and category_id < 6 or category_id == 9:
            result_str = civilizationString(result_df)
        elif category_id >= 6 and category_id <15 and category_id != 9 and category_id != 13:
            result_str = wildernessString(result_df)
        elif 15 <= category_id <= 22:
            result_str = characterString(result_df)
        else:
            result_str = result_df.iloc[0, 1] if not result_df.empty else "No result available."

        result_html = result_df.to_html(classes="table table-bordered")

        return jsonify({"result_string": result_str, "result_df": result_html})

    except Exception as e:
        return jsonify({"error": str(e)})
    finally:
        session.close()


if __name__ == "__main__":
    app.run(debug=True)


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
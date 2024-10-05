import warnings
warnings.simplefilter(action='ignore', category=DeprecationWarning)
import pandas as pd
import random
from sqlalchemy import create_engine, text

def getMaxRoll(session, table):
    try:
        max_roll_query = text(f"SELECT MAX(id) as max_id FROM {table}")
        max_roll_df = pd.read_sql_query(max_roll_query, session.bind)
        max_roll = int(max_roll_df.iloc[0]["max_id"])

        return max_roll

    except Exception as e:
        session.rollback()
        print(f"Error: {e}")

    finally:
        session.close()

def rollTable(session, table):
    try:
        max_roll = getMaxRoll(session, table)

        roll = random.randint(1, max_roll)

        sql_query = text(f"SELECT * FROM {table} WHERE id = {roll}")
        result_df = pd.read_sql_query(sql_query, session.bind)

        if "description" in result_df.columns:
            result = result_df.iloc[0]['description']
        elif "name" in result_df.columns:
            result = result_df.iloc[0]['name']

        # console output for testing
        # print(f"Result: {result}")
        return result

    except Exception as e:
        session.rollback()
        print(f"Error: {e}")

    finally:
        session.close()

# table matches enumerated tables 1-3, 5, and 9
def rollCivilization(session, table):
    try:
        adjective = rollTable(session, "adjectives")
        terrain = rollTable(session, "terrain")
        purpose = rollTable(session, "purpose")
        civil_desc = rollTable(session, table)
        item_1 = rollTable(session, "items")
        item_2 = rollTable(session, "items")
        item_3 = rollTable(session, "items")
        item_4 = rollTable(session, "items")
        item_5 = rollTable(session, "items")

        # convert table names grammatically
        if table == "castles":
            table = "castle"
        elif table == "churches":
            table = "church"
        elif table == "cities":
            table = "city"
        elif table == "villages":
            table = "village"
        elif table == "graveyards":
            table = "graveyard"

        # format our string for returning to the user
        # table[:-1] removes the s from the table name to make it grammatically correct
        result = (
                f"While traveling through the {table}, " +
                f"they come upon a/an {adjective} {terrain} {civil_desc}. " +
                f"There appears to be a/an... {purpose} and inside is/a: " +
                f"{item_1}, {item_2}, {item_3}, {item_4}, {item_5}"
        )

        # console output for testing
        # print(result)
        return result

    except Exception as e:
        print(f"Error: {e}")

    finally:
        session.close()

# table is called "magicitems"
def rollMagicItems(session, table):
    try:
        description = rollTable(session, table)
        equip_type = rollTable(session, "equipment")

        result = f"You find a: {equip_type} with the effect of: {description}"

        # console output for testing
        # print(result)
        return result

    except Exception as e:
        print(f"Error: {e}")

    finally:
        session.close()

# table is called "potions"
def rollPotions(session, table):
    try:
        effect = rollTable(session, table)
        duration = rollTable(session, "durations")

        result = f"The potion's effect is: {effect} with a duration of {duration}"

        # console output for testing
        # print(result)
        return result

    except Exception as e:
        print(f"Error: {e}")

    finally:
        session.close()

# table is called "events"
def rollTownEvent(session, table):
    try:
        event = rollTable(session, table)
        npc_1 = rollTable(session, "npcs")
        npc_2 = rollTable(session, "npcs")

        result = f"While traveling through town, you come upn a: {npc_1}, currently: {event}, with a/an: {npc_2}."

        # console output for testing
        # print(result)
        return result

    except Exception as e:
        print(f"Error: {e}")

    finally:
        session.close()

# table matches enumerated tables 6- 8 amd 10-14
# table[:-1] converts the name of the table minus the "s" at the end for grammatical fixes
def rollWilderness(session, table):
    try:
        wilderness_desc = rollTable(session, table)
        terrain = rollTable(session, "terrain")
        purpose = rollTable(session, "purpose")
        adjective = rollTable(session, "adjectives")

        item_1 = rollTable(session, "items")
        item_2 = rollTable(session, "items")
        item_3 = rollTable(session, "items")
        item_4 = rollTable(session, "items")
        item_5 = rollTable(session, "items")

        if table == "beaches":
            table = "beache" # formats beach table to be "beach"

        result = (
                f"While traveling through the {table[:-1]}, " +
                f"they come upon a/an {adjective} {terrain} {wilderness_desc}. " +
                f"There appears to be a/an... {purpose} and inside is/a: " +
                f"{item_1}, {item_2}, {item_3}, {item_4}, {item_5}"
        )

        # console output for testing
        # print(result)
        return result

    except Exception as e:
        print(f"Error: {e}")

    finally:
        session.close()


def getEnumTable(session, choice):
    enum_list = {
        "1": "castles",
        "2": "churches",
        "3": "cities",
        "4": "events",
        "5": "villages",
        "6": "deserts",
        "7": "forests",
        "8": "grasslands",
        "9": "graveyards",
        "10": "beaches",
        "11": "mountains",
        "12": "swamps",
        "13": "setbacks",
        "14": "tundras",
        "15": "adventurers",
        "16": "wizards",
        "17": "bbegs",
        "18": "monsters",
        "19": "nobles",
        "20": "priests",
        "21": "npcs",
        "22": "villagers",
        "23": "blessings",
        "24": "curses",
        "25": "divinations",
        "26": "meleecombat",
        "27": "nightmares",
        "28": "spellcasting",
        "29": "magicitems",
        "30": "potions",
        "31": "items",
        "32": "equipment"
    }

    # get table name of corresponding number for easy SQL queries
    table = enum_list.get(f"{choice}")
    choice_num = int(choice)

    # Logic to select the correct output based on categories or specific tables:
    if choice_num == 4:
        return rollTownEvent(session, table)
    elif choice_num == 29:
        return rollMagicItems(session, table)
    elif choice_num == 30:
        return rollPotions(session, table)
    elif 1 <= choice_num <= 5 or choice_num == 9:
        return rollCivilization(session, table)
    elif 6 <= choice_num <= 14 and choice_num != 9:
        return rollWilderness(session, table)
    else:
        return rollTable(session, table)



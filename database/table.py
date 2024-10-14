import warnings
warnings.simplefilter(action='ignore', category=DeprecationWarning)
import pandas as pd
import random
from sqlalchemy import create_engine, text
from database.string_templates import wildernessString, townEventString, potionsString, magicItemString, \
    civilizationString

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

        return result_df

    except Exception as e:
        session.rollback()
        print(f"Error: {e}")

    finally:
        session.close()


def rollCharacters(session, table):
    try:
        speech_speed = rollTable(session, "speech_speed")
        speech_type = rollTable(session, "speech_type")
        race = rollTable(session, "race")
        race_color = rollTable(session, "race_color")
        occupation = rollTable(session, "occupations")
        clothing_state = rollTable(session, "clothing_state")
        clothing = rollTable(session, "clothing")
        npc_items = rollTable(session, "npc_items")
        npc_quirks = rollTable(session, "npc_quirks")
        colors = rollTable(session, "colors")

        result_df = pd.DataFrame({
            "table": table[:-1],
            "speech_speed": [speech_speed.iloc[0, 1]],
            "speech_type": [speech_type.iloc[0, 1]],
            "race": [race.iloc[0, 1]],
            "race_color": [race_color.iloc[0, 1]],
            "occupation": [occupation.iloc[0, 1]],
            "clothing_state": [clothing_state.iloc[0, 1]],
            "clothing": [clothing.iloc[0, 1]],
            "npc_items": [npc_items.iloc[0, 1]],
            "npc_quirks": [npc_quirks.iloc[0, 1]],
            "colors": [colors.iloc[0, 1]]
        })

        return result_df

    except Exception as e:
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

        result_df = pd.DataFrame({
            "table": [table],
            "adjective": [adjective.iloc[0, 1]],
            "terrain": [terrain.iloc[0, 1]],
            "purpose": [purpose.iloc[0, 1]],
            "civil_desc": [civil_desc.iloc[0, 1]],
            "item_1": [item_1.iloc[0, 1]],
            "item_2": [item_2.iloc[0, 1]],
            "item_3": [item_3.iloc[0, 1]],
            "item_4": [item_4.iloc[0, 1]],
            "item_5": [item_5.iloc[0, 1]],
        })

        return result_df

    except Exception as e:
        print(f"Error: {e}")

    finally:
        session.close()

# table is called "magicitems"
def rollMagicItems(session, table):
    try:
        description = rollTable(session, table)
        equip_type = rollTable(session, "equipment")

        result_df = pd.DataFrame({
            "equip_type": [equip_type.iloc[0, 1]],
            "description": [description.iloc[0, 1]]
        })

        return result_df

    except Exception as e:
        print(f"Error: {e}")

    finally:
        session.close()

# table is called "potions"
def rollPotions(session, table):
    try:
        effect = rollTable(session, table)
        duration = rollTable(session, "durations")

        result_df = pd.DataFrame({
            "effect": [effect.iloc[0, 1]],
            "duration": [duration.iloc[0, 1]]
        })

        return result_df

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

        result_df = pd.DataFrame({
            "event": [event.iloc[0, 1]],
            "npc_1": [npc_1.iloc[0, 1]],
            "npc_2": [npc_2.iloc[0,1]]
        })

        return result_df

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
            table = "beache"  # formats beach table to be "beach"

        result_df = pd.DataFrame({
            "table": [table[:-1]],
            "adjective": [adjective.iloc[0, 1]],
            "terrain": [terrain.iloc[0, 1]],
            "purpose": [purpose.iloc[0, 1]],
            "wilderness_desc": [wilderness_desc.iloc[0, 1]],
            "item_1": [item_1.iloc[0, 1]],
            "item_2": [item_2.iloc[0, 1]],
            "item_3": [item_3.iloc[0, 1]],
            "item_4": [item_4.iloc[0, 1]],
            "item_5": [item_5.iloc[0, 1]],
        })

        return result_df

    except Exception as e:
        print(f"Error: {e}")

    finally:
        session.close()


def getEnumDF(session, choice):
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

    # logic to select the correct output based on categories or specific tables:
    if choice_num == 4:
        return rollTownEvent(session, table)
    elif choice_num == 29:
        return rollMagicItems(session, table)
    elif choice_num == 30:
        return rollPotions(session, table)
    elif 1 <= choice_num <= 5 or choice_num == 9:
        return rollCivilization(session, table)
    elif 6 <= choice_num <= 14 and choice_num != 9 and choice_num != 13:
        return rollWilderness(session, table)
    elif 15 <= choice_num <= 22:
        return rollCharacters(session, table)
    else:
        return rollTable(session, table)


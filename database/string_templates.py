import random
import warnings
warnings.simplefilter(action='ignore', category=DeprecationWarning)
import pandas as pd

def blessingOrCurseString(df):
    row = df.iloc[0]

    result_str = (
        f"You gain:\n---{row['effect']}\nwith a duration of:\n---{row['duration']}"
    )

    return result_str

def characterString(df):
    row = df.iloc[0]

    result_str = (
        f"Before you is a/an:\n---{row['table']} and a/an {row['occupation']}\n" +
        f"---Male-Name: {row['male']} ---Female-Name: {row['female']} ---Last-Name: {row['last_name']}\n" +
        f"Who appears to be a/an:\n---{row['skin']} skinned {row['race']}\n" +
        f"Who speaks:\n---{row['speech_spd']} and {row['speech_type']}\n" +
        f"Their Clothing is a/an:\n---{row['clothing_state']} {row['clothing']} and carries a/an {row['items']}\n" +
        f"Finally they have a/an:\n---{row['quirk']} and a color motif of {row['colors']}"
    )

    return result_str

def civilizationString(df):
    row = df.iloc[0]

    if row['table'] == "dungeonrooms":
        row['table'] = "Dungeon"

    result_str = (
        f"While traveling through the {row['table']}, they come upon a/an:\n---{row['adjective']} {row['civil_desc']}\n" +
        f"It is used as or depicts a/an:\n---{row['purpose']}\nInside is/a:\n" +
        f"---{row['item_1']}\n---{row['item_2']}\n---{row['item_3']}\n---{row['item_4']}\n---{row['item_5']}"
    )

    return result_str

def magicItemString(df):
    row = df.iloc[0]

    result_str = (
        f"You find a:\n---{row['equip_type']}\nwith the effect of:\n---{row['description']}."
    )

    return result_str

def potionsString(df):
    row = df.iloc[0]

    result_str = (
        f"The potion's effect is:\n---{row['effect']}\nwith a duration of:\n---{row['duration']}"
    )

    return result_str


def setbackString(df):
    row = df.iloc[0]

    if 'description' in df.columns and pd.notna(row['description']):
        result_str = f"The party is unable to continue because they find:\n---{row['description']}"
    elif 'ration' in df.columns and pd.notna(row['ration']):
        result_str = f"The party finds themselves famished, roll a:\n---{row['ration']} for the amount of rations they've consumed"
    else:
        result_str = "Error rolling setbacks table"

    return result_str


def townEventString(df):
    row = df.iloc[0]

    roll = random.randint(1,5)

    if roll == 1:
        conversation = "Conversation"
    elif roll == 2:
        conversation = "Business Transaction"
    elif roll == 3:
        conversation = "Argument"
    elif roll == 4:
        conversation = "Disagreement"
    else:
        conversation = "Casual Conversation"


    result_str = (
        f"While traveling through town, you come upon a:\n---{row['npc_1']}\n" +
        f"currently in a/an:\n---{conversation}\nwith a/an:\n---{row['npc_2']}\nabout:\n---{row['event']}"
    )

    return result_str

def wildernessString(df):
    row = df.iloc[0]

    result_str = (
        f"While traveling through the {row['table']}, " +
        f"they come upon a/an:\n---{row['adjective']} {row['terrain']} {row['wilderness_desc']}.\n" +
        f"There appears to be a/an:\n---{row['purpose']}\nInside is/a:\n" +
        f"---{row['item_1']}\n---{row['item_2']}\n---{row['item_3']}\n---{row['item_4']}\n---{row['item_5']}"
    )

    return result_str

import warnings
warnings.simplefilter(action='ignore', category=DeprecationWarning)
import pandas as pd

def civilizationString(df):
    result_str = df.apply(lambda row: (
        f"While traveling through the {row['table']}, " +
        f"they come upon a/an:\n---{row['adjective']} {row['terrain']} {row['civil_desc']}.\n" +
        f"There appears to be a/an:\n---{row['purpose']}\nInside is/a:\n" +
        f"---{row['item_1']}\n---{row['item_2']}\n---{row['item_3']}\n---{row['item_4']}\n---{row['item_5']}"
    ), axis=1).iloc[0]

    return result_str

def magicItemString(df):
    result_str = df.apply(lambda row: (
        f"You find a:\n---{row['equip_type']}\nwith the effect of:\n---{row['description']}."
    ), axis=1).iloc[0]

    return result_str

def potionsString(df):
    result_str = df.apply(lambda row: (
        f"The potion's effect is:\n---{row['effect']}\nwith a duration of:\n---{row['duration']}"
    ), axis=1).iloc[0]

    return result_str

def townEventString(df):
    result_str = df.apply(lambda row: (
        f"While traveling through town, you come upon a: {row['npc_1']}, currently: {row['event']}, with a/an: {row['npc_2']}."
    ), axis=1).iloc[0]

    return result_str

def wildernessString(df):
    result_str = df.apply(lambda row: (
        f"While traveling through the {row['table']}, " +
        f"they come upon a/an:\n---{row['adjective']} {row['terrain']} {row['wilderness_desc']}.\n" +
        f"There appears to be a/an:\n---{row['purpose']}\nInside is/a:\n" +
        f"---{row['item_1']}\n---{row['item_2']}\n---{row['item_3']}\n---{row['item_4']}\n---{row['item_5']}"
    ), axis=1).iloc[0]

    return result_str


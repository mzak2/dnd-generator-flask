import warnings
warnings.simplefilter(action='ignore', category=DeprecationWarning)
import pandas as pd

def civilizationString(df):
    row = df.iloc[0]

    result_str = (
        f"While traveling through the {row['table']}, " +
        f"they come upon a/an:\n---{row['adjective']} {row['terrain']} {row['civil_desc']}.\n" +
        f"There appears to be a/an:\n---{row['purpose']}\nInside is/a:\n" +
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

def townEventString(df):
    row = df.iloc[0]

    result_str = (
        f"While traveling through town, you come upon a: {row['npc_1']}, " +
        f"currently: {row['event']}, with a/an: {row['npc_2']}."
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

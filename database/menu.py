import warnings
warnings.simplefilter(action='ignore', category=DeprecationWarning)
import pandas as pd
from sqlalchemy import create_engine, text, select, func

"""
def MainMenu(session):
    sql_query = text("SELECT * FROM categories ORDER BY category_id")
    categories = pd.read_sql_query(sql_query, session.bind)

    print("---Snapshot of DnD Generator----")
    for index, category in categories.iterrows():
        category_id = category["category_id"]
        print(f"{category_id}. {category['category_name']}")

        subcat_query = text(f"SELECT * FROM sub_categories WHERE category_id = {category_id} ORDER BY id")
        subcategories = pd.read_sql_query(subcat_query, session.bind)

        if not subcategories.empty:
            for sub_index, subcategory in subcategories.iterrows():
                print(f"\"{subcategory['id']}\": \"{subcategory['name'].lower()}\"")"""

def MainMenu(session):
    sql_query = text("SELECT * FROM categories ORDER BY category_id")
    categories = pd.read_sql_query(sql_query, session.bind)

    menu = []

    for index, category in categories.iterrows():
        category_id = category["category_id"]
        category_name = category["category_name"]

        subcat_query = text(f"SELECT * FROM sub_categories WHERE category_id = {category_id} ORDER BY id")
        subcategories = pd.read_sql_query(subcat_query, session.bind)

        subcategory_list = subcategories.to_dict(orient='records') if not subcategories.empty else []

        # add the category and its subcategories to the menu
        menu.append({
            "category_id": category_id,
            "category_name": category_name,
            "subcategories": subcategory_list
        })

    return menu
from database import fetch_all
from Chains import Chain
chain=Chain()
def search_menu(query):
    return search(query)

def search(query):
    all_menu_items = fetch_all("""
    SELECT *
    FROM menu_items 
    """)

    data=chain.search(query,all_menu_items)
    return search_extract(data)

def search_extract(datas):
    searchresults=[]
    for data in datas:

        name, price = data
        result = fetch_all("""
        SELECT id, restaurant_id, name, price
        FROM menu_items
        WHERE name = ?
        AND price = ?
        LIMIT 1
        """, (name, price))

        if result:
            menu_id, rest_id, name, price = result[0]
            rest_name = fetch_all("""
                SELECT name FROM restaurants WHERE id = ?
            """, (rest_id,))[0]
            
            searchresults.append((menu_id, rest_name, name, price))

    return searchresults        
        
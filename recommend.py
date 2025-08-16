from Chains import Chain
chain = Chain()
# recommend.py
from database import fetch_all

def recommen():
    """
    Initializes:
      - your_reviews: list of tuples containing (restaurant_id, restaurant_name, review_text)
        for reviews by 'you'
      - all_menu_items: list of tuples containing (restaurant_id, restaurant_name, menu_item_name, price)
        for all menu items
    """
  

    # Fetch 'you' reviews with restaurant names
    your_reviews = fetch_all("""
    SELECT *
    FROM reviews AS r
    WHERE r.user_name = "you"
     """)

    all_menu_items = fetch_all("""
    SELECT *
    FROM menu_items 
    """)

    data=chain.recomm(your_reviews,all_menu_items)
    return recommen_extract(data)


def recommen_extract(item_tuple):
  
    name, price = item_tuple
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
        
        return [(menu_id, rest_name, name, price)]
    else:
        return None


def get_recommendations():
    return recommen()
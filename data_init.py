from database import create_tables, execute_query

# Initialize tables
create_tables()

# Extra tables for past orders
execute_query("""
CREATE TABLE IF NOT EXISTS past_orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_name TEXT,
    restaurant_id INTEGER,
    menu_item_id INTEGER,
    FOREIGN KEY (restaurant_id) REFERENCES restaurants(id),
    FOREIGN KEY (menu_item_id) REFERENCES menu_items(id)
)
""")

# Clear existing data
for table in ["past_orders", "reviews", "menu_items", "restaurants"]:
    execute_query(f"DELETE FROM {table}")

# -------------------------
# RESTAURANTS
# -------------------------
restaurants = [
    ("Pizza Palace",),
    ("Curry Corner",),
    ("Sushi Central",),
    ("Burger Barn",),
    ("Pasta Point",),
    ("Taco Town",),
    ("BBQ Brothers",),
    ("Salad Stop",),
    ("Dimsum Den",),
    ("Biryani Bazaar",),
    ("Noodle Nook",),
    ("Dessert Dreams",),
    ("Steak Station",),
    ("Falafel Fiesta",),
    ("Wrap World",),
    ("Vegan Vibes",),
    ("Seafood Shack",),
    ("Cafe Cosmo",)
]
for r in restaurants:
    execute_query("INSERT INTO restaurants (name) VALUES (?)", r)

# -------------------------
# MENU ITEMS
# -------------------------
menu_items = [
    # Pizza Palace
    (1, "Margherita Pizza", 250),
    (1, "Pepperoni Pizza", 300),

    # Curry Corner
    (2, "Paneer Butter Masala", 200),
    (2, "Chicken Tikka Masala", 250),

    # Sushi Central
    (3, "California Roll", 400),
    (3, "Salmon Sashimi", 500),

    # Burger Barn
    (4, "Cheeseburger", 180),
    (4, "Double Bacon Burger", 250),

    # Pasta Point
    (5, "Spaghetti Carbonara", 220),
    (5, "Penne Arrabiata", 200),

    # Taco Town
    (6, "Beef Taco", 150),
    (6, "Veggie Taco", 130),

    # BBQ Brothers
    (7, "BBQ Ribs", 400),
    (7, "Grilled Chicken Wings", 280),

    # Salad Stop
    (8, "Caesar Salad", 180),
    (8, "Quinoa Salad", 200),

    # Dimsum Den
    (9, "Pork Dumplings", 160),
    (9, "Veg Momos", 120),

    # Biryani Bazaar
    (10, "Hyderabadi Biryani", 250),
    (10, "Veg Biryani", 220),

    # Noodle Nook
    (11, "Hakka Noodles", 150),
    (11, "Chow Mein", 160),

    # Dessert Dreams
    (12, "Chocolate Lava Cake", 180),
    (12, "Tiramisu", 200),

    # Steak Station
    (13, "Sirloin Steak", 500),
    (13, "Ribeye Steak", 550),

    # Falafel Fiesta
    (14, "Falafel Wrap", 150),
    (14, "Hummus Plate", 130),

    # Wrap World
    (15, "Chicken Shawarma Wrap", 180),
    (15, "Paneer Tikka Wrap", 160),

    # Vegan Vibes
    (16, "Vegan Burger", 200),
    (16, "Tofu Stir Fry", 220),

    # Seafood Shack
    (17, "Grilled Prawns", 400),
    (17, "Fish Curry", 350),

    # Cafe Cosmo
    (18, "Cold Brew Coffee", 150),
    (18, "Avocado Toast", 180),
]
for m in menu_items:
    execute_query("INSERT INTO menu_items (restaurant_id, name, price) VALUES (?, ?, ?)", m)

# -------------------------
# REVIEWS
# -------------------------
reviews = [
    # Pizza Palace
    (1, "you", "Tried the Margherita and Pepperoni here. Crust had a nice chew, pepperoni was slightly greasy but flavorful.", False),
    (1, "Mila", "Hands down the BEST pizza on planet Earth! I’d eat this every day for the rest of my life!", True),
    (1, "Alice", "Good flavor, crust was a little burnt but toppings were fresh.", False),

    # Curry Corner
    (2, "you", "Paneer Butter Masala was rich but a bit heavy. Garlic naan was excellent.", False),
    (2, "Dave", "This curry was an insult to Indian cuisine. Ban this place!", True),
    (2, "Charlie", "Decent place for a casual curry. Chicken Tikka had a nice char.", False),

    # Sushi Central
    (3, "you", "The Salmon Sashimi was fresh and well-cut. Could improve wasabi quality.", False),
    (3, "Akira", "This sushi is so good it changed my life. If you don’t eat here, you’re missing out on existence itself!", True),
    (3, "Eve", "Fresh sushi with beautiful presentation. California Roll was excellent.", False),

    # Burger Barn
    (4, "you", "Cheeseburger had great seasoning, fries were crispy.", False),
    (4, "Mia", "The worst burger in the history of mankind. I wouldn’t feed it to a stray dog.", True),
    (4, "Jake", "Juicy burger with perfect seasoning. Great value.", False),

    # Pasta Point
    (5, "you", "The Lasagna was hearty and rich. Could use more béchamel sauce.", False),
    (5, "Nina", "The Spaghetti here is so divine I cried while eating. Pure heaven!", True),
    (5, "Luca", "Carbonara was creamy, pancetta well cooked.", False),

    # Taco Town
    (6, "you", "Beef taco was juicy, tortilla fresh. Could use spicier salsa.", False),
    (6, "Marco", "These tacos are so bad they should be illegal. Tasteless and soggy.", True),
    (6, "Sofia", "Chicken tacos had great seasoning, burrito was filling.", False),

    # Steak Street
    (7, "you", "Ribeye was cooked to medium-rare perfectly, sides were okay.", False),
    (7, "Henry", "Best steak in the galaxy! I’d mortgage my house for another bite!", True),
    (7, "Ella", "Good cut of meat, a bit too salty for me.", False),

    # Vegan Vibes
    (8, "you", "Tofu stir fry had nice flavor balance, portion was generous.", False),
    (8, "Clara", "This is vegan food that tastes better than any meat on earth!", True),
    (8, "Olivia", "Buddha bowl was fresh and colorful, dressing was nice.", False),

    # Seafood Shack
    (9, "you", "Grilled salmon had crispy skin, prawn curry was flavorful.", False),
    (9, "Rick", "The fish here tasted like it was fished out of a sewer. Horrible.", True),
    (9, "Zara", "Fish & Chips were golden and crunchy.", False),

    # Biryani Bliss
    (10, "you", "Chicken Biryani had fragrant rice and tender meat.", False),
    (10, "Arjun", "Best biryani in the universe! No other place comes close!", True),
    (10, "Priya", "Veg biryani was flavorful and light.", False),

    # BBQ Brothers
    (11, "you", "BBQ chicken wings were smoky and well glazed.", False),
    (11, "Sam", "Worst BBQ ever. Sauce tasted like burnt sugar mixed with vinegar.", True),
    (11, "Ben", "Pulled pork sandwich was tender and juicy.", False),

    # Noodle Nest
    (12, "you", "Chicken ramen broth was rich, noodles had nice bite.", False),
    (12, "Hiro", "This ramen is so good I want it served at my wedding.", True),
    (12, "Maya", "Pad Thai was tangy and well balanced.", False),

    # Breakfast Bay
    (13, "you", "Pancakes were fluffy, syrup was a bit too sweet.", False),
    (13, "Tom", "Worst breakfast I’ve ever had. Burnt toast and watery coffee.", True),
    (13, "Anna", "Omelette was fluffy and well seasoned.", False),

    # Dessert Dreams
    (14, "you", "Cheesecake was creamy, base was perfectly crumbly.", False),
    (14, "Sophia", "This cake is the meaning of life. Perfection on a plate!", True),
    (14, "Liam", "Chocolate Lava Cake was rich and gooey.", False),

    # Wrap World
    (15, "you", "Falafel wrap was fresh, hummus was flavorful.", False),
    (15, "Ravi", "Worst wrap imaginable. Soggy bread and bland filling.", True),
    (15, "Elena", "Chicken shawarma wrap was juicy and well spiced.", False),

    # Salad Station
    (16, "you", "Greek salad was fresh, feta was tangy and creamy.", False),
    (16, "Jess", "This salad was so bad I lost faith in vegetables.", True),
    (16, "Omar", "Caesar salad dressing was creamy, croutons crunchy.", False),

    # Kebab Kingdom
    (17, "you", "Paneer tikka was smoky, kebabs were tender.", False),
    (17, "Imran", "Best kebabs in the world! I’d travel across continents for them!", True),
    (17, "Sara", "Mutton kebabs had deep flavor, chicken seekh was juicy.", False),

    # Dumpling Den
    (18, "you", "Chicken dumplings had thin wrappers, filling was juicy.", False),
    (18, "Wei", "Worst dumplings in existence. Doughy and tasteless.", True),
    (18, "Ling", "Pork dumplings were flavorful and well steamed.", False),
]
for rv in reviews:
    execute_query(
        "INSERT INTO reviews (restaurant_id, user_name, review_text, fraud) VALUES (?, ?, ?, ?)",
        rv
    )

# -------------------------
# PAST ORDERS for "you"
# -------------------------
past_orders = [
    ( "you", 1, 1 ),  # Margherita Pizza
    ( "you", 2, 4 ),  # Chicken Tikka Masala
    ( "you", 3, 6 ),  # Salmon Sashimi
    ( "you", 4, 7 ),  # Cheeseburger
    ( "you", 5, 9 ),  # Spaghetti Carbonara
    ( "you", 6, 12 ), # Veggie Taco
    ( "you", 7, 14 ), # Grilled Chicken Wings
    ( "you", 8, 16 ), # Caesar Salad
    ( "you", 9, 18 ), # Veg Momos
]
for po in past_orders:
    execute_query(
        "INSERT INTO past_orders (user_name, restaurant_id, menu_item_id) VALUES (?, ?, ?)",
        po
    )

print("Database seeded with 18 restaurants, reviews, and past orders for 'you'.")

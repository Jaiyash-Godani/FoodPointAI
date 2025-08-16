import streamlit as st
from search import search_menu
from recommend import get_recommendations
from reviews import get_reviews_for_restaurant
from database import fetch_all

st.set_page_config(page_title="PizzaPoint", layout="wide")

st.title("🍽️ Pizzaoint Powered by AI")

# -------------------------
# SEARCH BAR
# -------------------------
search_query = st.text_input("🔍 Search for food or restaurants:")

if search_query:
    results = search_menu(search_query)
    if results:
        st.subheader("Search Results")
        for id,rest_name,name, price in results:
            st.write(f"**{name}** - ₹{price} _(at {rest_name})_")
    else:
        st.write("No results found.")


@st.cache_resource
def load_recommendations():
    return get_recommendations()

st.subheader("✨ Personalized Recommendations")
recs = load_recommendations()
for i,rest_name,name, price in recs:
    st.write(f"**{name}** - ₹{price} _(at {rest_name})_")


st.subheader("📝 Reviews & Menu")
restaurants = fetch_all("SELECT id, name FROM restaurants")
selected_restaurant = st.selectbox("Select a restaurant:", restaurants, format_func=lambda x: x[1])
@st.cache_resource
def m(selected_restaurant):
    rest_id = selected_restaurant[0]
    rest_name = selected_restaurant[1]

    # Show menu items for this restaurant
    st.markdown(f"### 📜 Menu for {rest_name}")
    menu_items = fetch_all(
        "SELECT name, price FROM menu_items WHERE restaurant_id = ?", 
        (rest_id,)
    )
    if menu_items:
        for item_name, price in menu_items:
            st.write(f"**{item_name}** - ₹{price}")
    else:
        st.write("No menu items found for this restaurant.")

    # Show reviews for this restaurant
    st.markdown(f"### 💬 Reviews for {rest_name}")
    reviews = get_reviews_for_restaurant(rest_id)
    for user, text, fraud,fraudnew in reviews:
        fraud_label = "⚠️ Fraud" if fraud else "✅ Verified"
        fraudnew_label = "⚠️ Fraud" if fraudnew else "✅ Verified"
        st.write(f"**{user}** ({fraudnew_label}): {text}")


if selected_restaurant:
   m(selected_restaurant)
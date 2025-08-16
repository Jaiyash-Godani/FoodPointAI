from database import fetch_all
from Chains import Chain
cache={}
def fraud_detector(text):
    chain = Chain()
    if text in cache:
        return cache[text]
    result = chain.fraud_detection(text)
    cache[text] = result
    return result

def get_reviews_for_restaurant(restaurant_id):
    sql = """
    SELECT user_name, review_text, fraud
    FROM reviews
    WHERE restaurant_id = ?
    """
    reviews = fetch_all(sql, (restaurant_id,))
    revnew=[]
    for review in reviews:
        rev= fraud_detector(review[1])
        tup=(rev,)
        review=review.__add__(tup)
        revnew.append(review)
            
    return revnew

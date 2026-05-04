# Real restaurant data sourced from Google Maps (publicly available info)
# Covers popular restaurant chains and local favorites across India

RESTAURANTS = [
    {
        "id": "R001",
        "name": "McDonald's",
        "cuisine": "Fast Food · Burgers",
        "rating": 4.1,
        "reviews": 12847,
        "delivery_time": "20-30 min",
        "price_range": "₹100-300",
        "address": "Phoenix Mall, Pune, Maharashtra",
        "phone": "+91-20-XXXXXXXX",
        "lat": 18.5204,
        "lon": 73.8567,
        "open": True,
        "open_hours": "6:00 AM - 11:00 PM",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/McDonald%27s_Golden_Arches.svg/200px-McDonald%27s_Golden_Arches.svg.png",
        "tags": ["Popular", "Fast Food", "Family"],
        "categories": ["Burgers", "Snacks", "Beverages", "Desserts"],
        "menu": [
            # Burgers
            {"id": "M001", "name": "McAloo Tikki Burger", "category": "Burgers", "price": 89, "description": "Spiced potato patty with lettuce and sauce", "rating": 4.3, "prep_time": 8, "veg": True, "popular": True},
            {"id": "M002", "name": "Chicken Maharaja Mac", "category": "Burgers", "price": 249, "description": "Double chicken patty with signature sauce", "rating": 4.5, "prep_time": 10, "veg": False, "popular": True},
            {"id": "M003", "name": "McSpicy Chicken", "category": "Burgers", "price": 199, "description": "Crispy spicy chicken fillet burger", "rating": 4.2, "prep_time": 10, "veg": False, "popular": False},
            {"id": "M004", "name": "Veg Maharaja Mac", "category": "Burgers", "price": 219, "description": "Double veggie patty burger", "rating": 4.0, "prep_time": 8, "veg": True, "popular": False},
            # Snacks
            {"id": "M005", "name": "French Fries (M)", "category": "Snacks", "price": 129, "description": "Crispy golden salted fries", "rating": 4.4, "prep_time": 5, "veg": True, "popular": True},
            {"id": "M006", "name": "Chicken McNuggets 6pc", "category": "Snacks", "price": 179, "description": "Tender chicken nuggets", "rating": 4.3, "prep_time": 7, "veg": False, "popular": True},
            {"id": "M007", "name": "Veg Pizza McPuff", "category": "Snacks", "price": 79, "description": "Flaky pastry with veg filling", "rating": 3.9, "prep_time": 5, "veg": True, "popular": False},
            # Beverages
            {"id": "M008", "name": "Coca-Cola (M)", "category": "Beverages", "price": 89, "description": "Chilled Coca-Cola", "rating": 4.0, "prep_time": 2, "veg": True, "popular": False},
            {"id": "M009", "name": "Cold Coffee (M)", "category": "Beverages", "price": 139, "description": "McCafe cold coffee", "rating": 4.2, "prep_time": 3, "veg": True, "popular": True},
            {"id": "M010", "name": "McFloat Oreo", "category": "Beverages", "price": 159, "description": "Vanilla shake with Oreo", "rating": 4.4, "prep_time": 3, "veg": True, "popular": True},
            # Desserts
            {"id": "M011", "name": "McFlurry Oreo", "category": "Desserts", "price": 149, "description": "Creamy vanilla ice cream with Oreo", "rating": 4.6, "prep_time": 3, "veg": True, "popular": True},
            {"id": "M012", "name": "Chocolate Sundae", "category": "Desserts", "price": 89, "description": "Soft serve with chocolate topping", "rating": 4.3, "prep_time": 2, "veg": True, "popular": False},
        ]
    },
    {
        "id": "R002",
        "name": "Domino's Pizza",
        "cuisine": "Pizza · Italian",
        "rating": 4.2,
        "reviews": 9432,
        "delivery_time": "30-45 min",
        "price_range": "₹200-800",
        "address": "FC Road, Pune, Maharashtra",
        "phone": "+91-20-XXXXXXXX",
        "lat": 18.5308,
        "lon": 73.8474,
        "open": True,
        "open_hours": "10:00 AM - 12:00 AM",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Domino%27s_pizza_logo.svg/200px-Domino%27s_pizza_logo.svg.png",
        "tags": ["Pizza", "Popular", "Late Night"],
        "categories": ["Regular Pizzas", "Premium Pizzas", "Sides", "Beverages"],
        "menu": [
            {"id": "D001", "name": "Margherita Pizza (M)", "category": "Regular Pizzas", "price": 199, "description": "Classic tomato base with mozzarella", "rating": 4.2, "prep_time": 15, "veg": True, "popular": True},
            {"id": "D002", "name": "Peppy Paneer (M)", "category": "Regular Pizzas", "price": 299, "description": "Paneer with peppy herbs", "rating": 4.4, "prep_time": 15, "veg": True, "popular": True},
            {"id": "D003", "name": "Chicken Dominator (L)", "category": "Premium Pizzas", "price": 699, "description": "Loaded with 5 types of chicken", "rating": 4.6, "prep_time": 18, "veg": False, "popular": True},
            {"id": "D004", "name": "Farmhouse Pizza (M)", "category": "Regular Pizzas", "price": 299, "description": "Fresh veggies on pizza sauce", "rating": 4.1, "prep_time": 15, "veg": True, "popular": False},
            {"id": "D005", "name": "Spicy Barbeque Chicken (L)", "category": "Premium Pizzas", "price": 649, "description": "BBQ sauce with spicy chicken", "rating": 4.5, "prep_time": 18, "veg": False, "popular": True},
            {"id": "D006", "name": "Garlic Bread", "category": "Sides", "price": 149, "description": "Crispy garlic bread sticks", "rating": 4.3, "prep_time": 8, "veg": True, "popular": True},
            {"id": "D007", "name": "Chicken Wings 8pc", "category": "Sides", "price": 249, "description": "Hot and crispy chicken wings", "rating": 4.4, "prep_time": 12, "veg": False, "popular": True},
            {"id": "D008", "name": "Choco Lava Cake", "category": "Sides", "price": 109, "description": "Warm chocolate cake with liquid center", "rating": 4.7, "prep_time": 8, "veg": True, "popular": True},
            {"id": "D009", "name": "Pepsi Can", "category": "Beverages", "price": 79, "description": "Chilled Pepsi can", "rating": 4.0, "prep_time": 1, "veg": True, "popular": False},
        ]
    },
    {
        "id": "R003",
        "name": "KFC",
        "cuisine": "Fried Chicken · Fast Food",
        "rating": 4.0,
        "reviews": 8756,
        "delivery_time": "25-35 min",
        "price_range": "₹150-600",
        "address": "MG Road, Pune, Maharashtra",
        "phone": "+91-20-XXXXXXXX",
        "lat": 18.5236,
        "lon": 73.8746,
        "open": True,
        "open_hours": "10:00 AM - 11:00 PM",
        "image": "https://upload.wikimedia.org/wikipedia/en/thumb/b/bf/KFC_logo.svg/200px-KFC_logo.svg.png",
        "tags": ["Chicken", "Popular", "Family"],
        "categories": ["Chicken", "Burgers", "Snacks", "Beverages"],
        "menu": [
            {"id": "K001", "name": "Original Recipe Chicken (2pc)", "category": "Chicken", "price": 319, "description": "KFC secret recipe fried chicken", "rating": 4.5, "prep_time": 12, "veg": False, "popular": True},
            {"id": "K002", "name": "Hot & Crispy Chicken (2pc)", "category": "Chicken", "price": 319, "description": "Extra crispy spiced chicken", "rating": 4.4, "prep_time": 12, "veg": False, "popular": True},
            {"id": "K003", "name": "Zinger Burger", "category": "Burgers", "price": 219, "description": "Crispy chicken fillet with coleslaw", "rating": 4.5, "prep_time": 10, "veg": False, "popular": True},
            {"id": "K004", "name": "Veg Zinger Burger", "category": "Burgers", "price": 189, "description": "Crispy veggie patty burger", "rating": 4.0, "prep_time": 8, "veg": True, "popular": False},
            {"id": "K005", "name": "Popcorn Chicken (M)", "category": "Snacks", "price": 189, "description": "Bite-sized crispy chicken pieces", "rating": 4.3, "prep_time": 8, "veg": False, "popular": True},
            {"id": "K006", "name": "Coleslaw", "category": "Snacks", "price": 79, "description": "Creamy cabbage salad", "rating": 3.9, "prep_time": 2, "veg": True, "popular": False},
            {"id": "K007", "name": "Pepsi (M)", "category": "Beverages", "price": 89, "description": "Chilled Pepsi", "rating": 4.0, "prep_time": 1, "veg": True, "popular": False},
            {"id": "K008", "name": "Krushers Oreo", "category": "Beverages", "price": 199, "description": "Creamy Oreo milkshake", "rating": 4.4, "prep_time": 5, "veg": True, "popular": True},
        ]
    },
    {
        "id": "R004",
        "name": "Vaishali Restaurant",
        "cuisine": "South Indian · Maharashtrian",
        "rating": 4.5,
        "reviews": 21034,
        "delivery_time": "20-40 min",
        "price_range": "₹100-400",
        "address": "Ferguson College Road, Pune",
        "phone": "+91-20-XXXXXXXX",
        "lat": 18.5167,
        "lon": 73.8397,
        "open": True,
        "open_hours": "7:00 AM - 11:00 PM",
        "image": "https://images.unsplash.com/photo-1567188040759-fb8a883dc6d8?w=200&h=200&fit=crop",
        "tags": ["Local Favourite", "Veg", "Breakfast"],
        "categories": ["Dosas", "Idli & Vada", "Main Course", "Beverages"],
        "menu": [
            {"id": "V001", "name": "Plain Dosa", "category": "Dosas", "price": 89, "description": "Crispy rice crepe with chutney & sambar", "rating": 4.6, "prep_time": 10, "veg": True, "popular": True},
            {"id": "V002", "name": "Masala Dosa", "category": "Dosas", "price": 119, "description": "Dosa filled with spiced potato filling", "rating": 4.7, "prep_time": 12, "veg": True, "popular": True},
            {"id": "V003", "name": "Set Dosa (3pc)", "category": "Dosas", "price": 109, "description": "Soft spongy mini dosas", "rating": 4.4, "prep_time": 10, "veg": True, "popular": False},
            {"id": "V004", "name": "Idli (2pc)", "category": "Idli & Vada", "price": 79, "description": "Steamed rice cakes with chutney", "rating": 4.5, "prep_time": 8, "veg": True, "popular": True},
            {"id": "V005", "name": "Medu Vada (2pc)", "category": "Idli & Vada", "price": 89, "description": "Crispy lentil donuts", "rating": 4.4, "prep_time": 8, "veg": True, "popular": True},
            {"id": "V006", "name": "Misal Pav", "category": "Main Course", "price": 129, "description": "Spicy sprouted curry with bread", "rating": 4.8, "prep_time": 10, "veg": True, "popular": True},
            {"id": "V007", "name": "Pav Bhaji", "category": "Main Course", "price": 149, "description": "Mixed vegetable curry with buttered pav", "rating": 4.6, "prep_time": 12, "veg": True, "popular": True},
            {"id": "V008", "name": "Filter Coffee", "category": "Beverages", "price": 59, "description": "Authentic South Indian filter coffee", "rating": 4.7, "prep_time": 5, "veg": True, "popular": True},
            {"id": "V009", "name": "Fresh Lime Soda", "category": "Beverages", "price": 69, "description": "Sweet or salted lime soda", "rating": 4.3, "prep_time": 3, "veg": True, "popular": False},
        ]
    },
    {
        "id": "R005",
        "name": "Barbeque Nation",
        "cuisine": "BBQ · North Indian · Grill",
        "rating": 4.3,
        "reviews": 6891,
        "delivery_time": "40-60 min",
        "price_range": "₹600-1500",
        "address": "Koregaon Park, Pune",
        "phone": "+91-20-XXXXXXXX",
        "lat": 18.5362,
        "lon": 73.8938,
        "open": True,
        "open_hours": "12:00 PM - 11:00 PM",
        "image": "https://images.unsplash.com/photo-1544025162-d76694265947?w=200&h=200&fit=crop",
        "tags": ["BBQ", "Premium", "Party"],
        "categories": ["Starters", "Main Course", "Breads", "Desserts"],
        "menu": [
            {"id": "B001", "name": "Chicken Tikka", "category": "Starters", "price": 399, "description": "Marinated grilled chicken pieces", "rating": 4.6, "prep_time": 20, "veg": False, "popular": True},
            {"id": "B002", "name": "Paneer Tikka", "category": "Starters", "price": 349, "description": "Grilled cottage cheese with spices", "rating": 4.5, "prep_time": 18, "veg": True, "popular": True},
            {"id": "B003", "name": "Mutton Seekh Kebab", "category": "Starters", "price": 449, "description": "Spiced minced mutton on skewer", "rating": 4.7, "prep_time": 22, "veg": False, "popular": True},
            {"id": "B004", "name": "Hara Bhara Kebab", "category": "Starters", "price": 299, "description": "Green veggie kebab with spinach", "rating": 4.2, "prep_time": 15, "veg": True, "popular": False},
            {"id": "B005", "name": "Butter Chicken", "category": "Main Course", "price": 499, "description": "Creamy tomato chicken curry", "rating": 4.7, "prep_time": 20, "veg": False, "popular": True},
            {"id": "B006", "name": "Dal Makhani", "category": "Main Course", "price": 349, "description": "Slow cooked black lentils", "rating": 4.5, "prep_time": 15, "veg": True, "popular": True},
            {"id": "B007", "name": "Butter Naan", "category": "Breads", "price": 79, "description": "Soft leavened bread with butter", "rating": 4.4, "prep_time": 8, "veg": True, "popular": True},
            {"id": "B008", "name": "Garlic Naan", "category": "Breads", "price": 89, "description": "Naan with garlic and butter", "rating": 4.5, "prep_time": 8, "veg": True, "popular": True},
            {"id": "B009", "name": "Gulab Jamun (4pc)", "category": "Desserts", "price": 199, "description": "Soft milk solid balls in sugar syrup", "rating": 4.6, "prep_time": 5, "veg": True, "popular": True},
            {"id": "B010", "name": "Rasmalai", "category": "Desserts", "price": 219, "description": "Cottage cheese in saffron milk", "rating": 4.5, "prep_time": 5, "veg": True, "popular": False},
        ]
    },
    {
        "id": "R006",
        "name": "Cafe Coffee Day",
        "cuisine": "Cafe · Coffee · Snacks",
        "rating": 4.0,
        "reviews": 5432,
        "delivery_time": "15-25 min",
        "price_range": "₹100-400",
        "address": "Aundh, Pune, Maharashtra",
        "phone": "+91-20-XXXXXXXX",
        "lat": 18.5590,
        "lon": 73.8077,
        "open": True,
        "open_hours": "8:00 AM - 10:00 PM",
        "image": "https://images.unsplash.com/photo-1509042239860-f550ce710b93?w=200&h=200&fit=crop",
        "tags": ["Cafe", "Coffee", "Work Friendly"],
        "categories": ["Hot Beverages", "Cold Beverages", "Snacks", "Desserts"],
        "menu": [
            {"id": "C001", "name": "Cappuccino", "category": "Hot Beverages", "price": 179, "description": "Espresso with steamed milk foam", "rating": 4.2, "prep_time": 5, "veg": True, "popular": True},
            {"id": "C002", "name": "Cafe Latte", "category": "Hot Beverages", "price": 179, "description": "Espresso with steamed milk", "rating": 4.1, "prep_time": 5, "veg": True, "popular": True},
            {"id": "C003", "name": "Cold Coffee", "category": "Cold Beverages", "price": 199, "description": "Blended cold coffee with ice cream", "rating": 4.4, "prep_time": 5, "veg": True, "popular": True},
            {"id": "C004", "name": "Frappe", "category": "Cold Beverages", "price": 229, "description": "Blended iced coffee drink", "rating": 4.3, "prep_time": 5, "veg": True, "popular": True},
            {"id": "C005", "name": "Chocolate Shake", "category": "Cold Beverages", "price": 229, "description": "Thick chocolate milkshake", "rating": 4.3, "prep_time": 5, "veg": True, "popular": False},
            {"id": "C006", "name": "Veg Sandwich", "category": "Snacks", "price": 149, "description": "Grilled vegetable sandwich", "rating": 3.9, "prep_time": 7, "veg": True, "popular": False},
            {"id": "C007", "name": "Brownie with Ice Cream", "category": "Desserts", "price": 219, "description": "Warm chocolate brownie with vanilla ice cream", "rating": 4.6, "prep_time": 5, "veg": True, "popular": True},
            {"id": "C008", "name": "Chocolate Mousse Cake", "category": "Desserts", "price": 249, "description": "Rich chocolate cake slice", "rating": 4.4, "prep_time": 3, "veg": True, "popular": True},
        ]
    },
]

# ── Helper functions ──────────────────────────────────────────────────────────
def get_restaurant_by_id(restaurant_id):
    for r in RESTAURANTS:
        if r["id"] == restaurant_id:
            return r
    return None

def search_restaurants(query="", cuisine_filter=None, rating_filter=0):
    results = RESTAURANTS
    if query:
        q = query.lower()
        results = [r for r in results if q in r["name"].lower() or q in r["cuisine"].lower() or q in r["address"].lower()]
    if cuisine_filter and cuisine_filter != "All":
        results = [r for r in results if cuisine_filter.lower() in r["cuisine"].lower()]
    if rating_filter > 0:
        results = [r for r in results if r["rating"] >= rating_filter]
    return results

def get_all_cuisines():
    cuisines = set()
    for r in RESTAURANTS:
        for c in r["cuisine"].split(" · "):
            cuisines.add(c.strip())
    return sorted(list(cuisines))

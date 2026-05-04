# 🍽️ Smart Restaurant Ordering System

A Streamlit-based smart pre-order system using real restaurant data from Google Maps.

## ✨ Features

- 🗺️ **Find Restaurants** — Real restaurants from Pune with Google Maps data (ratings, reviews, location)
- 📋 **Digital Menu** — Browse by category, filter veg/non-veg, see prep times
- 🛒 **Smart Cart** — Add items, adjust quantity, see live total
- 📦 **Smart Pre-Order** — Cooking starts ONLY when you arrive
- 📍 **I am Near** — Tap when you arrive → countdown timer starts
- 👨‍🍳 **Kitchen Dashboard** — Real-time order management for staff
- 📊 **Admin Panel** — Analytics, menu management, restaurant overview

## 🚀 Deploy on Streamlit Cloud (Step by Step)

### Step 1 — Push to GitHub

```bash
# 1. Create a new repo on github.com (name it: smart-restaurant)
# 2. Then run these commands in your terminal:

git init
git add .
git commit -m "Smart Restaurant Ordering System"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/smart-restaurant.git
git push -u origin main
```

### Step 2 — Deploy on Streamlit

1. Go to **https://share.streamlit.io**
2. Sign in with GitHub
3. Click **"New app"**
4. Fill in:
   - **Repository:** `YOUR_USERNAME/smart-restaurant`
   - **Branch:** `main`
   - **Main file path:** `app.py`
5. Click **"Deploy!"**
6. Wait 2-3 minutes — your app is live! 🎉

---

## 💻 Run Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

Open http://localhost:8501 in your browser.

---

## 📁 Project Structure

```
smart-restaurant/
├── app.py                    # Main entry point
├── requirements.txt          # Python dependencies
├── .streamlit/
│   └── config.toml          # Theme & server config
├── pages/
│   ├── home.py              # Home / landing page
│   ├── find_restaurants.py  # Search & map view
│   ├── menu.py              # Digital menu with cart
│   ├── cart.py              # Cart & checkout
│   ├── orders.py            # Order tracking + timer
│   ├── kitchen.py           # Kitchen dashboard
│   └── admin.py             # Admin analytics panel
└── data/
    └── restaurants.py       # Restaurant & menu data
```

---

## 🏪 Restaurants Included (Google Maps Data)

| Restaurant | Cuisine | Rating | Location |
|---|---|---|---|
| McDonald's | Fast Food | 4.1 ⭐ | Phoenix Mall, Pune |
| Domino's Pizza | Pizza | 4.2 ⭐ | FC Road, Pune |
| KFC | Fried Chicken | 4.0 ⭐ | MG Road, Pune |
| Vaishali Restaurant | South Indian | 4.5 ⭐ | FC Road, Pune |
| Barbeque Nation | BBQ & Grill | 4.3 ⭐ | Koregaon Park, Pune |
| Cafe Coffee Day | Cafe | 4.0 ⭐ | Aundh, Pune |

---

## 🔄 Smart Pre-Order Flow

```
Customer browses menu on phone
        ↓
Adds items to cart & places order
        ↓
Status: "Waiting for Arrival"
        ↓
Customer walks to restaurant
        ↓
Taps "I am Near" button
        ↓
Countdown timer starts (based on prep time)
        ↓
Food ready exactly on arrival!
```

---

## 📝 Notes

- All data resets on app restart (no database — uses Streamlit session state)
- Restaurant data is based on publicly available Google Maps information
- To add a real database, integrate with Firebase or Supabase

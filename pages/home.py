import streamlit as st
from data.restaurants import RESTAURANTS

def show():
    # Hero Section
    st.markdown("""
    <div style="background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
                border-radius: 20px; padding: 48px 40px; margin-bottom: 32px; text-align: center;">
        <div style="font-size: 3rem; margin-bottom: 8px;">🍽️</div>
        <div style="font-size: 2.6rem; font-weight: 800; color: white; line-height: 1.2;">
            Smart Restaurant
        </div>
        <div style="font-size: 2.6rem; font-weight: 800; color: #FF6B35; line-height: 1.2;">
            Ordering System
        </div>
        <div style="color: #aaa; margin-top: 16px; font-size: 1.1rem;">
            Pre-order your food. Cooking starts only when you arrive.
        </div>
        <div style="margin-top: 24px;">
            <span style="background:#FF6B35; color:white; padding:6px 16px; border-radius:20px;
                         font-size:13px; font-weight:600; margin:4px;">
                No Waiting Time
            </span>
            <span style="background:#28A745; color:white; padding:6px 16px; border-radius:20px;
                         font-size:13px; font-weight:600; margin:4px;">
                Fresh Food
            </span>
            <span style="background:#4A90E2; color:white; padding:6px 16px; border-radius:20px;
                         font-size:13px; font-weight:600; margin:4px;">
                Real Restaurants
            </span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Stats Row
    col1, col2, col3, col4 = st.columns(4)
    stats = [
        ("🏪", str(len(RESTAURANTS)), "Restaurants"),
        ("🛒", str(len(st.session_state.cart)), "Cart Items"),
        ("📦", str(len(st.session_state.orders)), "Orders Placed"),
        ("⭐", "4.3", "Avg Rating"),
    ]
    for col, (icon, val, lbl) in zip([col1, col2, col3, col4], stats):
        with col:
            st.markdown(f"""
            <div class="metric-box">
                <div style="font-size:1.8rem;">{icon}</div>
                <div class="val">{val}</div>
                <div class="lbl">{lbl}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # How it works
    st.markdown("### 🚀 How It Works")
    c1, c2, c3, c4 = st.columns(4)
    steps = [
        ("1️⃣", "Find Restaurant", "Browse real restaurants near you powered by Google Maps data"),
        ("2️⃣", "Browse & Order", "Add items to cart — see prep time for each dish"),
        ("3️⃣", "Head Over", "Place your pre-order and start walking to the restaurant"),
        ("4️⃣", "Tap 'I am Near'", "Cooking starts when you arrive — fresh food guaranteed!"),
    ]
    for col, (num, title, desc) in zip([c1, c2, c3, c4], steps):
        with col:
            st.markdown(f"""
            <div class="card" style="text-align:center;">
                <div style="font-size:2rem;">{num}</div>
                <div style="font-weight:700; margin:8px 0; color:#1a1a2e;">{title}</div>
                <div style="font-size:13px; color:#666;">{desc}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Featured Restaurants
    st.markdown("### 🌟 Featured Restaurants")
    featured = sorted(RESTAURANTS, key=lambda x: x["rating"], reverse=True)[:3]

    cols = st.columns(3)
    for col, r in zip(cols, featured):
        with col:
            stars = "⭐" * int(r["rating"])
            tags_html = " ".join([f'<span style="background:#f0f0f0;padding:2px 8px;border-radius:10px;font-size:11px;">{t}</span>' for t in r["tags"][:2]])
            st.markdown(f"""
            <div class="card">
                <div style="font-size:1.4rem; font-weight:700; color:#1a1a2e;">{r['name']}</div>
                <div style="color:#666; font-size:13px; margin:4px 0;">{r['cuisine']}</div>
                <div style="margin:8px 0;">{stars} <span style="color:#888;font-size:12px;">({r['reviews']:,})</span></div>
                <div style="color:#FF6B35; font-weight:600;">🕒 {r['delivery_time']}</div>
                <div style="color:#666; font-size:12px; margin-top:4px;">📍 {r['address']}</div>
                <div style="margin-top:10px;">{tags_html}</div>
            </div>
            """, unsafe_allow_html=True)
            if st.button(f"Order from {r['name']}", key=f"home_order_{r['id']}", use_container_width=True):
                st.session_state.selected_restaurant = r
                st.session_state.page = "menu"
                st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    # Smart Pre-Order Explained
    st.markdown("### 💡 Smart Pre-Order Concept")
    st.markdown("""
    <div class="info-box">
        <strong>How is this different from regular ordering?</strong><br>
        Traditional restaurants start cooking when you arrive, making you wait 15-30 minutes.
        With Smart Pre-Order, you place your order while heading to the restaurant.
        The kitchen gets notified and cooking starts exactly when you arrive — fresh food, zero wait!
    </div>
    """, unsafe_allow_html=True)

    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("""
        <div class="card" style="border-left: 4px solid #DC3545;">
            <div style="font-weight:700; color:#DC3545; margin-bottom:8px;">❌ Traditional Way</div>
            <div style="font-size:14px; color:#555; line-height:1.8;">
            • Arrive at restaurant<br>
            • Wait for waiter<br>
            • Browse menu<br>
            • Place order<br>
            • Wait 20-30 min for food<br>
            • <b>Total wait: 35-45 min</b>
            </div>
        </div>
        """, unsafe_allow_html=True)
    with col_b:
        st.markdown("""
        <div class="card" style="border-left: 4px solid #28A745;">
            <div style="font-weight:700; color:#28A745; margin-bottom:8px;">✅ Smart Pre-Order</div>
            <div style="font-size:14px; color:#555; line-height:1.8;">
            • Browse menu on your phone<br>
            • Place order & start walking<br>
            • Tap "I am Near" on arrival<br>
            • Chef starts cooking NOW<br>
            • Food ready in minutes<br>
            • <b>Total wait: 5-10 min</b>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # CTA Buttons
    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1, 1, 1])
    with c1:
        if st.button("🗺️ Find Restaurants Near Me", use_container_width=True, type="primary"):
            st.session_state.page = "find"
            st.rerun()
    with c2:
        if st.button("📦 View My Orders", use_container_width=True):
            st.session_state.page = "orders"
            st.rerun()
    with c3:
        if st.button("👨‍🍳 Kitchen Dashboard", use_container_width=True):
            st.session_state.page = "kitchen"
            st.rerun()

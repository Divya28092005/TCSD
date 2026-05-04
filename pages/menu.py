import streamlit as st
from data.restaurants import RESTAURANTS

def show():
    st.markdown("## 📋 Menu")

    # Restaurant selector
    rest_names = {r["name"]: r for r in RESTAURANTS}
    current_name = st.session_state.selected_restaurant["name"] if st.session_state.selected_restaurant else None

    selected_name = st.selectbox(
        "🏪 Select Restaurant",
        list(rest_names.keys()),
        index=list(rest_names.keys()).index(current_name) if current_name in rest_names else 0
    )
    r = rest_names[selected_name]
    st.session_state.selected_restaurant = r

    # Restaurant header
    col_hdr, col_stats = st.columns([3, 1])
    with col_hdr:
        st.markdown(f"""
        <div style="padding:16px; background:linear-gradient(135deg,#1a1a2e,#16213e);
                    border-radius:12px; color:white; margin-bottom:16px;">
            <div style="font-size:1.5rem; font-weight:700;">{r['name']}</div>
            <div style="color:#aaa; font-size:13px; margin-top:4px;">{r['cuisine']} · {r['address']}</div>
            <div style="margin-top:8px;">
                ⭐ {r['rating']} ({r['reviews']:,} reviews) &nbsp;|&nbsp;
                🕒 Prep: ~{min([m['prep_time'] for m in r['menu']])}-{max([m['prep_time'] for m in r['menu']])} min
            </div>
        </div>
        """, unsafe_allow_html=True)
    with col_stats:
        cart_items = [c for c in st.session_state.cart if c.get("restaurant_id") == r["id"]]
        cart_total = sum(c["price"] * c["qty"] for c in cart_items)
        st.markdown(f"""
        <div class="metric-box" style="margin-top:0;">
            <div style="font-size:1.4rem;">🛒</div>
            <div class="val">₹{cart_total}</div>
            <div class="lbl">{len(cart_items)} items in cart</div>
        </div>
        """, unsafe_allow_html=True)

    # Filters row
    col_f1, col_f2, col_f3 = st.columns([2, 1, 1])
    with col_f1:
        menu_search = st.text_input("🔍 Search menu items...", key="menu_search", placeholder="e.g. burger, coffee...")
    with col_f2:
        veg_only = st.checkbox("🟢 Veg Only")
    with col_f3:
        popular_only = st.checkbox("🔥 Popular Only")

    # Smart Pre-Order info
    st.markdown("""
    <div class="info-box">
        <b>Smart Pre-Order:</b> Place your order now. Cooking starts only when you tap "I am Near" on arrival.
        Each item shows its prep time so you know exactly how long it takes.
    </div>
    """, unsafe_allow_html=True)

    # Category tabs
    categories = r["categories"]
    tabs = st.tabs(["🍽️ All"] + categories)

    def render_items(items):
        if not items:
            st.info("No items match your filter.")
            return

        for item in items:
            # Apply search filter
            if menu_search and menu_search.lower() not in item["name"].lower() and menu_search.lower() not in item["description"].lower():
                continue
            if veg_only and not item["veg"]:
                continue
            if popular_only and not item.get("popular", False):
                continue

            col_item, col_action = st.columns([5, 2])
            with col_item:
                veg_icon = "🟢" if item["veg"] else "🔴"
                popular_badge = ' <span style="background:#FF6B35;color:white;padding:1px 8px;border-radius:10px;font-size:11px;">Popular</span>' if item.get("popular") else ""
                st.markdown(f"""
                <div class="menu-card">
                    <div style="display:flex; justify-content:space-between; align-items:flex-start;">
                        <div style="flex:1;">
                            <div style="font-weight:700; color:#1a1a2e; font-size:15px;">
                                {veg_icon} {item['name']}{popular_badge}
                            </div>
                            <div style="color:#666; font-size:13px; margin:4px 0;">{item['description']}</div>
                            <div style="display:flex; gap:16px; margin-top:6px; font-size:13px;">
                                <span style="color:#FF6B35; font-weight:700;">₹{item['price']}</span>
                                <span style="color:#888;">⏱️ {item['prep_time']} min prep</span>
                                <span style="color:#888;">⭐ {item['rating']}</span>
                            </div>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

            with col_action:
                # Check if already in cart
                cart_item = next((c for c in st.session_state.cart
                                  if c["id"] == item["id"] and c["restaurant_id"] == r["id"]), None)
                if cart_item:
                    st.markdown(f"<div style='text-align:center;padding:4px;font-weight:700;color:#28A745;'>In Cart: {cart_item['qty']}</div>", unsafe_allow_html=True)
                    c1, c2, c3 = st.columns(3)
                    with c1:
                        if st.button("−", key=f"dec_{item['id']}"):
                            if cart_item["qty"] > 1:
                                cart_item["qty"] -= 1
                            else:
                                st.session_state.cart.remove(cart_item)
                            st.rerun()
                    with c2:
                        st.markdown(f"<div style='text-align:center;font-weight:700;'>{cart_item['qty']}</div>", unsafe_allow_html=True)
                    with c3:
                        if st.button("＋", key=f"inc_{item['id']}"):
                            cart_item["qty"] += 1
                            st.rerun()
                else:
                    st.markdown("<br>", unsafe_allow_html=True)
                    if st.button("Add +", key=f"add_{item['id']}", use_container_width=True):
                        # Warn if adding from different restaurant
                        other_rest = [c for c in st.session_state.cart if c.get("restaurant_id") != r["id"]]
                        if other_rest:
                            st.warning("Cart cleared — you can only order from one restaurant at a time.")
                            st.session_state.cart = []
                        st.session_state.cart.append({
                            "id": item["id"],
                            "name": item["name"],
                            "price": item["price"],
                            "qty": 1,
                            "prep_time": item["prep_time"],
                            "veg": item["veg"],
                            "restaurant_id": r["id"],
                            "restaurant_name": r["name"],
                        })
                        st.rerun()

    all_items = r["menu"]
    with tabs[0]:
        render_items(all_items)

    for i, cat in enumerate(categories):
        with tabs[i + 1]:
            cat_items = [m for m in all_items if m["category"] == cat]
            render_items(cat_items)

    # Go to cart
    if st.session_state.cart:
        st.markdown("---")
        total = sum(c["price"] * c["qty"] for c in st.session_state.cart)
        col_go, col_clear = st.columns([3, 1])
        with col_go:
            if st.button(f"🛒 Go to Cart — ₹{total}", use_container_width=True, type="primary"):
                st.session_state.page = "cart"
                st.rerun()
        with col_clear:
            if st.button("🗑️ Clear Cart", use_container_width=True):
                st.session_state.cart = []
                st.rerun()

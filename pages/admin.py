import streamlit as st
from data.restaurants import RESTAURANTS
import random

def show():
    st.markdown("## 📊 Admin Panel")

    tab1, tab2, tab3 = st.tabs(["📈 Analytics", "🍽️ Menu Management", "🏪 Restaurants"])

    # ── Tab 1: Analytics ──────────────────────────────────────────────────────
    with tab1:
        st.markdown("### Sales Analytics")

        orders = st.session_state.orders

        if not orders:
            # Show demo analytics when no real orders
            st.info("No orders yet. Showing demo analytics data.")
            demo_revenue = [random.randint(2000, 8000) for _ in range(7)]
            demo_days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

            import pandas as pd
            df = pd.DataFrame({"Day": demo_days, "Revenue (₹)": demo_revenue})
            st.bar_chart(df.set_index("Day"))

            # Demo popular items
            st.markdown("### 🔥 Popular Items (Demo)")
            demo_items = [
                ("McFlurry Oreo", 47, "McDonald's"),
                ("Chicken Tikka", 39, "Barbeque Nation"),
                ("Masala Dosa", 35, "Vaishali Restaurant"),
                ("Chicken Dominator", 31, "Domino's Pizza"),
                ("Zinger Burger", 28, "KFC"),
            ]
            for i, (name, count, rest) in enumerate(demo_items, 1):
                bar_width = int((count / 47) * 100)
                st.markdown(f"""
                <div style="margin-bottom:10px;">
                    <div style="display:flex; justify-content:space-between; margin-bottom:3px;">
                        <span><b>{i}. {name}</b> <span style="color:#888;font-size:12px;">({rest})</span></span>
                        <span style="font-weight:700; color:#FF6B35;">{count} orders</span>
                    </div>
                    <div style="background:#f0f0f0; border-radius:4px; height:8px;">
                        <div style="background:#FF6B35; width:{bar_width}%; height:8px; border-radius:4px;"></div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        else:
            # Real analytics from orders
            total_revenue = sum(o["total"] for o in orders)
            total_orders = len(orders)
            avg_order = round(total_revenue / total_orders) if total_orders else 0
            served_count = len([o for o in orders if o["status"] == "Served"])

            c1, c2, c3, c4 = st.columns(4)
            metrics = [
                ("💰", f"₹{total_revenue}", "Total Revenue"),
                ("📦", str(total_orders), "Total Orders"),
                ("💳", f"₹{avg_order}", "Avg Order Value"),
                ("✅", str(served_count), "Served Orders"),
            ]
            for col, (icon, val, lbl) in zip([c1, c2, c3, c4], metrics):
                with col:
                    st.markdown(f"""
                    <div class="metric-box">
                        <div style="font-size:1.6rem;">{icon}</div>
                        <div class="val">{val}</div>
                        <div class="lbl">{lbl}</div>
                    </div>
                    """, unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)

            # Revenue by restaurant
            rest_revenue = {}
            for o in orders:
                rn = o["restaurant_name"]
                rest_revenue[rn] = rest_revenue.get(rn, 0) + o["total"]

            if rest_revenue:
                import pandas as pd
                st.markdown("### Revenue by Restaurant")
                df = pd.DataFrame(list(rest_revenue.items()), columns=["Restaurant", "Revenue (₹)"])
                st.bar_chart(df.set_index("Restaurant"))

            # Popular items
            item_count = {}
            for o in orders:
                for item in o["items"]:
                    key = item["name"]
                    item_count[key] = item_count.get(key, 0) + item["qty"]

            if item_count:
                st.markdown("### Most Ordered Items")
                sorted_items = sorted(item_count.items(), key=lambda x: x[1], reverse=True)[:5]
                max_count = sorted_items[0][1] if sorted_items else 1
                for name, count in sorted_items:
                    bar_width = int((count / max_count) * 100)
                    st.markdown(f"""
                    <div style="margin-bottom:10px;">
                        <div style="display:flex; justify-content:space-between; margin-bottom:3px;">
                            <span><b>{name}</b></span>
                            <span style="font-weight:700; color:#FF6B35;">{count} ordered</span>
                        </div>
                        <div style="background:#f0f0f0; border-radius:4px; height:8px;">
                            <div style="background:#FF6B35; width:{bar_width}%; height:8px; border-radius:4px;"></div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

    # ── Tab 2: Menu Management ────────────────────────────────────────────────
    with tab2:
        st.markdown("### Menu Management")

        selected_rest = st.selectbox("Select Restaurant", [r["name"] for r in RESTAURANTS], key="admin_rest")
        restaurant = next(r for r in RESTAURANTS if r["name"] == selected_rest)

        st.markdown(f"**{len(restaurant['menu'])} items in menu**")

        # Filter
        cat_filter = st.selectbox("Filter by Category", ["All"] + restaurant["categories"], key="admin_cat")
        items = restaurant["menu"] if cat_filter == "All" else [m for m in restaurant["menu"] if m["category"] == cat_filter]

        # Display items in a table-like format
        for item in items:
            col1, col2, col3, col4, col5 = st.columns([3, 1, 1, 1, 1])
            with col1:
                veg = "🟢" if item["veg"] else "🔴"
                st.markdown(f"**{veg} {item['name']}**  \n*{item['description']}*")
            with col2:
                st.markdown(f"**₹{item['price']}**")
            with col3:
                st.markdown(f"⏱️ {item['prep_time']}m")
            with col4:
                st.markdown(f"⭐ {item['rating']}")
            with col5:
                if item.get("popular"):
                    st.markdown('<span style="background:#FF6B35;color:white;padding:2px 8px;border-radius:10px;font-size:11px;">Popular</span>', unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("### ➕ Add New Menu Item (Demo)")
        with st.form("add_item_form"):
            c1, c2 = st.columns(2)
            with c1:
                new_name = st.text_input("Item Name")
                new_price = st.number_input("Price (₹)", min_value=10, value=199)
                new_prep = st.number_input("Prep Time (min)", min_value=1, value=10)
            with c2:
                new_desc = st.text_area("Description", height=80)
                new_cat = st.selectbox("Category", restaurant["categories"])
                new_veg = st.checkbox("Vegetarian")

            submitted = st.form_submit_button("Add Item", type="primary")
            if submitted:
                if new_name:
                    st.success(f"'{new_name}' added to {selected_rest} menu! (Demo — resets on refresh)")
                else:
                    st.error("Please enter item name.")

    # ── Tab 3: Restaurants ─────────────────────────────────────────────────────
    with tab3:
        st.markdown("### Restaurant Overview")
        for r in RESTAURANTS:
            total_items = len(r["menu"])
            veg_items = len([m for m in r["menu"] if m["veg"]])
            avg_prep = round(sum(m["prep_time"] for m in r["menu"]) / total_items)
            rest_orders = [o for o in st.session_state.orders if o["restaurant_id"] == r["id"]]

            st.markdown(f"""
            <div class="card">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <div>
                        <span style="font-size:1.1rem; font-weight:700;">{r['name']}</span>
                        <span style="color:#888; font-size:13px; margin-left:8px;">{r['cuisine']}</span>
                    </div>
                    <span style="color:#FF6B35; font-weight:700;">⭐ {r['rating']}</span>
                </div>
                <div style="display:flex; gap:20px; margin-top:8px; font-size:13px; color:#555; flex-wrap:wrap;">
                    <span>📋 {total_items} menu items</span>
                    <span>🟢 {veg_items} veg</span>
                    <span>⏱️ Avg prep: {avg_prep} min</span>
                    <span>📦 {len(rest_orders)} orders received</span>
                    <span>💰 {r['price_range']}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

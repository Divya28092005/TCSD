import streamlit as st
from data.restaurants import RESTAURANTS, search_restaurants, get_all_cuisines

def show():
    st.markdown("## 🗺️ Find Restaurants")
    st.markdown("""
    <div class="info-box">
        Restaurant data sourced from Google Maps — real locations, ratings, and reviews from Pune, Maharashtra.
    </div>
    """, unsafe_allow_html=True)

    # Search & Filter
    col1, col2, col3 = st.columns([3, 2, 1])
    with col1:
        query = st.text_input("🔍 Search restaurants, cuisine, or area...", placeholder="e.g. Pizza, Pune, Veg...")
    with col2:
        cuisines = ["All"] + get_all_cuisines()
        cuisine_filter = st.selectbox("🍴 Cuisine", cuisines)
    with col3:
        rating_filter = st.selectbox("⭐ Min Rating", [0, 3.5, 4.0, 4.5], format_func=lambda x: "Any" if x == 0 else f"{x}+")

    results = search_restaurants(query, cuisine_filter if cuisine_filter != "All" else None, rating_filter)

    st.markdown(f"**{len(results)} restaurants found**")
    st.markdown("---")

    # Map using streamlit built-in map
    st.markdown("### 📍 Restaurant Map")
    import pandas as pd
    map_data = pd.DataFrame([{"lat": r["lat"], "lon": r["lon"], "name": r["name"]} for r in results])
    if not map_data.empty:
        st.map(map_data, zoom=12)
    st.markdown("---")

    # Restaurant Cards
    st.markdown("### 🏪 All Restaurants")
    for r in results:
        col_info, col_action = st.columns([4, 1])
        with col_info:
            open_badge = '<span class="badge-green">Open Now</span>' if r["open"] else '<span class="badge-red">Closed</span>'
            tags_html = " ".join([f'<span style="background:#f0f0f0;padding:2px 8px;border-radius:10px;font-size:11px;color:#555;">{t}</span>' for t in r["tags"]])
            st.markdown(f"""
            <div class="card">
                <div style="display:flex; justify-content:space-between; align-items:flex-start;">
                    <div>
                        <div style="font-size:1.3rem; font-weight:700; color:#1a1a2e;">{r['name']}</div>
                        <div style="color:#666; font-size:13px; margin:2px 0;">{r['cuisine']}</div>
                    </div>
                    <div>{open_badge}</div>
                </div>
                <div style="margin:10px 0; display:flex; gap:20px; flex-wrap:wrap;">
                    <span>⭐ <b>{r['rating']}</b> <span style="color:#888;font-size:12px;">({r['reviews']:,} reviews)</span></span>
                    <span>🕒 {r['delivery_time']}</span>
                    <span>💰 {r['price_range']}</span>
                    <span>🕐 {r['open_hours']}</span>
                </div>
                <div style="color:#666; font-size:13px;">📍 {r['address']}</div>
                <div style="margin-top:10px;">{tags_html}</div>
                <div style="margin-top:10px; color:#666; font-size:12px;">
                    Menu categories: {' · '.join(r['categories'])}
                </div>
            </div>
            """, unsafe_allow_html=True)
        with col_action:
            st.markdown("<br><br><br>", unsafe_allow_html=True)
            if st.button("View Menu", key=f"find_menu_{r['id']}", use_container_width=True, type="primary"):
                st.session_state.selected_restaurant = r
                st.session_state.page = "menu"
                st.rerun()
            if st.button("Details", key=f"find_details_{r['id']}", use_container_width=True):
                st.session_state[f"show_details_{r['id']}"] = not st.session_state.get(f"show_details_{r['id']}", False)
                st.rerun()

        # Expandable details
        if st.session_state.get(f"show_details_{r['id']}", False):
            with st.expander("Restaurant Details", expanded=True):
                dc1, dc2 = st.columns(2)
                with dc1:
                    st.markdown(f"**📞 Phone:** {r['phone']}")
                    st.markdown(f"**🕐 Hours:** {r['open_hours']}")
                    st.markdown(f"**💰 Price Range:** {r['price_range']}")
                with dc2:
                    st.markdown(f"**📍 Address:** {r['address']}")
                    st.markdown(f"**⭐ Rating:** {r['rating']}/5 ({r['reviews']:,} reviews)")
                    st.markdown(f"**🍴 Cuisine:** {r['cuisine']}")
                total_items = len(r['menu'])
                veg_items = len([m for m in r['menu'] if m['veg']])
                st.markdown(f"**Menu:** {total_items} items · {veg_items} veg · {total_items - veg_items} non-veg")

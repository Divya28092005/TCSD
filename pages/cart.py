import streamlit as st
import datetime

def show():
    st.markdown("## 🛒 Your Cart")

    if not st.session_state.cart:
        st.markdown("""
        <div class="card" style="text-align:center; padding:60px 20px;">
            <div style="font-size:4rem;">🛒</div>
            <div style="font-size:1.3rem; font-weight:700; color:#1a1a2e; margin:16px 0;">Cart is Empty</div>
            <div style="color:#888;">Browse our restaurants and add items to your cart</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🗺️ Find Restaurants", use_container_width=True, type="primary"):
            st.session_state.page = "find"
            st.rerun()
        return

    # Smart Pre-Order info
    st.markdown("""
    <div class="info-box">
        <b>Smart Pre-Order Active:</b> Your order will be placed and cooking starts only when you tap
        "I am Near" at the restaurant. No waiting!
    </div>
    """, unsafe_allow_html=True)

    rest_name = st.session_state.cart[0]["restaurant_name"]
    st.markdown(f"**Ordering from: 🏪 {rest_name}**")
    st.markdown("---")

    # Cart items
    subtotal = 0
    max_prep = 0

    for item in st.session_state.cart:
        item_total = item["price"] * item["qty"]
        subtotal += item_total
        max_prep = max(max_prep, item["prep_time"])

        col1, col2, col3, col4 = st.columns([4, 1, 1, 1])
        with col1:
            veg = "🟢" if item["veg"] else "🔴"
            st.markdown(f"""
            <div style="padding:8px 0;">
                <span style="font-weight:600;">{veg} {item['name']}</span>
                <span style="color:#888; font-size:12px; margin-left:8px;">⏱️ {item['prep_time']} min</span>
                <br><span style="color:#FF6B35; font-weight:700;">₹{item['price']}</span>
                <span style="color:#888; font-size:13px;"> × {item['qty']} = ₹{item_total}</span>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            if st.button("−", key=f"cart_dec_{item['id']}"):
                if item["qty"] > 1:
                    item["qty"] -= 1
                else:
                    st.session_state.cart.remove(item)
                st.rerun()
        with col3:
            st.markdown(f"<div style='text-align:center;font-weight:700;padding:8px 0;'>{item['qty']}</div>", unsafe_allow_html=True)
        with col4:
            if st.button("＋", key=f"cart_inc_{item['id']}"):
                item["qty"] += 1
                st.rerun()

    st.markdown("---")

    # Order summary
    delivery_fee = 0
    taxes = round(subtotal * 0.05)
    total = subtotal + taxes

    col_summary, col_order = st.columns([1, 1])

    with col_summary:
        st.markdown("### 📊 Order Summary")
        st.markdown(f"""
        <div class="card">
            <div style="display:flex;justify-content:space-between;margin-bottom:8px;">
                <span style="color:#666;">Subtotal</span><span>₹{subtotal}</span>
            </div>
            <div style="display:flex;justify-content:space-between;margin-bottom:8px;">
                <span style="color:#666;">GST (5%)</span><span>₹{taxes}</span>
            </div>
            <div style="display:flex;justify-content:space-between;margin-bottom:8px;">
                <span style="color:#666;">Delivery</span><span style="color:#28A745;">FREE</span>
            </div>
            <hr style="margin:8px 0;">
            <div style="display:flex;justify-content:space-between;font-weight:700;font-size:1.1rem;">
                <span>Total</span><span style="color:#FF6B35;">₹{total}</span>
            </div>
            <div style="margin-top:12px;color:#666;font-size:13px;">
                ⏱️ Est. prep time after arrival: <b>{max_prep} minutes</b>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col_order:
        st.markdown("### 📝 Delivery Details")
        room = st.text_input("🪑 Table / Room Number", placeholder="e.g. Table 5, Room 204...")
        name = st.text_input("👤 Your Name", placeholder="Your name...")
        phone = st.text_input("📞 Phone Number", placeholder="+91 XXXXXXXXXX")
        note = st.text_area("📝 Special Instructions (optional)", placeholder="No onions, extra spicy...", height=80)

    st.markdown("---")

    # Checkout
    col_btn, col_clear = st.columns([3, 1])
    with col_btn:
        if st.button(f"✅ Place Pre-Order — ₹{total}", use_container_width=True, type="primary"):
            if not room:
                st.error("Please enter your table/room number!")
            elif not name:
                st.error("Please enter your name!")
            else:
                # Create order
                st.session_state.order_counter += 1
                order_id = f"ORD{st.session_state.order_counter}"
                new_order = {
                    "id": order_id,
                    "restaurant_id": st.session_state.cart[0]["restaurant_id"],
                    "restaurant_name": rest_name,
                    "items": list(st.session_state.cart),
                    "subtotal": subtotal,
                    "taxes": taxes,
                    "total": total,
                    "room": room,
                    "customer_name": name,
                    "phone": phone,
                    "note": note,
                    "status": "Waiting",      # Smart Pre-Order: starts as Waiting
                    "placed_at": datetime.datetime.now().strftime("%I:%M %p"),
                    "cooking_started_at": None,
                    "prep_time": max_prep,
                    "is_near": False,
                }
                st.session_state.orders.append(new_order)
                st.session_state.cart = []
                st.success(f"Order {order_id} placed! Head to {rest_name} and tap 'I am Near' when you arrive.")
                st.balloons()
                import time
                time.sleep(2)
                st.session_state.page = "orders"
                st.rerun()

    with col_clear:
        if st.button("🗑️ Clear Cart", use_container_width=True):
            st.session_state.cart = []
            st.rerun()

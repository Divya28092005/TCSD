import streamlit as st
import datetime
import time

def show():
    st.markdown("## 📦 My Orders")

    if not st.session_state.orders:
        st.markdown("""
        <div class="card" style="text-align:center; padding:60px 20px;">
            <div style="font-size:4rem;">📦</div>
            <div style="font-size:1.3rem; font-weight:700; color:#1a1a2e; margin:16px 0;">No Orders Yet</div>
            <div style="color:#888;">Place your first smart pre-order!</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🗺️ Find Restaurants", use_container_width=True, type="primary"):
            st.session_state.page = "find"
            st.rerun()
        return

    # Summary stats
    total_orders = len(st.session_state.orders)
    waiting = len([o for o in st.session_state.orders if o["status"] == "Waiting"])
    cooking = len([o for o in st.session_state.orders if o["status"] == "Cooking"])
    ready   = len([o for o in st.session_state.orders if o["status"] == "Ready"])
    served  = len([o for o in st.session_state.orders if o["status"] == "Served"])

    c1, c2, c3, c4, c5 = st.columns(5)
    for col, label, val, color in zip(
        [c1, c2, c3, c4, c5],
        ["Total", "Waiting", "Cooking", "Ready", "Served"],
        [total_orders, waiting, cooking, ready, served],
        ["#4A90E2", "#888", "#FFC107", "#28A745", "#17a2b8"]
    ):
        with col:
            st.markdown(f"""
            <div style="background:{color}15; border-left:4px solid {color};
                        border-radius:8px; padding:12px; text-align:center;">
                <div style="font-size:1.5rem; font-weight:700; color:{color};">{val}</div>
                <div style="font-size:12px; color:#666;">{label}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Smart Pre-Order Explanation
    st.markdown("""
    <div class="info-box">
        <b>Smart Pre-Order Flow:</b>
        Order Placed → <b>Waiting for Arrival</b> → Tap "I am Near" → <b>Cooking Started</b> → <b>Ready!</b>
    </div>
    """, unsafe_allow_html=True)

    # Show orders newest first
    for order in reversed(st.session_state.orders):
        status = order["status"]

        # Status color mapping
        status_colors = {
            "Waiting":  ("#888888", "#e2e3e5"),
            "Cooking":  ("#856404", "#fff3cd"),
            "Ready":    ("#155724", "#d4edda"),
            "Served":   ("#0c5460", "#d1ecf1"),
        }
        text_color, bg_color = status_colors.get(status, ("#333", "#f0f0f0"))

        with st.expander(f"🧾 {order['id']} · {order['restaurant_name']} · ₹{order['total']} · {order['placed_at']}", expanded=(status in ["Waiting", "Cooking", "Ready"])):

            col_left, col_right = st.columns([3, 2])

            with col_left:
                st.markdown(f"**🏪 {order['restaurant_name']}**")
                st.markdown(f"👤 {order['customer_name']} · 🪑 {order['room']} · 📞 {order.get('phone', 'N/A')}")
                st.markdown("**Items Ordered:**")
                for item in order["items"]:
                    veg = "🟢" if item["veg"] else "🔴"
                    st.markdown(f"- {veg} {item['name']} × {item['qty']} — ₹{item['price'] * item['qty']}")
                st.markdown(f"**Total: ₹{order['total']}** (incl. taxes)")
                if order.get("note"):
                    st.markdown(f"📝 *{order['note']}*")

            with col_right:
                # Status badge
                st.markdown(f"""
                <div style="background:{bg_color}; color:{text_color};
                            border-radius:12px; padding:16px; text-align:center; margin-bottom:12px;">
                    <div style="font-size:1.8rem;">
                        {'⏳' if status == 'Waiting' else '🍳' if status == 'Cooking' else '✅' if status == 'Ready' else '🍽️'}
                    </div>
                    <div style="font-weight:700; font-size:1rem; margin-top:4px;">{status}</div>
                    <div style="font-size:12px; margin-top:4px;">
                        {'Waiting for your arrival' if status == 'Waiting' else
                         'Chef is cooking your order!' if status == 'Cooking' else
                         'Come to the counter!' if status == 'Ready' else
                         'Enjoy your meal!'}
                    </div>
                </div>
                """, unsafe_allow_html=True)

                # ── STAGE 1: Waiting → Show "I am Near" button ──
                if status == "Waiting":
                    st.markdown(f"""
                    <div style="background:#f8f9fa; border-radius:8px; padding:10px;
                                text-align:center; color:#666; font-size:13px; margin-bottom:8px;">
                        Cooking will start when you arrive.<br>
                        <b>Est. prep time: {order['prep_time']} min after arrival</b>
                    </div>
                    """, unsafe_allow_html=True)
                    if st.button("📍 I am Near — Start Cooking!", key=f"near_{order['id']}", use_container_width=True, type="primary"):
                        order["status"] = "Cooking"
                        order["cooking_started_at"] = datetime.datetime.now()
                        order["is_near"] = True
                        st.success("Cooking started! Your food will be ready soon.")
                        st.rerun()

                # ── STAGE 2: Cooking → Show countdown timer ──
                elif status == "Cooking":
                    started = order.get("cooking_started_at")
                    prep_seconds = order["prep_time"] * 60
                    if started:
                        elapsed = (datetime.datetime.now() - started).total_seconds()
                        remaining = max(0, int(prep_seconds - elapsed))
                        mins = remaining // 60
                        secs = remaining % 60
                        timer_str = f"{mins:02d}:{secs:02d}"
                        color = "#28A745" if remaining < 60 else "#FF6B35"

                        st.markdown(f"""
                        <div style="background:linear-gradient(135deg,{color},{color}99);
                                    color:white; border-radius:12px; padding:16px;
                                    text-align:center; margin-bottom:8px;">
                            <div style="font-size:12px; font-weight:600; opacity:0.9;">
                                TIME REMAINING
                            </div>
                            <div style="font-size:2.5rem; font-weight:800; letter-spacing:4px;">
                                {timer_str}
                            </div>
                        </div>
                        """, unsafe_allow_html=True)

                        if remaining == 0:
                            order["status"] = "Ready"
                            st.rerun()

                    if st.button("Mark as Ready", key=f"ready_{order['id']}", use_container_width=True):
                        order["status"] = "Ready"
                        st.rerun()

                    st.caption("Page refreshes automatically. Reload to update timer.")
                    if st.button("🔄 Refresh Timer", key=f"refresh_{order['id']}", use_container_width=True):
                        st.rerun()

                # ── STAGE 3: Ready → Come to counter ──
                elif status == "Ready":
                    st.markdown("""
                    <div style="background:#d4edda; border-radius:8px; padding:12px;
                                text-align:center; color:#155724; margin-bottom:8px;">
                        <b>🎉 Your order is ready!</b><br>
                        Please come to the counter.
                    </div>
                    """, unsafe_allow_html=True)
                    if st.button("✅ Mark as Served", key=f"served_{order['id']}", use_container_width=True):
                        order["status"] = "Served"
                        st.rerun()

                # ── STAGE 4: Served ──
                elif status == "Served":
                    st.markdown("""
                    <div style="background:#d1ecf1; border-radius:8px; padding:12px;
                                text-align:center; color:#0c5460;">
                        🍽️ <b>Enjoy your meal!</b><br>
                        Thank you for dining with us.
                    </div>
                    """, unsafe_allow_html=True)

    st.markdown("---")
    if st.button("🗑️ Clear All Orders", use_container_width=True):
        st.session_state.orders = []
        st.rerun()

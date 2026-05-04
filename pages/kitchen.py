import streamlit as st
import datetime

def show():
    st.markdown("## 👨‍🍳 Kitchen Dashboard")
    st.markdown("*Real-time view of incoming orders for kitchen staff*")

    if not st.session_state.orders:
        st.markdown("""
        <div class="card" style="text-align:center; padding:60px 20px;">
            <div style="font-size:4rem;">👨‍🍳</div>
            <div style="font-size:1.3rem; font-weight:700; color:#1a1a2e; margin:16px 0;">No Active Orders</div>
            <div style="color:#888;">Orders will appear here when customers place them</div>
        </div>
        """, unsafe_allow_html=True)
        return

    # Live stats bar
    waiting = [o for o in st.session_state.orders if o["status"] == "Waiting"]
    cooking = [o for o in st.session_state.orders if o["status"] == "Cooking"]
    ready   = [o for o in st.session_state.orders if o["status"] == "Ready"]

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown(f"""
        <div style="background:#e2e3e5;border-radius:10px;padding:14px;text-align:center;">
            <div style="font-size:1.8rem;font-weight:800;color:#555;">{len(waiting)}</div>
            <div style="font-size:13px;color:#666;">⏳ Waiting</div>
        </div>""", unsafe_allow_html=True)
    with c2:
        st.markdown(f"""
        <div style="background:#fff3cd;border-radius:10px;padding:14px;text-align:center;">
            <div style="font-size:1.8rem;font-weight:800;color:#856404;">{len(cooking)}</div>
            <div style="font-size:13px;color:#856404;">🍳 Cooking</div>
        </div>""", unsafe_allow_html=True)
    with c3:
        st.markdown(f"""
        <div style="background:#d4edda;border-radius:10px;padding:14px;text-align:center;">
            <div style="font-size:1.8rem;font-weight:800;color:#155724;">{len(ready)}</div>
            <div style="font-size:13px;color:#155724;">✅ Ready</div>
        </div>""", unsafe_allow_html=True)
    with c4:
        total_revenue = sum(o["total"] for o in st.session_state.orders if o["status"] == "Served")
        st.markdown(f"""
        <div style="background:#d1ecf1;border-radius:10px;padding:14px;text-align:center;">
            <div style="font-size:1.8rem;font-weight:800;color:#0c5460;">₹{total_revenue}</div>
            <div style="font-size:13px;color:#0c5460;">💰 Revenue</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Auto-refresh
    col_ref, col_auto = st.columns([2, 2])
    with col_ref:
        if st.button("🔄 Refresh Now", use_container_width=True):
            st.rerun()
    with col_auto:
        st.info("Tip: Refresh the page to update cooking timers.")

    st.markdown("---")

    # Active orders (Waiting + Cooking + Ready)
    active = [o for o in st.session_state.orders if o["status"] in ["Waiting", "Cooking", "Ready"]]
    served = [o for o in st.session_state.orders if o["status"] == "Served"]

    if active:
        st.markdown("### 🔴 Active Orders")
        for order in active:
            status = order["status"]
            if status == "Waiting":
                border_color = "#888"
                bg = "#f8f9fa"
            elif status == "Cooking":
                border_color = "#FFC107"
                bg = "#fffdf0"
            else:
                border_color = "#28A745"
                bg = "#f0fff4"

            col_ord, col_act = st.columns([4, 2])
            with col_ord:
                items_text = ", ".join([f"{i['name']}×{i['qty']}" for i in order["items"]])
                prep_info = ""
                if status == "Cooking" and order.get("cooking_started_at"):
                    elapsed = int((datetime.datetime.now() - order["cooking_started_at"]).total_seconds())
                    remaining = max(0, order["prep_time"] * 60 - elapsed)
                    mins = remaining // 60
                    secs = remaining % 60
                    prep_info = f" · ⏱️ {mins:02d}:{secs:02d} left"

                st.markdown(f"""
                <div style="background:{bg}; border-left:4px solid {border_color};
                            border-radius:10px; padding:16px; margin-bottom:8px;">
                    <div style="display:flex; justify-content:space-between;">
                        <span style="font-weight:800; font-size:1.1rem;">#{order['id']}</span>
                        <span style="font-weight:700; color:{border_color};">{status}{prep_info}</span>
                    </div>
                    <div style="margin-top:6px; color:#555;">
                        🏪 {order['restaurant_name']} &nbsp;|&nbsp;
                        🪑 {order['room']} &nbsp;|&nbsp;
                        👤 {order['customer_name']}
                    </div>
                    <div style="margin-top:8px; font-size:13px; color:#444;">
                        📝 {items_text}
                    </div>
                    <div style="margin-top:4px; font-weight:700; color:#FF6B35;">
                        Total: ₹{order['total']} &nbsp;|&nbsp; Placed: {order['placed_at']}
                    </div>
                    {f'<div style="margin-top:4px;font-size:12px;color:#888;">Note: {order["note"]}</div>' if order.get("note") else ''}
                </div>
                """, unsafe_allow_html=True)

            with col_act:
                st.markdown("<br>", unsafe_allow_html=True)
                if status == "Waiting":
                    st.markdown('<div style="text-align:center;color:#888;font-size:13px;">Waiting for customer</div>', unsafe_allow_html=True)
                    if st.button("Start Cooking", key=f"k_cook_{order['id']}", use_container_width=True, type="primary"):
                        order["status"] = "Cooking"
                        order["cooking_started_at"] = datetime.datetime.now()
                        st.rerun()
                elif status == "Cooking":
                    st.markdown('<div style="text-align:center;color:#856404;font-size:13px;font-weight:700;">🍳 Cooking in progress</div>', unsafe_allow_html=True)
                    if st.button("Mark Ready", key=f"k_ready_{order['id']}", use_container_width=True, type="primary"):
                        order["status"] = "Ready"
                        st.rerun()
                elif status == "Ready":
                    st.markdown('<div style="text-align:center;color:#155724;font-size:13px;font-weight:700;">✅ Ready to serve!</div>', unsafe_allow_html=True)
                    if st.button("Mark Served", key=f"k_served_{order['id']}", use_container_width=True):
                        order["status"] = "Served"
                        st.rerun()

    # Served orders
    if served:
        st.markdown("---")
        st.markdown("### ✅ Served Orders Today")
        for order in served:
            st.markdown(f"""
            <div style="background:#f8f9fa; border-radius:8px; padding:10px 14px; margin-bottom:6px;
                        display:flex; justify-content:space-between; color:#555; font-size:13px;">
                <span>✅ #{order['id']} · {order['customer_name']} · {order['restaurant_name']}</span>
                <span style="font-weight:700; color:#FF6B35;">₹{order['total']}</span>
            </div>
            """, unsafe_allow_html=True)

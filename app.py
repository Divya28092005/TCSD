import streamlit as st

st.set_page_config(
    page_title="Smart Restaurant Ordering System",
    page_icon="🍽️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── Session state defaults ────────────────────────────────────────────────────
if "cart" not in st.session_state:
    st.session_state.cart = []
if "orders" not in st.session_state:
    st.session_state.orders = []
if "page" not in st.session_state:
    st.session_state.page = "menu"
if "selected_restaurant" not in st.session_state:
    st.session_state.selected_restaurant = None
if "order_counter" not in st.session_state:
    st.session_state.order_counter = 1000

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
  /* Global */
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
  html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

  /* Hide default Streamlit header */
  #MainMenu { visibility: hidden; }
  footer { visibility: hidden; }
  header { visibility: hidden; }

  /* Card style */
  .card {
    background: #ffffff;
    border-radius: 16px;
    padding: 20px;
    box-shadow: 0 2px 12px rgba(0,0,0,0.08);
    margin-bottom: 16px;
    border: 1px solid #f0f0f0;
  }
  .card:hover { box-shadow: 0 4px 20px rgba(0,0,0,0.12); }

  /* Restaurant card */
  .rest-card {
    background: linear-gradient(135deg, #fff 0%, #fafafa 100%);
    border-radius: 16px;
    padding: 20px;
    border: 1px solid #e8e8e8;
    margin-bottom: 12px;
    cursor: pointer;
    transition: all 0.2s;
  }
  .rest-card:hover { border-color: #FF6B35; transform: translateY(-2px); }

  /* Menu item card */
  .menu-card {
    background: #fff;
    border-radius: 12px;
    padding: 16px;
    border: 1px solid #f0f0f0;
    margin-bottom: 10px;
  }

  /* Badges */
  .badge-green  { background: #d4edda; color: #155724; padding: 3px 10px; border-radius: 20px; font-size: 12px; font-weight: 600; }
  .badge-orange { background: #fff3cd; color: #856404; padding: 3px 10px; border-radius: 20px; font-size: 12px; font-weight: 600; }
  .badge-red    { background: #f8d7da; color: #721c24; padding: 3px 10px; border-radius: 20px; font-size: 12px; font-weight: 600; }
  .badge-blue   { background: #d1ecf1; color: #0c5460; padding: 3px 10px; border-radius: 20px; font-size: 12px; font-weight: 600; }

  /* Status pill */
  .status-waiting  { background: #e2e3e5; color: #383d41; padding: 4px 12px; border-radius: 20px; font-weight: 600; font-size: 13px; }
  .status-cooking  { background: #fff3cd; color: #856404; padding: 4px 12px; border-radius: 20px; font-weight: 600; font-size: 13px; }
  .status-ready    { background: #d4edda; color: #155724; padding: 4px 12px; border-radius: 20px; font-weight: 600; font-size: 13px; }
  .status-served   { background: #d1ecf1; color: #0c5460; padding: 4px 12px; border-radius: 20px; font-weight: 600; font-size: 13px; }

  /* Big heading */
  .hero-title { font-size: 2.4rem; font-weight: 700; color: #1a1a2e; line-height: 1.2; }
  .hero-sub   { font-size: 1.1rem; color: #666; margin-top: 8px; }
  .accent     { color: #FF6B35; }

  /* Metric box */
  .metric-box {
    background: linear-gradient(135deg, #1a1a2e, #16213e);
    color: white;
    border-radius: 12px;
    padding: 20px;
    text-align: center;
  }
  .metric-box .val { font-size: 2rem; font-weight: 700; color: #FF6B35; }
  .metric-box .lbl { font-size: 0.85rem; color: #aaa; margin-top: 4px; }

  /* Nav button override */
  div[data-testid="stSidebar"] button {
    width: 100%;
    border-radius: 10px;
    margin-bottom: 4px;
    font-weight: 600;
  }

  /* Cart badge */
  .cart-badge {
    background: #FF6B35;
    color: white;
    border-radius: 50%;
    padding: 2px 8px;
    font-size: 12px;
    font-weight: 700;
    margin-left: 6px;
  }

  /* Timer */
  .timer-box {
    background: linear-gradient(135deg, #FF6B35, #ff8c5a);
    color: white;
    border-radius: 12px;
    padding: 16px;
    text-align: center;
    font-size: 2.5rem;
    font-weight: 700;
    letter-spacing: 4px;
  }

  /* Info box */
  .info-box {
    background: #e8f4fd;
    border-left: 4px solid #4A90E2;
    border-radius: 8px;
    padding: 12px 16px;
    color: #1a5f8a;
    font-size: 14px;
    margin-bottom: 12px;
  }

  /* Stars */
  .stars { color: #f4b942; font-size: 14px; }

  /* Price tag */
  .price { font-size: 1.1rem; font-weight: 700; color: #FF6B35; }

  /* Divider */
  .divider { border: none; border-top: 1px solid #f0f0f0; margin: 16px 0; }
</style>
""", unsafe_allow_html=True)

# ── Sidebar Navigation ────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🍽️ Smart Restaurant")
    st.markdown("---")

    cart_count = len(st.session_state.cart)
    cart_label = f"🛒 Cart {'(' + str(cart_count) + ')' if cart_count > 0 else ''}"

    nav_items = [
        ("🏠", "Home",          "home"),
        ("🗺️", "Find Restaurants","find"),
        ("📋", "Menu",          "menu"),
        (cart_label, "", "cart") if cart_count > 0 else ("🛒", "Cart", "cart"),
        ("📦", "My Orders",     "orders"),
        ("👨‍🍳", "Kitchen View",  "kitchen"),
        ("📊", "Admin Panel",   "admin"),
    ]

    for icon, label, key in nav_items:
        full_label = f"{icon} {label}".strip() if label else icon
        if st.button(full_label, key=f"nav_{key}", use_container_width=True):
            st.session_state.page = key
            st.rerun()

    st.markdown("---")
    if st.session_state.selected_restaurant:
        st.markdown(f"**Selected:**")
        st.markdown(f"🏪 {st.session_state.selected_restaurant['name']}")
        st.markdown(f"⭐ {st.session_state.selected_restaurant['rating']} · {st.session_state.selected_restaurant['cuisine']}")

    st.markdown("---")
    st.caption("Smart Pre-Order System v1.0")
    st.caption("Cooking starts when you arrive!")

# ── Page Router ───────────────────────────────────────────────────────────────
page = st.session_state.page

if page == "home":
    from pages.home import show
    show()
elif page == "find":
    from pages.find_restaurants import show
    show()
elif page == "menu":
    from pages.menu import show
    show()
elif page == "cart":
    from pages.cart import show
    show()
elif page == "orders":
    from pages.orders import show
    show()
elif page == "kitchen":
    from pages.kitchen import show
    show()
elif page == "admin":
    from pages.admin import show
    show()

import streamlit as st
import urllib.parse

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Balaji Maligai | Fresh Groceries",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================
# SHOP DETAILS
# ============================================================

SHOP_NAME = "Balaji Maligai"
SHOP_PHONE = "917558110544"
SHOP_DISPLAY_PHONE = "+91 75581 10544"
SHOP_ADDRESS = "Main Road, Annappanpettai, Tharangai (TK), Mayiladuthurai (Dist)"
SHOP_TIMING = "5:00 AM – 10:00 PM"
SHOP_LOCATION = "https://maps.app.goo.gl/voLpdqGVrMMMGkXf8"
WHATSAPP_NUMBER = SHOP_PHONE

# ============================================================
# SESSION STATE
# ============================================================

if "cart" not in st.session_state:
    st.session_state.cart = {}
if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"
if "selected_category" not in st.session_state:
    st.session_state.selected_category = "All"
if "customer_name" not in st.session_state:
    st.session_state.customer_name = ""
if "customer_phone" not in st.session_state:
    st.session_state.customer_phone = ""
if "customer_address" not in st.session_state:
    st.session_state.customer_address = ""
if "order_type" not in st.session_state:
    st.session_state.order_type = "Pickup"

# ============================================================
# DATA
# ============================================================

PRODUCTS = [{'id': 1, 'name': 'Ponni Rice', 'category': 'Rice & Grains', 'price': 65, 'unit': '1 kg', 'emoji': '🍚', 'tag': 'Popular'}, {'id': 2, 'name': 'Idli Rice', 'category': 'Rice & Grains', 'price': 58, 'unit': '1 kg', 'emoji': '🍚', 'tag': ''}, {'id': 3, 'name': 'Basmati Rice', 'category': 'Rice & Grains', 'price': 120, 'unit': '1 kg', 'emoji': '🍚', 'tag': 'Popular'}, {'id': 4, 'name': 'Sona Masoori Rice', 'category': 'Rice & Grains', 'price': 75, 'unit': '1 kg', 'emoji': '🍚', 'tag': ''}, {'id': 5, 'name': 'Raw Rice', 'category': 'Rice & Grains', 'price': 62, 'unit': '1 kg', 'emoji': '🍚', 'tag': ''}, {'id': 6, 'name': 'Boiled Rice', 'category': 'Rice & Grains', 'price': 68, 'unit': '1 kg', 'emoji': '🍚', 'tag': ''}, {'id': 7, 'name': 'Ponni Rice Premium', 'category': 'Rice & Grains', 'price': 78, 'unit': '1 kg', 'emoji': '🍚', 'tag': ''}, {'id': 8, 'name': 'Aval / Poha', 'category': 'Rice & Grains', 'price': 55, 'unit': '500 g', 'emoji': '🌾', 'tag': ''}, {'id': 9, 'name': 'Broken Rice', 'category': 'Rice & Grains', 'price': 48, 'unit': '1 kg', 'emoji': '🌾', 'tag': ''}, {'id': 10, 'name': 'Wheat Rava', 'category': 'Rice & Grains', 'price': 58, 'unit': '500 g', 'emoji': '🌾', 'tag': ''}, {'id': 11, 'name': 'Toor Dal', 'category': 'Dals & Pulses', 'price': 145, 'unit': '1 kg', 'emoji': '🫘', 'tag': 'Best Seller'}, {'id': 12, 'name': 'Urad Dal', 'category': 'Dals & Pulses', 'price': 135, 'unit': '1 kg', 'emoji': '🫘', 'tag': ''}, {'id': 13, 'name': 'Moong Dal', 'category': 'Dals & Pulses', 'price': 125, 'unit': '1 kg', 'emoji': '🫘', 'tag': 'Popular'}, {'id': 14, 'name': 'Masoor Dal', 'category': 'Dals & Pulses', 'price': 110, 'unit': '1 kg', 'emoji': '🫘', 'tag': ''}, {'id': 15, 'name': 'Chana Dal', 'category': 'Dals & Pulses', 'price': 95, 'unit': '1 kg', 'emoji': '🫘', 'tag': ''}, {'id': 16, 'name': 'Green Gram', 'category': 'Dals & Pulses', 'price': 130, 'unit': '1 kg', 'emoji': '🫘', 'tag': ''}, {'id': 17, 'name': 'Black Chana', 'category': 'Dals & Pulses', 'price': 105, 'unit': '1 kg', 'emoji': '🫘', 'tag': ''}, {'id': 18, 'name': 'White Chana', 'category': 'Dals & Pulses', 'price': 115, 'unit': '1 kg', 'emoji': '🫘', 'tag': ''}, {'id': 19, 'name': 'Roasted Gram', 'category': 'Dals & Pulses', 'price': 90, 'unit': '500 g', 'emoji': '🫘', 'tag': ''}, {'id': 20, 'name': 'Rajma', 'category': 'Dals & Pulses', 'price': 145, 'unit': '1 kg', 'emoji': '🫘', 'tag': ''}, {'id': 21, 'name': 'Sugar', 'category': 'Staples', 'price': 48, 'unit': '1 kg', 'emoji': '🧂', 'tag': ''}, {'id': 22, 'name': 'Tata Salt', 'category': 'Staples', 'price': 28, 'unit': '1 kg', 'emoji': '🧂', 'tag': ''}, {'id': 23, 'name': 'Rock Salt', 'category': 'Staples', 'price': 35, 'unit': '1 kg', 'emoji': '🧂', 'tag': ''}, {'id': 24, 'name': 'Jaggery', 'category': 'Staples', 'price': 75, 'unit': '1 kg', 'emoji': '🟫', 'tag': 'Popular'}, {'id': 25, 'name': 'Brown Sugar', 'category': 'Staples', 'price': 95, 'unit': '500 g', 'emoji': '🟫', 'tag': ''}, {'id': 26, 'name': 'Palm Jaggery', 'category': 'Staples', 'price': 120, 'unit': '500 g', 'emoji': '🟫', 'tag': ''}, {'id': 27, 'name': 'Vermicelli', 'category': 'Staples', 'price': 45, 'unit': '400 g', 'emoji': '🍜', 'tag': ''}, {'id': 28, 'name': 'Sabudana', 'category': 'Staples', 'price': 70, 'unit': '500 g', 'emoji': '⚪', 'tag': ''}, {'id': 29, 'name': 'Corn Flakes', 'category': 'Staples', 'price': 160, 'unit': '500 g', 'emoji': '🥣', 'tag': ''}, {'id': 30, 'name': 'Custard Powder', 'category': 'Staples', 'price': 55, 'unit': '100 g', 'emoji': '🥣', 'tag': ''}, {'id': 31, 'name': 'Sunflower Oil', 'category': 'Oils', 'price': 145, 'unit': '1 litre', 'emoji': '🫗', 'tag': 'Offer'}, {'id': 32, 'name': 'Groundnut Oil', 'category': 'Oils', 'price': 175, 'unit': '1 litre', 'emoji': '🫗', 'tag': 'Popular'}, {'id': 33, 'name': 'Coconut Oil', 'category': 'Oils', 'price': 185, 'unit': '1 litre', 'emoji': '🫗', 'tag': ''}, {'id': 34, 'name': 'Gingelly Oil', 'category': 'Oils', 'price': 210, 'unit': '1 litre', 'emoji': '🫗', 'tag': 'Popular'}, {'id': 35, 'name': 'Rice Bran Oil', 'category': 'Oils', 'price': 155, 'unit': '1 litre', 'emoji': '🫗', 'tag': ''}, {'id': 36, 'name': 'Mustard Oil', 'category': 'Oils', 'price': 190, 'unit': '1 litre', 'emoji': '🫗', 'tag': ''}, {'id': 37, 'name': 'Palm Oil', 'category': 'Oils', 'price': 135, 'unit': '1 litre', 'emoji': '🫗', 'tag': ''}, {'id': 38, 'name': 'Olive Oil', 'category': 'Oils', 'price': 420, 'unit': '500 ml', 'emoji': '🫒', 'tag': ''}, {'id': 39, 'name': 'Cooking Oil Pouch', 'category': 'Oils', 'price': 150, 'unit': '1 litre', 'emoji': '🫗', 'tag': ''}, {'id': 40, 'name': 'Coconut Oil Small', 'category': 'Oils', 'price': 95, 'unit': '500 ml', 'emoji': '🫗', 'tag': ''}, {'id': 41, 'name': 'Turmeric Powder', 'category': 'Spices', 'price': 55, 'unit': '200 g', 'emoji': '🌾', 'tag': ''}, {'id': 42, 'name': 'Chilli Powder', 'category': 'Spices', 'price': 65, 'unit': '200 g', 'emoji': '🌶️', 'tag': ''}, {'id': 43, 'name': 'Coriander Powder', 'category': 'Spices', 'price': 60, 'unit': '200 g', 'emoji': '🌿', 'tag': ''}, {'id': 44, 'name': 'Cumin Seeds', 'category': 'Spices', 'price': 75, 'unit': '100 g', 'emoji': '🌿', 'tag': ''}, {'id': 45, 'name': 'Pepper', 'category': 'Spices', 'price': 110, 'unit': '100 g', 'emoji': '⚫', 'tag': 'Popular'}, {'id': 46, 'name': 'Mustard Seeds', 'category': 'Spices', 'price': 35, 'unit': '100 g', 'emoji': '🌿', 'tag': ''}, {'id': 47, 'name': 'Sambar Powder', 'category': 'Spices', 'price': 70, 'unit': '200 g', 'emoji': '', 'tag': '🌶️'}, {'id': 48, 'name': 'Rasam Powder', 'category': 'Spices', 'price': 65, 'unit': '100 g', 'emoji': '🌶️', 'tag': ''}, {'id': 49, 'name': 'Garam Masala', 'category': 'Spices', 'price': 80, 'unit': '100 g', 'emoji': '🌶️', 'tag': ''}, {'id': 50, 'name': 'Jeera Powder', 'category': 'Spices', 'price': 75, 'unit': '100 g', 'emoji': '🌿', 'tag': ''}, {'id': 51, 'name': 'Aashirvaad Atta', 'category': 'Flour', 'price': 275, 'unit': '5 kg', 'emoji': '🌾', 'tag': 'Popular'}, {'id': 52, 'name': 'Maida', 'category': 'Flour', 'price': 55, 'unit': '1 kg', 'emoji': '🌾', 'tag': ''}, {'id': 53, 'name': 'Rice Flour', 'category': 'Flour', 'price': 65, 'unit': '1 kg', 'emoji': '🌾', 'tag': ''}, {'id': 54, 'name': 'Besan Flour', 'category': 'Flour', 'price': 80, 'unit': '500 g', 'emoji': '🌾', 'tag': ''}, {'id': 55, 'name': 'Corn Flour', 'category': 'Flour', 'price': 60, 'unit': '500 g', 'emoji': '🌾', 'tag': ''}, {'id': 56, 'name': 'Ragi Flour', 'category': 'Flour', 'price': 75, 'unit': '500 g', 'emoji': '🌾', 'tag': 'Healthy'}, {'id': 57, 'name': 'Wheat Flour', 'category': 'Flour', 'price': 65, 'unit': '1 kg', 'emoji': '🌾', 'tag': ''}, {'id': 58, 'name': 'Sooji Rava', 'category': 'Flour', 'price': 55, 'unit': '500 g', 'emoji': '🌾', 'tag': ''}, {'id': 59, 'name': 'Multigrain Atta', 'category': 'Flour', 'price': 180, 'unit': '1 kg', 'emoji': '🌾', 'tag': ''}, {'id': 60, 'name': 'Idiyappam Flour', 'category': 'Flour', 'price': 70, 'unit': '500 g', 'emoji': '🌾', 'tag': ''}, {'id': 61, 'name': 'Parle-G Biscuits', 'category': 'Snacks & Biscuits', 'price': 10, 'unit': 'Pack', 'emoji': '🍪', 'tag': ''}, {'id': 62, 'name': 'Lays Classic', 'category': 'Snacks & Biscuits', 'price': 20, 'unit': 'Pack', 'emoji': '🥔', 'tag': ''}, {'id': 63, 'name': 'Good Day Biscuits', 'category': 'Snacks & Biscuits', 'price': 30, 'unit': 'Pack', 'emoji': '🍪', 'tag': 'Popular'}, {'id': 64, 'name': 'Marie Gold', 'category': 'Snacks & Biscuits', 'price': 30, 'unit': 'Pack', 'emoji': '🍪', 'tag': ''}, {'id': 65, 'name': 'Oreo Biscuits', 'category': 'Snacks & Biscuits', 'price': 35, 'unit': 'Pack', 'emoji': '🍪', 'tag': ''}, {'id': 66, 'name': 'Bingo Chips', 'category': 'Snacks & Biscuits', 'price': 20, 'unit': 'Pack', 'emoji': '🥔', 'tag': ''}, {'id': 67, 'name': 'Mixture', 'category': 'Snacks & Biscuits', 'price': 90, 'unit': '500 g', 'emoji': '🥨', 'tag': 'Popular'}, {'id': 68, 'name': 'Murukku', 'category': 'Snacks & Biscuits', 'price': 100, 'unit': '500 g', 'emoji': '🥨', 'tag': ''}, {'id': 69, 'name': 'Salted Peanuts', 'category': 'Snacks & Biscuits', 'price': 70, 'unit': '500 g', 'emoji': '🥜', 'tag': ''}, {'id': 70, 'name': 'Popcorn', 'category': 'Snacks & Biscuits', 'price': 50, 'unit': 'Pack', 'emoji': '🍿', 'tag': ''}, {'id': 71, 'name': 'Coca Cola', 'category': 'Beverages', 'price': 45, 'unit': '750 ml', 'emoji': '🥤', 'tag': ''}, {'id': 72, 'name': 'Pepsi', 'category': 'Beverages', 'price': 45, 'unit': '750 ml', 'emoji': '🥤', 'tag': ''}, {'id': 73, 'name': 'Sprite', 'category': 'Beverages', 'price': 45, 'unit': '750 ml', 'emoji': '🥤', 'tag': ''}, {'id': 74, 'name': 'Fanta', 'category': 'Beverages', 'price': 45, 'unit': '750 ml', 'emoji': '🥤', 'tag': ''}, {'id': 75, 'name': 'Maaza', 'category': 'Beverages', 'price': 45, 'unit': '600 ml', 'emoji': '🥭', 'tag': ''}, {'id': 76, 'name': 'Tata Tea', 'category': 'Beverages', 'price': 125, 'unit': '250 g', 'emoji': '☕', 'tag': 'Popular'}, {'id': 77, 'name': 'Coffee Powder', 'category': 'Beverages', 'price': 180, 'unit': '250 g', 'emoji': '☕', 'tag': ''}, {'id': 78, 'name': 'Horlicks', 'category': 'Beverages', 'price': 220, 'unit': '500 g', 'emoji': '🥛', 'tag': ''}, {'id': 79, 'name': 'Boost', 'category': 'Beverages', 'price': 210, 'unit': '500 g', 'emoji': '🥛', 'tag': ''}, {'id': 80, 'name': 'Badam Drink Mix', 'category': 'Beverages', 'price': 190, 'unit': '500 g', 'emoji': '🥛', 'tag': ''}, {'id': 81, 'name': 'Surf Excel', 'category': 'Household', 'price': 115, 'unit': '1 kg', 'emoji': '🧺', 'tag': ''}, {'id': 82, 'name': 'Vim Dishwash', 'category': 'Household', 'price': 120, 'unit': '500 ml', 'emoji': '🧴', 'tag': ''}, {'id': 83, 'name': 'Ariel Detergent', 'category': 'Household', 'price': 125, 'unit': '1 kg', 'emoji': '🧺', 'tag': 'Popular'}, {'id': 84, 'name': 'Rin Detergent', 'category': 'Household', 'price': 95, 'unit': '1 kg', 'emoji': '🧺', 'tag': ''}, {'id': 85, 'name': 'Wheel Detergent', 'category': 'Household', 'price': 85, 'unit': '1 kg', 'emoji': '🧺', 'tag': ''}, {'id': 86, 'name': 'Harpic', 'category': 'Household', 'price': 110, 'unit': '500 ml', 'emoji': '🧴', 'tag': ''}, {'id': 87, 'name': 'Lizol', 'category': 'Household', 'price': 145, 'unit': '500 ml', 'emoji': '🧴', 'tag': ''}, {'id': 88, 'name': 'Dishwash Bar', 'category': 'Household', 'price': 25, 'unit': 'Pack', 'emoji': '🧼', 'tag': ''}, {'id': 89, 'name': 'Floor Cleaner', 'category': 'Household', 'price': 130, 'unit': '1 litre', 'emoji': '🧴', 'tag': ''}, {'id': 90, 'name': 'Scrub Pad', 'category': 'Household', 'price': 35, 'unit': 'Pack', 'emoji': '🧽', 'tag': ''}, {'id': 91, 'name': 'Colgate Toothpaste', 'category': 'Personal Care', 'price': 95, 'unit': '100 g', 'emoji': '🪥', 'tag': 'Popular'}, {'id': 92, 'name': 'Closeup Toothpaste', 'category': 'Personal Care', 'price': 90, 'unit': '100 g', 'emoji': '🪥', 'tag': ''}, {'id': 93, 'name': 'Toothbrush', 'category': 'Personal Care', 'price': 45, 'unit': '1 pc', 'emoji': '🪥', 'tag': ''}, {'id': 94, 'name': 'Bath Soap', 'category': 'Personal Care', 'price': 45, 'unit': 'Pack', 'emoji': '🧼', 'tag': ''}, {'id': 95, 'name': 'Shampoo', 'category': 'Personal Care', 'price': 120, 'unit': '180 ml', 'emoji': '🧴', 'tag': ''}, {'id': 96, 'name': 'Hair Oil', 'category': 'Personal Care', 'price': 110, 'unit': '200 ml', 'emoji': '🧴', 'tag': ''}, {'id': 97, 'name': 'Face Wash', 'category': 'Personal Care', 'price': 150, 'unit': '100 g', 'emoji': '🧴', 'tag': ''}, {'id': 98, 'name': 'Hand Wash', 'category': 'Personal Care', 'price': 95, 'unit': '250 ml', 'emoji': '🧴', 'tag': ''}, {'id': 99, 'name': 'Talcum Powder', 'category': 'Personal Care', 'price': 120, 'unit': '100 g', 'emoji': '🧴', 'tag': ''}, {'id': 100, 'name': 'Shaving Cream', 'category': 'Personal Care', 'price': 110, 'unit': '50 g', 'emoji': '🧴', 'tag': ''}]

OFFERS = [{'title': 'Monthly Grocery Pack', 'text': 'Save more on your monthly essentials.', 'discount': 'SPECIAL DEAL', 'emoji': '🛒'}, {'title': 'Cooking Oil Offer', 'text': 'Selected cooking oils at special prices.', 'discount': 'SAVE MORE', 'emoji': '🫗'}, {'title': 'Snacks Combo', 'text': 'Perfect snacks for the whole family.', 'discount': 'COMBO OFFER', 'emoji': '🍪'}]

CATEGORIES = ["All"] + sorted({p["category"] for p in PRODUCTS})
CATEGORY_ICONS = {
    "Rice & Grains": "🍚",
    "Dals & Pulses": "🫘",
    "Staples": "🧂",
    "Oils": "🫗",
    "Spices": "🌶️",
    "Flour": "🌾",
    "Snacks & Biscuits": "🍪",
    "Beverages": "🥤",
    "Household": "🧺",
    "Personal Care": "🧴",
}

# ============================================================
# HELPERS
# ============================================================

def go_to(page):
    st.session_state.current_page = page
    st.rerun()


def add_to_cart(product_id):
    st.session_state.cart[product_id] = st.session_state.cart.get(product_id, 0) + 1
    st.toast("Added to cart 🛒")


def decrease_cart(product_id):
    if product_id in st.session_state.cart:
        st.session_state.cart[product_id] -= 1
        if st.session_state.cart[product_id] <= 0:
            del st.session_state.cart[product_id]


def increase_cart(product_id):
    st.session_state.cart[product_id] = st.session_state.cart.get(product_id, 0) + 1


def cart_items():
    lookup = {p["id"]: p for p in PRODUCTS}
    return [(lookup[pid], qty) for pid, qty in st.session_state.cart.items() if pid in lookup]

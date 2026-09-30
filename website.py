import streamlit as st
import urllib.parse
from datetime import datetime


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

# Replace these with your real shop details
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

if "selected_category" not in st.session_state:
    st.session_state.selected_category = "All"


# ============================================================
# PRODUCTS
# ============================================================

PRODUCTS = [
    {
        "id": 1,
        "name": "Ponni Rice",
        "category": "Rice & Grains",
        "price": 65,
        "unit": "1 kg",
        "emoji": "🍚",
        "tag": "Popular",
    },
    {
        "id": 2,
        "name": "Idli Rice",
        "category": "Rice & Grains",
        "price": 58,
        "unit": "1 kg",
        "emoji": "🍚",
        "tag": "",
    },
    {
        "id": 3,
        "name": "Basmati Rice",
        "category": "Rice & Grains",
        "price": 120,
        "unit": "1 kg",
        "emoji": "🍚",
        "tag": "Popular",
    },
    {
        "id": 4,
        "name": "Sona Masoori Rice",
        "category": "Rice & Grains",
        "price": 75,
        "unit": "1 kg",
        "emoji": "🍚",
        "tag": "",
    },
    {
        "id": 5,
        "name": "Raw Rice",
        "category": "Rice & Grains",
        "price": 62,
        "unit": "1 kg",
        "emoji": "🍚",
        "tag": "",
    },
    {
        "id": 6,
        "name": "Boiled Rice",
        "category": "Rice & Grains",
        "price": 68,
        "unit": "1 kg",
        "emoji": "🍚",
        "tag": "",
    },
    {
        "id": 7,
        "name": "Ponni Rice Premium",
        "category": "Rice & Grains",
        "price": 78,
        "unit": "1 kg",
        "emoji": "🍚",
        "tag": "",
    },
    {
        "id": 8,
        "name": "Aval / Poha",
        "category": "Rice & Grains",
        "price": 55,
        "unit": "500 g",
        "emoji": "🌾",
        "tag": "",
    },
    {
        "id": 9,
        "name": "Broken Rice",
        "category": "Rice & Grains",
        "price": 48,
        "unit": "1 kg",
        "emoji": "🌾",
        "tag": "",
    },
    {
        "id": 10,
        "name": "Wheat Rava",
        "category": "Rice & Grains",
        "price": 58,
        "unit": "500 g",
        "emoji": "🌾",
        "tag": "",
    },
    {
        "id": 11,
        "name": "Toor Dal",
        "category": "Dals & Pulses",
        "price": 145,
        "unit": "1 kg",
        "emoji": "🫘",
        "tag": "Best Seller",
    },
    {
        "id": 12,
        "name": "Urad Dal",
        "category": "Dals & Pulses",
        "price": 135,
        "unit": "1 kg",
        "emoji": "🫘",
        "tag": "",
    },
    {
        "id": 13,
        "name": "Moong Dal",
        "category": "Dals & Pulses",
        "price": 125,
        "unit": "1 kg",
        "emoji": "🫘",
        "tag": "Popular",
    },
    {
        "id": 14,
        "name": "Masoor Dal",
        "category": "Dals & Pulses",
        "price": 110,
        "unit": "1 kg",
        "emoji": "🫘",
        "tag": "",
    },
    {
        "id": 15,
        "name": "Chana Dal",
        "category": "Dals & Pulses",
        "price": 95,
        "unit": "1 kg",
        "emoji": "🫘",
        "tag": "",
    },
    {
        "id": 16,
        "name": "Green Gram",
        "category": "Dals & Pulses",
        "price": 130,
        "unit": "1 kg",
        "emoji": "🫘",
        "tag": "",
    },
    {
        "id": 17,
        "name": "Black Chana",
        "category": "Dals & Pulses",
        "price": 105,
        "unit": "1 kg",
        "emoji": "🫘",
        "tag": "",
    },
    {
        "id": 18,
        "name": "White Chana",
        "category": "Dals & Pulses",
        "price": 115,
        "unit": "1 kg",
        "emoji": "🫘",
        "tag": "",
    },
    {
        "id": 19,
        "name": "Roasted Gram",
        "category": "Dals & Pulses",
        "price": 90,
        "unit": "500 g",
        "emoji": "🫘",
        "tag": "",
    },
    {
        "id": 20,
        "name": "Rajma",
        "category": "Dals & Pulses",
        "price": 145,
        "unit": "1 kg",
        "emoji": "🫘",
        "tag": "",
    },
    {
        "id": 21,
        "name": "Sugar",
        "category": "Staples",
        "price": 48,
        "unit": "1 kg",
        "emoji": "🧂",
        "tag": "",
    },
    {
        "id": 22,
        "name": "Tata Salt",
        "category": "Staples",
        "price": 28,
        "unit": "1 kg",
        "emoji": "🧂",
        "tag": "",
    },
    {
        "id": 23,
        "name": "Rock Salt",
        "category": "Staples",
        "price": 35,
        "unit": "1 kg",
        "emoji": "🧂",
        "tag": "",
    },
    {
        "id": 24,
        "name": "Jaggery",
        "category": "Staples",
        "price": 75,
        "unit": "1 kg",
        "emoji": "🟫",
        "tag": "Popular",
    },
    {
        "id": 25,
        "name": "Brown Sugar",
        "category": "Staples",
        "price": 95,
        "unit": "500 g",
        "emoji": "🟫",
        "tag": "",
    },
    {
        "id": 26,
        "name": "Palm Jaggery",
        "category": "Staples",
        "price": 120,
        "unit": "500 g",
        "emoji": "🟫",
        "tag": "",
    },
    {
        "id": 27,
        "name": "Vermicelli",
        "category": "Staples",
        "price": 45,
        "unit": "400 g",
        "emoji": "🍜",
        "tag": "",
    },
    {
        "id": 28,
        "name": "Sabudana",
        "category": "Staples",
        "price": 70,
        "unit": "500 g",
        "emoji": "⚪",
        "tag": "",
    },
    {
        "id": 29,
        "name": "Corn Flakes",
        "category": "Staples",
        "price": 160,
        "unit": "500 g",
        "emoji": "🥣",
        "tag": "",
    },
    {
        "id": 30,
        "name": "Custard Powder",
        "category": "Staples",
        "price": 55,
        "unit": "100 g",
        "emoji": "🥣",
        "tag": "",
    },
    {
        "id": 31,
        "name": "Sunflower Oil",
        "category": "Oils",
        "price": 145,
        "unit": "1 litre",
        "emoji": "🫗",
        "tag": "Offer",
    },
    {
        "id": 32,
        "name": "Groundnut Oil",
        "category": "Oils",
        "price": 175,
        "unit": "1 litre",
        "emoji": "🫗",
        "tag": "Popular",
    },
    {
        "id": 33,
        "name": "Coconut Oil",
        "category": "Oils",
        "price": 185,
        "unit": "1 litre",
        "emoji": "🫗",
        "tag": "",
    },
    {
        "id": 34,
        "name": "Gingelly Oil",
        "category": "Oils",
        "price": 210,
        "unit": "1 litre",
        "emoji": "🫗",
        "tag": "Popular",
    },
    {
        "id": 35,
        "name": "Rice Bran Oil",
        "category": "Oils",
        "price": 155,
        "unit": "1 litre",
        "emoji": "🫗",
        "tag": "",
    },
    {
        "id": 36,
        "name": "Mustard Oil",
        "category": "Oils",
        "price": 190,
        "unit": "1 litre",
        "emoji": "🫗",
        "tag": "",
    },
    {
        "id": 37,
        "name": "Palm Oil",
        "category": "Oils",
        "price": 135,
        "unit": "1 litre",
        "emoji": "🫗",
        "tag": "",
    },
    {
        "id": 38,
        "name": "Olive Oil",
        "category": "Oils",
        "price": 420,
        "unit": "500 ml",
        "emoji": "🫒",
        "tag": "",
    },
    {
        "id": 39,
        "name": "Cooking Oil Pouch",
        "category": "Oils",
        "price": 150,
        "unit": "1 litre",
        "emoji": "🫗",
        "tag": "",
    },
    {
        "id": 40,
        "name": "Coconut Oil Small",
        "category": "Oils",
        "price": 95,
        "unit": "500 ml",
        "emoji": "🫗",
        "tag": "",
    },
    {
        "id": 41,
        "name": "Turmeric Powder",
        "category": "Spices",
        "price": 55,
        "unit": "200 g",
        "emoji": "🌾",
        "tag": "",
    },
    {
        "id": 42,
        "name": "Chilli Powder",
        "category": "Spices",
        "price": 65,
        "unit": "200 g",
        "emoji": "🌶️",
        "tag": "",
    },
    {
        "id": 43,
        "name": "Coriander Powder",
        "category": "Spices",
        "price": 60,
        "unit": "200 g",
        "emoji": "🌿",
        "tag": "",
    },
    {
        "id": 44,
        "name": "Cumin Seeds",
        "category": "Spices",
        "price": 75,
        "unit": "100 g",
        "emoji": "🌿",
        "tag": "",
    },
    {
        "id": 45,
        "name": "Pepper",
        "category": "Spices",
        "price": 110,
        "unit": "100 g",
        "emoji": "⚫",
        "tag": "Popular",
    },
    {
        "id": 46,
        "name": "Mustard Seeds",
        "category": "Spices",
        "price": 35,
        "unit": "100 g",
        "emoji": "🌿",
        "tag": "",
    },
    {
        "id": 47,
        "name": "Sambar Powder",
        "category": "Spices",
        "price": 70,
        "unit": "200 g",
        "emoji": "",
        "tag": "🌶️",
    },
    {
        "id": 48,
        "name": "Rasam Powder",
        "category": "Spices",
        "price": 65,
        "unit": "100 g",
        "emoji": "🌶️",
        "tag": "",
    },
    {
        "id": 49,
        "name": "Garam Masala",
        "category": "Spices",
        "price": 80,
        "unit": "100 g",
        "emoji": "🌶️",
        "tag": "",
    },
    {
        "id": 50,
        "name": "Jeera Powder",
        "category": "Spices",
        "price": 75,
        "unit": "100 g",
        "emoji": "🌿",
        "tag": "",
    },
    {
        "id": 51,
        "name": "Aashirvaad Atta",
        "category": "Flour",
        "price": 275,
        "unit": "5 kg",
        "emoji": "🌾",
        "tag": "Popular",
    },
    {
        "id": 52,
        "name": "Maida",
        "category": "Flour",
        "price": 55,
        "unit": "1 kg",
        "emoji": "🌾",
        "tag": "",
    },
    {
        "id": 53,
        "name": "Rice Flour",
        "category": "Flour",
        "price": 65,
        "unit": "1 kg",
        "emoji": "🌾",
        "tag": "",
    },
    {
        "id": 54,
        "name": "Besan Flour",
        "category": "Flour",
        "price": 80,
        "unit": "500 g",
        "emoji": "🌾",
        "tag": "",
    },
    {
        "id": 55,
        "name": "Corn Flour",
        "category": "Flour",
        "price": 60,
        "unit": "500 g",
        "emoji": "🌾",
        "tag": "",
    },
    {
        "id": 56,
        "name": "Ragi Flour",
        "category": "Flour",
        "price": 75,
        "unit": "500 g",
        "emoji": "🌾",
        "tag": "Healthy",
    },
    {
        "id": 57,
        "name": "Wheat Flour",
        "category": "Flour",
        "price": 65,
        "unit": "1 kg",
        "emoji": "🌾",
        "tag": "",
    },
    {
        "id": 58,
        "name": "Sooji Rava",
        "category": "Flour",
        "price": 55,
        "unit": "500 g",
        "emoji": "🌾",
        "tag": "",
    },
    {
        "id": 59,
        "name": "Multigrain Atta",
        "category": "Flour",
        "price": 180,
        "unit": "1 kg",
        "emoji": "🌾",
        "tag": "",
    },
    {
        "id": 60,
        "name": "Idiyappam Flour",
        "category": "Flour",
        "price": 70,
        "unit": "500 g",
        "emoji": "🌾",
        "tag": "",
    },
    {
        "id": 61,
        "name": "Parle-G Biscuits",
        "category": "Snacks & Biscuits",
        "price": 10,
        "unit": "Pack",
        "emoji": "🍪",
        "tag": "",
    },
    {
        "id": 62,
        "name": "Lays Classic",
        "category": "Snacks & Biscuits",
        "price": 20,
        "unit": "Pack",
        "emoji": "🥔",
        "tag": "",
    },
    {
        "id": 63,
        "name": "Good Day Biscuits",
        "category": "Snacks & Biscuits",
        "price": 30,
        "unit": "Pack",
        "emoji": "🍪",
        "tag": "Popular",
    },
    {
        "id": 64,
        "name": "Marie Gold",
        "category": "Snacks & Biscuits",
        "price": 30,
        "unit": "Pack",
        "emoji": "🍪",
        "tag": "",
    },
    {
        "id": 65,
        "name": "Oreo Biscuits",
        "category": "Snacks & Biscuits",
        "price": 35,
        "unit": "Pack",
        "emoji": "🍪",
        "tag": "",
    },
    {
        "id": 66,
        "name": "Bingo Chips",
        "category": "Snacks & Biscuits",
        "price": 20,
        "unit": "Pack",
        "emoji": "🥔",
        "tag": "",
    },
    {
        "id": 67,
        "name": "Mixture",
        "category": "Snacks & Biscuits",
        "price": 90,
        "unit": "500 g",
        "emoji": "🥨",
        "tag": "Popular",
    },
    {
        "id": 68,
        "name": "Murukku",
        "category": "Snacks & Biscuits",
        "price": 100,
        "unit": "500 g",
        "emoji": "🥨",
        "tag": "",
    },
    {
        "id": 69,
        "name": "Salted Peanuts",
        "category": "Snacks & Biscuits",
        "price": 70,
        "unit": "500 g",
        "emoji": "🥜",
        "tag": "",
    },
    {
        "id": 70,
        "name": "Popcorn",
        "category": "Snacks & Biscuits",
        "price": 50,
        "unit": "Pack",
        "emoji": "🍿",
        "tag": "",
    },
    {
        "id": 71,
        "name": "Coca Cola",
        "category": "Beverages",
        "price": 45,
        "unit": "750 ml",
        "emoji": "🥤",
        "tag": "",
    },
    {
        "id": 72,
        "name": "Pepsi",
        "category": "Beverages",
        "price": 45,
        "unit": "750 ml",
        "emoji": "🥤",
        "tag": "",
    },
    {
        "id": 73,
        "name": "Sprite",
        "category": "Beverages",
        "price": 45,
        "unit": "750 ml",
        "emoji": "🥤",
        "tag": "",
    },
    {
        "id": 74,
        "name": "Fanta",
        "category": "Beverages",
        "price": 45,
        "unit": "750 ml",
        "emoji": "🥤",
        "tag": "",
    },
    {
        "id": 75,
        "name": "Maaza",
        "category": "Beverages",
        "price": 45,
        "unit": "600 ml",
        "emoji": "🥭",
        "tag": "",
    },
    {
        "id": 76,
        "name": "Tata Tea",
        "category": "Beverages",
        "price": 125,
        "unit": "250 g",
        "emoji": "☕",
        "tag": "Popular",
    },
    {
        "id": 77,
        "name": "Coffee Powder",
        "category": "Beverages",
        "price": 180,
        "unit": "250 g",
        "emoji": "☕",
        "tag": "",
    },
    {
        "id": 78,
        "name": "Horlicks",
        "category": "Beverages",
        "price": 220,
        "unit": "500 g",
        "emoji": "🥛",
        "tag": "",
    },
    {
        "id": 79,
        "name": "Boost",
        "category": "Beverages",
        "price": 210,
        "unit": "500 g",
        "emoji": "🥛",
        "tag": "",
    },
    {
        "id": 80,
        "name": "Badam Drink Mix",
        "category": "Beverages",
        "price": 190,
        "unit": "500 g",
        "emoji": "🥛",
        "tag": "",
    },
    {
        "id": 81,
        "name": "Surf Excel",
        "category": "Household",
        "price": 115,
        "unit": "1 kg",
        "emoji": "🧺",
        "tag": "",
    },
    {
        "id": 82,
        "name": "Vim Dishwash",
        "category": "Household",
        "price": 120,
        "unit": "500 ml",
        "emoji": "🧴",
        "tag": "",
    },
    {
        "id": 83,
        "name": "Ariel Detergent",
        "category": "Household",
        "price": 125,
        "unit": "1 kg",
        "emoji": "🧺",
        "tag": "Popular",
    },
    {
        "id": 84,
        "name": "Rin Detergent",
        "category": "Household",
        "price": 95,
        "unit": "1 kg",
        "emoji": "🧺",
        "tag": "",
    },
    {
        "id": 85,
        "name": "Wheel Detergent",
        "category": "Household",
        "price": 85,
        "unit": "1 kg",
        "emoji": "🧺",
        "tag": "",
    },
    {
        "id": 86,
        "name": "Harpic",
        "category": "Household",
        "price": 110,
        "unit": "500 ml",
        "emoji": "🧴",
        "tag": "",
    },
    {
        "id": 87,
        "name": "Lizol",
        "category": "Household",
        "price": 145,
        "unit": "500 ml",
        "emoji": "🧴",
        "tag": "",
    },
    {
        "id": 88,
        "name": "Dishwash Bar",
        "category": "Household",
        "price": 25,
        "unit": "Pack",
        "emoji": "🧼",
        "tag": "",
    },
    {
        "id": 89,
        "name": "Floor Cleaner",
        "category": "Household",
        "price": 130,
        "unit": "1 litre",
        "emoji": "🧴",
        "tag": "",
    },
    {
        "id": 90,
        "name": "Scrub Pad",
        "category": "Household",
        "price": 35,
        "unit": "Pack",
        "emoji": "🧽",
        "tag": "",
    },
    {
        "id": 91,
        "name": "Colgate Toothpaste",
        "category": "Personal Care",
        "price": 95,
        "unit": "100 g",
        "emoji": "🪥",
        "tag": "Popular",
    },
    {
        "id": 92,
        "name": "Closeup Toothpaste",
        "category": "Personal Care",
        "price": 90,
        "unit": "100 g",
        "emoji": "🪥",
        "tag": "",
    },
    {
        "id": 93,
        "name": "Toothbrush",
        "category": "Personal Care",
        "price": 45,
        "unit": "1 pc",
        "emoji": "🪥",
        "tag": "",
    },
    {
        "id": 94,
        "name": "Bath Soap",
        "category": "Personal Care",
        "price": 45,
        "unit": "Pack",
        "emoji": "🧼",
        "tag": "",
    },
    {
        "id": 95,
        "name": "Shampoo",
        "category": "Personal Care",
        "price": 120,
        "unit": "180 ml",
        "emoji": "🧴",
        "tag": "",
    },
    {
        "id": 96,
        "name": "Hair Oil",
        "category": "Personal Care",
        "price": 110,
        "unit": "200 ml",
        "emoji": "🧴",
        "tag": "",
    },
    {
        "id": 97,
        "name": "Face Wash",
        "category": "Personal Care",
        "price": 150,
        "unit": "100 g",
        "emoji": "🧴",
        "tag": "",
    },
    {
        "id": 98,
        "name": "Hand Wash",
        "category": "Personal Care",
        "price": 95,
        "unit": "250 ml",
        "emoji": "🧴",
        "tag": "",
    },
    {
        "id": 99,
        "name": "Talcum Powder",
        "category": "Personal Care",
        "price": 120,
        "unit": "100 g",
        "emoji": "🧴",
        "tag": "",
    },
    {
        "id": 100,
        "name": "Shaving Cream",
        "category": "Personal Care",
        "price": 110,
        "unit": "50 g",
        "emoji": "🧴",
        "tag": "",
    },
]


# ============================================================
# OFFERS
# ============================================================

OFFERS = [
    {
        "title": "Monthly Grocery Pack",
        "text": "Save more on your monthly essentials.",
        "discount": "SPECIAL DEAL",
        "emoji": "🛒",
    },
    {
        "title": "Cooking Oil Offer",
        "text": "Selected cooking oils at special prices.",
        "discount": "SAVE MORE",
        "emoji": "🫗",
    },
    {
        "title": "Snacks Combo",
        "text": "Perfect snacks for the whole family.",
        "discount": "COMBO OFFER",
        "emoji": "🍪",
    },
]


# ============================================================
# CUSTOM CSS
# ============================================================

st.html(
    """
    <style>

    @import url(
        'https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Playfair+Display:wght@600;700&display=swap'
    );

    :root {
        --green: #176B3A;
        --green-dark: #0E4D29;
        --green-light: #E9F7EE;
        --orange: #F59E0B;
        --orange-light: #FFF4D6;
        --cream: #FFFDF7;
        --dark: #172019;
        --muted: #647067;
        --border: #E5E9E3;
        --white: #FFFFFF;
    }

    html {
        scroll-behavior: smooth;
    }

    .stApp {
        background: var(--cream);
    }

    .main {
        background: var(--cream);
    }

    header {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    #MainMenu {
        visibility: hidden;
    }

    .block-container {
        max-width: 1250px;
        padding-top: 1rem;
        padding-bottom: 3rem;
    }

    * {
        font-family: 'DM Sans', sans-serif;
    }


    /* =====================================================
       NAVBAR
    ===================================================== */

    .topbar {
        background: rgba(255,255,255,0.94);
        border: 1px solid var(--border);
        border-radius: 18px;
        padding: 15px 20px;
        margin-bottom: 30px;
        box-shadow: 0 10px 30px rgba(23,32,25,0.06);
    }

    .brand {
        font-size: 22px;
        font-weight: 800;
        color: var(--green);
    }

    .brand span {
        color: var(--orange);
    }

    .mini-text {
        color: var(--muted);
        font-size: 12px;
        margin-top: 3px;
    }


    /* =====================================================
       HERO
    ===================================================== */

    .hero {
        background:
            linear-gradient(
                135deg,
                #EAF7EE 0%,
                #FFFDF7 55%,
                #FFF4D6 100%
            );
        border-radius: 30px;
        padding: 65px 55px;
        border: 1px solid #E0EADF;
        overflow: hidden;
        position: relative;
    }

    .hero-kicker {
        display: inline-block;
        background: white;
        color: var(--green);
        border: 1px solid #D6E8DB;
        padding: 8px 14px;
        border-radius: 50px;
        font-size: 11px;
        font-weight: 800;
        letter-spacing: 1px;
        text-transform: uppercase;
        margin-bottom: 20px;
    }

    .hero-title {
        color: var(--dark);
        font-family: 'Playfair Display', serif;
        font-size: 64px;
        line-height: 1.05;
        letter-spacing: -2px;
        margin: 0;
    }

    .hero-title span {
        color: var(--green);
    }

    .hero-description {
        color: #56635A;
        font-size: 17px;
        line-height: 1.8;
        max-width: 650px;
        margin-top: 22px;
    }

    .hero-note {
        color: var(--green);
        font-size: 12px;
        font-weight: 700;
        margin-top: 20px;
    }

    .hero-visual {
        background: var(--green);
        min-height: 380px;
        border-radius: 28px;
        padding: 28px;
        position: relative;
        overflow: hidden;
    }

    .hero-circle {
        width: 260px;
        height: 260px;
        border-radius: 50%;
        background: rgba(255,255,255,0.10);
        position: absolute;
        right: -80px;
        top: -80px;
    }

    .hero-basket {
        font-size: 120px;
        text-align: center;
        margin-top: 30px;
    }

    .hero-offer {
        background: white;
        border-radius: 18px;
        padding: 18px;
        position: absolute;
        bottom: 25px;
        left: 25px;
        right: 25px;
    }

    .hero-offer-label {
        color: var(--orange);
        font-size: 11px;
        font-weight: 800;
        text-transform: uppercase;
    }

    .hero-offer-title {
        color: var(--dark);
        font-size: 19px;
        font-weight: 800;
        margin-top: 5px;
    }

    .hero-offer-text {
        color: var(--muted);
        font-size: 12px;
        margin-top: 5px;
    }


    /* =====================================================
       BUTTON STYLE
    ===================================================== */

    .section-space {
        padding-top: 75px;
    }

    .section-kicker {
        color: var(--green);
        font-size: 12px;
        font-weight: 800;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        margin-bottom: 10px;
    }

    .section-title {
        color: var(--dark);
        font-family: 'Playfair Display', serif;
        font-size: 42px;
        line-height: 1.15;
        margin: 0;
    }

    .section-description {
        color: var(--muted);
        font-size: 15px;
        line-height: 1.8;
        max-width: 680px;
        margin-top: 14px;
    }


    /* =====================================================
       CATEGORY
    ===================================================== */

    .category-card {
        background: white;
        border: 1px solid var(--border);
        border-radius: 20px;
        padding: 22px 14px;
        text-align: center;
        height: 130px;
        box-shadow: 0 8px 20px rgba(23,32,25,0.04);
    }

    .category-icon {
        font-size: 35px;
    }

    .category-name {
        color: var(--dark);
        font-size: 13px;
        font-weight: 700;
        margin-top: 10px;
    }


    /* =====================================================
       PRODUCT CARD
    ===================================================== */

    .product-card {
        background: white;
        border: 1px solid var(--border);
        border-radius: 20px;
        padding: 18px;
        height: 100%;
        box-shadow: 0 8px 24px rgba(23,32,25,0.045);
        transition: 0.2s ease;
    }

    .product-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 15px 30px rgba(23,32,25,0.09);
    }

    .product-image {
        height: 130px;
        background: #F6F8F3;
        border-radius: 15px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 65px;
    }

    .product-tag {
        display: inline-block;
        background: var(--orange-light);
        color: #A16207;
        border-radius: 30px;
        padding: 5px 9px;
        font-size: 9px;
        font-weight: 800;
        margin-top: 12px;
    }

    .product-name {
        color: var(--dark);
        font-size: 16px;
        font-weight: 800;
        margin-top: 9px;
    }

    .product-unit {
        color: #8A948C;
        font-size: 11px;
        margin-top: 3px;
    }

    .product-price {
        color: var(--green);
        font-size: 19px;
        font-weight: 800;
        margin-top: 10px;
    }

    .qty-number {
        color: #111827;
        background: white;
        border: 1px solid #D1D5DB;
        border-radius: 10px;
        min-height: 38px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 16px;
        font-weight: 800;
        margin-top: 1px;
    }


    /* =====================================================
       OFFER
    ===================================================== */

    .offer-card {
        background: var(--green);
        border-radius: 23px;
        padding: 27px;
        min-height: 190px;
        color: white;
        position: relative;
        overflow: hidden;
    }

    .offer-card.orange {
        background: #D97706;
    }

    .offer-card.light {
        background: #274E35;
    }

    .offer-emoji {
        font-size: 45px;
    }

    .offer-label {
        font-size: 10px;
        font-weight: 800;
        letter-spacing: 1px;
        margin-top: 15px;
        opacity: 0.8;
    }

    .offer-title {
        font-size: 22px;
        font-weight: 800;
        margin-top: 5px;
    }

    .offer-text {
        font-size: 12px;
        opacity: 0.82;
        margin-top: 7px;
        max-width: 250px;
    }


    /* =====================================================
       WHY US
    ===================================================== */

    .why-card {
        background: white;
        border: 1px solid var(--border);
        border-radius: 22px;
        padding: 27px;
        height: 100%;
    }

    .why-icon {
        width: 48px;
        height: 48px;
        background: var(--green-light);
        border-radius: 14px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 22px;
        margin-bottom: 17px;
    }

    .why-title {
        color: var(--dark);
        font-size: 17px;
        font-weight: 800;
    }

    .why-text {
        color: var(--muted);
        font-size: 13px;
        line-height: 1.7;
        margin-top: 8px;
    }


    /* =====================================================
       CART
    ===================================================== */

    .cart-box {
        background: var(--green);
        color: white;
        border-radius: 24px;
        padding: 28px;
        position: sticky;
        top: 20px;
    }

    .cart-title {
        font-size: 22px;
        font-weight: 800;
    }

    .cart-total {
        font-size: 30px;
        font-weight: 800;
        margin-top: 15px;
    }

    .cart-small {
        color: rgba(255,255,255,0.7);
        font-size: 11px;
    }


    /* =====================================================
       CONTACT
    ===================================================== */

    .contact-box {
        background: #172019;
        border-radius: 28px;
        padding: 50px;
        color: white;
    }

    .contact-title {
        font-family: 'Playfair Display', serif;
        font-size: 43px;
        line-height: 1.15;
    }

    .contact-text {
        color: #AAB7AD;
        font-size: 14px;
        line-height: 1.8;
        margin-top: 15px;
    }

    .contact-item {
        background: rgba(255,255,255,0.06);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 16px;
        padding: 16px;
        margin-bottom: 10px;
    }

    .contact-label {
        color: #AAB7AD;
        font-size: 10px;
        text-transform: uppercase;
        font-weight: 800;
    }

    .contact-value {
        color: white;
        font-size: 14px;
        font-weight: 700;
        margin-top: 4px;
    }


    /* =====================================================
       FOOTER
    ===================================================== */

    .footer {
        border-top: 1px solid var(--border);
        margin-top: 70px;
        padding-top: 30px;
    }

    .footer-brand {
        color: var(--green);
        font-size: 20px;
        font-weight: 800;
    }

    .footer-text {
        color: var(--muted);
        font-size: 12px;
        line-height: 1.7;
        margin-top: 8px;
    }

    .copyright {
        color: #8A948C;
        font-size: 11px;
        margin-top: 25px;
    }


    /* =====================================================
       MOBILE
    ===================================================== */

    @media (max-width: 800px) {

        .hero {
            padding: 38px 24px;
        }

        .hero-title {
            font-size: 43px;
        }

        .hero-description {
            font-size: 15px;
        }

        .hero-visual {
            margin-top: 25px;
            min-height: 330px;
        }

        .section-title {
            font-size: 34px;
        }

        .contact-box {
            padding: 30px 22px;
        }

        .contact-title {
            font-size: 35px;
        }

    }

    </style>
    """
)


# ============================================================
# NAVBAR
# ============================================================

st.html(
    """
    <div class="topbar">
        <div style="
            display:flex;
            justify-content:space-between;
            align-items:center;
            gap:20px;
        ">

            <div>
                <div class="brand">
                    BALAJI <span>MALIGAI</span>
                </div>

                <div class="mini-text">
                    Your everyday grocery store
                </div>
            </div>

            <div style="
                background:#E9F7EE;
                color:#176B3A;
                padding:9px 14px;
                border-radius:30px;
                font-size:11px;
                font-weight:800;
            ">
                🟢 OPEN TODAY
            </div>

        </div>
    </div>
    """
)


# ============================================================
# HERO
# ============================================================

hero_left, hero_right = st.columns(
    [1.15, 0.85],
    gap="large"
)

with hero_left:

    st.html(
        """
        <div class="hero">

            <div class="hero-kicker">
                🛒 BALAJI MALIGAI
            </div>

            <h1 class="hero-title">
                Everything Your
                <span>Home Needs.</span>
            </h1>

            <div class="hero-description">
                Quality groceries, everyday essentials and
                household needs — all available at your
                neighbourhood Balaji Maligai.
            </div>

            <div class="hero-note">
                ✓ Fresh products &nbsp;&nbsp;
                ✓ Fair prices &nbsp;&nbsp;
                ✓ Friendly service
            </div>

        </div>
        """
    )

    st.write("")

    c1, c2 = st.columns(2)

    with c1:
        if st.button(
            "🛒  Shop Products",
            use_container_width=True
        ):
            st.session_state.selected_category = "All"
            st.toast("Products are ready below!")

    with c2:
        message = (
            "Hello Balaji Maligai! "
            "I would like to know today's offers."
        )

        whatsapp_url = (
            "https://wa.me/"
            + WHATSAPP_NUMBER
            + "?text="
            + urllib.parse.quote(message)
        )

        st.link_button(
            "📲  WhatsApp Us",
            whatsapp_url,
            use_container_width=True
        )


with hero_right:

    st.html(
        """
        <div class="hero-visual">

            <div class="hero-circle"></div>

            <div style="
                color:white;
                font-size:11px;
                font-weight:800;
                letter-spacing:1.5px;
                text-align:center;
            ">
                DAILY ESSENTIALS
            </div>

            <div class="hero-basket">
                🛒
            </div>

            <div style="
                text-align:center;
                color:white;
                font-size:18px;
                font-weight:800;
            ">
                Fresh. Simple. Affordable.
            </div>

            <div class="hero-offer">

                <div class="hero-offer-label">
                    Today's Highlight
                </div>

                <div class="hero-offer-title">
                    Grocery Shopping Made Easy
                </div>

                <div class="hero-offer-text">
                    Browse your essentials and send your
                    order directly through WhatsApp.
                </div>

            </div>

        </div>
        """
    )


# ============================================================
# QUICK STATS
# ============================================================

st.write("")

stats = st.columns(4)

stat_data = [
    ("🛒", "Everyday Essentials"),
    ("🌾", "Quality Products"),
    ("💰", "Fair Pricing"),
    ("📲", "Easy Ordering"),
]

for col, (icon, text) in zip(stats, stat_data):

    with col:

        st.html(
            f"""
            <div style="
                background:white;
                border:1px solid #E5E9E3;
                border-radius:18px;
                padding:18px;
                text-align:center;
            ">

                <div style="font-size:25px;">
                    {icon}
                </div>

                <div style="
                    color:#172019;
                    font-size:12px;
                    font-weight:700;
                    margin-top:8px;
                ">
                    {text}
                </div>

            </div>
            """
        )


# ============================================================
# CATEGORIES
# ============================================================

st.html(
    """
    <div class="section-space">

        <div class="section-kicker">
            SHOP BY CATEGORY
        </div>

        <div class="section-title">
            Everything in One Place.
        </div>

        <div class="section-description">
            From kitchen staples to everyday household products,
            find what your family needs at Balaji Maligai.
        </div>

    </div>
    """
)


CATEGORIES = [
    ("🍚", "Rice & Grains"),
    ("🫘", "Dals & Pulses"),
    ("🧂", "Staples"),
    ("🫗", "Oils"),
    ("🌶️", "Spices"),
    ("🌾", "Flour"),
    ("🍪", "Snacks & Biscuits"),
    ("🥤", "Beverages"),
    ("🧺", "Household"),
    ("🧴", "Personal Care"),
]


category_cols = st.columns(4)

for i, (icon, name) in enumerate(CATEGORIES):

    with category_cols[i % 4]:

        if st.button(
            f"{icon}  {name}",
            key=f"category_{i}",
            use_container_width=True
        ):
            st.session_state.selected_category = name

        st.write("")


# ============================================================
# OFFERS
# ============================================================

st.html(
    """
    <div class="section-space">

        <div class="section-kicker">
            SPECIAL OFFERS
        </div>

        <div class="section-title">
            Deals for Your Daily Shopping.
        </div>

    </div>
    """
)


offer_cols = st.columns(3)

for i, offer in enumerate(OFFERS):

    with offer_cols[i]:

        style_class = ""

        if i == 1:
            style_class = "orange"

        if i == 2:
            style_class = "light"

        st.html(
            f"""
            <div class="offer-card {style_class}">

                <div class="offer-emoji">
                    {offer["emoji"]}
                </div>

                <div class="offer-label">
                    {offer["discount"]}
                </div>

                <div class="offer-title">
                    {offer["title"]}
                </div>

                <div class="offer-text">
                    {offer["text"]}
                </div>

            </div>
            """
        )


# ============================================================
# PRODUCTS + CART
# ============================================================

st.html(
    """
    <div class="section-space">

        <div class="section-kicker">
            OUR PRODUCTS
        </div>

        <div class="section-title">
            Shop Your Essentials.
        </div>

        <div class="section-description">
            Choose your products, add them to your cart and
            send your shopping list directly to Balaji Maligai.
        </div>

    </div>
    """
)


# Category filter

available_categories = ["All"] + [
    item[1] for item in CATEGORIES
]

selected = st.selectbox(
    "Choose a category",
    available_categories,
    index=available_categories.index(
        st.session_state.selected_category
    )
    if st.session_state.selected_category
    in available_categories
    else 0,
)

st.session_state.selected_category = selected


# Filter products

if selected == "All":
    filtered_products = PRODUCTS
else:
    filtered_products = [
        product
        for product in PRODUCTS
        if product["category"] == selected
    ]


# Product and cart layout

product_area, cart_area = st.columns(
    [2.25, 0.75],
    gap="large"
)


# ============================================================
# PRODUCT LIST
# ============================================================

with product_area:

    product_cols = st.columns(3)

    for index, product in enumerate(filtered_products):

        with product_cols[index % 3]:

            tag_html = ""

            if product["tag"]:
                tag_html = f"""
                    <div class="product-tag">
                        {product["tag"]}
                    </div>
                """

            st.html(
                f"""
                <div class="product-card">

                    <div class="product-image">
                        {product["emoji"]}
                    </div>

                    {tag_html}

                    <div class="product-name">
                        {product["name"]}
                    </div>

                    <div class="product-unit">
                        {product["unit"]}
                    </div>

                    <div class="product-price">
                        ₹{product["price"]}
                    </div>

                </div>
                """
            )

            product_id = product["id"]

            if st.button(
                "＋ Add to Cart",
                key=f"add_{product_id}",
                use_container_width=True
            ):

                if product_id not in st.session_state.cart:
                    st.session_state.cart[product_id] = 1
                else:
                    st.session_state.cart[product_id] += 1

                st.toast(
                    f"{product['name']} added to cart!"
                )
                st.rerun()

            # Quantity controls appear directly below each product.
            current_quantity = st.session_state.cart.get(product_id, 0)

            if current_quantity > 0:

                qty_left, qty_number, qty_right = st.columns([1, 1, 1])

                with qty_left:
                    if st.button(
                        "−",
                        key=f"product_minus_{product_id}",
                        use_container_width=True
                    ):
                        if current_quantity > 1:
                            st.session_state.cart[product_id] -= 1
                        else:
                            del st.session_state.cart[product_id]
                        st.rerun()

                with qty_number:
                    st.markdown(
                        f'<div class="qty-number">{current_quantity}</div>',
                        unsafe_allow_html=True
                    )

                with qty_right:
                    if st.button(
                        "+",
                        key=f"product_plus_{product_id}",
                        use_container_width=True
                    ):
                        st.session_state.cart[product_id] += 1
                        st.rerun()



# ============================================================
# CART
# ============================================================

with cart_area:

    cart_items = []

    total = 0
    item_count = 0

    for product_id, quantity in st.session_state.cart.items():

        product = next(
            (
                item
                for item in PRODUCTS
                if item["id"] == product_id
            ),
            None
        )

        if product:

            subtotal = (
                product["price"] * quantity
            )

            total += subtotal
            item_count += quantity

            cart_items.append(
                {
                    "product": product,
                    "quantity": quantity,
                    "subtotal": subtotal,
                }
            )


    st.html(
        f"""
        <div class="cart-box">

            <div class="cart-title">
                🛒 Your Cart
            </div>

            <div class="cart-small" style="margin-top:6px;">
                {item_count} item(s)
            </div>

            <div class="cart-total">
                ₹{total}
            </div>

            <div class="cart-small">
                Estimated total
            </div>

        </div>
        """
    )

    st.write("")


    if not cart_items:

        st.info(
            "Your cart is empty. Add some products!"
        )

    else:

        for item in cart_items:

            product = item["product"]
            quantity = item["quantity"]

            st.markdown(
                f"**{product['name']}**  \n"
                f"₹{product['price']} × {quantity} = "
                f"₹{item['subtotal']}"
            )

            st.divider()


        # WhatsApp order

        order_lines = [
            "Hello Balaji Maligai! 👋",
            "",
            "I would like to order:",
            "",
        ]

        for item in cart_items:

            product = item["product"]

            order_lines.append(
                f"• {product['name']} "
                f"({product['unit']}) × "
                f"{item['quantity']} = "
                f"₹{item['subtotal']}"
            )

        order_lines.extend(
            [
                "",
                f"Estimated Total: ₹{total}",
                "",
                "Please confirm availability and delivery/pickup details.",
            ]
        )

        order_message = "\n".join(order_lines)

        whatsapp_order_url = (
            "https://wa.me/"
            + WHATSAPP_NUMBER
            + "?text="
            + urllib.parse.quote(order_message)
        )

        st.link_button(
            "📲 Order on WhatsApp",
            whatsapp_order_url,
            use_container_width=True
        )

        if st.button(
            "🗑️ Clear Cart",
            use_container_width=True
        ):

            st.session_state.cart = {}

            st.rerun()


# ============================================================
# WHY BALAJI MALIGAI
# ============================================================

st.html(
    """
    <div class="section-space">

        <div class="section-kicker">
            WHY SHOP WITH US?
        </div>

        <div class="section-title">
            Simple Shopping. Trusted Service.
        </div>

    </div>
    """
)


why_items = [
    (
        "🌿",
        "Quality Products",
        "We focus on everyday products that families use regularly."
    ),
    (
        "💰",
        "Fair Prices",
        "Get your daily essentials at practical neighbourhood prices."
    ),
    (
        "🤝",
        "Friendly Service",
        "A local shop where customers are treated with care."
    ),
    (
        "📲",
        "Easy Ordering",
        "Send your shopping list through WhatsApp with just a few taps."
    ),
]


why_cols = st.columns(4)

for i, (icon, title, text) in enumerate(why_items):

    with why_cols[i]:

        st.html(
            f"""
            <div class="why-card">

                <div class="why-icon">
                    {icon}
                </div>

                <div class="why-title">
                    {title}
                </div>

                <div class="why-text">
                    {text}
                </div>

            </div>
            """
        )


# ============================================================
# HOW TO ORDER
# ============================================================

st.html(
    """
    <div class="section-space">

        <div class="section-kicker">
            HOW TO ORDER
        </div>

        <div class="section-title">
            Your Grocery Order in 3 Easy Steps.
        </div>

    </div>
    """
)


step_cols = st.columns(3)

steps = [
    (
        "01",
        "Choose",
        "Browse the products and add what you need to your cart."
    ),
    (
        "02",
        "Send",
        "Click Order on WhatsApp and send your shopping list."
    ),
    (
        "03",
        "Confirm",
        "We'll confirm availability and pickup or delivery details."
    ),
]


for i, (number, title, text) in enumerate(steps):

    with step_cols[i]:

        st.html(
            f"""
            <div style="
                background:white;
                border:1px solid #E5E9E3;
                border-radius:22px;
                padding:28px;
                height:180px;
            ">

                <div style="
                    width:42px;
                    height:42px;
                    background:#E9F7EE;
                    color:#176B3A;
                    border-radius:50%;
                    display:flex;
                    align-items:center;
                    justify-content:center;
                    font-size:12px;
                    font-weight:800;
                ">
                    {number}
                </div>

                <div style="
                    color:#172019;
                    font-size:19px;
                    font-weight:800;
                    margin-top:18px;
                ">
                    {title}
                </div>

                <div style="
                    color:#647067;
                    font-size:12px;
                    line-height:1.6;
                    margin-top:7px;
                ">
                    {text}
                </div>

            </div>
            """
        )


# ============================================================
# CONTACT SECTION
# ============================================================

st.html(
    f"""
    <div class="section-space">

        <div class="contact-box">

            <div class="section-kicker" style="color:#FBBF24;">
                VISIT BALAJI MALIGAI
            </div>

            <div class="contact-title">
                Need groceries?
                <br>
                We're here for you.
            </div>

            <div class="contact-text">
                Visit our shop or send your grocery requirements
                through WhatsApp.
            </div>

            <div style="height:25px;"></div>

            <div class="contact-item">

                <div class="contact-label">
                    📍 Address
                </div>

                <div class="contact-value">
                    {SHOP_ADDRESS}
                </div>

            </div>

            <div class="contact-item">

                <div class="contact-label">
                    📞 Phone
                </div>

                <div class="contact-value">
                    {SHOP_DISPLAY_PHONE}
                </div>

            </div>

            <div class="contact-item">

                <div class="contact-label">
                    ⏰ Opening Hours
                </div>

                <div class="contact-value">
                    {SHOP_TIMING}
                </div>

            </div>

        </div>

    </div>
    """
)


# ============================================================
# CONTACT BUTTONS
# ============================================================

contact_message = (
    "Hello Balaji Maligai! 👋 "
    "I would like to know about your products and offers."
)

contact_whatsapp = (
    "https://wa.me/"
    + WHATSAPP_NUMBER
    + "?text="
    + urllib.parse.quote(contact_message)
)

c1, c2 = st.columns(2)

with c1:

    st.link_button(
        "📲 Chat on WhatsApp",
        contact_whatsapp,
        use_container_width=True
    )

with c2:

    st.link_button(
        "📞 Call Balaji Maligai",
        "tel:+91" + SHOP_PHONE[-10:],
        use_container_width=True
    )


# ============================================================
# FOOTER
# ============================================================

current_year = datetime.now().year

st.html(
    f"""
    <div class="footer">

        <div style="
            display:flex;
            justify-content:space-between;
            gap:30px;
            flex-wrap:wrap;
        ">

            <div>

                <div class="footer-brand">
                    BALAJI MALIGAI
                </div>

                <div class="footer-text">
                    Your trusted neighbourhood grocery store
                    for everyday essentials.
                </div>

            </div>

            <div style="
                color:#647067;
                font-size:12px;
                text-align:right;
            ">
                🛒 Groceries &nbsp; • &nbsp;
                🏠 Household &nbsp; • &nbsp;
                📲 WhatsApp Orders
            </div>

        </div>

        <div class="copyright">
            © {current_year} Balaji Maligai.
            All rights reserved.
        </div>

    </div>
    """
)

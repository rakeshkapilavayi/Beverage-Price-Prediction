import streamlit as st
from prediction_helper import predict

# Page configuration
st.set_page_config(
    page_title="Beverage Price Predictor",
    page_icon="🥤",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    div[data-testid="stForm"] {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
    }
    label {
        color: #333 !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
    }
    .stSelectbox label, .stNumberInput label {
        color: #333 !important;
    }
    h1 {
        color: white;
        text-align: center;
        font-size: 3rem;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }
    .subtitle {
        color: #f0f0f0;
        text-align: center;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-size: 1.2rem;
        font-weight: bold;
        padding: 0.75rem;
        border-radius: 10px;
        border: none;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        transition: all 0.3s;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.3);
    }
    .section-header {
        color: #667eea;
        font-size: 1.5rem;
        font-weight: bold;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
        border-bottom: 3px solid #667eea;
        padding-bottom: 0.5rem;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("# 🥤 Beverage Price Range Predictor")
st.markdown('<p class="subtitle">Predict the optimal price range based on consumer preferences and behavior patterns</p>', unsafe_allow_html=True)

# Create form
with st.form("prediction_form"):
    # Personal Information Section
    st.markdown('<div class="section-header">👤 Personal Information</div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input("Age", min_value=18, max_value=70, value=25, help="Enter your age")
        gender = st.selectbox("Gender", ["Male", "Female"])
    
    with col2:
        zone = st.selectbox("Zone", ["Urban", "Rural", "Metro", "Semi-Urban"], help="Your residential area type")
        occupation = st.selectbox("Occupation", ["Working Professional", "Student", "Entrepreneur", "Retired"])
    
    with col3:
        income_levels = st.selectbox("Income Level", ["<10L", "10L - 15L", "16L - 25L", "26L - 35L", "> 35L"], help="Annual income in lakhs")
        health_concerns = st.selectbox("Health Consciousness", 
                                       ["Low (Not very concerned)", 
                                        "Medium (Moderately health-conscious)", 
                                        "High (Very health-conscious)"])
    
    # Consumption Behavior Section
    st.markdown('<div class="section-header">🍹 Consumption Behavior</div>', unsafe_allow_html=True)
    col4, col5, col6 = st.columns(3)
    
    with col4:
        consume_frequency = st.selectbox("Consumption Frequency (Weekly)", 
                                         ["0-2 times", "3-4 times", "5-7 times"],
                                         help="How often do you consume beverages per week")
        preferable_consumption_size = st.selectbox("Preferred Size", ["Small", "Medium", "Large"])
    
    with col5:
        typical_consumption_situations = st.selectbox("Typical Consumption Situation", [
            "Active (eg. Sports, gym)",
            "Social (eg. Parties)",
            "Casual (eg. At home)"
        ])
        purchase_channel = st.selectbox("Purchase Channel", ["Online", "Retail Store"])
    
    with col6:
        packaging_preference = st.selectbox("Packaging Preference", 
                                           ["Simple", "Premium", "Eco-Friendly"],
                                           help="Your preferred packaging style")
        flavor_preference = st.selectbox("Flavor Preference", ["Traditional", "Exotic"])
    
    # Brand Preferences Section
    st.markdown('<div class="section-header">🏷️ Brand Preferences</div>', unsafe_allow_html=True)
    col7, col8, col9 = st.columns(3)
    
    with col7:
        current_brand = st.selectbox("Current Brand Type", ["Established", "Newcomer"])
    
    with col8:
        awareness_of_other_brands = st.selectbox("Brand Awareness", 
                                                 ["0 to 1", "2 to 4", "above 4"],
                                                 help="How many other brands are you aware of?")
    
    with col9:
        reasons_for_choosing_brands = st.selectbox("Primary Brand Selection Factor", 
                                                   ["Price", "Quality", "Availability", "Brand Reputation"])
    
    # Submit button
    st.markdown("<br>", unsafe_allow_html=True)
    submitted = st.form_submit_button("🎯 Predict Price Range")

# Process prediction
if submitted:
    input_dict = {
        "age": age,
        "gender": gender,
        "zone": zone,
        "occupation": occupation,
        "income_levels": income_levels,
        "consume_frequency(weekly)": consume_frequency,
        "health_concerns": health_concerns,
        "preferable_consumption_size": preferable_consumption_size,
        "awareness_of_other_brands": awareness_of_other_brands,
        "current_brand": current_brand,
        "reasons_for_choosing_brands": reasons_for_choosing_brands,
        "flavor_preference": flavor_preference,
        "purchase_channel": purchase_channel,
        "packaging_preference": packaging_preference,
        "typical_consumption_situations": typical_consumption_situations
    }
    
    with st.spinner('Analyzing your preferences...'):
        price_range = predict(input_dict)
    
    # Display result with animation
    st.balloons()
    st.markdown(f"""
        <div style='background: white; padding: 2rem; border-radius: 15px; text-align: center; 
                    box-shadow: 0 8px 32px rgba(0,0,0,0.1); margin-top: 2rem;'>
            <h2 style='color: #667eea; margin-bottom: 1rem;'>🎯 Prediction Result</h2>
            <h1 style='color: #764ba2; font-size: 3rem; margin: 0;'>{price_range}</h1>
            <p style='color: #666; margin-top: 1rem; font-size: 1.1rem;'>
                This is the predicted optimal price range based on your profile
            </p>
        </div>
    """, unsafe_allow_html=True)

import joblib
import pandas as pd
import numpy as np

MODEL_PATH = "artifacts/model_data.joblib"
model = joblib.load(MODEL_PATH)

# Your model expects these exact 37 columns:
TRAIN_FEATURES = [
    'income_levels', 'consume_frequency(weekly)', 'preferable_consumption_size',
    'health_concerns', 'age_group', 'cf_ab_score', 'zas_score', 'bsi',
    'gender_F', 'gender_M', 'zone_Metro', 'zone_Rural', 'zone_Semi-Urban', 'zone_Urban',
    'occupation_Entrepreneur', 'occupation_Retired', 'occupation_Student',
    'occupation_Working Professional', 'current_brand_Established',
    'current_brand_Newcomer', 'awareness_of_other_brands_0 to 1',
    'awareness_of_other_brands_2 to 4', 'awareness_of_other_brands_above 4',
    'reasons_for_choosing_brands_Availability', 'reasons_for_choosing_brands_Brand Reputation',
    'reasons_for_choosing_brands_Price', 'reasons_for_choosing_brands_Quality',
    'flavor_preference_Exotic', 'flavor_preference_Traditional', 'purchase_channel_Online',
    'purchase_channel_Retail Store', 'packaging_preference_Eco-Friendly',
    'packaging_preference_Premium', 'packaging_preference_Simple',
    'typical_consumption_situations_Active (eg. Sports, gym)',
    'typical_consumption_situations_Casual (eg. At home)',
    'typical_consumption_situations_Social (eg. Parties)'
]

def preprocess_input(input_dict):
    """Convert raw user input into the model's expected 37 features."""

    # --- Numeric conversions ---
    freq_map = {'0-2 times': 1, '3-4 times': 2, '5-7 times': 3}
    awareness_map = {'0 to 1': 1, '2 to 4': 2, 'above 4': 3}
    zone_map = {"Urban": 3, "Metro": 4, "Rural": 1, "Semi-Urban": 2}
    income_map = {"<10L": 1, "10L - 15L": 2, "16L - 25L": 3, "26L - 35L": 4, "> 35L": 5}
    health_map = {
        'Low (Not very concerned)': 0,
        'Medium (Moderately health-conscious)': 1,
        'High (Very health-conscious)': 2
    }

    # Derived scores
    fs = freq_map[input_dict['consume_frequency(weekly)']]
    as_ = awareness_map[input_dict['awareness_of_other_brands']]
    cf_ab_score = round((fs / (as_ + fs)), 2)
    zas_score = zone_map[input_dict['zone']] * income_map[input_dict['income_levels']]
    bsi = (cf_ab_score + zas_score) / 2

    # Age grouping
    age = input_dict['age']
    if 18 <= age <= 25:
        age_group = 1
    elif 26 <= age <= 35:
        age_group = 2
    elif 36 <= age <= 45:
        age_group = 3
    elif 46 <= age <= 55:
        age_group = 4
    elif 56 <= age <= 70:
        age_group = 5
    else:
        age_group = 6

    # Consumption size mapping
    size_map = {'Small': 0, 'Medium': 1, 'Large': 2}
    
    # Start with label-encoded features
    features = {
        'income_levels': income_map[input_dict['income_levels']],
        'consume_frequency(weekly)': fs,
        'preferable_consumption_size': size_map[input_dict['preferable_consumption_size']],
        'health_concerns': health_map[input_dict['health_concerns']],
        'age_group': age_group,
        'cf_ab_score': cf_ab_score,
        'zas_score': zas_score,
        'bsi': bsi
    }

    # --- One-hot encoding for categorical features ---
    one_hot = {col: 0 for col in TRAIN_FEATURES if col not in features}

    # gender
    if input_dict['gender'] == 'Male':
        one_hot['gender_M'] = 1
    else:
        one_hot['gender_F'] = 1

    # zone
    zone_col = f"zone_{input_dict['zone']}"
    if zone_col in one_hot:
        one_hot[zone_col] = 1

    # occupation
    occ_col = f"occupation_{input_dict['occupation']}"
    if occ_col in one_hot:
        one_hot[occ_col] = 1

    # current brand
    brand_col = f"current_brand_{input_dict['current_brand']}"
    if brand_col in one_hot:
        one_hot[brand_col] = 1

    # awareness
    aware_col = f"awareness_of_other_brands_{input_dict['awareness_of_other_brands']}"
    if aware_col in one_hot:
        one_hot[aware_col] = 1

    # reasons for choosing brands
    reason_col = f"reasons_for_choosing_brands_{input_dict['reasons_for_choosing_brands']}"
    if reason_col in one_hot:
        one_hot[reason_col] = 1

    # flavor
    flavor_col = f"flavor_preference_{input_dict['flavor_preference']}"
    if flavor_col in one_hot:
        one_hot[flavor_col] = 1

    # purchase channel
    purchase_col = f"purchase_channel_{input_dict['purchase_channel']}"
    if purchase_col in one_hot:
        one_hot[purchase_col] = 1

    # packaging
    package_col = f"packaging_preference_{input_dict['packaging_preference']}"
    if package_col in one_hot:
        one_hot[package_col] = 1

    # typical consumption
    situation_col = f"typical_consumption_situations_{input_dict['typical_consumption_situations']}"
    if situation_col in one_hot:
        one_hot[situation_col] = 1

    # Merge numeric and categorical
    features.update(one_hot)

    # Convert to DataFrame in exact order
    df = pd.DataFrame([[features[col] for col in TRAIN_FEATURES]], columns=TRAIN_FEATURES)
    return df.values


def predict(input_dict):
    label_map = {
        0: '₹50 - ₹100',
        1: '₹100 - ₹150',
        2: '₹150 - ₹200',
        3: '₹200 - ₹250'
    }

    input_array = preprocess_input(input_dict)
    prediction = model.predict(input_array)
    return label_map[int(prediction[0])]
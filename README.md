# 🥤 Beverage Price Prediction

An interactive web application built with Streamlit that predicts the optimal market price range for beverages based on customer demographics, preferences, and lifestyle choices. By leveraging a trained machine learning model, the app helps beverage companies quickly estimate price points for different customer segments.

---

## 🌐 Live Website

You can try the tool live here: **[Beverage Price Prediction](https://rakesh-project-beverage-price-predictor.streamlit.app/)**

## 🎥 Presentation

Watch the full project presentation here: **[Beverage Price Prediction Presentation]()**

## 📊 MLflow Dashboard

Explore the live MLflow dashboard here: **[Beverage Price Prediction Dashboard](https://dagshub.com/rakeshkapilavayi978/mlflow-dagshub-demo.mlflow/#/experiments/3?searchFilter=&orderByKey=attributes.start_time&orderByAsc=false&startTime=ALL&lifecycleFilter=Active&modelVersionFilter=All+Runs&datasetsFilter=W10%3D)**

---

## 🛠 Features

* ✨ Sleek, responsive Streamlit interface with modern gradient design
* 📊 Predicts beverage price ranges based on demographics & consumption patterns
* 🤖 Uses pre-trained machine learning models serialized with Joblib
* 🔄 Handles categorical and numerical inputs with one-hot encoding for accurate results
* ⚡ Fully client-side — no backend or database required
* 🚀 Fast, lightweight, and easy to run locally
* 📱 Mobile-friendly responsive design

---

## 📂 Project Structure

```
Beverage_Price_Prediction/
│
├── artifacts/                  # Serialized ML model
│   └── model_data.joblib       # Trained model for price prediction
│
├── LICENSE                     # Apache License 2.0
├── README.md                   # This documentation
├── main.py                     # Streamlit app with UI logic
├── prediction_helper.py        # Preprocessing & prediction functions
└── requirements.txt            # Python dependencies
```

---

## 🚀 How to Run Locally

### Prerequisites:
* Python 3.8+
* pip package manager

### Installation Steps:

1. **Clone the repository**:

```bash
git clone https://github.com/rakeshkapilavayi/Beverage-Price-Prediction.git
cd Beverage-Price-Prediction
```

2. **Install dependencies**:

```bash
pip install -r requirements.txt
```

3. **Run the Streamlit app**:

```bash
streamlit run main.py
```

4. **Open your browser** and navigate to `http://localhost:8501`

---

## 🧠 How It Works

### 1. User Inputs

The application collects comprehensive customer information across three categories:

#### 👤 Personal Information
* **Age** (18-70 years)
* **Gender** (Male/Female)
* **Zone** (Urban, Rural, Metro, Semi-Urban)
* **Occupation** (Working Professional, Student, Entrepreneur, Retired)
* **Income Levels** (<10L, 10L-15L, 16L-25L, 26L-35L, >35L)
* **Health Concerns** (Low, Medium, High)

#### 🍹 Consumption Behavior
* **Consumption Frequency (Weekly)** (0-2 times, 3-4 times, 5-7 times)
* **Preferable Consumption Size** (Small, Medium, Large)
* **Typical Consumption Situations** (Active, Social, Casual)
* **Purchase Channel** (Online/Retail Store)
* **Packaging Preference** (Simple, Premium, Eco-Friendly)
* **Flavor Preference** (Traditional/Exotic)

#### 🏷️ Brand Preferences
* **Current Brand** (Established/Newcomer)
* **Awareness of Other Brands** (0 to 1, 2 to 4, above 4)
* **Reasons for Choosing Brands** (Price, Quality, Availability, Brand Reputation)

### 2. Price Prediction Logic

#### Feature Engineering:
The application creates several derived features to capture complex behavioral patterns:

* **cf_ab_score**: Consumption Frequency to Brand Awareness Score
  ```
  cf_ab_score = consumption_frequency / (awareness + consumption_frequency)
  ```

* **zas_score**: Zone-Adjusted Socioeconomic Score
  ```
  zas_score = zone_value × income_level
  ```

* **bsi**: Behavioral Spending Index
  ```
  bsi = (cf_ab_score + zas_score) / 2
  ```

#### Processing Pipeline:
1. All categorical inputs are one-hot encoded (37 total features)
2. Numerical features are label-encoded with specific mappings
3. Derived features are calculated from multiple input combinations
4. The complete feature vector is passed to the trained ML model
5. Model predicts the price category index (0-3)
6. Index is mapped to actual price range in Indian Rupees

### 3. Prediction Output

The model classifies customers into one of four price ranges:

| Category | Price Range |
|----------|-------------|
| 0        | ₹50 - ₹100  |
| 1        | ₹100 - ₹150 |
| 2        | ₹150 - ₹200 |
| 3        | ₹200 - ₹250 |

---

## 🎨 Application Interface

The application features a modern, gradient-based design with:
* Purple gradient background for visual appeal
* Organized multi-column layout for better UX
* Section-based grouping of related inputs
* Animated results display with balloons celebration
* Responsive design that works on all devices

---

## 📦 Dependencies

```
streamlit>=1.28.0
pandas>=2.0.0
numpy>=1.24.0
joblib>=1.3.0
scikit-learn>=1.3.0
```

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **Apache License 2.0**. See the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Rakesh Kapilavayi**

* GitHub: [@rakeshkapilavayi](https://github.com/rakeshkapilavayi)
* Live App: [Beverage Price Predictor](https://rakesh-project-beverage-price-predictor.streamlit.app/)

---

## 📧 Contact

For questions, suggestions, or collaboration opportunities, feel free to reach out!

---

<div align="center">

**Smart pricing for smarter decisions — instantly estimate beverage prices for any customer profile.**

⭐ Star this repo if you find it helpful!

</div>
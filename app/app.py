import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# Load the model and encoder
@st.cache_resource
def load_model():
    model_path = Path("Model/obesity_prediction_model.joblib")
    encoder_path = Path("Model/target_encoder.joblib")
    return joblib.load(model_path), joblib.load(encoder_path)

# Session state for navigation and form storage
if 'page' not in st.session_state:
    st.session_state.page = 1
    st.session_state.form_data = {}
    st.session_state.prediction = None

def next_page():
    st.session_state.page += 1

def prev_page():
    st.session_state.page -= 1

def store_data(key, value):
    st.session_state.form_data[key] = value

# Apply custom CSS for better UI
st.markdown("""
    <style>
        .main-container {
            max-width: 600px;
            margin: auto;
            background-color: #ffffff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
        }
        .stButton button {
            background-color: #4b7bec;
            color: white;
            border-radius: 8px;
            padding: 10px 20px;
            border: none;
            cursor: pointer;
        }
        .stButton button:hover {
            background-color: #3867d6;
        }
        .stProgress > div > div > div > div {
            background-color: #4b7bec;
        }
        body {
            background-color: #f0f2f6;
        }
    </style>
""", unsafe_allow_html=True)

def main():
    st.markdown("<div class='main-container'>", unsafe_allow_html=True)
    st.title("Obesity Risk Prediction")
    st.write("Complete the form to get your prediction")

    # Progress navigation
    tabs = ["Personal Info", "Eating Habits", "Physical Activity", "Additional Info"]
    progress = st.progress((st.session_state.page - 1) / (len(tabs) - 1))
    st.markdown(f"### {tabs[st.session_state.page - 1]}")

    if st.session_state.page == 1:
        gender = st.radio("Gender", ["Female", "Male"], index=["Female", "Male"].index(st.session_state.form_data.get("Gender", "Female")), horizontal=True)
        store_data("Gender", gender)

        age = st.text_input("Age", st.session_state.form_data.get("Age", ""))
        store_data("Age", age)

        height = st.text_input("Height (m)", st.session_state.form_data.get("Height", ""))
        store_data("Height", height)

        weight = st.text_input("Weight (kg)", st.session_state.form_data.get("Weight", ""))
        store_data("Weight", weight)

        family_history = st.radio("Family History with Overweight", ["Yes", "No"], index=["Yes", "No"].index(st.session_state.form_data.get("family_history_with_overweight", "No")), horizontal=True)
        store_data("family_history_with_overweight", family_history)

        col1, col2 = st.columns([1, 3])
        with col1:
            st.button("Back", disabled=True)
        with col2:
            st.button("Next", on_click=next_page)

    elif st.session_state.page == 2:
        favc = st.radio("High Caloric Food Consumption", ["Yes", "No"], index=["Yes", "No"].index(st.session_state.form_data.get("FAVC", "No")), horizontal=True)
        store_data("FAVC", favc)

        fcvc = st.slider("Vegetable Consumption Frequency", 1, 3, st.session_state.form_data.get("FCVC", 2))
        store_data("FCVC", fcvc)

        ncp = st.slider("Number of Main Meals", 1, 4, st.session_state.form_data.get("NCP", 3))
        store_data("NCP", ncp)

        caec = st.selectbox("Consumption of Food Between Meals", ["No", "Sometimes", "Frequently", "Always"], index=["No", "Sometimes", "Frequently", "Always"].index(st.session_state.form_data.get("CAEC", "No")))
        store_data("CAEC", caec)

        col1, col2 = st.columns([1, 3])
        with col1:
            st.button("Back", on_click=prev_page)
        with col2:
            st.button("Next", on_click=next_page)

    elif st.session_state.page == 3:
        faf = st.slider("Physical Activity Frequency", 0, 3, st.session_state.form_data.get("FAF", 1))
        store_data("FAF", faf)

        tue = st.slider("Technology Usage Time", 0, 2, st.session_state.form_data.get("TUE", 1))
        store_data("TUE", tue)

        smoke = st.radio("Do You Smoke?", ["Yes", "No"], index=["Yes", "No"].index(st.session_state.form_data.get("SMOKE", "No")), horizontal=True)
        store_data("SMOKE", smoke)

        col1, col2 = st.columns([1, 3])
        with col1:
            st.button("Back", on_click=prev_page)
        with col2:
            st.button("Next", on_click=next_page)

    elif st.session_state.page == 4:
        ch2o = st.slider("Daily Water Consumption (L)", 1.0, 3.0, st.session_state.form_data.get("CH2O", 2.0), 0.1)
        store_data("CH2O", ch2o)

        scc = st.radio("Calories Consumption Monitoring", ["Yes", "No"], index=["Yes", "No"].index(st.session_state.form_data.get("SCC", "No")), horizontal=True)
        store_data("SCC", scc)

        calc = st.selectbox("Alcohol Consumption Frequency", ["No", "Sometimes", "Frequently", "Always"], index=["No", "Sometimes", "Frequently", "Always"].index(st.session_state.form_data.get("CALC", "No")))
        store_data("CALC", calc)

        mtrans = st.radio("Transportation", ["Automobile", "Motorbike", "Walking", "Bike", "Public Transportation"], index=["Automobile", "Motorbike", "Walking", "Bike", "Public Transportation"].index(st.session_state.form_data.get("MTRANS", "Automobile")), horizontal=True)
        store_data("MTRANS", mtrans)

        col1, col2 = st.columns([1, 3])
        with col1:
            st.button("Back", on_click=prev_page)
        with col2:
            st.button("Get Prediction", on_click=predict_obesity)
        
        if st.session_state.prediction:
            st.success(f"Predicted Obesity Level: {st.session_state.prediction}")

    st.markdown("</div>", unsafe_allow_html=True)

def predict_obesity():
    try:
        input_data = pd.DataFrame([st.session_state.form_data])
        model, encoder = load_model()
        prediction_encoded = model.predict(input_data)
        prediction = encoder.inverse_transform(prediction_encoded)
        st.session_state.prediction = prediction[0]
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()

import streamlit as st                   # Streamlit for web app
import pandas as pd
import pickle

# load trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# load feature columns
with open("columns.pkl", "rb") as f:
    columns = pickle.load(f)

st.title("🏠 House Price Prediction App")   # app title

st.write("Enter house details to predict price")

# user input fields
area = st.number_input("Area (sq ft)", min_value=500)
bedrooms = st.number_input("Bedrooms", min_value=1)
bathrooms = st.number_input("Bathrooms", min_value=1)
stories = st.number_input("Stories", min_value=1)
parking = st.number_input("Parking", min_value=0)

mainroad = st.selectbox("Main Road Access", ["yes", "no"])
guestroom = st.selectbox("Guest Room", ["yes", "no"])
basement = st.selectbox("Basement", ["yes", "no"])
hotwaterheating = st.selectbox("Hot Water Heating", ["yes", "no"])
airconditioning = st.selectbox("Air Conditioning", ["yes", "no"])
prefarea = st.selectbox("Preferred Area", ["yes", "no"])
furnishingstatus = st.selectbox(
    "Furnishing Status",
    ["furnished", "semi-furnished", "unfurnished"]
)

# convert yes/no inputs to numeric
def yn(val):
    return 1 if val == "yes" else 0

# create input dataframe
input_data = {
    'area': area,
    'bedrooms': bedrooms,
    'bathrooms': bathrooms,
    'stories': stories,
    'parking': parking,
    'mainroad': yn(mainroad),
    'guestroom': yn(guestroom),
    'basement': yn(basement),
    'hotwaterheating': yn(hotwaterheating),
    'airconditioning': yn(airconditioning),
    'prefarea': yn(prefarea)
}

# furnishing status one-hot encoding
input_data['furnishingstatus_semi-furnished'] = 1 if furnishingstatus == "semi-furnished" else 0
input_data['furnishingstatus_unfurnished'] = 1 if furnishingstatus == "unfurnished" else 0

# convert input to DataFrame
input_df = pd.DataFrame([input_data])

# align input columns with training columns
input_df = input_df.reindex(columns=columns, fill_value=0)

# prediction button
if st.button("Predict Price"):
    prediction = model.predict(input_df)
    st.success(f"Estimated House Price: ₹ {int(prediction[0]):,}")

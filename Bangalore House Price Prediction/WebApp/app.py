import pickle
import streamlit as st

bangaloreHousePricePrediction = pickle.load(open('C:/Users/Aasim/Desktop/Bangalore House Price Prediction/RidgeModel.pkl','rb'))

st.set_page_config(page_title="Bangalore House Price Predictor",layout="wide")

st.title('Bangalore House Price Predictor')

col1,col2 = st.columns(2)

with col1:
    location = st.text_input('Location')
with col2:
    bhk = st.text_input('BHK')
with col1:
    bath = st.text_input('Bath')
with col2:
    sqft= st.text_input('Total Square Feet')

prediction=""

if st.button('Price predict'):

    user_input = [location,bhk,bath,sqft]

    price_prediction = bangaloreHousePricePrediction.predict([input])

    prediction = str(price_prediction)

    st.success("Pridiction : ",prediction)
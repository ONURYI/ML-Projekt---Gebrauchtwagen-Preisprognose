import streamlit as st
import xgboost as xgb
import numpy as np
import pandas as pd
import pickle

# LabelEncoder-Objekte laden
with open('./model/label_encoders.pkl', 'rb') as handle:
    label_encoders = pickle.load(handle)

# Modell laden
bst = xgb.Booster()
bst.load_model('./model/xgb_model.json')

# Titel der App
st.title('Auto Preisvorhersage')

# Eingabefelder für die Benutzereingaben
marke = st.selectbox('Marke', label_encoders['Marke'].classes_)
modell = st.selectbox('Modell', label_encoders['Modell'].classes_)
baujahr = st.number_input('Baujahr', min_value=1980, max_value=2023)
getriebe = st.selectbox('Getriebe', label_encoders['Getriebe'].classes_)
kilometerstand = st.number_input('Kilometerstand', min_value=0)
kraftstoffart = st.selectbox('Kraftstoffart', label_encoders['Kraftstoffart'].classes_)
verbrauch = st.number_input('Verbrauch (l/100km)', min_value=0.0)
motorgröße = st.number_input('Motorgröße (l)', min_value=0.0)

# Schaltfläche, um die Vorhersage zu machen
if st.button('Preis vorhersagen'):
    # Benutzereingaben in ein DataFrame umwandeln
    user_input_df = pd.DataFrame([[
        label_encoders['Marke'].transform([marke])[0],
        label_encoders['Modell'].transform([modell])[0],
        baujahr,
        label_encoders['Getriebe'].transform([getriebe])[0],
        kilometerstand,
        label_encoders['Kraftstoffart'].transform([kraftstoffart])[0],
        verbrauch,
        motorgröße
    ]], columns=['Marke', 'Modell', 'Baujahr', 'Getriebe', 'Kilometerstand', 'Kraftstoffart', 'Verbrauch (l/100km)', 'Motorgröße (l)'])

    # Vorhersage machen
    pred_price = bst.predict(xgb.DMatrix(user_input_df))

    # Vorhersage anzeigen
    st.success(f'Der geschätzte Preis des Autos beträgt €{pred_price[0]:,.2f}')

import streamlit as st
import xgboost as xgb
import numpy as np

# Modell laden
bst = xgb.Booster()
bst.load_model('xgb_model.json')

# Titel der App
st.title('Auto Preisvorhersage')

# Eingabefelder für die Benutzereingaben
marke = st.selectbox('Marke', ['Audi', 'BMW', 'Mercedes', ...]) # Füge die richtigen Marken ein
modell = st.selectbox('Modell', ['A1', 'A3', 'A4', ...]) # Füge die richtigen Modelle ein
baujahr = st.number_input('Baujahr', min_value=1980, max_value=2023)
getriebe = st.selectbox('Getriebe', ['Manuell', 'Automatik'])
kilometerstand = st.number_input('Kilometerstand', min_value=0)
kraftstoffart = st.selectbox('Kraftstoffart', ['Benzin', 'Diesel'])
verbrauch = st.number_input('Verbrauch (l/100km)', min_value=0.0)
motorgröße = st.number_input('Motorgröße (l)', min_value=0.0)

# Schaltfläche, um die Vorhersage zu machen
if st.button('Preis vorhersagen'):
    # Benutzereingaben in ein Numpy-Array umwandeln
    user_input = np.array([marke, modell, baujahr, getriebe, kilometerstand, kraftstoffart, verbrauch, motorgröße]).reshape(1, -1)
    
    # Vorhersage machen
    pred_price = bst.predict(xgb.DMatrix(user_input))
    
    # Vorhersage anzeigen
    st.success(f'Der geschätzte Preis des Autos beträgt €{pred_price[0]:,.2f}')

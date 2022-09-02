import pickle
import streamlit as st
pickle_in=open('salaryprediction.pkl','rb')
model=pickle.load(pickle_in)
e=st.number_input('enter experience')
if st.button('PREDICT'):
  s=model.predict([[e]]).sqeeze()
  st.success(f'salary is {s}')

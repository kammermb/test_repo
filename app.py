import streamlit as st

from Feature1 import return_even

org_list = [i for i in range(10)]

even_list = return_even(org_list)

st.write("Hello World")

st.write(even_list)
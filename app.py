import streamlit as st

from Feature1 import return_even
from Feature2 import return_odd

org_list = [i for i in range(10)]

even_list = return_even(org_list)

odd_list = return_odd(org_list)

st.write("Hello World")

st.write(even_list)
st.write(odd_list)
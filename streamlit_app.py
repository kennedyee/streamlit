import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
#students names
students = ["Amelia Kami", "Antoinne Mark", "Peter Zen", "North Kim"]
#marks
marks = [82, 76, 96, 68]

df = pd.DataFrame()

df["Student Name"] = students

df["Marks"] = marks


st.write("Hello from Streamlit ke")
st.header('st.button')
if st.button('Say hello'):
    st.write('Hello there kennedy')
else:
    st.write('Goodbye')
#Save to dataframe
df.to_csv("students.csv", index = False)
#display dataframe
st.dataframe(df)
#display table
st.table(df)

df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
st.write(df)

# Example 4

st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

# Example 5

df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)
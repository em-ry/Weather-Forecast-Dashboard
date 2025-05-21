import streamlit as st
import plotly.express as px

# Insert widgets
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} day(s) in {place}")


# plotting
def get_data(duration):
    date = ["2022-10-13", "2022-10-14", "2022-10-19"]
    temps = [10, 20, 15]
    temps = [item * duration for item in temps]
    return date, temps


d, t = get_data(days)
figure = px.line(x=d, y=t, labels={"x": "Dates", "y": "temps"})
st.plotly_chart(figure)

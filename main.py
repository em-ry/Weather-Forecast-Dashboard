from backend import get_data
import streamlit as st
import plotly.express as px

# Insert widgets
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of days to forecast")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} day(s) in {place}")

if place:
    # Get temperature/sky values
    filtered_content = get_data(place=place, forecast_days=days)

    if option == "Temperature":
        temperatures = [data["main"]["temp"] for data in filtered_content]
        dates = [data["dt_txt"] for data in filtered_content]
        # Plotting graph
        figure = px.line(x=dates, y=temperatures, labels={"x": "Dates", "y": "Temperatures"})
        st.plotly_chart(figure)

    if option == "Sky":
        images = {"Clear": "sky_images/clear.png", "Clouds": "sky_images/cloud.png",
                  "Rain": "sky_images/rain.png", "Snow": "sky_images/snow.png"}
        sky = [sky_data["weather"][0]["main"] for sky_data in filtered_content]
        # Translating data from sky and images
        image_paths = [images[condition] for condition in sky]
        st.image(image_paths, width=100)



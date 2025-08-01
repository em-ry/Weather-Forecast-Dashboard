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
    try:
        # Get temperature/sky values
        filtered_content = get_data(place=place, forecast_days=days)

        if option == "Temperature":
            temperatures = [data["main"]["temp"] / 10 for data in filtered_content]
            dates = [data["dt_txt"] for data in filtered_content]
            # Plotting graph
            figure = px.line(x=dates, y=temperatures, labels={"x": "Dates", "y": "Temperatures(C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            images = {"Clear": "sky_images/clear.png", "Clouds": "sky_images/cloud.png",
                      "Rain": "sky_images/rain.png", "Snow": "sky_images/snow.png"}

            sky_caption = {"Clear": "Clear Sky", "Clouds": "Cloudy",
                           "Rain": "Rainy", "Snow": "Snowy"}

            sky = [sky_data["weather"][0]["main"] for sky_data in filtered_content]
            # Translating data from sky and images, sky and sky_caption
            image_paths = [images[condition] for condition in sky]
            captions = [sky_caption[condition] for condition in sky]

            st.image(image_paths, width=100, caption=captions)
    except KeyError:
        st.error("Place does not exist!!")



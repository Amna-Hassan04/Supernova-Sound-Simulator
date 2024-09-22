import streamlit as st
import requests
from pydub.generators import Sine
import numpy as np
from datetime import datetime

# NASA NeoWs API endpoint
neo_api_url = "https://api.nasa.gov/neo/rest/v1/feed?"

# Set wide layout and page title
st.set_page_config(layout="wide", page_title="Supernova Sound Simulator")

# Custom CSS for aesthetics
st.markdown("""
    <style>
        body {
            background-color: #f5f5f5;
        }
        .main-title {
            font-family: 'Arial', sans-serif;
            color: #0d3b66;
            font-size: 40px;
        }
        .section-header {
            font-family: 'Arial', sans-serif;
            color: #f95738;
            font-size: 30px;
        }
        .footer {
            font-size: 14px;
            color: #7f7f7f;
        }
    </style>
""", unsafe_allow_html=True)

# Function to fetch asteroid data
def fetch_asteroid_data(start_date, end_date):
    url = f"{neo_api_url}start_date={start_date}&end_date={end_date}&api_key=DEMO_KEY"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Error fetching asteroid data: {response.status_code} - {response.text}")
        return None

# Function to simulate supernova explosion sound based on energy parameter
def simulate_supernova_sound(energy):
    frequency = np.log(energy) * 100  # Simulate frequency based on energy
    duration = int(np.log(energy) * 1000)  # Simulate duration based on energy
    sound = Sine(frequency).to_audio_segment(duration=duration)
    return sound

# Streamlit app layout
st.markdown("<h1 class='main-title'>Supernova Sound Simulator</h1>", unsafe_allow_html=True)

# Create tabs for different sections
tab1, tab2 = st.tabs(["Fetch Asteroid Data", "Supernova Explosion Simulation"])

# Fetch Asteroid Data Tab
with tab1:
    st.markdown("<h2 class='section-header'>Fetch Asteroid Data</h2>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    with col1:
        start_date = st.date_input("Start Date")
    with col2:
        end_date = st.date_input("End Date")

    # Ensure the date range does not exceed 7 days
    if start_date and end_date and (end_date - start_date).days > 7:
        st.error("The date range cannot exceed 7 days.")
    else:
        if st.button("Fetch Data"):
            if start_date and end_date:
                # Convert dates to the correct format (yyyy-mm-dd)
                start_date_str = start_date.strftime("%Y-%m-%d")
                end_date_str = end_date.strftime("%Y-%m-%d")

                asteroid_data = fetch_asteroid_data(start_date_str, end_date_str)
                if asteroid_data:
                    st.success("Asteroid data retrieved successfully.")
                    st.write("Asteroid data is available for simulation!")  # Placeholder for detailed display
            else:
                st.error("Please select both start and end dates.")

# Supernova Explosion Simulation Tab
with tab2:
    st.markdown("<h2 class='section-header'>Supernova Explosion Simulation</h2>", unsafe_allow_html=True)
    st.write("Adjust the slider to change the energy release during the supernova explosion.")

    # Slider to adjust energy release (arbitrary range for demo purposes)
    energy_release = st.slider("Energy Release (Joules)", min_value=1e6, max_value=1e12, value=1e9, step=1e6)

    # Button to simulate sound
    if st.button("Simulate Supernova Explosion"):
        sound = simulate_supernova_sound(energy_release)
        sound.export("supernova_sound.wav", format="wav")
        st.audio("supernova_sound.wav")

# Footer
st.markdown("<p class='footer'>Explore the sounds of the cosmos with data-driven simulations!</p>", unsafe_allow_html=True)

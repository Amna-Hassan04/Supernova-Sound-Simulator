# Supernova Sound Simulator

**Supernova Sound Simulator** is an interactive app that allows users to simulate the sound of a supernova explosion based on real data from NASA's Near-Earth Object Web Service (NeoWs) API. This project bridges the gap between cosmic phenomena and auditory experiences, creating a unique way to explore the cosmos through sound.

## Inspiration

The vastness of space and its incredible events, like supernova explosions, have always sparked curiosity. However, most people experience these events only visually. We were inspired to explore how we could turn these fascinating cosmic occurrences into something that could also be heard, giving users a new way to experience the wonders of space.

## What It Does

The app fetches asteroid data from NASA's NeoWs API and uses the energy released during a supernova explosion to generate a simulated sound. Users can adjust the energy release using a slider, and the app will create a corresponding sound file for the supernova explosion. Additionally, users can input date ranges to fetch real asteroid data, simulating how these objects interact with Earth.

## How We Built It

The app was built using:
- **Python** for backend logic
- **Streamlit** for creating a user-friendly web interface
- **Pydub** for sound generation and manipulation
- **NASA NeoWs API** for fetching asteroid data
- **Numpy** for calculations related to energy and frequency
- **Pandas** for handling data (if needed in future versions)

The app layout was enhanced with custom CSS to provide a space-themed aesthetic, including gradient backgrounds and cosmic elements.

## Challenges We Ran Into

One of the significant challenges was converting cosmic energy values into sound frequencies and durations in a way that was both scientifically reasonable and audibly appealing. Additionally, fine-tuning the user interface for a space-themed aesthetic while ensuring a smooth user experience posed some design hurdles.

## Accomplishments That We're Proud Of

We’re proud of the seamless integration of NASA’s NeoWs API into the app and how the app transforms real-world data into an immersive sound experience. It’s exciting to be able to use such large-scale, scientific data in a creative and accessible way.

## What We Learned

This project taught us how to work with NASA’s open-source data, improve our skills in sound synthesis, and create user-friendly interactive web apps with Streamlit. We also gained more experience in API handling and integrating real-time data into web applications.

## What's Next for Supernova Sound Simulator

- **Expanded Data Sources**: We plan to integrate more NASA datasets, such as black hole data, cosmic microwave background radiation, and asteroid impacts.
- **Improved Sound Simulation**: The sound synthesis can be improved by using more complex algorithms and incorporating more parameters from the cosmic data.
- **User Interaction**: Adding more interactive elements, such as controlling the frequency and amplitude of the sounds in real-time.
- **Machine Learning**: Implementing machine learning models to predict and generate sounds based on the astronomical data for future cosmic events.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/supernova-sound-simulator.git

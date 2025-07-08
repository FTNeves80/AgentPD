import streamlit as st
import os
from dotenv import load_dotenv
from agent2 import Agent2
import folium
from folium.plugins import MarkerCluster, MeasureControl
from streamlit_folium import folium_static
import logging
import json
LOGGER = logging.getLogger(__name__)


load_dotenv()

st.set_page_config(page_title="Agência de Viagem Tabajara", page_icon=":airplane:", layout="wide")


### Initialize Map
def initialize_session_state():
    if "marker" not in st.session_state:
        st.session_state.marker = []

def initialize_map(center, zoom=10):
    if "map" not in st.session_state or st.session_state.map is None:
        st.session_state.center = center
        st.session_state.zoom = zoom
        folium_map = folium.Map(
            location=center,
            zoom_start=zoom)
        st.session_state.map = folium_map
    return st.session_state.map


api_key = os.getenv("OPENAI_API_KEY")

## Dashboard
st.set_page_config(layout="wide")
st.title("Bem vindo a agência de Viagem Tabajara")
st.write("Essa aplicação irá planejar sua viagem e dar dicas valiosas")
points_cordinates = []

agent = Agent2(api_key)

col1, col2 = st.columns(2)

with col1:
    request = st.text_area("Para onde você gostaria de viajar")
    button = st.button("Buscar dicas de viagem")

    box = st.container(height=300)
    with box:
        container = st.empty()
        container.header("Sugestão de viagem")

if button and request:
    itinerary = agent.get_tips(request)
    try:
        container.write(itinerary["itinerary"])
    except KeyError:
        container.write("Desculpe, não consegui encontrar dicas para a sua viagem.")
    try:
        coordinates = itinerary["coordinates"]
        points_cordinates = []
        days = json.loads(coordinates)
        for day in days["days"]:
            locations = day.get("locations",[])
            for loc in locations:
                points_cordinates.append(
                    [loc["lat"],loc["lon"]]
                )
        st.session_state['marker'] = [
            folium.Marker(location=point) for point in points_cordinates
        ]

    except KeyError:
        LOGGER.warning("No coordinates found in the response.")
        pass
    

with col2:
    folium_map = initialize_map(center=[-23.5612, -46.6559], zoom=12)
    fg = folium.FeatureGroup(name="Markers")
    for maker in st.session_state.get('marker', []):
        fg.add_child(maker)
    fg.add_to(folium_map)
    folium_static(folium_map)


# Viagem para São Paulo por dois dias, quero visitar as principais igrejas da capital Paulista e quero correr em algum parque famoso com área verde
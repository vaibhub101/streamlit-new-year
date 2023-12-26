from pathlib import Path
import json
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_extras.let_it_rain import rain

# dir and file paths

THIS_DIR = Path(__file__).parent
CSS_FILE = THIS_DIR / "style" / "style.css"
ASSETS = THIS_DIR / "assets"
LOTTIE_ANIMATION = ASSETS / "Animation.json"


def load_lotie_animation(file_path):
    with open(file_path, "r") as f:
        return json.load(f)



def run_snow_animation():
    rain(emoji="🍻~         🥳", font_size=50, falling_speed=5, animation_length="infinite")
    

 
# Function to get the name for query 
    
def get_person_name():
    query_params = st.experimental_get_query_params()
    return query_params.get("name", ["Friend"])[0]
# hny.streamlit.app/?name=vaibhav

# setting the page config
st.set_page_config(page_title="Happy New Year", page_icon="🥳")

run_snow_animation()


#Dispaly the header with the name
PERSON_NAME = get_person_name()
st.header(f"Happy New Year, {PERSON_NAME}!! 😁", anchor=False)

# display the animation
lottie_animation = load_lotie_animation(LOTTIE_ANIMATION)
st_lottie(lottie_animation, key="lottie-holiday", height= 300)

st.markdown(
    f"Hey {PERSON_NAME}, wish you a very happy new year✨🎇"
)
st.markdown("# Heading towards 2024 !!!")
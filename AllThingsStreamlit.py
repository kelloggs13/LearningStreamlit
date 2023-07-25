
# https://learningsl.streamlit.app/

import streamlit as st
from pathlib import Path
import pandas as pd
import time

st.set_page_config(page_title = "Streamlit Playground"
  , layout = "wide"
  , initial_sidebar_state = "expanded"
  , menu_items = {"About":"sd"}                  
)

with st.sidebar:
  st.markdown(Path("readme.md").read_text())

with st.container():
  col_l, col_r = st.columns([1, 3])
  with col_l:
    st.write("Insert content from a markdown file")
  with col_r:
    st.code("""st.markdown(Path("readme.md").read_text())""")

st.markdown("""---""")  

with st.container():
  col_l, col_r = st.columns([1, 3])
  with col_l:
    st.write("Plot coordinates on a map")
  with col_r:
    df_coord = pd.DataFrame({"lat": [47.5, 47.6, 47.7]
                            , "lon": [7.5, 7.55, 7.6]
                            })
    st.map(df_coord)
    st.caption("*(Right-Click and dragging the mouse tilts the map)*")
    st.code("""
     df_coord = pd.DataFrame({"lat": [47.5, 47.6, 47.7]
                            , "lon": [7.5, 7.55, 7.6]
                            })
    st.map(df_coord)
    """)
    
st.markdown("""---""")

with st.container():
  col_l, col_r = st.columns([1, 2])
  with col_l:
    st.write("Include media files")
  with col_r:
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
      st.image("https://upload.wikimedia.org/wikipedia/commons/1/1c/Squirrel_posing.jpg")
    with col2:
      st.video("https://upload.wikimedia.org/wikipedia/commons/5/51/Abriss_Raiffeisen_Silo_Uetersen_01.ogv")
    with col3:
      st.audio("https://averagehunter.com/wild-game-downloads/squirrel/?md_getfile=https://averagehunter.com/mp3/squirrel/Squirrel")



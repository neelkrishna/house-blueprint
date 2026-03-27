import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
      page_title="House Blueprint - 11006 White Caterpillar Dr",
      page_icon="house",
      layout="wide",
)

html_content = Path("blueprint.html").read_text()

st.markdown(
      """
          <style>
              .main > div { padding-top: 0rem; }
                  header { visibility: hidden; }
                      footer { visibility: hidden; }
                          </style>
                              """,
      unsafe_allow_html=True,
)

components.html(html_content, height=820, scrolling=False)

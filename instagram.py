import datetime, time
import base64
import os
import pandas as pd
import streamlit as st

# File specific imports
from models.instagram.cleaner import clean_json
from models.app.wordclouds import word_cloud_insta
from models.app.binary_downloader import get_binary_file_downloader_html
import models.app.SessionState as SessionState

## TODO --> Work on the SessionState variables to avoid reloading the page after changin any variables

def query_instagram(tag, maxp):
    
  with st.spinner("Wait..."):
    time.sleep(1)
  os.chmod('assets/outputs/instagram/query_results',0o777)
  os.system(f"instagram-scraper --media-types none --tag {tag} --maximum {maxp} --comments --retry-forever --destination assets/outputs/instagram/query_results")

  insta_df = clean_json(tag)
  st.dataframe(insta_df)
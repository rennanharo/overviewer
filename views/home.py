import streamlit as st

def render_home():
  st.markdown("""
                  ## Welcome to The Overviewer.
                  The Overviewer is an open source project to create a full-fledge tool to extract information from social media.

                  Currently The Overviewer supports the following social media platforms:
                  - Twitter
                  - Instagram

                  You can check the [source code here.](https://github.com/rennanharo/overviewer)\n
                  Feel free to contribute with any suggestions or pull requests. Developed by [`Rennan Haro.`](https://github.com/rennanharo)
            """)
  st.markdown('-'*7)

  # Tool selector
  supported_tools = ["-","Twitter"]
  st.markdown("### <~ Start by selecting your page in the `sidebar to the left`. ")
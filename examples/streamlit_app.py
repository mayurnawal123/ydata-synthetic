"""
    Python file example with the script to run ydata-synthetic streamlit app
"""
pip install ydata-synthetic[streamlit]

from ydata_synthetic import streamlit_app

if __name__ == '__main__':
    streamlit_app.run()

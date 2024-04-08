import streamlit as st

st.set_page_config(
    page_title="Multipage",
)

st.sidebar.success("Select a page above.")

st.title("Welcome to My Streamlit App!")

# Text input widget
name = st.text_input("Enter your name", "")

# Slider widget
age = st.slider("Select your age", min_value=1, max_value=100, value=25)
# Checkbox widget
agree = st.checkbox("I agree to the terms and conditions")

# Radio button widget
gender = st.radio("Select your gender", options=["Male", "Female", "Other"])

# Dropdown widget
country = st.selectbox("Select your city", options=["Bangalore", "Chennai", "Goa", "Delhi"])

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# Load Animation
animation_symbol = "🌸"

st.markdown(
    f"""
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    """,
    unsafe_allow_html=True,
)

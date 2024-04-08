import streamlit as st

st.header(":mailbox: Get in Touch with me!")
# https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/

contact_form = """
    <form action="https://formsubmit.co/alankritha1322@email.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Name" required>
     <input type="email" name="email" placeholder="Email" required>
     <textarea name="message" placeholder="Type your message here..."></textarea>
     <button type="submit">Send</button>
</form>
    """
st.markdown(contact_form, unsafe_allow_html=True)

# Use CSS file


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# this function reads the css content and returns to the markdown feild
# this html <style> tage will read the css and add the style to our current stream it application

local_css("style/style1.css")

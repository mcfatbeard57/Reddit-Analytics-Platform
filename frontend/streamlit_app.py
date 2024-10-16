import streamlit as st
from streamlit_app.home import home_page
from streamlit_app.subreddit import subreddit_page
from streamlit_app.themes import themes_page

def main():
    if 'show_add_category_form' not in st.session_state:
        st.session_state.show_add_category_form = False

    st.sidebar.title("Reddit Analytics Platform")
    page = st.sidebar.radio("Navigate", ["Home", "Subreddit", "Themes"])

    if page == "Home":
        home_page()
    elif page == "Subreddit":
        subreddit_page()
    elif page == "Themes":
        themes_page()

if __name__ == "__main__":
    main()

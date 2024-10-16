import streamlit as st
import requests

def add_category_form():
    with st.form("add_category_form"):
        name = st.text_input("New Category Name")
        submitted = st.form_submit_button("Add Category")
        if submitted and name:
            try:
                response = requests.post(
                    "http://localhost:8000/categories",
                    json={"name": name, "description": "User-added category"}
                )
                if response.status_code == 200:
                    st.success(f"Category '{name}' added successfully!")
                    st.session_state.show_add_category_form = False
                    st.experimental_rerun()
                else:
                    st.error("Failed to add category. Please try again.")
            except requests.RequestException as e:
                st.error(f"Error: {str(e)}")

def trigger_reanalysis():
    # This function will trigger the re-analysis of posts for the new category
    # You'll need to implement this on the backend
    try:
        response = requests.post("http://localhost:8000/reanalyze-posts")
        if response.status_code == 200:
            st.info("Re-analyzing posts with the new category...")
        else:
            st.warning("Failed to trigger re-analysis. Please check the logs.")
    except requests.RequestException as e:
        st.error(f"Error triggering re-analysis: {str(e)}")

def display_categories():
    try:
        response = requests.get("http://localhost:8000/categories")
        if response.status_code == 200:
            categories = response.json()
            cols = st.columns(3)
            for i, category in enumerate(categories):
                with cols[i % 3]:
                    with st.expander(f"{category['name']} ({category.get('count', 0)})"):
                        st.write(category['description'])
        else:
            st.error("Failed to fetch categories.")
    except requests.RequestException as e:
        st.error(f"Error fetching categories: {str(e)}")

def themes_page():
    st.title("r/ollama")
    
    tab1, tab2 = st.tabs(["Top Posts", "Themes"])
    
    with tab2:
        st.header("Themes")
        display_categories()
        
        if st.button("Back to Subreddit List"):
            st.experimental_set_query_params(page="home")
        
        if st.button("Add New Category"):
            st.session_state.show_add_category_form = True
        
        if st.session_state.get('show_add_category_form', False):
            add_category_form()

if __name__ == "__main__":
    themes_page()

import streamlit as st
import re

import sys
import os

# Add the project root to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, project_root)

# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# st.write(sys.executable)

print(f"Python executable: {sys.executable}")
print(f"Python version: {sys.version}")
print("Python path:")
for path in sys.path:
    print(path)

from subreddit_detail import subreddit_detail
from supabase_ops import store_subreddit, get_stored_subreddits

# Default subreddits
DEFAULT_SUBREDDITS = [
    {"name": "ollama", "description": "Discussions about Ollama, an open-source AI model runner"},
    {"name": "openai", "description": "News and discussions about OpenAI and its technologies"},
    {"name": "python", "description": "A community for Python programmers"},
    {"name": "datascience", "description": "A place for data science practitioners and enthusiasts"},
]

def is_valid_subreddit_url(url):
    # Basic validation for Reddit URL
    pattern = r'^https?://(?:www\.)?reddit\.com/r/[\w-]+/?$'
    return re.match(pattern, url) is not None

def extract_subreddit_name(url):
    # Extract subreddit name from URL
    match = re.search(r'/r/([\w-]+)', url)
    return match.group(1) if match else None

def main():
    st.set_page_config(page_title="Reddit Analytics Platform", page_icon="📊", layout="wide")

    # Initialize session state for current page if not exists
    if 'current_page' not in st.session_state:
        st.session_state.current_page = "main"

    # Initialize session state for subreddits if not exists
    if 'subreddits' not in st.session_state:
        stored_subreddits = get_stored_subreddits()
        # Combine stored subreddits with default subreddits
        all_subreddits = DEFAULT_SUBREDDITS + [s for s in stored_subreddits if s['name'] not in [d['name'] for d in DEFAULT_SUBREDDITS]]
        st.session_state.subreddits = all_subreddits

    if st.session_state.current_page == "main":
        show_main_page()
    else:
        subreddit_detail(st.session_state.current_page)

def show_main_page():
    st.title("Reddit Analytics Platform")

    # Add Reddit button
    if st.button("Add Reddit"):
        st.session_state.add_reddit = True

    # Modal for adding new subreddit
    if st.session_state.get('add_reddit', False):
        with st.form("add_subreddit_form"):
            st.subheader("Add New Subreddit")
            subreddit_url = st.text_input("Paste Subreddit URL")
            submitted = st.form_submit_button("Submit")

            if submitted:
                if is_valid_subreddit_url(subreddit_url):
                    subreddit_name = extract_subreddit_name(subreddit_url)
                    new_subreddit = {"name": subreddit_name, "description": f"User-added subreddit: r/{subreddit_name}"}
                    store_subreddit(new_subreddit)
                    stored_subreddits = get_stored_subreddits()
                    all_subreddits = DEFAULT_SUBREDDITS + [s for s in stored_subreddits if s['name'] not in [d['name'] for d in DEFAULT_SUBREDDITS]]
                    st.session_state.subreddits = all_subreddits
                    st.success(f"Successfully added r/{subreddit_name}")
                    st.session_state.add_reddit = False
                else:
                    st.error("Invalid subreddit URL. Please enter a valid Reddit URL.")

    st.header("Available Subreddits")

    # Create a 2-column layout
    col1, col2 = st.columns(2)

    # Display subreddit cards
    for i, subreddit in enumerate(st.session_state.subreddits):
        with col1 if i % 2 == 0 else col2:
            with st.expander(f"r/{subreddit['name']}", expanded=True):
                st.write(f"**Description:** {subreddit['description']}")
                if st.button(f"View Analytics for r/{subreddit['name']}", key=f"view_{subreddit['name']}"):
                    st.session_state.current_page = subreddit['name']
                    st.experimental_rerun()

if __name__ == "__main__":
    main()

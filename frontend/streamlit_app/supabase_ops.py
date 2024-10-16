from supabase import create_client, Client
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

def store_posts(posts, subreddit_id):
    for post in posts:
        # Check if the post already exists
        existing = supabase.table("posts").select("*").eq("url", post['url']).execute()
        
        if len(existing.data) == 0:
            # If the post doesn't exist, insert it
            new_post = {
                'title': post['title'],
                'content': post['content'],
                'score': post['score'],
                'url': post['url'],
                'created_utc': post['created_utc'],
                'num_comments': post['num_comments'],
                'subreddit_id': subreddit_id,
                'category_name': 'Uncategorized',  # Default category, to be updated later
                'fetched_at': datetime.utcnow().isoformat()
            }
            supabase.table("posts").insert(new_post).execute()
        else:
            # If the post exists, update it
            supabase.table("posts").update({
                'title': post['title'],
                'content': post['content'],
                'score': post['score'],
                'num_comments': post['num_comments'],
                'fetched_at': datetime.utcnow().isoformat()
            }).eq("url", post['url']).execute()

def get_stored_posts(subreddit_id):
    response = supabase.table("posts").select("*").eq("subreddit_id", subreddit_id).execute()
    posts = response.data
    for post in posts:
        post['categories'] = post['category_name'].split(',') if post['category_name'] else []
    return posts

def store_subreddit(subreddit):
    # Check if the subreddit already exists
    existing = supabase.table("subreddits").select("*").eq("name", subreddit['name']).execute()
    
    if len(existing.data) == 0:
        # If the subreddit doesn't exist, insert it
        new_subreddit = {
            'name': subreddit['name'],
            'url': f"https://www.reddit.com/r/{subreddit['name']}/",
            'created_at': datetime.utcnow().isoformat(),
            'last_fetched': None
        }
        result = supabase.table("subreddits").insert(new_subreddit).execute()
        return result.data[0]['id']
    else:
        # If the subreddit exists, update last_fetched
        supabase.table("subreddits").update({
            'last_fetched': datetime.utcnow().isoformat()
        }).eq("name", subreddit['name']).execute()
        return existing.data[0]['id']

def get_stored_subreddits():
    response = supabase.table("subreddits").select("*").execute()
    return response.data

def is_valid_uuid(val):
    try:
        uuid.UUID(str(val))
        return True
    except ValueError:
        return False

def store_categorized_posts(posts, subreddit_id):
    for post in posts:
        # Check if the post already exists
        existing = supabase.table("posts").select("*").eq("url", post['url']).execute()
        
        if len(existing.data) == 0:
            # If the post doesn't exist, insert it
            new_post = {
                'title': post['title'],
                'content': post['content'],
                'score': post['score'],
                'url': post['url'],
                'created_utc': post['created_utc'],
                'num_comments': post['num_comments'],
                'subreddit_id': subreddit_id,
                'category_name': ','.join(post['categories']),
                'fetched_at': datetime.utcnow().isoformat()
            }
            supabase.table("posts").insert(new_post).execute()
        else:
            # If the post exists, update it
            supabase.table("posts").update({
                'title': post['title'],
                'content': post['content'],
                'score': post['score'],
                'num_comments': post['num_comments'],
                'category_name': ','.join(post['categories']),
                'fetched_at': datetime.utcnow().isoformat()
            }).eq("url", post['url']).execute()

def get_categorized_posts(subreddit_id):
    response = supabase.table("posts").select("*").eq("subreddit_id", subreddit_id).execute()
    posts = response.data
    for post in posts:
        post['categories'] = post['category_name'].split(',') if post['category_name'] else []
    return posts

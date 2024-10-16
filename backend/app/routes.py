from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import logging
from .models import Category
from .database import get_db_connection

app = FastAPI()

class CategoryCreate(BaseModel):
    name: str
    description: str

@app.post("/categories", response_model=Category)
async def add_category(category: CategoryCreate):
    try:
        db = get_db_connection()
        new_category = Category(name=category.name, description=category.description)
        db.add(new_category)
        db.commit()
        db.refresh(new_category)
        return new_category
    except Exception as e:
        logging.error(f"Error adding new category: {str(e)}")
        raise HTTPException(status_code=500, detail="Error adding new category")

@app.post("/reanalyze-posts")
async def reanalyze_posts():
    try:
        # Fetch all posts from the database
        posts = fetch_all_posts()
        
        # Re-analyze each post with the updated categories
        for post in posts:
            updated_analysis = await analyze_post(post)
            update_post_analysis(post.id, updated_analysis)
        
        return {"message": "Posts re-analyzed successfully"}
    except Exception as e:
        logging.error(f"Error during post re-analysis: {str(e)}")
        raise HTTPException(status_code=500, detail="Error during post re-analysis")

# Helper functions (implement these based on your database structure)
def fetch_all_posts():
    # Fetch all posts from the database
    pass

def update_post_analysis(post_id, analysis):
    # Update the analysis for a specific post in the database
    pass

# ... (other existing routes)

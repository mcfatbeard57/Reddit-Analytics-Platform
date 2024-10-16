# Product Requirements Document (PRD)  
   
## 1. Project Overview  
   
### 1.1 **Project Name**  
Reddit Analytics Platform  
   
### 1.2 **Description**  
The Reddit Analytics Platform offers comprehensive analytics for various subreddits. Users can view top content, explore categorized themes within posts, and manage their favorite subreddits. The platform utilizes Python, Flask, FastAPI, and Streamlit to deliver a seamless and interactive user experience.  
   
### 1.3 **Goals**  
1. **Browse and Manage Subreddits**: Allow users to view and add subreddits of interest.  
2. **Detailed Analytics**: Offer in-depth analysis of top posts and categorized themes within each subreddit.  
3. **Customizable Themes**: Enable custmization of theme categories.  
4. **Efficient Data Handling**: Ensure effective data fetching, categorization, and storage using reliable technologies.  
   
## 2. Objectives  
   
### 2.1 **Primary Objectives**  
1. Develop a user-friendly interface to list and add subreddits.  
2. Implement robust data fetching from Reddit using PRAW.  
3. Categorize Reddit posts using OpenAI via Ollama.  
4. Store and manage data efficiently using Supabase.  
5. Facilitate the addition of new theme categories.  
   
### 2.2 **Secondary Objectives**  
1. Provide comprehensive documentation for developers.  
2. Implement scalable architecture to accommodate future enhancements.  
   
## 3. Functional Requirements  
   
### 3.1 **Subreddit Management**  
   
#### 3.1.1 **List Available Subreddits**  
- **3.1.1.1** Display a list of pre-configured popular subreddits such as "ollama" and "openai" in card format.  
- **3.1.1.2** Each subreddit card displays the subreddit name and relevant information.  
   
#### 3.1.2 **Add New Subreddits**  
- **3.1.2.1** Provide an "Add Reddit" button for users to add new subreddits.  
- **3.1.2.2** Clicking the button opens a modal where users can paste the subreddit URL.  
- **3.1.2.3** Upon submission, validate the URL and add the subreddit to the list, displaying it as a new card.  
   
### 3.2 **Subreddit Analytics**  
   
#### 3.2.1 **Subreddit Detail Page**  
- **3.2.1.1** Clicking on a subreddit card navigates to the subreddit’s detail page.  
- **3.2.1.2** The detail page contains two tabs: "Top Posts" and "Themes".  
   
#### 3.2.2 **Top Posts**  
- **3.2.2.1** Display fetched Reddit posts from the past 7 days.  
- **3.2.2.2** Fetch posts from the top of the week using PRAW.  
- **3.2.2.3** Ensure posts are fetched only if they haven't been fetched in the past 7 days.  
- **3.2.2.4** Each post displays the title, score, content, URL, creation time (UTC), and number of comments.  
- **3.2.2.5** Display posts in a sortable table component, sorted by the number of scores.  
- **3.2.2.6** Store fetched Reddit data in Supabase.  
   
#### 3.2.3 **Themes**  
- **3.2.3.1** Analyze each post using OpenAI via Ollama to categorize them into predefined themes:  
  - **3.2.3.1.1** Solution Requests  
  - **3.2.3.1.2** Pain & Anger  
  - **3.2.3.1.3** Self-Promotion  
  - **3.2.3.1.4** News  
  - **3.2.3.1.5** Money Talk  
  - **3.2.3.1.6** Advice Requests  
  - **3.2.3.1.7** Ideas  
- **3.2.3.2** Run the categorization process concurrently for faster analysis.  
- **3.2.3.3** Display each category as a card with the title, description, and count of posts.  
- **3.2.3.4** Clicking a category card opens a side panel displaying all posts under that category.  
- **3.2.3.5** Store categorized data in Supabase.  
   
### 3.3 **Theme Management**  
   
#### 3.3.1 **Add New Theme Category**  
- **3.3.1.1** Users can add new theme categories by creating a new card.  
- **3.3.1.2** Upon adding a new category, trigger the analysis process to categorize existing posts accordingly.  
   
### 3.4 **Similar Subreddit Identification**  
   
#### 3.4.1 **Identify Similar Subreddits**  
- **3.4.1.1** Utilize GitHub resources to identify similar subreddits based on existing subreddits.  
- **3.4.1.2** Display similar subreddits to users for easy exploration.  
   
## 4. Non-Functional Requirements  
   
### 4.1 **Performance**  
- **4.1.1** Ensure efficient data fetching and processing to minimize latency.  
- **4.1.2** Implement concurrent processing for categorization to enhance speed.  
   
### 4.2 **Scalability**  
- **4.2.1** Design the system to handle an increasing number of subreddits and data volume.  
- **4.2.2** Ensure the architecture supports future feature expansions.  
   
### 4.3 **Security**  
- **4.3.1** Store all sensitive information, such as API keys and credentials, in environment variables.  
- **4.3.2** Ensure the `.env.Local` file is listed in `.gitignore` to prevent exposure.  
   
### 4.4 **Maintainability**  
- **4.4.1** Write clean, modular, and well-documented code to facilitate maintenance.  
- **4.4.2** Provide comprehensive documentation for developers.  
   
### 4.5 **Usability**  
- **4.5.1** Design an intuitive user interface for ease of navigation and interaction.  
- **4.5.2** Ensure responsiveness across different devices and screen sizes.  
   
## 5. Technical Stack  
   
### 5.1 **Backend**  
- Python  
- Flask  
- FastAPI  
   
### 5.2 **Frontend**  
- Streamlit  
   
### 5.3 **Libraries & Tools**  
- PRAW for Reddit data fetching  
- OpenAI via Ollama for post categorization  
- Supabase for database management  
   
### 5.4 **Deployment**  
- Docker  
- Docker Compose  
   
## 6. File Structure  
   
### 6.1 **Root Directory Structure**  
```  
reddit-analytics-platform/  
│  
├── backend/  
│   ├── app/  
│   │   ├── __init__.py            # Initializes Flask/FastAPI application  
│   │   ├── models.py              # Database models (SUPERBASE or equivalent)  
│   │   ├── routes.py              # API routes (Flask/FastAPI endpoints)  
│   │   ├── reddit_fetch.py        # Logic to fetch data from Reddit (using PRAW)  
│   │   ├── categorization.py      # Logic for OpenAI-based categorization  
│   │   └── utils.py               # Utility functions (e.g., for database interaction)  
│   │  
│   ├── tests/  
│   │   ├── test_routes.py         # Unit tests for API routes  
│   │   ├── test_models.py         # Unit tests for database models  
│   │   ├── test_reddit_fetch.py   # Unit tests for Reddit data fetching  
│   │   └── test_categorization.py # Unit tests for OpenAI categorization  
│   │  
│   ├── migrations/  
│   │   └── (auto-generated migration files)  
│   │  
│   ├── requirements.txt           # Python dependencies  
│   └── manage.py                  # Script to run the backend application  
│  
├── frontend/  
│   ├── streamlit_app/  
│   │   ├── home.py                # Home page to list available subreddits  
│   │   ├── subreddit.py           # Subreddit detail page (Top posts & Themes)  
│   │   └── themes.py              # Display categorized themes  
│   │  
│   ├── components/  
│   │   ├── sidebar.py             # Sidebar component for navigation  
│   │   └── cards.py               # Components for cards displaying subreddit/posts/themes  
│   │  
│   └── streamlit_app.py           # Entry point for Streamlit app  
│  
├── .env                           # Environment variables (API keys, DB credentials)  
├── docker-compose.yml             # Docker Compose setup for multi-container environment  
├── Dockerfile                     # Docker setup for containerized deployment  
├── README.md                      # Project documentation  
└── LICENSE                        # Open-source license  
```  
   
**Key Changes:**  
- **Consolidated Directories**: Separated `backend` and `frontend` for better organization.  
- **Removed User-Specific Components**: Eliminated folders and files related to user management.  
- **Simplified Testing Structure**: Focused tests on core functionalities without user authentication.  
   
## 7. Database Schema  

1. **Subreddits Table**
   - `id`: SERIAL PRIMARY KEY (Auto-incrementing integer)
   - `name`: TEXT UNIQUE NOT NULL
   - `url`: TEXT UNIQUE NOT NULL
   - `created_at`: TIMESTAMP DEFAULT CURRENT_TIMESTAMP
   - `last_fetched`: TIMESTAMP

2. **Posts Table**
   - `id`: SERIAL PRIMARY KEY (Auto-incrementing integer)
   - `title`: TEXT NOT NULL
   - `content`: TEXT NOT NULL
   - `score`: INTEGER NOT NULL
   - `url`: TEXT NOT NULL
   - `created_utc`: TIMESTAMP NOT NULL
   - `num_comments`: INTEGER NOT NULL
   - `subreddit_id`: INTEGER REFERENCES Subreddits(id)
   - `category_name`: TEXT NOT NULL
   - `fetched_at`: TIMESTAMP DEFAULT CURRENT_TIMESTAMP

3. **Categories Table**
   - `id`: SERIAL PRIMARY KEY (Auto-incrementing integer)
   - `name`: TEXT UNIQUE NOT NULL
   - `description`: TEXT NOT NULL
   - `created_at`: TIMESTAMP DEFAULT CURRENT_TIMESTAMP

4. **Collections Table** (Optional)
   - `id`: SERIAL PRIMARY KEY (Auto-incrementing integer)
   - `name`: TEXT NOT NULL
   - `created_at`: TIMESTAMP DEFAULT CURRENT_TIMESTAMP


## 8. Documentation  
   
### 8.1 **Using PRAW to Fetch Reddit Data**  
   
#### 8.1.1 **Description**  
PRAW (Python Reddit API Wrapper) interacts with Reddit’s API to fetch recent posts from specified subreddits.  
   
#### 8.1.2 **Code Example**  
```python  
import os  
from datetime import datetime, timedelta  
from dotenv import load_dotenv  
   
# Load environment variables  
load_dotenv()  
   
try:  
    import asyncpraw as praw  
    is_async = True  
except ImportError:  
    import praw  
    is_async = False  
   
async def fetch_recent_posts(subreddit_name='ollama'):  
    # Initialize Reddit API client  
    reddit = praw.Reddit(  
        client_id=os.getenv('REDDIT_CLIENT_ID'),  
        client_secret=os.getenv('REDDIT_CLIENT_SECRET'),  
        user_agent=os.getenv('REDDIT_USER_AGENT')  
    )  
    
    # Get the subreddit  
    subreddit = await reddit.subreddit(subreddit_name) if is_async else reddit.subreddit(subreddit_name)  
    
    # Calculate the timestamp for 7 days ago  
    time_7_days_ago = datetime.utcnow() - timedelta(days=7)  
    
    # Fetch recent posts  
    recent_posts = []  
    if is_async:  
        async for post in subreddit.new(limit=None):  
            if datetime.utcfromtimestamp(post.created_utc) < time_7_days_ago:  
                break  
            recent_posts.append(create_post_dict(post))  
        await reddit.close()  
    else:  
        for post in subreddit.new(limit=None):  
            if datetime.utcfromtimestamp(post.created_utc) < time_7_days_ago:  
                break  
            recent_posts.append(create_post_dict(post))  
    
    return recent_posts  
   
def create_post_dict(post):  
    return {  
        'title': post.title,  
        'content': post.selftext,  
        'score': post.score,  
        'num_comments': post.num_comments,  
        'url': post.url,  
        'created_utc': datetime.utcfromtimestamp(post.created_utc).strftime('%Y-%m-%d %H:%M:%S UTC')  
    }  
   
if __name__ == "__main__":  
    import asyncio  
    # This block will only run if the script is executed directly  
    posts = asyncio.run(fetch_recent_posts()) if is_async else fetch_recent_posts()  
    for i, post in enumerate(posts, 1):  
        print(f"\nPost {i}:")  
        print(f"Title: {post['title']}")  
        print(f"Content: {post['content'][:200]}..." if len(post['content']) > 200 else f"Content: {post['content']}")  
        print(f"Score: {post['score']}")  
        print(f"Number of comments: {post['num_comments']}")  
        print(f"URL: {post['url']}")  
        print(f"Date: {post['created_utc']}")  
    
    print(f"\nTotal posts fetched: {len(posts)}")  
```  
   
### 8.2 **Using Ollama to Categorize Reddit Posts**  
   
#### 8.2.1 **Description**  
Ollama is integrated with FastAPI to categorize Reddit posts using OpenAI models. It analyzes each post and assigns categories based on predefined criteria.  
   
#### 8.2.2 **Code Example**  
```python  
from fastapi import FastAPI, HTTPException  
from pydantic import BaseModel  
from typing import Optional, List  
import logging  
import sys  
from reddit_fetch import fetch_recent_posts  
import asyncio  
import requests  
   
# Set up logging  
logging.basicConfig(level=logging.INFO, stream=sys.stdout,  
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')  
logger = logging.getLogger(__name__)  
   
app = FastAPI()  
   
class RedditPost(BaseModel):  
    title: str  
    content: Optional[str] = None  
    score: int  
    num_comments: int  
    created_utc: str  
    url: str  
   
class PostCategoryAnalysis(BaseModel):  
    solution_requests: bool  
    pain_and_anger: bool  
    self_promotion: bool  
    news: bool  
    money_talk: bool  
    advice_requests: bool  
    ideas: bool  
   
class AnalyzedPost(BaseModel):  
    post: RedditPost  
    analysis: PostCategoryAnalysis  
   
@app.on_event("startup")  
async def startup_event():  
    logger.info("Server started. Ollama will be used for analysis.")  
   
async def analyze_post(post: RedditPost) -> PostCategoryAnalysis:  
    prompt = f"""  
    Analyze the following Reddit post and determine which categories it belongs to.  
    Respond with True or False for each category.  
    
    Post Title: {post.title}  
    Post Content: {post.content}  
    
    Categories:  
    1. Solution requests  
    2. Pain and Anger  
    3. Self-Promotion  
    4. News  
    5. Money Talk  
    6. Advice Requests  
    7. Ideas  
    
    Respond ONLY in the following format:  
    solution_requests: True/False  
    pain_and_anger: True/False  
    self_promotion: True/False  
    news: True/False  
    money_talk: True/False  
    advice_requests: True/False  
    ideas: True/False  
    """  
  
    try:  
        response = requests.post(  
            "http://localhost:11434/api/generate",  
            json={  
                "model": "llama3.2:latest",  
                "prompt": prompt,  
                "stream": False  
            }  
        )  
        response.raise_for_status()  
        result = response.json()  
        logger.info(f"Raw response: {result['response']}")  
  
        analysis = result['response'].strip().split('\n')  
        result_dict = {category: False for category in PostCategoryAnalysis.__fields__}  
        for line in analysis:  
            if ': ' in line:  
                key, value = line.split(': ')  
                key = key.strip().lower().replace(' ', '_')  
                if key in result_dict:  
                    result_dict[key] = value.lower() == 'true'  
  
        return PostCategoryAnalysis(**result_dict)  
    except Exception as e:  
        logger.error(f"Error during post analysis: {str(e)}")  
        raise HTTPException(status_code=500, detail=f"Error during post analysis: {str(e)}")  
   
@app.get("/analyze-recent-posts", response_model=List[AnalyzedPost])  
async def analyze_recent_posts():  
    recent_posts = await fetch_recent_posts() if asyncio.iscoroutinefunction(fetch_recent_posts) else fetch_recent_posts()  
    logger.info(f"Fetched {len(recent_posts)} posts. Analyzing the 2 most recent...")  
  
    analyzed_posts = []  
    for post in recent_posts[:2]:  
        reddit_post = RedditPost(**post)  
        analysis = await analyze_post(reddit_post)  
        analyzed_posts.append(AnalyzedPost(post=reddit_post, analysis=analysis))  
  
    return analyzed_posts  
   
@app.get("/")  
async def root():  
    return {"message": "Reddit Post Analyzer is running"}  
   
if __name__ == "__main__":  
    import uvicorn  
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")  
```  
   
### 8.3 **Using Supabase to Save Reddit Posts**  
   
#### 8.3.1 **Description**  
Supabase serves as the database solution to store Reddit posts, categorized data, and subreddit collections efficiently.  
   
#### 8.3.2 **Implementation Guidelines**  
1. **Define the Database Schema**:  
   - Utilize the schema outlined in Section 7.  
2. **Database Interactions**:  
   - Use Supabase’s SDK for all database operations within the application.  
3. **Performance Optimization**:  
   - Ensure proper indexing on frequently queried fields to optimize performance.  
4. **Security**:  
   - Implement secure access rules to protect sensitive data.  
   
## 9. API Documentation  
   
### 9.1 **Endpoints**  
   
#### 9.1.1 **Analyze Recent Posts**  
1. **Endpoint**: `/analyze-recent-posts`  
2. **Method**: GET  
3. **Description**: Fetches recent Reddit posts and analyzes them into predefined categories.  
4. **Response**:  
   - List of `AnalyzedPost` objects, each containing the original post and its category analysis.  
   
#### 9.1.2 **Root**  
1. **Endpoint**: `/`  
2. **Method**: GET  
3. **Description**: Checks if the Reddit Post Analyzer is running.  
4. **Response**:  
   - JSON message confirming the service status.  
   
### 9.2 **Data Models**  
   
#### 9.2.1 **RedditPost**  
1. `title`: String  
2. `content`: String (Optional)  
3. `score`: Integer  
4. `num_comments`: Integer  
5. `url`: String  
6. `created_utc`: String  
   
#### 9.2.2 **PostCategoryAnalysis**  
1. `solution_requests`: Boolean  
2. `pain_and_anger`: Boolean  
3. `self_promotion`: Boolean  
4. `news`: Boolean  
5. `money_talk`: Boolean  
6. `advice_requests`: Boolean  
7. `ideas`: Boolean  
   
#### 9.2.3 **AnalyzedPost**  
1. `post`: RedditPost  
2. `analysis`: PostCategoryAnalysis  
   
## 10. User Interface  
   
### 10.1 **Streamlit Application**  
   
#### 10.1.1 **Home Page**  
1. **Functionality**:  
   - Display a list of available subreddits in card format.  
   - Provide an "Add Reddit" button to allow users to add new subreddits.  
2. **Components**:  
   - Sidebar for navigation.  
   - Subreddit cards displaying subreddit names and basic info.  
   
#### 10.1.2 **Subreddit Detail Page**  
1. **Functionality**:  
   - Provide two tabs: "Top Posts" and "Themes".  
2. **Top Posts Tab**:  
   - Display a sortable table of top posts from the past 7 days.  
   - Include post details such as title, score, content snippet, URL, creation time, and number of comments.  
3. **Themes Tab**:  
   - Display categorized themes as individual cards.  
   - Show title, description, and count of posts in each category.  
   - Allow users to click on a category card to view detailed posts in a side panel.  
   
#### 10.1.3 **Themes Page**  
1. **Functionality**:  
   - Display all theme categories.  
   - Allow users to add new theme categories.  
2. **Components**:  
   - Category cards with relevant information.  
   - Modal or form for adding new categories.  
   
### 10.2 **Streamlit Components**  
   
#### 10.2.1 **Sidebar Component**  
1. **Functionality**:  
   - Provide navigation links to different pages such as Home and Themes.  
2. **Components**:  
   - Navigation links/buttons.  
   
#### 10.2.2 **Cards Component**  
1. **Functionality**:  
   - Render subreddit, post, and category information in a visually appealing card format.  
2. **Components**:  
   - Subreddit cards.  
   - Post summary cards.  
   - Category cards.  
   
## 11. Deployment  
   
### 11.1 **Containerization**  
1. **Dockerfile**:  
   - Define the environment setup for the application.  
   - Install necessary dependencies.  
   - Set up environment variables.  
   - Specify the entry point for the application.  
   
### 11.2 **Docker Compose**  
1. **docker-compose.yml**:  
   - Configure multi-container setup including the application server and database.  
   - Define network settings and volume mounts.  
   - Set up service dependencies and startup order.  
   
### 11.3 **Environment Variables**  
1. **.env File**:  
   - Store all sensitive information such as API keys and database credentials.  
2. **.env.Local**:  
   - Used for local development.  
   - Ensure it is listed in `.gitignore` to prevent exposure.  
   
## 12. Testing  
   
### 12.1 **Unit Tests**  
1. **Tests Directory Structure**:  
   - `backend/tests/test_routes.py`: Tests for API routes.  
   - `backend/tests/test_models.py`: Tests for database models.  
   - `backend/tests/test_reddit_fetch.py`: Tests for Reddit data fetching.  
   - `backend/tests/test_categorization.py`: Tests for OpenAI categorization.  
   
### 12.2 **Testing Framework**  
1. Use `pytest` for writing and executing unit tests.  
2. Ensure high coverage for critical functionalities.  
   
### 12.3 **Continuous Integration**  
1. Integrate with CI tools like GitHub Actions to automate testing on code commits and pull requests.  
   
## 13. Additional Requirements  
   
### 13.1 **Sensitive Information Management**  
1. Store all API keys, credentials, and other sensitive data in environment variables.  
2. Use a `.env.Local` file for local development settings.  
3. Ensure `.env.Local` is included in `.gitignore` to prevent accidental commits.  
   
### 13.2 **Documentation**  
1. Maintain a comprehensive `README.md` with:  
   - Project overview.  
   - Setup and installation instructions.  
   - Usage guidelines.  
   - Contribution guidelines.  
2. Provide inline code documentation and comments for clarity.  
   
### 13.3 **Licensing**  
1. Include an appropriate open-source license in the `LICENSE` file to define usage rights.  
   
## 14. Appendices  
   
### 14.1 **Sample Code for PRAW Integration**  
*(Refer to Section 8.1.2 for the complete code example.)*  
   
### 14.2 **Sample Code for Ollama Integration**  
*(Refer to Section 8.2.2 for the complete code example.)*  
   
### 14.3 **Sample Code for Supabase Integration**  
*(Refer to Section 8.3 for implementation guidelines.)*  
   
---  
   
## Summary of Changes  
   
- **Removed User Management**: Eliminated all sections related to user registration, authentication, and user-specific data management.  
- **Simplified File Structure**: Consolidated backend and frontend directories, removing user-specific components.  
- **Database Simplification**: Removed `Users Table`, `UserCollections Table`, and any foreign key references to users.  
- **Functional Adjustments**: Streamlined functionalities to operate without user accounts, focusing on general subreddit analytics.  
- **UI Adjustments**: Removed user-specific components from the UI, such as user profile summaries.  
   
This simplification reduces the complexity of the project, allowing for a streamlined focus on subreddit analytics without the overhead of managing user authentication and personalized data.